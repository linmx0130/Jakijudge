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
