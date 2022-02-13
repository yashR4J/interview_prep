from typing import List

def firstDuplicate(a):
    # Given an array a that contains only numbers in the 
    # range from 1 to a.length, find the first duplicate 
    # number for which the second occurrence has the minimal 
    # index. In other words, if there are more than 1 duplicated 
    # numbers, return the number for which the second occurrence 
    # has a smaller index than the second occurrence of the other 
    # number does. If there are no such elements, return -1.
    
    aset = set()
    for x in a:
        if x in aset:
            return x
        else:
            aset.add(x)
    return -1

def firstNotRepeatingCharacter(s):
    # Given a string s consisting of small English letters, find 
    # and return the first instance of a non-repeating character 
    # in it. If there is no such character, return '_'.
    for c in s:
        if s.index(c) == s.rindex(c):
            return c
    return "_"

def rotateImage(a):
    # You are given an n x n 2D matrix that represents an image. 
    # Rotate the image by 90 degrees (clockwise).
    
    # # Solution 1
    # b = [[0]*len(a) for i in range(len(a))]
    # for x in range(len(a[0])):
    #     for y in range(len(a)):
    #         b[x][y] = a[len(a)-y-1][x]
    # return b
    
    # # Solution 2
    return list(zip(*reversed(a)))

class SodukuSolution:   
    def __print_board(self, board: List[List[str]]):
        for i in range(len(board)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - - ")

            for j in range(len(board[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(board[i][j])
                else:
                    print(str(board[i][j]) + " ", end="")
        print("\n")
         
    def __find_empty(self, board: List[List[str]]):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    return (i, j)  # row, col

        return None
            
    def __solve(self, board: List[List[str]]) -> bool:    
        find = self.__find_empty(board)
        if not find: return True
        else: row, col = find 

        for i in range(1, 10):
            if self.__valid(board, i, (row, col)):
                board[row][col] = str(i)
                if self.__solve(board):
                    return True
                board[row][col] = "."

        return False

    def __valid(self, board: List[List[str]], num: int, pos) -> bool:
        # Check if any other box in the same row has already has the number
        for i in range(len(board[0])):
            if board[pos[0]][i] == str(num) and pos[1] != i:
                return False

        # Check if any other box in the same col has already has the number
        for i in range(len(board)):
            if board[i][pos[1]] == str(num) and pos[0] != i:
                return False

        # Find the box the position is in
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x * 3, box_x*3 + 3):
                if board[i][j] == str(num) and (i,j) != pos:
                    return False

        return True
        
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.__print_board(board)
        self.__solve(board)
        self.__print_board(board)

def soduku(grid):
    # Sudoku is a number-placement puzzle. The objective is to 
    # fill a 9 × 9 grid with numbers in such a way that each 
    # column, each row, and each of the nine 3 × 3 sub-grids 
    # that compose the grid all contain all of the numbers from 
    # 1 to 9 one time.

    # Implement an algorithm that will check whether the given 
    # grid of numbers represents a valid Sudoku puzzle according 
    # to the layout rules described above. Note that the puzzle 
    # represented by grid does not have to be solvable.
    
    rows = grid
    cols = zip(*grid)
    sqrs = []
    
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            sqrs.append([grid[r][c] for r in range(i, i+3) for c in range(j, j+3)])
            
    def valid(arr):
        nums = [x for x in arr if str.isdigit(x)]
        return len(nums) == len(set(nums))
    
    return all([
        all(map(valid, rows)),
        all(map(valid, cols)),
        all(map(valid, sqrs))
    ])
# board = [["4",".",".","9",".",".",".",".","1"],
#          [".","9","7",".","5","1",".","6","."],
#          ["2",".","1",".",".",".","7",".","."],
#          ["1",".",".",".",".","3",".","4","."],
#          [".",".","2",".",".",".","1",".","."],
#          [".","7","5","1",".",".","3",".","."],
#          ["7","1","3","5",".",".","4",".","."],
#          ["9",".",".",".","1",".",".",".","."],
#          [".",".",".",".","6",".",".","1","8"]]

# x = SodukuSolution()
# x.solveSudoku(board)

def isCryptSolution(crypt, solution):
    crypt_s = crypt
    for i in range(0, 3):
        for s in solution:
            crypt_s[i] = crypt_s[i].replace(s[0], s[1])
        
        if crypt_s[i] != '0' and crypt_s[i][0] == '0':
            return False
        
    if int(crypt_s[0]) + int(crypt_s[1]) != int(crypt_s[2]):
        return False
    
    return True
