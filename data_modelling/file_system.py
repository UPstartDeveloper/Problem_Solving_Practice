"""
CtcI 7.11: File System

Explain the data structures and algorithms that you would use to 
design an in-memory file system. 
Illustrate with an example in code where possible.

Scope:
- what
    - digital recipe sharing app

- why
    - CRUD a single user's recipes

- who - 1 individual user in a USA setting

- where - desktop

Key Objects:
    1. Folder: M-way tree folder strcutres ✅
        - children: contains files/more folders
        - location: str
    2. File -- dictionary
        - file_name: str ✅
        - memory_size: float
        - location: str
        - content: Any

Relationships:
    - 1 files --- 1 location
    - Tree --> File
    - File -- Tree ✅

Actions:
1. create (folder)
    - input the path to parent
    - recusion down the tree - add the object
2. create (file)
    - location: str
    DEMO N/A:
    - file_name: str
    - memory_size: float
    - content: Any
2. read:
    a. folder.read_recursively: backtracking
    b. file.read --> return file.content
    c. folder.size() --> backtracking
3. U: moving to a new location:
    update that thing's .location AND rm from enclosing folder.children
4. D: 
    a: folder/file.move_location("Trash")
    b: file.permanent_delete(): TODO
    c: folderpermanent_delete(recursive=True/False): TODO
"""


class FileSystemObject:
    # TODO: add a property "object_name" for both that comes from splitting the location
    def __init__(self, location):
        self.location = location  # absolute path
        folder_names = location.split("/")
        self.object_name = ""
        if len(folder_names) > 0:
            self.object_name = folder_names[-1]


class File(FileSystemObject):
    def __init__(self, location, memory_size, content):
        super().__init__(location)
        self.data = {"size": memory_size, "content": content}


class Folder(FileSystemObject):
    def __init__(self, location, children=dict()):
        super().__init__(location)  # only gives the name of the folder itself
        self.children = children  # map object_name --> FileSystemObject


class FileSystem:
    """An M-way tree"""

    def __init__(self):
        self.root = Folder("/")

    def create_folder(self, full_path):
        """
        Expects an absolute path

        ex: /Users/zain/Downloads
        
        """
        pass
