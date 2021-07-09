import re
import os
import json
import random 
import tarfile

import tensorflow as tf
import gpt_2_simple as gpt2

from . import Constants 
from datetime import datetime
from gpt_2_simple.src import model


def generate(a_chars_in_location, b_chars_in_location, SERIES, LENGTH):
    start = datetime.now()
    # start temporary list to hold our output text
    templist = []
    # generate text for each act 
    for i in Constants.series[SERIES]:
        k = 0
        # if it's the first run through, we have to start the session
        try:
            if bool(sess): 
                sess = gpt2.reset_session(sess)
        except:
            sess = gpt2.start_tf_sess()
        # print('opening TAR')
        with tarfile.open(f"../..tars/checkpoint_{i}.tar", 'r') as tar:
            tar.extractall(os.path.join('models', '774M', '.checkpoint'))
        # print('opening checkpoint path')
        checkpoint_path = os.path.join('models', '774M')
        # print('setting default hparams')
        hparams = model.default_hparams()
        # print('loading default hparams')
        with open(os.path.join(checkpoint_path, 'hparams.json')) as f:
            hparams.override_from_dict(json.load(f))
        # print('whatever the fuck context is doing ')
        context = tf.compat.v1.placeholder(tf.int32, [1, None])
        # print('setting output')
        output = model.model(hparams=hparams, X=context)
        # print('loading latest checkpoint')
        ckpt = tf.train.latest_checkpoint(checkpoint_path)
        # print('setting memory saver')
        saver = tf.compat.v1.train.Saver(allow_empty=True)
        # print('starting the session')
        sess.run(tf.compat.v1.global_variables_initializer())
        # print('restoring last known variables')
        saver.restore(sess, ckpt)
        # print('determining scene length')
        # determine how much we need to generate 
        if LENGTH == 'SCENE':
            length = 100
            rng = 1
        elif LENGTH == 'SHORT':
            length = 200
            rng = 2
        else:
            length = 400
            rng = 4
        # print('start generating')
        # start generating            
        for j in range(rng):
            txt = ''
            # use the input as the set up for the model 
            # print('making our prefix')
            if len(templist) == 0:
                prefix = f'STAR TREK: {SERIES}.\n' 
            # otherwise have it grab the end of the last generated text
            else:
                prefix = '\n'.join(templist[-500:])
            # print('adding our characters')
            # on even generations we'll generate A plot scenes
            # if LENGTH != 'SHORT':
            #     alst = [0, 2]
            #     blst = [1, 3]
            # else:
            #     alst = [0]
            #     blst = [2]
            if j == 0 and len(a_chars_in_location) > 0:#and k in alst:
                prefix = prefix + str(a_chars_in_location.pop(0))
                prefix = ' '.join(prefix.split(' ')[-500:])
                if len(templist) == 0:
                    templist.append(prefix)
            # on even generations we'll generate A plot scenes
            elif j == 1 and len(b_chars_in_location) > 0:# and k in blst:
                print(prefix)
                prefix = prefix + str(b_chars_in_location.pop(0))
                prefix = ' '.join(prefix.split(' ')[-500:])
            # print('generating and putting our text into a list')
            # append our generated text to our list for storage 
            length = min((length + len(prefix)), 1000)
            txt += gpt2.generate(sess,
                                run_name = i,
                                length = length,
                                temperature = .01,
                                top_k = 100, 
                                top_p= .50,
                                prefix = prefix,
                                nsamples = 1,
                                include_prefix = False,
                                model_name = '774M',
                                batch_size = 1, 
                                truncate='<|endoftext|>',
                                return_as_list = True
                                )[0]
            print(f'this is the text {txt}')
            txt = txt.replace('<br>', '').replace('<b>', '').replace('--', '-')
            txt = txt.replace('</b>', '').replace('*', '').replace('(x2)', '')
            txt = txt.replace('>', '').replace('<', '').replace('.', '.\n')
            txt = txt.replace('!', '!\n').replace('?', '?\n').replace('  ', ' ')
            txt = txt.replace(' .', '.').replace(' ,', ',').replace(' !', '!')
            txt = txt.replace(' ?', '?')
            for word in txt.split(' '):
                # print(word)
                if ':' in word and word != 'TREK:':
                    last_word = txt.split()[txt.split().index(word)-1]
                    if last_word.isupper():
                        txt = txt.replace(f'{last_word} {word}', f'\n{last_word} {word}')
                    else:
                        txt = txt.replace(word, f'\n{word}')
            for l in txt.split('\n'):
                # print(l)
                if len(templist) > 0:
                    len_ = len(set(re.sub(r'[^\w\s]', '', l).strip().split(' ')))
                    new_ = len(set(re.sub(r'[^\w\s]', '', l + templist[-1]).strip().split(' ')))
                    print('len' + str(len_))
                    print('new' + str(new_))
                else:
                    len_ = 0
                    new_ = 10
                    # print('len' + len_)
                    # print('new' + new_)
                if l not in templist and 'written by' not in l.lower() and new_-len_ >= 2:
                    # print(l)
                    templist.append(l)
            k += 1
    # print('list to text')
    text = '\n'.join(templist).replace('\n', '<br>')
    for i in range(3):
        text = text.replace('<br><br>', '<br>')
    text = text[:text.rfind('<br>')]
    text += '<br><br><br><br>'
    # return the string 
    # print('return text')
    end = datetime.now()
    print(end-start)
    return text 

def inputs(char_input, loc_input, setting, names, locs):
    # either get or sample characters to feature 
    if char_input:
        inp = char_input.upper().split(',')
        while len(inp) < 6:
            inp.append(random.sample(names, k=1)[0])
        a_chars = random.sample(inp, k=len(inp)//2)
        b_chars = inp
    else:
        a_chars = random.sample(names, k=3)
        b_chars = random.sample(names, k=3)
    # either get or sample location
    if loc_input:
        locations = loc_input.upper().split(',')
        if len(locations) < 4:
            locations.append(random.sample(locs, k=1)[0])
    else:
        locations = random.sample(locs, k=4)
    a_chars_in_location, b_chars_in_location = [], []
    for k in range(2):
        a_chars_in_location.append(f'{", ".join(a_chars[:-1])} and {a_chars[-1]} are in the {locations[random.randint(0, len(locations)-1)]}.<br>')
        b_chars_in_location.append(f'{", ".join(b_chars[:-1])} and {b_chars[-1]} are in the {locations[random.randint(0, len(locations)-1)]}.<br>')
    if setting:
        setting = f'{setting}.<br>'
    a_chars_in_location[0] += setting
    return a_chars_in_location, b_chars_in_location