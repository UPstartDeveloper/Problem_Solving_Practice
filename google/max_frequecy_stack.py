from collections import OrderedDict


class FreqStack:
    def __init__(self):
        """
        LeetCode: https://leetcode.com/problems/maximum-frequency-stack/
        
        Design:
            top - tenatively, last index in ArrayStack
            
        Stepping Stone:
            Array
                top is last index - push in O(1) 
                                    pop in O(n)
                                    
        Idea:
            Array + HT: unique elem --> count, "index_closest_to_top"
            
            stack = [
                5, 7,
                ^ 
            ]
                
                
            ht = {
                5: (1, )
                7: (1, 1)
                type: (count, [indices])
                
            }
            
            .push(5)
            .push(7)
            .push(5)
            .pop()
            
            1) have a FAST way to lookup most freq
                a) and resolve ties
            2) have a way to FAST-ly go to last added elem of a type ✅
                b) max heap? --> O(1)
                c) 2nd stack?
                                                  v  v
                stack1 = pushed_elems =    [5, 7, 5, 4] ---> 
                stack2 = most_freq_elems = [5, 7, 5, 5] ---> 5]
                                                     ^
                                                     
                                                     
                                           [5, -1, 7, 4]
                                           [5, 5, 5] ----> 5
                 ht = {
                    5: (1, [0]
                    7: 1
                    4: 1
                }
                
                .pop()
                    ---> look at top of most_freq_elems
                    ---> pop from most_freq_elems
                        ---> update the ht (decrement count)
                    ---> swap top of pushed_elem w/ last pushed of most_freq type
                        ---> ht: pop the last index of most_freq
                    ---> pop from pushed_elems
                    ---> for most_freq_elems:
                        compare counts of prev_top (4) vs. that of last_most_freq (5)
                            if prev_top_count >= last_most_freq
                                then overwrite most_freq_elems 
                                
                                
        Idea #3:
            2D stack + ordered dict
            
                push()
                    see if the elem in HT
                    if so --> increment count; else init count = 1 + RECORD it in HT
                    find the max freq elem (using "2 candidate" approach)
                    add (push, max_freq) to stack
                    
                pop()
                    get the last tuple added to the stack
                    unpack it ---> last_pushed, most_freq (at this position)
                    
                    if most_freq != last_pushed
                    
                    
                    return most_freq
                    
                        p   f
                    [
                        (5, 5),
                        (5, 5),
                        (7, 5),
                        ________
                        (4, 5) <---
                    ]
                    
                    ht = {
                        5: 2, 
                        7: 1, 
                        4: 1,
                    }
                    
        """
        self.elem_frequencies = self.ef = OrderedDict()
        self.max_freq = -1  # largest frequency of any pushed elems
        self.freq_groups = self.fg = dict()  # freq --> [unique val types]

    def push(self, val: int) -> None:
        """
        add elem to the top of the stack
        """
        # record the proper key-val pairs
        prev_count, new_count = 0, 1
        if val in self.ef:
            prev_count = self.ef[val]
            new_count += prev_count

        self.ef[val] = new_count

        # update the max frequency (will need it later)
        self.max_freq = max(self.max_freq, new_count)

        # place the val in the right group
        if new_count not in self.fg:
            self.fg[new_count] = list([val])
        else:
            self.fg[new_count].append(val)

    def pop(self) -> int:
        # get max freq element!
        current_mfe = self.fg[self.max_freq].pop()

        # update state
        self.ef[current_mfe] -= 1

        if len(self.fg[self.max_freq]) == 0:
            self.max_freq -= 1

        # all done!
        return current_mfe


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
