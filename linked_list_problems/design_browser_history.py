class BrowserHistory:
    """
    LeetCode: https://leetcode.com/problems/design-browser-history/

    Approach:
        iterative
        2 pointers on a list
            the reason for two is that 
            we don't let ourselves go further than
            we should be able to (aka, only as far
            as the last input to the "visit()" method)

    O(1) time + O(n) space

    Solution inspired by code posted online by jithmsmy:
        https://leetcode.com/problems/design-browser-history/discuss/2191507/Python-simple-solution
    """
    def __init__(self, homepage: str):
        self.history = list()  # last item is the most recent 
        self.current_pos = self.last_added = -1
        self.visit(homepage)
        
    def visit(self, url: str) -> None:
        self.current_pos += 1
        self.last_added = self.current_pos
        
        if self.current_pos == len(self.history):
            self.history.append(url)
        else:
            self.history[self.current_pos] = url

    def back(self, steps: int) -> str:
        self.current_pos = max(self.current_pos - steps, 0)
        return self.history[self.current_pos]

    def forward(self, steps: int) -> str:
        self.current_pos = min(self.last_added, self.current_pos + steps)
        return self.history[self.current_pos]
        

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
