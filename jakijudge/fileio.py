#  -*- coding: utf-8 -*-
#  fileio.py
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

from __future__ import print_function
import base
import os
log_out=open("testing.txt","w")

def delete_last_char(s):
    """
        I use this function to delete the "\n" of a string 
    """
    return s[0:len(s)-1] 

def load_problem_directory(pname,data_directory):
    """
        this function will read the config.ini in the data_directory and
        return a Problem_config
    """
    f=open(data_directory+'config.ini',"r")
    
    #read first line
    buf=f.readline()
    (input_file,output_file,diff_type,diff_tool_name)=buf.split("|")
    diff_tool_name=delete_last_char(diff_tool_name)

    if (os.path.exists(data_directory+diff_tool_name)):
        diff_tool_name=os.getcwd()+"/"+data_directory+diff_tool_name

    diff_type=int(diff_type)
    d=base.Diff_config(diff_type,diff_tool_name)
    p=base.Problem_config(pname,input_file,output_file,d)
    
    #read second line
    buf=f.readline()
    N=int(buf)

    #read next N lines
    current_work_directory=os.getcwd()+"/";
    for i in range(0,N):
        buf=f.readline()
        (std_if,std_of,time_l,mem_l,score)=buf.split("|")
        score=int(score)

        l_tmp=base.Limit_config(time_limit=time_l,memory_limit=mem_l)
        std_if=current_work_directory+data_directory+std_if
        std_of=current_work_directory+data_directory+std_of
        p.push_data(std_if,std_of,l_tmp,score)
    return p

def load_jaki_file():
    """
        This function will load JAKI file and build base.problem_set
    """
    pwd=os.getcwd();
    f=open(pwd+"/JAKI","r")
    buf=f.readline()
    #Test the Head
    if (buf!="FORMOSA\n"):
        raise base.JakiError("Wrong Jaki File!") 
    buf=f.readline()
    N=int(buf)

    for i in range(0,N):
        buf=f.readline()
        (pname,data_directory,sourcefile)=buf.split("|")
        sourcefile=delete_last_char(sourcefile)
        base.problem_set.push(pname,sourcefile,load_problem_directory(pname,"Data/"+data_directory+"/"))
        base.problem_list.append(sourcefile)

def log_print(s):
    print (s)
    print (s,file=log_out)
