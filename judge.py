# -*- coding:utf-8 -*-
#  judge.py
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
module judge:the base judger module of jaki judge
It recieves all the testing infomation and start the test processing.
The only one public function is Main, it will start the testing.
    def Main(self,exe_file_name,file_info,limit_info,diff_info)
"""
from base import File_config
from base import Diff_config
from base import Limit_config
from base import JakiError
import os
import shutil
class Judge:
    def __init__(self):
        self._watcher_path=os.getcwd()+"/watcher/watcher"
        #only for develop :)
    def _test_argument(self,point_information,exe_file_name,file_info,limit_info,diff_info):
        if (not isinstance(point_information,(str))):
            return True
        if (not isinstance(exe_file_name,(str))):
            return True
        if (not isinstance(file_info,(File_config))):
            return True
        if (not isinstance(limit_info,(Limit_config))):
            return True
        if (not isinstance(diff_info,(Diff_config))):
            return True
        return False
    def main(self,exe_file_name,file_info,limit_info,diff_info,point_information="",testing_path=""):
        """
            def main(exe_file_name,file_info,limit_info,diff_info,point_information,testing_path)
            exe_file_name: a string, the filename of the program
            file_info: a File_config, the config about file
            limit_info: a Limit_config, the config about resource limit
            diff_info: a Diff_config, the diff config
            point_information: the number for the data point
            testing_path: the path (a dir) to run the testing work

            this function will start a judge to test the program with the data and the resoure limit, and using the diff tool to test.
        """

       
        if (self._test_argument(point_information,exe_file_name,file_info,limit_info,diff_info)):
            raise JakiError("Wrong argument type")

        shutil.copy(file_info.std_input_file,testing_path+file_info.input_file);
        #call watcher to test
        command=self._watcher_path+" -e "+exe_file_name
        if (limit_info.time_l>0): 
            command+=" -t"+limit_info.time_l;
        if (limit_info.memory_l>0): 
            command+=" -m"+limit_info.memory_l;
        if (limit_info.stack_l>0): 
            command+=" -s"+limit_info.stack_l;
        if (limit_info.file_l>0): 
            command+=" -f"+limit_info.file_l;

        #runprogram in the testing directory
        current_work_directory=os.getcwd()
        os.chdir(testing_path)

        watcher_pipe=os.popen(command,"r",3096);
        message=watcher_pipe.read()
        ret_message="";
        if (message[0]=='1'):
            print (point_information+"Time Limit Excceed!")
            ret_message="T";
        if (message[0]=='2'):
            print (point_information+"Runtime Error!")
            ret_message="R";
        if (message[0]=='3'):
            print (point_information+"Memory Limit Excceed!")
            ret_message="M";
        #call diff to test
        if (not diff_info.run(file_info)):
            print (point_information+"Wrong Answer!")
            ret_message="W";
        else:
            print(point_information+"Accept")
            ret_message="A";
        #come back
        os.chdir(current_work_directory)
        #clean temp file
        os.remove(testing_path+file_info.input_file)
        os.remove(testing_path+file_info.output_file)

