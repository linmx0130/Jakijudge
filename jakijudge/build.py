# -*- coding:utf-8 -*-
#  build.py
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
import os

def buildjaki_py():
    """
    The function to build jaki.py
    """
    f=open('jaki.py','w')
    c="import sys"
    print >>f,c
    c="sys.path.append('/usr/lib/jaki/')"
    print >>f,c
    c="from jakijudge import jaki,base"
    print >>f,c
    c="def special_setting():"
    print >>f,c
    c="    # You can write some scripts to set the jaki"
    print >>f,c
    c="    pass"
    print >>f,c
    c="jaki.Main(special_setting)"
    print >>f,c


def buildjaki_file():
    """
    The function to build JAKI file
    Before this function being run, the config.ini must exist in each problem
    directory.
    """
    problem_list=[]
    for dir_name in os.listdir("Data/"):
        if (os.path.isdir("Data/"+dir_name)):
            if (os.path.exists("Data/"+dir_name+"/config.ini")):
                #Found a problem
                print ("Found a problem at Data/"+dir_name+"/")
                s1=raw_input("Input the problem name please:")
                s2=raw_input("Input the source file name please:")
                problem_list.append((s1,dir_name,s2))
    f=open("JAKI","w")
    f.write("FORMOSA\n")
    f.write(str(len(problem_list)))
    f.write("\n")
    for pd in problem_list:
        f.write("%s|%s|%s\n"%(pd[0],pd[1],pd[2]))
def buildproblem_config():
    data_file_list=[];
    for file_name in os.listdir("./"):
        if (os.path.isfile(file_name)):
            if (file_name[len(file_name)-3:]=='.in'):
                t=file_name[:len(file_name)-3]
                if (os.path.isfile(t+'.out')):
                    data_file_list.append(t)
    data_file_list.sort()
    f=open("config.ini","w")
    print "Found "+str(len(data_file_list))+" case(s) data!"
    input_file_name=raw_input("Enter the input file name:")
    output_file_name=raw_input("Enter the output file name:")
    checker_name=raw_input("Enter the checker name(oidiff):") or "oidiff"
    time_limit=raw_input("Enter the time limit in ms(1000):") or "1000"
    memory_limit=raw_input("Enter the memory limit in KB(65535):") or "65535"
    score=str(int(100/len(data_file_list)))
    f.write(input_file_name+"|"+output_file_name+"|"+"1"+"|"+checker_name+"\n")
    f.write(str(len(data_file_list))+"\n")
    for file_name in data_file_list:
        f.write(file_name+".in|")
        f.write(file_name+".out|")
        f.write(time_limit+"|")
        f.write(memory_limit+"|")
        f.write(score+"\n")
    f.close()
    print "Finished! Please check config.ini."
    
