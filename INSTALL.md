# Steps to use the script

## Clone this repo 

1. Open your terminal window
2. Use `cd` command to go to your desired directory for this project 
3. Use `git clone` with HTTPS or SSH for this repo 

## Create your virtual environment 

1. Open your terminal
2. Change your position to the directory of the actual project 
3. Run `virtualenv -p python3 trello-env` to create your virtual environment 
4. Run `source trello-env-again/bin/activate` to activate your virtual environment 
5. Run `python -V` and make sure you are using Python 3. 

You're done! If you want to exit the environment, run `deactivate` !

## Install the package 
To do this script, I used a [wrapper](https://github.com/sarumont/py-trello) written in Python for the Trello API. 

Run this line to install the package: 

`pip install py-trello`



## How to get your Tokens 

    client = TrelloClient(
        api_key='your-key',
        api_secret='your-secret',
        token='your-oauth-token-key',
        token_secret='your-oauth-token-secret'
    )

### The Trello tokens 

`api_key` : Get it [here](https://trello.com/app-key) in the "Developer API Key" section.

`api_secret` : Get it [here](https://trello.com/app-key) in the OAuth section.

### Get the Trello OAuth tokens

Set the following environment variables : 

* `TRELLO_API_KEY`
* `TRELLO_API_SECRET`

To do so, just write, for example: `export TRELLO_API_KEY=xxx` in a terminal.

*  Run `python ./trello/util.py`

You will get the following output : 

```Request Token:    
        - oauth_token        = xxx
        - oauth_token_secret = xxx
Go to the following link in your browser:
https://trello.com/1/OAuthAuthorizeToken?oauth_token=XXX&scope=read,write&expiration=never&name=py-trello```

Go to the link as mentioned, and copy the provided PIN. Authorize it. Write `y` to say yes, and then hit enter. 
```
Have you authorized me? (y/n) y
What is the PIN? xxx
Access Token:
    - oauth_token        = !!! YOUR TOKEN !!! 
    - oauth_token_secret = !!! YOUR OTHER SECRET TOKEN !!!
You may now access protected resources using the access tokens above.
```

Paste the PIN when you're asked, and then you'll finally receive your tokens. 

From the config of client earlier, now add these new informations : 

* `token` : oauth_token
* `token_secret` : oauth_token_secret

## Run the script 

1. Make sure you are still in the right directory where is the repo. If not, use `cd`.
2. Run `python3 TrelloWrapper.py` to launch the script! 

# To run tests 

Run `python -m unittest tests/Test_TrelloWrapper.py`, but these environment variables must be set: 

* `TRELLO_API_KEY` : your Trello API key
* `TRELLO_TOKEN` : your Trello OAuth token
* `TRELLO_TEST_BOARD_COUNT` : the number of boards in your Trello account
* `TRELLO_TEST_BOARD_NAME` : name of the board to test card manipulation on. Must be unique, or the first match will be used
