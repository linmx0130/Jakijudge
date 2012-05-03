#  -*- coding: utf-8 -*-
#  base/base.py
#  Jaki Judge: Offline OI Judger in Linux
#  Copyright (c) by Sweetdumplings<linmx0130@163.com> 
#
#    Jakijudge is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

"""
module base: the base of all the other modules of jaki judge
It provides jaki with some class which should be used in different modules.
All the class need a member: _jaki_class_mark. It is a string and it show what it is.

the list of classes the base module supported:
    File_config
    Diff_config
"""
    
class File_config:
    """
    This class 5 has members:
        1.std_input_file
        2.std_output_file
        3.input_file
        4.output_file
        5.define(std_input_file,std_output_file,output_file,input_file)
    """
    
    def __init__(self,std_input_file,std_output_file,input_file,output_file):
        self._jaki_class_mark="FILE_CONFIG"
        self.define(std_input_file,std_output_file,input_file,output_file)
    
    def define(self,std_input_file,std_output_file,input_file,output_file):
        """
        this function will help user to set up a file config class
        """
        self.std_input_file=std_input_file
        self.std_output_file=std_output_file
        self.input_file=input_file
        self.output_file=output_file

class Diff_config:
    """
    The tester will use a object of Diff_config to tell what diff program
    the judge should to use.
    It has two members: 
        1.standard: the standard which the diff to follow
        2.filename: the path of the diff program
        3.run() 
    """
    def __init__(self,standard=1,file_name="oidiff"):
        self._jaki_class_mark="DIFF_CONFIG"
         
    def run():
    #TODO

        """
        This function is used to call the diff program to compare the 
        answer and return the result.
        """     
    
if __name__=="__main__":
    print("This file can't be called by user directly.")
    print(__doc__)
