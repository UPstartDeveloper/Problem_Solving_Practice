def absSort(arr):
  # A: form the dict of freq dist of abs vals
  freq_dist = dict()
  for num in arr:
    if abs(num) in freq_dist:
        if num < 0:
            freq_dist[abs(num)][0] += 1
        else:
            freq_dist[abs(num)][1] += 1
    else:
        if num < 0:
            freq_dist[abs(num)] = [1, 0]  # how many times it appears negative
        else:
            freq_dist[abs(num)] = [0, 1]  # how many times it appears positive
        
    # sort the items 
    items = sorted(freq_dist.items())
    # make the right number of pos and neg
    sorted_items = list()
    for key, value in items:
        negs, pos = value  # [0 , 1]
        for _ in range(negs):
            sorted_items.append(-1 * key)
        for _ in range(pos):
            sorted_items.append(key)
      
    return sorted_items
