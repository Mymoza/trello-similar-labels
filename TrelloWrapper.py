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

def levenshtein_distance(first, second):
    # Source: https://www.stavros.io/posts/finding-the-levenshtein-distance-in-python/
    """Find the Levenshtein distance between two strings."""
    if len(first) > len(second):
        first, second = second, first
    if len(second) == 0:
        return len(first)
    first_length = len(first) + 1
    second_length = len(second) + 1
    distance_matrix = [[0] * second_length for x in range(first_length)]
    for i in range(first_length):
       distance_matrix[i][0] = i
    for j in range(second_length):
       distance_matrix[0][j]=j
    for i in xrange(1, first_length):
        for j in range(1, second_length):
            deletion = distance_matrix[i-1][j] + 1
            insertion = distance_matrix[i][j-1] + 1
            substitution = distance_matrix[i-1][j-1]
            if first[i-1] != second[j-1]:
                substitution += 1
            distance_matrix[i][j] = min(insertion, deletion, substitution)
    return distance_matrix[first_length-1][second_length-1]

# Print the name of the board to make sure we are on the right one
my_board = client.get_board(board_id='588ac0fdb470f37826a8e06c')
print my_board


list_labels = my_board.get_labels()

for i in range(0, len(list_labels)-1):
    for k in range(i+1, len(list_labels)):
        if len(list_labels[i].name) >=2 and len(list_labels[k].name) >= 2 and levenshtein_distance(list_labels[i].name, list_labels[k].name) == 1:
            print list_labels[i].name, " and ", list_labels[k].name, " are similar"



# Print the labels of the board
print my_board.get_labels()

# Print the labels of the boards in ID
obj = client.fetch_json('/boards/588ac0fdb470f37826a8e06c/labels',  http_method='GET')
print obj




