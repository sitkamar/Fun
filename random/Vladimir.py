from freegames import floor, vector
from random import choice
from turtle import *
from freegames import vector, square

class Vladimir():
    board = []
    n = None
    help = []
    def __init__(self,n):
        self.n = n
        print(self.n)
        self.board = [[-1 for i in range(self.n)] for j in range(self.n)]
        for i in range(self.n-1):
            self.makeSection(i)
        self.draw()
    def toString(self):
        s = ""
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                s += str(self.board[i][j]) + " "
            s += "\n"
        return s
    def draw(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                colour = 'grey' if self.board[i][j] == -1 else 'black' if self.board[i][j] == 0 else 'red' if self.board[i][j] == 1 else 'blue' if self.board[i][j] == 2 else 'yellow' if self.board[i][j] == 3 else 'purple' if self.board[i][j] == 4 else 'green' if self.board[i][j] == 5 else 'orange' if self.board[i][j] == 6 else 'brown' if self.board[i][j] == 7 else 'pink' if self.board[i][j] == 8 else 'grey' if self.board[i][j] == 9 else 'white'
                square(100-i*20, 100-j*20, 20, colour)
                
    def makeSection(self, sec):
        section = [self.getFirstEmpty(self.board)]
        self.board[section[0][0]][section[0][1]] = sec
        choices = self.getChoices(self.board, section)
        banned = []
        i = 0
        while i < self.n-1:
            newChoices = self.getChoices(self.board, section[-1])
            for ch in newChoices:
                if ch not in section and ch not in choices and ch not in banned:
                    choices.append(ch)
            if len(choices) == 0:
                i +=self.fill(section, banned)
                banned = []
            else:
                final = choice(choices)
                if self.checkContinuity(self.board, final,self.n-i-1) == True and self.board[final[0]][final[1]] == -1:
                    section.append(final)
                    self.board[final[0]][final[1]] = sec
                    banned = []
                    i+=1
                else:
                    banned.append(final)
                choices.remove(final)
        return section
    def fill(self,section, banned):
        used = len(section)
        for b in banned:
            filling = self.checkContinuity(self.board, b, left=self.n-len(section)-1)
            if filling == True:
                pass
            else:
                filling.append(b)
                if len(filling) < self.n-len(section):
                    for f in filling:
                        self.board[f[0]][f[1]] = self.board[section[0][0]][section[0][1]]
                    break
        return len(section)-used
        
    
    # def filler(self, board, pos, left):
    #     if left == 1:
    #         if self.checkContinuity(board, pos,0):
    #             self.help.append(pos)
    #             return True
    #         else:
    #             board[pos[0]][pos[1]] = -1
    #             return False
    #     board[pos[0]][pos[1]] = self.n + 2
    #     answers = []
    #     choices = self.getChoices(board, pos)
    #     if len(choices)==0:
    #         if self.checkContinuity(board, pos,left-1):
    #             self.help.append(pos)
    #             return True
    #         else:
    #             board[pos[0]][pos[1]] = -1
    #             return False 
    #     for ch in choices:
    #         if self.filler(board,ch,left-1):
    #             self.help.append(pos)
    #             return True
    #         else:
    #             board[pos[0]][pos[1]] = -1
    #     return False
    def checkContinuity(self, board, pos, left):
        choices = []
        copyBoard = []
        for row in self.board:
            copyBoard.append(row.copy())
        copyBoard[pos[0]][pos[1]] = self.n + 1
        while self.getFirstEmpty(copyBoard) != None:
            section = [self.getFirstEmpty(copyBoard)]
            copyBoard[section[0][0]][section[0][1]] = self.n
            choices = self.getChoices(copyBoard, section[0])
            max = 0
            while len(choices) !=0:
                for ch in choices:
                    if ch not in section:
                        section.append(ch)
                        copyBoard[ch[0]][ch[1]] = self.n
                choices = []
                for seg in section:
                    choices += self.getChoices(copyBoard, seg)
            if (len(section)-left+1)% self.n != 0:
                return section
        return True
    def getFirstEmpty(self, board):
        for i in range(0,len(board)):
            for j in range(0,len(board[i])):
                if board[i][j] == -1:
                    return [i, j]
        return None
    def getChoices(self, board, section):
        choces = []
        try:
            if board[section[0]+1][section[1]] == -1 and section[0]+1 < len(board):
                choces.append([section[0]+1, section[1]])
        except:
            pass
        try:
            if board[section[0]][section[1]+1] == -1 and section[1]+1 < len(board[0]):
                choces.append([section[0], section[1]+1])
        except:
            pass
        try:
            if board[section[0]-1][section[1]] == -1 and section[0]-1 >= 0:
                choces.append([section[0]-1, section[1]])
        except:
            pass
        try:
            if board[section[0]][section[1]-1] == -1 and section[1]-1 >= 0:
                choces.append([section[0], section[1]-1])
        except:
            pass
        return choces
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
vladimir = Vladimir(9)
done()