from tkinter import *

board = [[0 for x in range(3)] for y in range(3)]
tile_size = 100
player = 'X'
message = ' '
end = '\nClick to Restart'

root = Tk()  # type: Tk
root.grid()
root.config(cursor = 'spider')

canvas = Canvas(root, width=400, height=400)
canvas.pack()
#root.eval('tk::PLaceWindow %s center' % root.winfo_pathname(root.winfo_id()))

class Tile:
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    def is_clicked(self, x, y):
        return x > self.x and x < self.x +tile_size and y > self.y and y < self.y +tile_size

    def is_available(self):
        return self.text is not 'X' and self.text is not 'O'

    def draw(self):
        canvas.create_rectangle(self.x, self.y, tile_size-5+self.x, tile_size-5+self.y, fill = 'black')
        if self.text == 'X':
            canvas.create_text(self.x + tile_size/2, self.y + tile_size/2, fill = 'purple', text = self.text)
        else:
            canvas.create_text(self.x + tile_size/2, self.y + tile_size/2, fill = 'green', text = self.text)

def create_board():
    for r in range(0,3):
        for c in range(0,3):
            board[r][c] = Tile(50 + c * tile_size, 50 + r * tile_size, ' ')

def showBoard():
    for r in range(0,3):
        for c in range(0,3):
            board[r][c].draw()
    canvas.create_text(200, 25, fill ='blue', text = message)

def show_board_console():
    for r in range(0,3):
        for c in range(0,3):
            print(board[r][c].text),
        print("")
    print("")

def change_player():
    global player
    if player == 'X':
        player = 'O'
    else:
        player = 'X'

def reset_board():
    canvas.delete(ALL)
    for r in range(0,3):
        for c in range(0,3):
            board[r][c].text = ' '
    global message
    message = ' '
    global player
    player = 'X'

def is_board_full():
    for r in range(0,3):
        for c in range(0,3):
            if board[r][c].text != 'X' and board[r][c].text != 'O':
                return False
    return True

def is_board_empty():
    for r in range(0,3):
        for c in range(0,3):
            if board[r][c].text == 'X' or board[r][c].text == 'O':
                return False
    return True


def is_winner():
    for i in range(0,3):
        if board[i][0].text is board[i][1].text is board[i][2].text is not ' ' or board[0][i].text is board[1][i].text is board[2][i].text is not ' ':
            return True
    if board[0][0].text is board[1][1].text is board[2][2].text is not ' ' or board[2][0].text is board[1][1].text is board[0][2].text is not ' ':
            return True
    return False

def on_click(event):
    change_player()
    if is_winner() or is_board_full():
        reset_board()
    x = event.x
    y = event.y
    for r in range(0,3):
        for c in range(0,3):
            if board[r][c].is_clicked(x,y) and board[r][c].is_available():
                board[r][c].text = player
    global message
    if is_winner():
        message = player + " WON THE GAME" +end
    elif is_board_full():
        message = "THERE WAS A TIE" + end
    showBoard()

canvas.bind("<Button-1>", on_click)

create_board()
showBoard()

root.mainloop() #for displaying window
