#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created Feb 2023

@author: renettej
"""

from pathlib import Path

# Reference:
#https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python

# prefix components:
space =  '    '
branch = '│   '
# pointers:
tee =    '├── '
last =   '└── '

class Tree():

    def __init__(self, dir_path):
        self.dir_path = dir_path
    
    
    def print_next(self, dir_path: Path, prefix: str=''):
        """A recursive generator, given a directory Path object
        will yield a visual tree structure line by line
        with each line prefixed by the same characters
        """    
        contents = list(dir_path.iterdir())
        # contents each get pointers that are ├── with a final └── :
        pointers = [tee] * (len(contents) - 1) + [last]
        for pointer, path in zip(pointers, contents):
            # exclude the .git directory
            if path.name != '.git':
                # yield - return value and continue
                yield prefix + pointer + path.name
                if path.is_dir(): # extend the prefix and recurse:
                    extension = branch if pointer == tee else space
                    # i.e. space because last, └── , above so no more |
                    yield from self.print_next(path, prefix=prefix+extension)

    def print_tree(self):
        p = Path(self.dir_path)
        #print (type(p))
        for line in self.print_next(p):
            print(line)            
