"""
Created by Riley Verdier Feb 7, 2021
"""
# Assignment 2 is a maze search algorithm that's goal is to find the optimal path using two different algorithms
# The first is Breadth First Search and the second is Depth First Search

totalBFS = 0
totalDFS = 0

# Dr. Kolta
maze1 = [[" |", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯|"],
         [" |", " |", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", " |"],
         [" |", " |", "  ", "¯ ", "¯ ", "¯ ", "¯|", "¯ ", "¯ ", "¯ ", " |"],
         [" |", " |", "¯ ", "¯ ", "¯ ", " |", "¯ ", "¯ ", "¯ ", "¯ ", "¯|"],
         [" |", " |", "  ", "  ", "  ", " |", "  ", "¯|", "¯ ", "¯|", " |"],
         [" |", " |", "  ", "  ", "  ", "  ", "¯ ", "¯ ", "¯ ", "¯ ", " |"],
         [" |", " |", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", " |"],
         [" |", " |", " |", "¯ ", "¯|", "¯ ", "¯|", "¯|", "¯|", "¯ ", " |"],
         [" |", " |", " |", " |", " |", " |", " |", "  ", " |", "  ", "¯|"],
         [" |", " |", "  ", " |", "  ", " |", "  ", "¯ ", "  ", "¯ ", " |"],
         ["  ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ "]]

# Riley
maze2 = [[" |", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯|"],
         [" |", " |", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", " |"],
         [" |", " |", "  ", "¯ ", "¯ ", "¯ ", "¯|", "¯ ", "¯ ", "¯ ", " |"],
         [" |", " |", "¯ ", "¯ ", "¯ ", " |", "¯ ", "¯ ", "¯ ", "¯ ", "¯|"],
         [" |", " |", "  ", "  ", "  ", " |", "  ", "¯ ", "¯ ", "¯|", " |"],
         [" |", " |", "  ", "  ", "  ", "  ", "¯ ", "¯ ", "¯ ", "¯ ", " |"],
         [" |", " |", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", " |"],
         [" |", " |", " |", "¯ ", "¯|", "¯ ", "¯|", "¯|", "¯|", "¯ ", " |"],
         [" |", " |", " |", " |", " |", " |", " |", "  ", " |", "  ", "¯|"],
         [" |", " |", "  ", " |", "  ", " |", "  ", "¯ ", "  ", "¯ ", "¯|"],
         ["  ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ "]]


# Constructor for cell info
class Cell:
    # Initializes the constructor to have position of the current cell and have the previous cell/parent
    def __init__(self, position: (), previous: ()):
        self.position = position
        self.previous = previous

    # Allows for two nodes positions to be compared to one another
    def __eq__(self, other):
        return self.position == other.position

    def __getitem__(self, item):
        return self.position == item.position


# Function to determine if given a cell and direction, can it move in said direction
def movable(cell, direction):
    # Checks to make sure coordinates are 0 or positive numbers
    if cell[0] < 0 or cell[1] < 0:
        return False

    # Creates default variables to return a boolean and r for row and c for column
    canMove = False
    r = cell[0]
    c = cell[1]

    # If direction is up
    if direction == 'U':
        if r - 1 >= 0:
            value = maze1[r][c]
            if '¯' not in value:
                canMove = True

    # If direction is down
    if direction == 'D':
        if r + 1 < len(maze1):
            value = maze1[r + 1][c]
            if '¯' not in value:
                canMove = True

    # If direction is right
    if direction == 'R':
        if c + 1 < len(maze1[0]):
            value = maze1[r][c]
            if '|' not in value:
                canMove = True

    # If direction is left
    if direction == 'L':
        if c - 1 >= 0:
            value = maze1[r][c - 1]
            if '|' not in value:
                canMove = True

    return canMove


# This function is the first agent used, the breadth first search, parameters are start and goal
def bfs(s, g):
    # Queues and variables used
    fifoQueue = []
    nodeVisited = []
    startingNode = Cell(s, None)
    endingNode = Cell(g, None)

    # Adds first node to queue without parent
    fifoQueue.append(startingNode)

    # Loops until queue is empty or until solution is found or until an error occurs
    while len(fifoQueue) > 0:
        global totalBFS
        totalBFS += 1
        currCell = fifoQueue.pop(0)
        nodeVisited.append(currCell)

        if currCell == endingNode:
            optimalSolution = []
            while currCell != startingNode:
                optimalSolution.append(currCell.position)
                currCell = currCell.previous

            return optimalSolution

        (x, y) = currCell.position
        directions = ['U', 'D', 'R', 'L']

        for d in directions:
            nextCell = []
            canMove = movable([x, y], d)
            if not canMove:
                continue

            # Determines next cell by using the direction to move in the direction it found movable
            if d == 'U':
                nextCell.append(x - 1)
                nextCell.append(y)
            elif d == 'D':
                nextCell.append(x + 1)
                nextCell.append(y)
            elif d == 'R':
                nextCell.append(x)
                nextCell.append(y + 1)
            elif d == 'L':
                nextCell.append(x)
                nextCell.append(y - 1)
            else:
                continue

            next = Cell(nextCell, currCell)

            if next in nodeVisited:
                continue
            elif next not in fifoQueue:
                fifoQueue.append(Cell(nextCell, currCell))

    return 'No optimal path found, maze is not solvable!'


# This function is the first agent used, the breadth first search, parameters are start and goal
def dfs(s, g):
    # Queues and variables used
    lifoStack = []
    nodeVisited = []
    startingNode = Cell(s, None)
    endingNode = Cell(g, None)

    # Adds first node to queue without parent
    lifoStack.append(startingNode)

    # Loops until queue is empty or until solution is found or until an error occurs
    while len(lifoStack) > 0:
        global totalDFS
        totalDFS += 1
        currCell = lifoStack.pop()
        nodeVisited.append(currCell)

        if currCell == endingNode:
            optimalSolution = []
            while currCell != startingNode:
                optimalSolution.append(currCell.position)
                currCell = currCell.previous

            return optimalSolution

        (x, y) = currCell.position
        directions = ['U', 'D', 'L', 'R']

        for d in directions:
            nextCell = []
            canMove = movable([x, y], d)
            if not canMove:
                continue

            # Determines next cell by using the direction to move in the direction it found movable
            if d == 'U':
                nextCell.append(x - 1)
                nextCell.append(y)
            elif d == 'D':
                nextCell.append(x + 1)
                nextCell.append(y)
            elif d == 'R':
                nextCell.append(x)
                nextCell.append(y + 1)
            elif d == 'L':
                nextCell.append(x)
                nextCell.append(y - 1)
            else:
                continue

            next = Cell(nextCell, currCell)

            if next in nodeVisited:
                continue
            elif next not in lifoStack:
                lifoStack.append(Cell(nextCell, currCell))

    return 'No optimal path found, maze is not solvable!'


# Outputs maze details
print(maze1)
for row in maze1:
    for col in row:
        print(col, end='')
    print('')
print('\n')

# print('\n' + 'Can you move from this position? ' + str(movable([8,0], 'L')))

# BFS Output
optimalBFS = bfs([0, 1], [9, 10])
print('---Breadth First Search---')
print('Optimal Path Found: ' + str(optimalBFS[::-1]))

if optimalBFS != 'No path found, maze is not solvable!':
    print('Optimal Path Length (cells traversed): ' + str(len(optimalBFS)))
    print('Total cells traversed through: ' + str(totalBFS))

print('\n')

# DFS Output
optimalDFS = dfs([0, 1], [9, 10])
print('---Depth First Search---')
print('Optimal Path Found: ' + str(optimalDFS[::-1]))
if optimalDFS != 'No path found, maze is not solvable!':
    print('Optimal Path Length (cells traversed): ' + str(len(optimalDFS)))
    print('Total cells traversed through: ' + str(totalDFS))
