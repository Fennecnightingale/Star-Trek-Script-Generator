Generating Star Trek scripts with GPT-2<br>
Author: Fennec C. Nightingale<br>

<img width="1000" alt="lcars panel 1" src="https://user-images.githubusercontent.com/68678808/125071899-bef9d300-e06e-11eb-8fcd-becbcbb08fbe.jpg"><br><br>

<font size="+5"><center>Overview</center></font><br>
Writing storylines is incredibly difficult, for even the most experienced humans. and Star Trek is near and dear to my and many other fans hearts, which is why it's so truly tragic when somehow a particularly bad episode makes its way out of the writers room, or shows get cancelled seemingly out of nowhere. This project was put together hoping we can use the mistakes of the past and the technology of the future (machine learning!) to ensure the future of Star Trek is always looking as bright as the future Star Trek promises. <br>

<font size="+5"><center>Business Problem</center></font><br>
Sometimes you come up with just a scene or a word and you aren't quite sure where to take it. Wether you're suffering from witers block, looking to jazz your stories up a bit, just love Star Trek, or are hoping to incorporate the same sort of feeling into your work, this script generator is here for you to use for a wide variety of applications as well as just getting more comfortable with and diving a bit deeper into machine learning than you might have done previously. How will you know if your scripts are any good? Test out my proof of concept script review predictor to see what your season ratings might roughly look like based on the episode you inspired. <br><br><br><br>

<img width="1000" alt="lcars panel 2" src="https://user-images.githubusercontent.com/68678808/125073788-54966200-e071-11eb-8da7-788ce90bbfee.png">


Method<br>
I used the OSEMN process while developing this project, taking an iterative approach and trying many different methods of exploration and generation. 

O - Obtain Data<br>

Over the last 50+ years roughly 400 hours of Star Trek have aired, for this project I gathered every script available online. <br>

This required sourcing scripts from a variety of sites online: <br>
https://www.st-minutiae.com/resources/scripts/<br>
http://www.chakoteya.net/StarTrek/<br>
https://scifi.media/star-trek/transcripts/<br>
https://subslikescript.com/ (Names not listed, had to rewatch all recent series and hand enter names as people spoke)<br>
https://scrapsfromtheloft.com/ (Names partially listed, had to rewatch all recent series and hand enter names)<br>


S - Scrub Data<br> 
Cleaning up and scrubbing the scripts involved reformatting them so that all of the lines read the same, breaking them up into 4 roughly equal parts after personally determining when scenes have ended, fixing typos and standardizing punctuation and spacing, and removing stop words and lemmatizing the text to see our most frequent/relevant words.

E - Explore Data<br>
Outside of reading scripts & watching the show, exploring the data took the form of comparing the number of lines each person has, looking at the differences in word counts between series, trying to determine if positivity or negativity had any correlation with ratings, and other interesting comparisons of location frequencies, most frequent phrases, and anything else I could think of that might make a good feature for my model. 

M - Model Data<br> 
In this project I did 2 different forms of modeling,
My main text generator is a GPT-2 model, trained on scripts slipt up into quarters, as it gave the best storyline with starts and ends compared to one, two, or 3 splits. In total there are 44 models, 4 for each series, and one for Old-Trek as well as another for New-Trek; These models trained for 100s of hours, sometimes getting overtrained, sometimes under, until I found a point that turned out just right. 
The second kind of model is a linear regression model with TDIDF vectorization that is meant as a proof of concept review predictor, which hopefully someday with enough data will be capable of telling the difference btween good and bad scripts, making text generation that much easier!  


iNterpret Results<br>

Conclusions<br>
My recommendations are on how a buisness like Paramount that is interested in my product could help to make it a reality, with reasonable assumptions made with the analysis done on the data I collected, due to the fact that currently, there is not enough data to draw any meaningful statistical conclusions from my modeling and therefore it is currently just a proof of concept. That said, this analysis leads me to make these three recommendations:<br>

ONE. <br>
Use books & other approved media to train more robust models that can make more accurate predictions.<br>
TWO. <br>
Standardize script formatting for easier use in future projects.<br>
THREE. <br>
Expirement with generating unique new feautres that may give more complete insight into fans wants.<br>

Future Work<br>
Train on newer and/or larger models (GPT-3/1558M)<br>
Add more scripts, wether branching out into more general Sci-Fi or waiting for more Star Trek. <br>
Exlpore the scripts in more fun ways to learn more about the series. <br>
Create chatbots for individual characters. <br> 

For More Information<br>
See the full analysis in my Jupyter Notebook or review my Presentation.<br>

For additional info, contact me at: fenneccharles@gmail.com<br>

Repository Structure<br>
```
├──.ipynb_checkpoints
├──.gitignore
├──data
    ├─
├──Images
    ├── 
├── pdfs
    ├──
├──
├── README.ipynb
└──.tars
