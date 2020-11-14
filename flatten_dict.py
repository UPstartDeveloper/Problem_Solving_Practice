def flatten_dictionary(dictionary):
  # init keys array
  new_dict = dict()
  keys = list()
  def make_key(keys, key):
    """Form the key"""
    new_key = ".".join(keys)
    if key != "":
      new_key = ".".join((new_key, key))
    return new_key
  def flatten(flatten_dict, keys):
    # iterate over kv pair
    for key, value in flatten_dict.items():
      # Base Case: if key normal
      if isinstance(value, dict) is False:
        # use what's in the keys array to form the new key
        if len(keys) > 0:
          key = make_key(keys, key)
        # add to a new dict, 
        new_dict[key] = value
      # Recursive Case if leads to a nested dict:
      elif isinstance(value, dict) is True:
        # add to the keys array
        if key != "":
          keys.append(key)
        flatten(value, keys)
        # pop from the keys array
        if len(keys) > 0:
            keys.pop()
      # print(new_dict)
  # call the helper func
  flatten(dictionary, keys)
  # return the dictionary
  return new_dict
"""
diction = {
  "Key1" : "1",
  "Key2" : {
      "a" : "2",
      "b" : "3",
      "c" : {
          "d" : "3",
          "e" : {
              "" : "1"
          }
      }
  }
}
"""
diction = {"": {"a": 1}, "b": 2}
print(flatten_dictionary(diction))