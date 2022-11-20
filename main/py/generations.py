import re
import os
import json
import random 
import tarfile

from pathlib import Path
import tensorflow as tf
import gpt_2_simple as gpt2

from . import Constants 
from datetime import datetime
from gpt_2_simple.src import model


def generate(a_chars_in_location, b_chars_in_location, SERIES, LENGTH):
    '''
    Given Characters in locations, series, and length you wish to 
    generate, this function will use GPT-2 to generate a single piece
    of text and return it as a string to be used in any application you need. 
    '''
    start = datetime.now()
    # print('downloading model')
    # gpt2.download_gpt2(model_dir='models', model_name='1558M')
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
        # loaded this function up with print statments, so that if something 
        # goes wrong but doesn't have a clear error message, we can still
        # debug exactly where it's happening 
        print('gathering TAR directory')
        p = str(Path(__file__).parents[2]).replace('\\', '/')
        print('opening TAR')
        with tarfile.open(f"{p}/tars/checkpoint_{i}.tar", 'r') as tar:
            def is_within_directory(directory, target):
                
                abs_directory = os.path.abspath(directory)
                abs_target = os.path.abspath(target)
            
                prefix = os.path.commonprefix([abs_directory, abs_target])
                
                return prefix == abs_directory
            
            def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
            
                for member in tar.getmembers():
                    member_path = os.path.join(path, member.name)
                    if not is_within_directory(path, member_path):
                        raise Exception("Attempted Path Traversal in Tar File")
            
                tar.extractall(path, members, numeric_owner=numeric_owner) 
                
            
            safe_extract(tar, os.path.join("models","1558M",".checkpoint"))
        print('opening checkpoint path')
        checkpoint_path = os.path.join('models', '1558M')
        print('setting default hparams')
        hparams = model.default_hparams()
        print('loading default hparams')
        with open(os.path.join(checkpoint_path, 'hparams.json')) as f:
            hparams.override_from_dict(json.load(f))
        print('whatever context is doing ')
        context = tf.compat.v1.placeholder(tf.int32, [1, None])
        print('setting output')
        output = model.model(hparams=hparams, X=context)
        print('loading latest checkpoint')
        ckpt = tf.train.latest_checkpoint(checkpoint_path)
        print('setting memory saver')
        saver = tf.compat.v1.train.Saver(allow_empty=True)
        print('starting the session')
        sess.run(tf.compat.v1.global_variables_initializer())
        print('restoring last known variables')
        saver.restore(sess, ckpt)
        print('determining scene length')
        # determine how much we need to generate 
        if LENGTH == 'SCENE':
            length = 200
            rng = 1
        elif LENGTH == 'SHORT':
            length = 400
            rng = 1
        else:
            length = 500
            rng = 3
        print('start generating')
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
            if j == 0 and len(a_chars_in_location) > 0:
                prefix = prefix + str(a_chars_in_location.pop(0))
                prefix = ' '.join(prefix.split(' ')[-500:])
                if len(templist) == 0:
                    templist.append(prefix)
            # on even generations we'll generate A plot scenes
            elif j == 1 and len(b_chars_in_location) > 0:
                print(prefix)
                prefix = prefix + str(b_chars_in_location.pop(0))
                prefix = ' '.join(prefix.split(' ')[-500:])
            print('generating and putting our text into a list')
            # append our generated text to our list for storage 
            final_len = min(((length*(j+1)) + len(prefix.split(' '))), 1000)
            txt += gpt2.generate(sess,
                                run_name = i,
                                length = final_len,
                                temperature = .80,
                                top_k = 100, 
                                top_p= .80,
                                prefix = prefix,
                                nsamples = 1,
                                include_prefix = False,
                                model_name = '1558M',
                                batch_size = 1, 
                                truncate='<|endoftext|>',
                                return_as_list = True
                                )[0]
            print(f'this is the text {txt}')
            txt = txt.replace(prefix, '')
            txt = txt.replace('<br>', '').replace('<b>', '')
            txt = txt.replace('--', '-').replace('(x2)', '')
            txt = txt.replace('</b>', '').replace('*', '')
            txt = txt.replace('.', '.\n').replace('  ', ' ')
            txt = txt.replace('>', '').replace('<', '')
            txt = txt.replace('!', '!\n').replace('?', '?\n')
            txt = txt.replace(' ,', ',').replace('/n', ' /n ')
            for word in txt.split(' '):
                if ':' in word and word != 'TREK:':
                    if word in txt.replace('\n', ' ').split(' '):
                        last_word = txt.split()[txt.split().index(word)-1]
                        if last_word.isupper():
                            txt = txt.replace(f'{last_word} {word}', 
                                              f'\n {last_word} {word}')
                        else:
                            txt = txt.replace(word, f'\n {word}')
            templist.append(txt)
    text = '\n'.join(templist).replace('\n', '<br>')
    for i in range(3):
        text = text.replace('<br><br>', '<br>')
    text = text[:text.rfind('.')]
    text += '<br><br><br><br>'
    # return the string 
    print('return text')
    end = datetime.now()
    print(end-start)
    return text 

def inputs(char_input, loc_input, setting, names, locs):
    """
    Recieves inputs from user, splits characters and locations up
    and translates them into a prefix to start our text with. 
    """
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
        a_chars_in_location.append(f'{", ".join(a_chars[:-1])}' +
                                   f'and {a_chars[-1]} are in the' +
                                   f'{locations[random.randint(0, len(locations)-1)]}.<br>')
        b_chars_in_location.append(f'{", ".join(b_chars[:-1])}' + 
                                   f'and {b_chars[-1]} are in the' + 
                                   f'{locations[random.randint(0, len(locations)-1)]}.<br>')
    if setting:
        setting = f'{setting}.<br>'
    a_chars_in_location[0] += setting
    return a_chars_in_location, b_chars_in_location