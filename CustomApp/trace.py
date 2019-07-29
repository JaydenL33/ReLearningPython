from z3 import *
from grid import GRID

# pip install z3-solver

TRACES = 0
VISITED = {}
def trace(pos, d):
    global TRACES
    global VISITED
    TRACES += 1
    x,y = pos
    while True:
        c = GRID[x][y]
        if c == '-' and d == 'right':
            x+=1
        elif c == '-' and d == 'left': # <----
            x-=1
        elif c == '|' and d == 'up':
            y-=1
        elif c == '|' and d == 'down':
            y+=1
        elif c == 'A' and d == 'down':
            return (x,y+1),'AND_{}_{}'.format(x,y+1)
        elif c == 'A' and d == 'left': # <----
            if 'AND_{}_{}'.format(x,y+1) not in VISITED:
                VISITED['AND_{}_{}'.format(x,y+1)] = simplify(And(trace((x,y+1),'down'), trace((x,y-1),'up')))
            return VISITED['AND_{}_{}'.format(x,y+1)]
        elif c == 'A' and d == 'up':
            return (x,y-1),'AND_{}_{}'.format(x,y-1)
        elif c == 'X' and d == 'down':
            return (x,y+1),'XOR_{}_{}'.format(x,y+1)
        elif c == 'X' and d == 'up':
            return (x,y-1),'XOR_{}_{}'.format(x,y-1)
        elif c == 'X' and d == 'left': # <----
            if 'XOR_{}_{}'.format(x,y+1) not in VISITED:
                VISITED['XOR_{}_{}'.format(x,y+1)] = simplify(Xor(trace((x,y+1),'down'), trace((x,y-1),'up')))
            return VISITED['XOR_{}_{}'.format(x,y+1)]
        elif c == 'O' and d == 'left': # <----
            if 'OR_{}_{}'.format(x,y+1) not in VISITED:
                VISITED['OR_{}_{}'.format(x,y+1)] = simplify(Or(trace((x,y+1),'down'), trace((x,y-1),'up')))
            return VISITED['OR_{}_{}'.format(x,y+1)]
        elif c == 'O' and d == 'down':
            return (x,y+1),'OR_{}_{}'.format(x,y+1)
        elif c == 'O' and d == 'up':
            return (x,y-1),'OR_{}_{}'.format(x,y-1)
        elif c == 'N' and d == 'right':
            return (x+1,y),'NOT_{}_{}'.format(x+1,y)
        elif c == 'N' and d == 'left': # <---- # <----
            if 'NOT_{}_{}'.format(x,y+1) not in VISITED:
                VISITED['NOT_{}_{}'.format(x,y+1)] =simplify(Not(trace((x-1,y), 'left')))
            return VISITED['NOT_{}_{}'.format(x,y+1)]
        elif c == '+' and d == 'right':
            x+=1
        elif c == '+' and d == 'left': # <----
            x-=1
        elif c == '+' and d == 'up':
            y-=1
        elif c == '+' and d == 'down':
            y+=1
        elif c == '.' and d == 'up':
            x+=1
            d = 'right'
        elif c == '.' and d == 'left': # <----
            y+=1
            d = 'down'
        elif c == '`' and d == 'right':
            y-=1
            d = 'up'
        elif c == '`' and d == 'down':
            x-=1
            d = 'left'
        elif c == ',' and d == 'right':
            y+=1
            d = 'down'
        elif c == ',' and d == 'up':
            x-=1
            d = 'left'
        elif c == '"' and d == 'right':
            y-=1
            d = 'up'
        elif c == '"' and d == 'left': # <----
            y-=1
            d = 'up'
        elif c == '"' and d == 'down':
            x+=1
            d = 'right'
        elif c == '^' and d == 'left': # <----
            d = 'left'
            x -= 1
        elif c == '^' and d == 'down':
            d = 'left'
            x -= 1
        elif c == '^' and d == 'right':
            return trace((x+1,y), 'right'), trace((x,y-1), 'up')
        elif c == 'T' and d == 'right':
            return trace((x+1,y), 'right'), trace((x,y+1), 'down')
        elif c == 'T' and d == 'up':
            d = 'left'
            x -= 1
        elif c == 'T' and d == 'left': # <----
            d = 'left'
            x -= 1
        elif c == '@': # input lever
            d = 'left'
            x -= 1
            return Bool('input_{}'.format(y))
        else:
            print("ERROR ({}/{}) {}: {}".format(x,y,d,c))
            exit(0)

print("[*] tracing the network")


circuit  = trace((1937,1), 'left')


print("[*] circuit done")
print(circuit)
print("[*] solving it")


solved = solve(circuit==True)





































