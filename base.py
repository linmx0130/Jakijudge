#  -*- coding: utf-8 -*-
#  base.py
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
    Compiler_config
    Limit_config
"""
import os
class JakiError(Exception):
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return repr(self.value)

class File_config:
    """
    This class has 5 members:
        1.std_input_file
        2.std_output_file
        3.input_file
        4.output_file
        5.define(std_input_file,std_output_file,output_file,input_file)
    """
    
    def __init__(self,std_input_file,std_output_file,input_file,output_file):
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
        4.addition_info: the addition information from the diff program
    """
    def __init__(self,standard=1,diff_filename="diff"):
        self.diff_filename=diff_filename
        self.standard=standard;
    def run(self,data):
        """
        This function is used to call the diff program to compare the 
        answer and return the result.
        """     
        if (not isinstance(data,(File_config))):
            raise Wrong_inside_information
        if (self.standard==1):
            command=self.diff_filename+" "+data.std_output_file+" "+data.output_file+"> /dev/null"
            tmp=os.system(command)
            if (tmp!=0):
                return False 
            else:
                return True

class Compiler_config:
    """
        you can use "%source%" replace the source filename and use 
        "%obj%" replace the object filename
    """
    def __init__(self,language,command):
        self.language=language
        self.command=command
    def run(self,source,obj):
        shell_c=self.command.replace("%source%",source)
        shell_c=shell_c.replace("%obj%",obj)
        print("===Compiling...===")
        print("  Command:"+shell_c)
        if (os.system(shell_c)==0):
            print("===Compiled!===")
            return 0
        else: 
            print("===Compiling Error!===")
            return 1
class Compiler_set_type:
    def __init__(self):
        self.compiler_set={}
        self.last_name_set={}

    def push(self,language_mark,last_name,compiler_config):
        self.compiler_set[language_mark]=compiler_config
        self.last_name_set[last_name]=language_mark
    
    def find(self,last_name):
        return self.compiler_set[self.last_name_set[last_name]]

class Limit_config:
    """
        saved information of resource limit
    """
    def __init__(self,time_limit=-1,memory_limit=-1,stack_limit=-1,file_limit=-1):
        self.time_l=time_limit;
        self.memory_l=memory_limit;
        self.stack_l=stack_limit;
        self.file_l=file_limit;
class Problem_config:
    """
        saved the information of a problem
        it's member:
            1.pname: the name of the problem
            2.input_file: the input filename
            3.output_file: the output filename
            4.diff_tool: the diff config
            5.data_array: the information of the data point
        it's function:
            def push_data(self,std_input_file,std_output_file,limit_data,score):
            def data_tot(self):
            def get_file_config(self,index):
            def get_limit_config(self,index):
            def get_score(self,index):

    """
    def __init__(self,pname,input_file,output_file,diff_tool):
        self.problem_name=pname
        self.input_file=input_file
        self.output_file=output_file
        self.diff_tool=diff_tool
        self.data_array=[]
    def push_data(self,std_input_file,std_output_file,limit_data,score):
        self.data_array.append((std_input_file,std_output_file,limit_data,score))
    def data_tot(self):
        return len(self.data_array)
    def get_file_config(self,index):
        ret=File_config(self.data_array[index][0],self.data_array[index][1],self.input_file,self.output_file)
        return ret
    def get_limit_config(self,index):
        return self.data_array[index][2]
    def get_score(self,index):
        return self.data_array[index][3]


if __name__=="__main__":
    print("This file can't be called by user directly.")
    print(__doc__)
