from collections import deque

capacity = (12,8,5,3)
start = (12,0,0,0)
goal = (6,6,0,0)

def pour(state,i,j):
    state=list(state)
    amount=min(state[i],capacity[j]-state[j])
    state[i]-=amount
    state[j]+=amount
    return tuple(state)

def get_next_states(state):
    states=[]
    
    for i in range(4):
        s=list(state)
        s[i]=capacity[i]
        states.append(tuple(s))
    
    for i in range(4):
        s=list(state)
        s[i]=0
        states.append(tuple(s))
    
    for i in range(4):
        for j in range(4):
            if i!=j:
                states.append(pour(state,i,j))
    
    return states

def bfs():
    queue=deque()
    queue.append((start,[start]))
    visited=set()

    while queue:
        state,path=queue.popleft()

        if state in visited:
            continue
        
        visited.add(state)

        if state==goal:
            return path
        
        for next_state in get_next_states(state):
            if next_state not in visited:
                queue.append((next_state,path+[next_state]))

solution=bfs()

print("Solution Path:")
for step in solution:
    print(step)
