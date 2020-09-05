from collections import deque

class SocialGraph:
  def __init__(self):
    self.members = {}


  def add_node(self,node):
    self.members[node] = set()


  def add_edge(self,node_a,node_b):
    self.members[node_a].add(node_b)
    self.members[node_b].add(node_a)
    
  def subgraph(self, root):
    '''BFS'''
    to_visit = deque([root])

    visited = set()

    while len(to_visit) > 0:
      node = to_visit.popleft()
      if node not in visited:
        
        visited.add(node)

        for neighbor in self.members[node]:
          to_visit.append(neighbor)
    return visited

  def suggest_friends(self, me):  # takes in a user's name
    # find the people they are already friends with
    my_friends = self.members[me]
    # find all 2nd-degree connections
    friends_of_friends = [
      friend for friend in self.subgraph(me) if
      not (friend is me or friend in my_friends)
    ]
    # early exit: if no 2nd 2nd-degree, then return empty set
    if len(friends_of_friends) == 0:
      return set()
    # map each 2nd-degree connection, to the number of shared friends
    mutual_friends = dict()
    for friend in friends_of_friends:
      their_friends = self.members[friend]
      shared_friend_count = len(my_friends.intersection(their_friends))
      mutual_friends[friend] = shared_friend_count

    # [{}, {}, {}]
    # count up the number of times each 2nd-degree connection showed up
    """suggested_friend_appearances = dict()
    for friend_set in friends_of_friends:
      for friend in friend_set:
        if friend not in suggested_friend_appearances:
          suggested_friend_appearances[friend] = 1
        else:
          suggested_friend_appearances[friend] += 1"""
          
    # {'B': 1, 'A': 1}
    # return the friends who showed up most frequently
    max_appearances = max(mutual_friends.values())
    return set([
        friend for friend in mutual_friends if 
        mutual_friends[friend] == max_appearances
      ])
    """# combine these sets of 2nd-degree connections into one set 
    all_possible_friends = set()
    for friend_set in friends_of_friends:
      for friend in friend_set:
        if friend not in all_possible_friends:
          all_possible_friends.add(friend)"""
    # find the difference
    # pass

graph = SocialGraph()
## Friend Group 1
graph.add_node('Alice')
graph.add_node('Bob')
graph.add_node('Carol')
graph.add_node('Dave')
graph.add_node('Eve')
graph.add_node('Faythe')
graph.add_node('Grace')

## Friend Group 2
graph.add_node('Zed')
graph.add_node('Xavier')
graph.add_node('Quill')
graph.add_node('Robert')


## Friend Group 3
graph.add_node('Heidi')
graph.add_node('Niaj')
graph.add_node('Ivan')
graph.add_node('Trent')
  
## Friendships
graph.add_edge('Alice', 'Bob')
graph.add_edge('Alice', 'Carol')
graph.add_edge('Alice', 'Dave')
graph.add_edge('Bob', 'Dave')
graph.add_edge('Carol', 'Dave')
graph.add_edge('Alice', 'Eve')
graph.add_edge('Eve', 'Grace')
graph.add_edge('Eve', 'Bob')
graph.add_edge('Faythe', 'Eve')
graph.add_edge('Dave', 'Faythe')
graph.add_edge('Grace', 'Faythe')


graph.add_edge('Xavier', 'Quill')
graph.add_edge('Robert', 'Quill')
graph.add_edge('Xavier', 'Robert')
graph.add_edge('Zed', 'Quill')
graph.add_edge('Zed', 'Xavier')

graph.add_edge('Heidi', 'Niaj')
graph.add_edge('Heidi', 'Ivan')
graph.add_edge('Heidi', 'Trent')
graph.add_edge('Niaj', 'Trent')
graph.add_edge('Ivan', 'Trent')
graph.add_edge('Niaj', 'Ivan')

"""
{
  ##  Friend Group 1
  'Alice': {'B', 'C', 'D', 'E'}
  'Bob': {'D'}
  'Carol': {'D'}
  'Dave': {'F'}
  'Eve': {'B', 'G'}
  'Faythe': {'E'}
  'Grace': {'F'}
  ## Friend Group 2
  'Zed': {'Q', 'X'}
  'Xavier': {'Q', 'R'}
  'Quill': {}
  'Robert': {'Q'}
  ## Friend Group 3
  'Heidi': {'I', 'T', 'N'}
  'Niaj': {'T', 'I'}
  'Ivan': {'T'}
  'Trent': {}
   
}


me    |   user_friends   |  friends_of_friends    |   all_possible_friends    |
F     |   {'E'}               [ {'B', 'G'}]
"""