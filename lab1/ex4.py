
#%%
import csv

class State:
    def __init__(self, name, abbrev, land, pop):
        self.name = name
        self.abbrev = abbrev
        self.land = int(land)
        self.pop= int(pop)
        
    def pop_density(self):
        return self.pop/self.land
    
    def __str__(self):
        return self.name
        
        
        
        
        
        
def load_us_states(filename):
    state = []
    with open(filename, 'r') as f:
        for s in csv.reader(f): 
            a_state = State(s[0], s[1], s[2],  s[3])
            state.append(a_state)
        state= sorted(state, key = State.pop_density, reverse= True)
    return state
