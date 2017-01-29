from trello import TrelloClient # to import the trello API python library

# api_key : get it from Trello
# api_secret : get it from Trello
# token : set API_KEY and API_SECRET as ENV variables and then Run the script to get your token
# token_scret : same as for token you will recieve it at the same time
client = TrelloClient(
    api_key='api_key',
    api_secret='api_secret',
    token='token',
    token_secret='token_secret'
)


# Print the name of the board to make sure we are on the right one
my_board = client.get_board(board_id='588ac0fdb470f37826a8e06c')
print my_board

# Print the labels of the board
print my_board.get_labels()

# Print the labels of the boards in ID
obj = client.fetch_json('/boards/588ac0fdb470f37826a8e06c/labels',  http_method='GET')
print obj




