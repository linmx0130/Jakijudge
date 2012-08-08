# -*- coding:utf-8 -*-
#  judge/judge.py
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
from base import JakiError
class Judge:
    def __init__(self):
        pass
    def _test_argument(self,exe_file_name,file_info,limit_info,diff_info):
        if (exe_file_name.__class__!="str"):
            return True
        if (file_info.__class__!="File_config"):
            return True
        
    def main(self,exe_file_name,file_info,limit_info,diff_info):
        # TODO
        # 1.Test the argument is right or not.
        # 2.run the exe_file_name under the limit
        # 3.tell the ansfile is right or not
        if (self._test_argument(exe_file_name,file_info,limit_info,diff_info)):
            raise JakiError("Wrong argument type")
