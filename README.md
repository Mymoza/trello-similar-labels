# Trello-Similar-Labels
Challenge with Trello API in Python. This script can be used to detect similar label in a Trello board. 

## How to use + install this script 

Read the INSTALL file :)


## What I learned while playing with Python + Trello API + ...

Wow, I never thought I would encounter so much troubles while making this project. However, I can honestly say I am proud of myself because I learned a lot. And I can admit : I thought I knew python, but oh, I was wrong! 

There is so much things I learned, and I'm not even done with this projet. 

Bugs I had to fix: 

* I created at least 5 different virtual environments. Yup. At least now I can say I think _hope_ I understand them now and won't be making huge mistakes anymore! 

* I had troubles with `brew`. I did a `brew doctor` and I detected a problem with the message `unlinked kegs in your Cellar` this was with python3. I fixed it with `brew link --overwrite python3`...

* I had troubles to use pip. When I was doing `pip install`, it always said `permission denied`! When I looked around on the internet on a way to fix this, I read that it's not a "good practice" to use sudo. So then I found myself searching for an hour or two how to solve this problem without using sudo, because it's not the best thing to do. If I recall correctly, I fixed this problem with a parameter like `--user` or `easy_install` 

* I had another problem with pip. It said I needed to upgrade pip to solve the problem. I did, but at the same time I created another problem elsewhere. I searched a bit on StackOverflow and was able to fix the problem with another command... 

* The package I chose to use (py-trello) didn't have much documentation. I must admit it took me hours to understand how to get my OAuth tokens (never used that before)! I understood how it all worked when, by luck, I found a file in the package which had the information on how to get those tokens!!! I was so glad to found documentation in the code itself. That's another lesson learned. 

* I also had troubles to import the modules `requests`. It doesn't seems to be the same in python 2.7 than in python 3. Even though the package is supposed to work with 2.7, I tried to update my virutalenvironment to 3 to see if that would fix the requests import. It did, mostly. 

* Launching the script in the commandline didn't work at first. So much fun! Everything looked great, so that's also another reason why I updated to python 3. When I successfully created another virtual environment with python 3, my script was executing in the command line! 

* Installing the requirements from `requirements.txt` wasn't an easy tasks ! 

* Did you know that if you are already in a virtual environment, let's say "marie", if you run again `virtualenv marie` you will overwrite it?!!! You should! I wanted to activate my virtualenv and I just deleted my env all over again. Ugh! Please, run `source marie/bin/activate` if you want to activate the environment! Not `virtualenv` again...! 

... Wow, this list is huge. At least I can be proud of what I accomplished! It took me 10 hours for now. 

## Cool things to note 

* I also learned about the Levenhstein distance algorithm, which is fun to work with ! 

* I am super proud that, at first, my algorithm that checks  for similar labels had a complexity of O(N^2). I wasn't glad because I thought it was too complex for no reason. I was super happy when I was able to use what I am currently learning in LOG320 (Algorithm and data structures) to reduce the complexity to O(N(N+1)/2) which is what happens when you reduce how much you iterate (`i+1`) in the second loop.


## What's next ? 

1. Work on tests  

2. Complete the INSTALL.md for the installation process

3. Clean the code in comments (used as examples to go further) + add some comments to help understand the code (PEP8)

4. I hope I am able to merge similar labels in the next days 

5. I'd like to ask the user which board he wants to use for the detection 

6. I'd love to use Flask or Django to do a mini web app (never used those two), would be a learning activity too! 
