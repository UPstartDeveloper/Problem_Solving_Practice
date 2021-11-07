class RecentCounter(object):
    def __init__(self):
        self.times_requests_made = set()  # constant
        # counter for number of recent requests
        # self.total_requests = 0
        # time_of_last_request

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        """
        Timeline               
        #                                              rr = 1, t = 1
                                                                
        #                     t-3000                   t
        # <--------------------------------------------->
        
        A: increment # of total_request
        B: calculate the start of time range: t - 3000 - -2999
        C: calculate# of total_requests that are recent
            if start time < time of last request --> all recent
        
        ----------------------------------------------------
        B: copy time of last request into a temp var
        C: update .time_of_last_request property --> t
        D: 
        
        recent_requests = 0, 1
        time_of_last_request = 1
        
        temp = 0
        
        """
        # add t to the set of times that requests are made
        self.times_requests_made.add(t)  # O(1)
        # calculate range of time in the last 3 sec [t - 3000, t]
        start_end_times = (t - 3000, t)  # O(1)
        # find the number of recent_requests
        recent_requests = 0  # O(1)
        # search for each time in that range in the set
        start, end = start_end_times  # O(1)
        for time in range(start, end + 1):  # 3000 iterations
            # if found, increment a count of the request_made
            if time in self.times_requests_made:  # constant
                recent_requests += 1  # O(1)
            # otherwise, remove the time from the set
        # return the count
        return recent_requests  # O(1)

    # Time: O(1)
    # n: # calls to ping
    # Space: O(n)


"""
["RecentCounter",         "ping", "ping", "ping", "ping"]
[[],                        [1], [100], [3001], [3002]]


obj.times_requests_made = set() = {1}
[-2999, 1]
time = 1
recent_requests = 1
"""


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
"""
- we need to have a way to know the time frame at which a request was made
- range is inclusive

1. Use buckets
    - recent requests - # requests made within the last 3000
    - non recent
    
    
2. Set
- all the values will be unique
- Con: unordered

times_requests_are_made = {1}
range = [-2999, 1]
requests = 1
time_searched = 1
ping:
    - add t to the set of times that requests are made
    - calculate range of time in the last 3 sec [t - 3000, t]
    # find the number of recent_requests
    - search for each time in that range in the set
        - if found, increment a count of the request_made
    - return the count
    
init method
- properties:
    - requests_made: set()
    
3. counters
    

"""
