from trello import TrelloClient # to import the trello API python library
import urllib2

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
    for i in range(1, first_length):
        for j in range(1, second_length):
            deletion = distance_matrix[i-1][j] + 1
            insertion = distance_matrix[i][j-1] + 1
            substitution = distance_matrix[i-1][j-1]
            if first[i-1] != second[j-1]:
                substitution += 1
            distance_matrix[i][j] = min(insertion, deletion, substitution)
    return distance_matrix[first_length-1][second_length-1]

# Ask the user which board he or she wants to use
boardID = str(input("Please enter the ID of the board you want to look at: "))

# Print the name of the board to make sure we are on the right one
if boardID:
    my_board = client.get_board(board_id=boardID)
else:
    my_board = client.get_board(board_id='588ac0fdb470f37826a8e06c')
print(my_board)


# List of the labels in the board
list_labels = my_board.get_labels()

# List of the cards in the board
list_cards = my_board.get_cards()

# Loop to show to the user the labels that are similar
for i in range(0, len(list_labels)-1):
    for k in range(i+1, len(list_labels)):
        if len(list_labels[i].name) >=2 and len(list_labels[k].name) >= 2 and \
            levenshtein_distance(list_labels[i].name, list_labels[k].name) <= 2:
            print(str(list_labels[i].name), " and ", list_labels[k].name, " are similar")


# Ask the user which label he or she wants to keep
strlabelToKeep = str(input("Please enter the name of the label you want to keep: "))
print("you entered", strlabelToKeep)


similarLabels = list()


# TODO this algorithm is too complex
# TODO 'Exception' is too broad, shoud catch an HTTP error code 400 instead
# TODO tests some limits like having 5 labels, 3 times same label, etc

# Loop in all the labels
for i in range(0, len(list_labels)-1):
    labelToDelete = None
    # If the label we want to king is the one we found, go fetch info and put it in a Label object
    if strlabelToKeep == str(list_labels[i].name):
        labelToKeep = list_labels[i].fetch()
    # if the levenshtein distance is 1 between labelToKind and the label we're on, fetch the
    # info about the Label we have to delete
    if 0 < levenshtein_distance(labelToKeep.name, list_labels[i].name) <= 2:
        labelToDelete = list_labels[i].fetch()
        similarLabels.append(labelToDelete)
        # Loop in all the cards of the board
        for card in range(0, len(list_cards) - 1):
            # Loop in all the labels the current card has
            for label in list_cards[card].labels:
                # If the label we want to delete is the label we currently are on
                if labelToDelete.name == label.name:
                    try:
                        list_cards[card].remove_label(labelToDelete)
                        list_cards[card].add_label(labelToKeep)
                        print("deleted the label ", labelToDelete.name, " and added ", labelToKeep.name)
                    except Exception:
                        print("This label is already on the card")