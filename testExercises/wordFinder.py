# Exercise to find a word from a given grid 

BOARD = [
    ['a','p','b','e'],
    ['p','r','q','z'],
    ['b','a','p','b']
]
# BOARD = [
#     ['a','p','b','e'],
#     ['c','r','q','z'],
#     ['x','l','g','t']
# ]

x = [-1,-1,-1,0,0,1,1,1]
y = [-1,0,1,-1,1,-1,0,1]

R = 3
C = 4

# This should come out as true
WORD = 'apb' 
# WORD = 'apbe' 

# This should come false
# WORD = 'ABTX'

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
    for row in board:
        for elem in row:
            print(elem, end=' ')
        print()

def search2D(board, row, col, word):
    # if (board[row][col] != word[0]):
    # if (board[row][col] is not word[0]):
    if (board[row][col] is not word[0]):
        # print(board[row][col])
        # print(word[0])
        # print()
        return False
    
    for i in range(0,8):
        rd = row + x[i]
        cd = col + y[i]

        for j in range(1, len(word)):
            # print (j)
            # print(word)
            # print(len(word))
            # print("rd = {},R = {},cd={}.c={}".format(rd,R,cd,C))
            # print("rd = {},cd={}".format(rd,cd))
            if (rd >= R or rd < 0 or cd >= C or cd < 0):
                # print("Outta bounds")
                break
            
            if (board[rd][cd] is not word[j]):
                # print("board: {} didnt match word char: {}".format(board[rd][cd],word[j]))
                break

            rd += x[i]
            cd += y[i]
            # print("board:{} matched word: {}".format(board[rd][cd],word[j]))
        # j + 1
        if(j+1 is (len(word))):
            # print("match found")
            # print("j: {} matched len: {}".format(j, len(word)))
            return True
    # return False

def pattern_search(board, word):
    for row in range(0,R):
        for col in range(0, C):
            # print("in colummn: {}".format(col))
            if(search2D(board, row, col, word)):
                # print(search2D(board, row, col, word))
                print("word '{}' found at {} , {}".format(word,row, col))
                # print()


def main():
    # print_board(BOARD)
    pattern_search(BOARD, WORD)

    #debugging
    # print(search2D(BOARD,0,0,WORD))
    # print(search2D(BOARD,1,1,WORD))

if __name__ == '__main__':
    main()
