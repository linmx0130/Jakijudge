# -*- coding:utf-8 -*-
#  jaki.py
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

import base
import fileio
import tester
import judge
import os
from fileio import log_print

class Contestant_result:
    def __init__(name):
        self.name=name
        self.problem_result=[]

def default_setting():
    #compiler settings
    c=base.Compiler_config("C","gcc -o %obj% %source% -lm")
    base.compiler_set.push("C",".c",c)
    c=base.Compiler_config("C++","g++ -o %obj% %source% -lm")
    base.compiler_set.push("C++",".cpp",c)
    c=base.Compiler_config("Pascal","fpc -o%obj% %source%")
    base.compiler_set.push("Pascal",".pas",c)
    #temp_directory
    base.temp_directory="/tmp/jaki/"
    try:
        os.mkdir(base.temp_directory)
    except OSError:
        pass
        #the lock system is TODO!
def load_contestant():
    for dir_name in os.listdir("Source/"):
        if (os.path.isdir("Source/"+dir_name)):
            base.contestant_list.append(dir_name)

def Main(special_setting):
    #load settings
    default_setting()
    special_setting()
    #load JAKI file
    fileio.load_jaki_file()
    load_contestant()
    #start test
    for contestant in base.contestant_list:
        log_print("Contestant: "+contestant)
        contestant_score=0
        result_message="Test status:"
        print(base.problem_list)
        for problem_source_file in base.problem_list:
            found_source=False
            for last_name in base.compiler_set.last_name_set.keys():
                file_name="Source/"+contestant+"/"+problem_source_file+last_name
                if (os.path.exists(file_name)):
                    print ("  Found source file: "+file_name)
                    found_source=True
                    (tmp1,tmp2)=tester.tester_run(file_name,base.problem_set.find(problem_source_file))
                    contestant_score+=tmp1
                    result_message+="\n  --"+base.problem_set.find(problem_source_file).problem_name+":"

                    for i in range(0,len(tmp2)):
                        result_message+="\n    "+str(i)+":"+tmp2[i]
                    break

            if (not found_source):
                print("NOT FOUND source file for: "+base.problem_set.find(problem_source_file).problem_name)
                result_message+="\n  --"+base.problem_set.find(problem_source_file).problem_name+": No submit\n"
        log_print(contestant_score)
        log_print(result_message)

