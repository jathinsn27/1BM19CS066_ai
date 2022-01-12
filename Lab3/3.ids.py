class Node:
    def __init__(self, state, level):
        self.grid = state
        self.limit = limit
       

def dfs(src,target,limit,visited_states):
    if src == target:
        return printGrid(src)
    if limit <= 0:
        return None
    visited_states.append(src)
    moves = possible_moves(src,visited_states)   
    for move in moves:
        if dfs(move, target, limit-1, visited_states):
            return printGrid(src)
    return None



def printGrid(state):
    state = state.copy()
    state[state.index(0)] = ' '
    print(state[0], state[1], state[2])
    print(state[3], state[4], state[5])
    print(state[6], state[7], state[8])
    print()


def possible_moves(state,visited_states): 
    b = state.index(0)  
    d = []
    if b not in [0,1,2]: 
        d += 'u'
    if b not in [6,7,8]:
        d += 'd'
    if b not in [2,5,8]: 
        d += 'r'
    if b not in [0,3,6]: 
        d += 'l'
    pos_moves = []
    for move in d:
        pos_moves.append(gen(state,move,b))
    return [move for move in pos_moves if move not in visited_states]

def gen(state, move, blank):
    temp = state.copy()                              
    if move == 'u':
        temp[blank-3], temp[blank] = temp[blank], temp[blank-3]
    elif move == 'd':
        temp[blank+3], temp[blank] = temp[blank], temp[blank+3]
    elif move == 'r':
        temp[blank+1], temp[blank] = temp[blank], temp[blank+1]
    elif move == 'l':
        temp[blank-1], temp[blank] = temp[blank], temp[blank-1]
    return temp

def inFrontier(frontier, neighbour):
    return len([state for state in frontier if state.grid == neighbour.grid]) > 0
    
    while frontier:
        frontier.sort(key = lambda x: x.cost)
        state = frontier.pop(0)
        print('Step: {state.limit}')
        printGrid(state)
        
        if state.grid == target:
            print("Puzzle solved! ")
            return
        
        neighbours = possible_moves(state, visited_states)
        for neighbour in neighbours:
            neighbour = Node(neighbour, state.limit + 1)
            neighbour.cost = F(neighbour, target)
            if not inFrontier(frontier, neighbour):
                frontier.append(neighbour)
    
    print("Can't solve puzzle! ")

def iddfs(src,target,limit):
    for i in range(limit):
        visited_states = []
        if dfs(src,target,i+1,visited_states):
            return printGrid(src)
    return None

src = [1,2,3,4,0,6,7,5,8]
target = [1,2,3,4,5,6,7,8,0]         
       
   
iddfs(src,target,limit=5)
