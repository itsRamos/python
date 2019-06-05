# Exercise to find a word from a given grid 
BOARD = [
    ['h','i','h','e','l','l','o'],
    ['p','e','q','z','h','e','l'],
    ['y','h','h','i','o','l','l']
]

# Variables to search in all directions
x = [-1,-1,-1,0,0,1,1,1]
y = [-1,0,1,-1,1,-1,0,1]

# Variables to define the size of the board
R = 3
C = 7

# Function to print elements of the given board
def print_board_long(board):
    n = len(board)
    for board_row in range(n):
        board_element = board[board_row]
        k = len(board_element)
        
        for board_col in range(k):
            print(board_element[board_col], end = ' ')
        print()

# more optimized way to print the given board
def print_board(board):
    print("#BOARD#")
    for row in board:
        for elem in row:
            print(elem, end=' ')
        print()


# Function to search for the adjacent letters
def search_board(board, row, col, word):
    if (board[row][col] is not word[0]):
        return False
    
    for i in range(0,8):
        rd = row + x[i]
        cd = col + y[i]

        for j in range(1, len(word)):
            # If search goes out of bounds (edges)
            if (rd >= R or rd < 0 or cd >= C or cd < 0):
                break
            
            if (board[rd][cd] is not word[j]):
                break

            rd += x[i]
            cd += y[i]
        
        if(j+1 is (len(word))):
            return True


# Function to search the board
def pattern_search(board, word):
    for row in range(0,R):
        for col in range(0, C):
            if(search_board(board, row, col, word)):
                print("word '{}' found at {} , {}".format(word,row, col))


# Function to print a single word
def find_single_word(word):
    print_board(BOARD)
    pattern_search(BOARD, word)


# Function to print multiple words
def find_multiple_words(list_of_words):
    print_board(BOARD)
    n = len(list_of_words)
    for i in range(n):
        pattern_search(BOARD, list_of_words[i])


def main():
    WORD = 'hi'
    find_single_word(WORD)

    WORDS = ['hi','hello']
    find_multiple_words(WORDS)
 

if __name__ == '__main__':
    main()
