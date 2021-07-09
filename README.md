## Generating Star Trek scripts with GPT-2
### Author: Fennec C. Nightingale<br>

<img width="1000" alt="UFP logo" src="https://user-images.githubusercontent.com/68678808/125075120-0eda9900-e073-11eb-8789-877db73e5323.png"><br><br>
<img width="1000" alt="lcars panel 1" src="https://user-images.githubusercontent.com/68678808/125074916-c9b66700-e072-11eb-8807-50fa8b6aad75.png"><br><br>



##  <center>Overview</center><br>
Writing storylines is incredibly difficult, for even the most experienced humans. and Star Trek is near and dear to my and many other fans hearts, which is why it's so truly tragic when somehow a particularly bad episode makes its way out of the writers room, or shows get cancelled seemingly out of nowhere. This project was put together hoping we can use the mistakes of the past and the technology of the future (machine learning!) to ensure the future of Star Trek is always looking as bright as the future Star Trek promises. <br>

## <center>Business Problem</center><br>
Sometimes you come up with just a scene or a word and you aren't quite sure where to take it. Wether you're suffering from witers block, looking to jazz your stories up a bit, just love Star Trek, or are hoping to incorporate the same sort of feeling into your work, this script generator is here for you to use for a wide variety of applications as well as just getting more comfortable with and diving a bit deeper into machine learning than you might have done previously. How will you know if your scripts are any good? Test out my proof of concept script review predictor to see what your season ratings might roughly look like based on the episode you inspired. 
<br><br>
<img width="1000" alt="lcars panel 2" src="https://user-images.githubusercontent.com/68678808/125075304-434e5500-e073-11eb-8116-9de37a6eca4f.png">

<br><br><br><br><br><br><br><br><br>

<img width="1000" alt="lcars panel 2" src="https://user-images.githubusercontent.com/68678808/125075325-4d705380-e073-11eb-8738-2733de4e5fab.png">


## Method<br>
I used the OSEMN process while developing this project, taking an iterative approach and trying many different methods of exploration and generation. 

### O - Obtain Data<br>

Over the last 50+ years roughly 400 hours of Star Trek have aired, for this project I gathered every script available online. <br>

This required sourcing scripts from a variety of sites online: <br>
https://www.st-minutiae.com/resources/scripts/<br>
http://www.chakoteya.net/StarTrek/<br>
https://scifi.media/star-trek/transcripts/<br>
https://subslikescript.com/ (Names not listed, had to rewatch all recent series and hand enter names as people spoke)<br>
https://scrapsfromtheloft.com/ (Names partially listed, had to rewatch all recent series and hand enter names)<br>


### S - Scrub Data<br> 
Cleaning up and scrubbing the scripts involved reformatting them so that all of the lines read the same, breaking them up into 4 roughly equal parts after personally determining when scenes have ended, fixing typos and standardizing punctuation and spacing, and removing stop words and lemmatizing the text to see our most frequent/relevant words.

### E - Explore Data<br>
Outside of reading scripts & watching the show, exploring the data took the form of comparing the number of lines each person has, looking at the differences in word counts between series, trying to determine if positivity or negativity had any correlation with ratings, and other interesting comparisons of location frequencies, most frequent phrases, and anything else I could think of that might make a good feature for my model. One of my favorite ways to explore the data was looking at what different kinds of characters have to say, like in these words plots below which show the most commonly used, mostly unique words that Captains, Doctors, and Engineers of Star Trek use. 

#### Captains
![captains](https://user-images.githubusercontent.com/68678808/125079738-d211a080-e078-11eb-8a54-2a99b08429ea.png)
#### Doctors 
![doctors](https://user-images.githubusercontent.com/68678808/125079786-dccc3580-e078-11eb-94fa-0afc868f14f4.png)
#### Engineers 
![engineers](https://user-images.githubusercontent.com/68678808/125079794-dfc72600-e078-11eb-8e2f-438387600aa5.png)


### M - Model Data<br> 
In this project I did 2 different forms of modeling,
My main text generator is a GPT-2 model, trained on scripts slipt up into quarters, as it gave the best storyline with starts and ends compared to one, two, or 3 splits. In total there are 44 models, 4 for each series, and one for Old-Trek as well as another for New-Trek; These models trained for 100s of hours, sometimes getting overtrained, sometimes under, until I found a point that turned out just right. 
The second kind of model is a linear regression model with TDIDF vectorization that is meant as a proof of concept review predictor, which hopefully someday with enough data will be capable of telling the difference btween good and bad scripts, making text generation that much easier!  


### iNterpret Results<br>

<img width="1000" alt="bttm 2" src="https://user-images.githubusercontent.com/68678808/125076045-439b2000-e074-11eb-883f-7f7254a1e315.png"><br><br><br><br><br><br><br><br><br>

<img width="1000" alt="env 1" src="https://user-images.githubusercontent.com/68678808/125076285-970d6e00-e074-11eb-87f8-ba095b2a5dd3.png">

## Conclusions<br>
My recommendations are on how a buisness like Paramount that is interested in my product could help to make it a reality, with reasonable assumptions made with the analysis done on the data I collected, due to the fact that currently, there is not enough data to draw any meaningful statistical conclusions from my modeling and therefore it is currently just a proof of concept. That said, this analysis leads me to make these three recommendations:<br>

### -- Use books & other approved media to train more robust models that can make more accurate predictions.<br>
### -- Standardize script formatting for easier use in future projects.<br>
### -- Expirement with generating unique new feautres that may give more complete insight into fans wants.<br>

## Future Work<br>
Train on newer and/or larger models (GPT-3/1558M)<br>
Add more scripts, wether branching out into more general Sci-Fi or waiting for more Star Trek. <br>
Exlpore the scripts in more fun ways to learn more about the series. <br>
Create chatbots for individual characters. <br> 

### For More Information<br>
See the full analysis in my Jupyter Notebook or review my Presentation.<br>

For additional info, contact me at: fenneccharles@gmail.com<br>

<img width="1000" alt="bttm 3" src="https://user-images.githubusercontent.com/68678808/125076529-e2c01780-e074-11eb-8d90-60176722f093.png">
<br><br><br><br><br><br><br><br><br>


Repository Structure<br>
```
├──.ipynb_checkpoints
├──.gitignore
├──data
    ├─ -0.txt ~ -797.txt
├──Images
    ├── captains.png
    ├── doctors.png
    ├── engineers.png
├── main
    ├──_pycache_
    ├──migrations
    ├──py
        ├──_pycache_
            ├──Constants.cpython-37.pyc
            ├──generations.cpython-37.pyc
        ├──.ipynb_checkpoints
        ├──Constants.py
        ├──Generations.py
    ├──static
        ├──css
            ├──stlye.css
        ├──fonts
            ├──FinalFrontierOldStyle-8Pg.ttf
            ├──Startrekfuture-EK6e.ttf
        ├──images
            ├──byo.png
            ├──lcars.png
            ├──random.png
        ├──js
            ├──script.js
    ├──templates
        ├──index.html
        ├──text.html
    ├──__init__.py
    ├──admin.py
    ├──apps.py
    ├──models.py
    ├──tests.py
    ├──urls.py
    ├──views.py
├── models (empty until Download_Checkpoints.py is run)
    ├──1558M
        ├──checkpoint
        ├──encoder.json
        ├──hparams.json
        ├──model.ckpt.data-00000-of-00001
        ├──model.ckpt.index
        ├──model.ckpt.meta
        ├──vocab.bpe
├── pdfs
    ├──
├── tars 
    ├──checkpoint_a.tar
    ├──checkpoint_b.tar
    ├──checkpoint_c.tar
    ├──checkpoint_d.tar
    ├──checkpoint_old_a.tar
    ├──checkpoint_old_b.tar
    ├──checkpoint_old_c.tar
    ├──checkpoint_old_d.tar
    ├──checkpoint_new_a.tar
    ├──checkpoint_new_b.tar
    ├──checkpoint_new_c.tar
    ├──checkpoint_new_d.tar
    ├──checkpoint_TOS_A.tar
    ├──checkpoint_TOS_B.tar
    ├──checkpoint_TOS_C.tar
    ├──checkpoint_TOS_D.tar
    ├──checkpoint_TNG_A.tar
    ├──checkpoint_TNG_B.tar
    ├──checkpoint_TNG_C.tar
    ├──checkpoint_TNG_D.tar
    ├──checkpoint_DS9_A.tar
    ├──checkpoint_DS9_B.tar
    ├──checkpoint_DS9_C.tar
    ├──checkpoint_DS9_D.tar
    ├──checkpoint_VOY_A.tar
    ├──checkpoint_VOY_B.tar
    ├──checkpoint_VOY_C.tar
    ├──checkpoint_VOY_D.tar
    ├──checkpoint_ENT_A.tar
    ├──checkpoint_ENT_B.tar
    ├──checkpoint_ENT_C.tar
    ├──checkpoint_ENT_D.tar
    ├──checkpoint_DSC_A.tar
    ├──checkpoint_DSC_B.tar
    ├──checkpoint_DSC_C.tar
    ├──checkpoint_DSC_D.tar
    ├──checkpoint_PIC_A.tar
    ├──checkpoint_PIC_B.tar
    ├──checkpoint_PIC_C.tar
    ├──checkpoint_PIC_D.tar
    ├──checkpoint_LD_A.tar
    ├──checkpoint_LD_B.tar
    ├──checkpoint_LD_C.tar
    ├──checkpoint_LD_D.tar
    ├── NOTE.txt
├──trekgenerator
    ├──__pycache__
        ├──__init__.cpython-37.pyc
        ├──settings.cpython-37.pyc
        ├──urls.cpython-37.pyc
        ├──wsgi.cpython-37.pyc
    ├──__init__.py
    ├──settings.py
    ├──urls.py
    ├──asgi.py
    ├──wsgi.py
├──.gitattributes
├──db.sqlite3
├──Download_Checkpoints.py
├──environment.yml
├──Linear_Regression.ipynb
├──manage.py
└──README.ipynb
