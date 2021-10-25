class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        """
        Input/Problem:
            - "." = 
                input = not being itself push
                output = upright
            - ASSUME net forces once / sec
                - it only takes 1 sec fall down
                - only between adj. dominoes
            - Output: 
                - altered string
            - immutable 
            - NO empty str
            - 
        RL,
        LR
        .L --> LL
        .R --> .R
        
        EC: TODO
        
            1) "falling on top of each other"
            2) 
            
        Intuition:
            - motion is 1D
            - time dimension - forces prop w/o resistance
            - encode str
            
            
            -x      0       +x
            <---------------->
            L       .        R
            
        Approach:
        
        stepping ston:
            - net force on ONE domino, for a given second:
                - 1) look at that index
                  2) check for -1 to the right
                  3) check for a +1 coming from the index before
                    
                - add 2-3 values together --> net force
                    - highest pos --> +1
                    - lowest neg --> -1
        
            1) DIY: sec-by-sec
                A: encode string as arr of ints
                B: pass over the line until there's no more changes
                C: decode arr --> output str
                
                RR.L
                
              t    |     dominoes 
              0    |    [+1, +1, 0, -1]
              1    |    [+1, +1, 0, -1] --->   
                
        
        """
        ### HELPERS
        def _encode(dominoes: str) -> list[int]:
            forces = {"L": -1, "R": 1, ".": 0}
            return [forces[char] for char in dominoes]
                
        def _decode(states: list[int]) -> str:
            forces = {-1: "L", 1: "R", 0: "."}
            return ''.join([forces[values] for values in states])      
        
        def _update(states):
            # A: make a new array of net forces (poss diff from input)
            net_forces = list()
            for index, domino in enumerate(states):
                net_force = domino
                # 2) check for -1 to the right
                if (
                    (index < len(states) - 1 and states[index + 1] == -1)
                    or 
                    (index == len(states) - 1 and states[index] == -1)
                ):
                    net_force -= 1
                # 3) check for a +1 coming from the index before
                if (index > 0 and states[index-1] == 1) or (index == 0 and states[index] == 1):
                    net_force += 1
                # 4) add 2-3 values together --> net force
                if net_force > 0:
                    net_force = min(1, net_force)
                elif net_force < 0:
                    net_force = max(-1, net_force)
                net_forces.append(net_force)
            # B: output
            return net_forces
        
        def _run_simulation(states):
            """TODO[Refactor]: renaming states var"""
            keep_running = True  # <----- exec pter
            while keep_running is True:
                # A: run 1 time step
                updated_states = _update(states)
                if states == updated_states:
                    keep_running = False
                # B: move on to next time step
                states = updated_states
            return states
        
        ### DRIVER
        # A: encode string as arr of ints
        states = _encode(dominoes)  
        # B: pass over the line until there's no more changes
        final_states = _run_simulation(states) 
        # C: decode arr --> output str
        return _decode(final_states)
    
    
    """
    
     keep_running       states              `net_forces
                         0. 1. 2.  3.        [1, 1, 0, -1]
     True               [1, 1, 0, -1]
                               ^
                         
    d = 1, 1, 0, -1
    nf = 1, 1, 2, 1, 0, -1, 0, -1
    
    """
