from __future__ import print_function


import os
import sys
from tokenize import Name
from robotremoteserver import RobotRemoteServer

try:
    basestring
except NameError:
    basestring = str


class ExampleLibrary(object):
    """
     测试用例库
    Args:
        object (_type_): _description_
    """
    def count_items_in_direcory(self,path):


        items = [i for i in os.listdir(path) if not i.startswith('.')]

        return len(items)
    
    def string_should_be_equal(self,str1,str2):
        print("Comparing '%s' to '%s'. "%(str1,str2))

        if not (isinstance(str1,basestring) and isinstance(str2,basestring)):
            raise AssertionError("Given string are not strings.")
        
        if str1 !=str2:
            raise AssertionError("Given string are not equal.")
        


if __name__ == '__main__':
    RobotRemoteServer(ExampleLibrary(),host='150.168.1.79',port=8270)
    
