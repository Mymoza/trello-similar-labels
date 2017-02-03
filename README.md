# trello-similar-labels
Challenge with Trello API in Python

## How to get your Tokens 
`client = TrelloClient(
    api_key='your-key',
    api_secret='your-secret',
    token='your-oauth-token-key',
    token_secret='your-oauth-token-secret'
)`

`api_key : Get it (here)[https://trello.com/app-key] in the "Developer API Key" section. 
`api_secret` : Get it (here)[https://trello.com/app-key] in the OAuth section.

### Get the Trello OAuth tokens

1. Set the following environment variables : 
* TRELLO_API_KEY 
* TRELLO_API_SECRET

To do so, just write, for example: `export $TRELLO_API_KEY=xxx` in a terminal.

2. Run `python ./trello/util.py`
You will get the following output : 

`Request Token:
    - oauth_token        = xxx
    - oauth_token_secret = xxx

Go to the following link in your browser:
https://trello.com/1/OAuthAuthorizeToken?oauth_token=XXX&scope=read,write&expiration=never&name=py-trello`

Go to the link as mentioned, and copy the provided PIN. Authorize it. Write `y` to say yes, and then hit enter. 

`Have you authorized me? (y/n) y
What is the PIN? xxx
Access Token:
    - oauth_token        = !!! YOUR TOKEN !!! 
    - oauth_token_secret = !!! YOUR OTHER SECRET TOKEN !!! 

You may now access protected resources using the access tokens above.`

Paste the PIN when you're asked, and then you'll finally receive your tokens. 

From the config of client earlier, now add these new informations : 
* `token` : oauth_token
* `token_secret` : oauth_token_secret` 
