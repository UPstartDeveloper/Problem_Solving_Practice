"""
Problem: Building a new version of the Finder app in macOS

Your input:
        - you get a dict
        - each key is a path
        - value is 
            1) a file, which is a dict with the size (in GB) + contents of that file, OR
            2) a folder, which is a dict of more files/folders
        - AND, you will be given the full path of a file that exists in the Finder somewhere
        - you can assume each file only exists at one path location

Question and Follow-Up
        - Write a function to get the size of any file/folder, given the path?
        - follow-up: optimize the time efficiency of your approach, so we can deploy into the newest notebooks by Apple?
        
Example data structure:
       directory = {
         "dev": {
                "keras_model.py": {"size": 6, "content": "this is fake src code"},  ---> 6
                "tf_model.py": {"size": 6, "content": "this is fake src code"}, ---> 12
                "flax_model.py": {"size": 6, "content": "this is fake src code"}, -> 18, 24, 30
                "torch_model.py": {"size": 6, "content": "this is fake src code"},
                "sklearn_model.py": {"size": 6, "content": "this is fake src code"},
          },
          "selfie.png": {"size": 200, "content": "blah blah RGB values"}
            
        }
        
Input and Output:
    your_function(directoy, "/dev") ---> 30
    your_function(directory, "/dev/torch_model.py") ---> 6
    your_function(directory, "/selfie.png") ---> 200
    your_function(directory, "selfie.png") ---> 200   (this is an edge case)
"""

"""
Intuition:
    m-way tree
    recursion - variable # of folders
        base case - querying file ---> get size
        recursive - querying directory (sum of file queries)

EC:
    w/o leading slash ---> check for leading slash


Approach:

    1) OOP 

        # A: split the path --> [str w/ no slashs] <--- queue
        # B: traverse the tree ---> TODO[compute the size]
        # C: return the size

        ["dev", "torch_model.py"]
            ^
        B:

            1) dequeue
            
            2) acculmulating size
                Base: if item is a file ----> add "size" to running_sum
                Recursive: if a folder ---> recurse

            3) return!

"""


class Solution:
    def compute_size(self, directory, full_path):
        ### HELPERS
        def _find_file_or_folder():
            """iterative search"""
            path_queue = full_path.split("/")
            current_directory = cd = directory

            # find the next level "down" in the tree
            for path in path_queue:
                if path:
                    cd = cd[path]

            return cd

        def _compute_size_helper(folder_or_file):
            """recursive backtracking"""
            # base case?
            if "size" in folder_or_file.keys():
                self.full_size += folder_or_file["size"]

            # recursive - iterating over nested files
            else:
                for nested_path in folder_or_file.keys():
                    nested_obj = folder_or_file[nested_path]
                    _compute_size_helper(nested_obj)

        ### EC - TODO[test]
        if full_path in directory and "." in full_path:
            return directory[full_path]["size"]

        ### DRIVER
        if full_path not in self.cache:
            # A
            desired_folder_or_file = _find_file_or_folder()

            # B:
            self.full_size = 0
            _compute_size_helper(desired_folder_or_file)

            # C
            self.cache[full_path] = self.full_size

        return self.cache[full_path]


if __name__ == "__main__":
    directory = {
        "dev": {
            "keras_model.py": {"size": 6, "content": "this is fake src code"},  # ---> 6
            "tf_model.py": {"size": 6, "content": "this is fake src code"},  # ---> 12
            "flax_model.py": {
                "size": 6,
                "content": "this is fake src code",
            },  # -> 18, 24, 30
            "torch_model.py": {"size": 6, "content": "this is fake src code"},
            "sklearn_model.py": {"size": 6, "content": "this is fake src code"},
        },
        "selfie.png": {"size": 200, "content": "blah blah RGB values"},
    }
    sol = Solution()

    print(sol.compute_size(directory, "/dev"))  # 30
    print(sol.compute_size(directory, "/dev/torch_model.py"))
    # sol.compute_size(directory, "/selfie.png") # ---> 200
    print(sol.compute_size(directory, "selfie.png"))  # 6
