# -*- coding:utf-8 -*-
#  tester.py
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
import judge
import os
import fileio
def get_last_name(source):
    for i in range(len(source)-1,-1,-1):
        if (source[i]=='.'):
            return source[i:len(source)]

def tester_run(source,problem):
    """
        compile the source file and start judge
    """
    c=base.compiler_set.find(get_last_name(source))
    runfile='"'+base.temp_directory+"program"+'"'
    c.run(source,'"'+base.temp_directory+"program"+'"');

    j=judge.Judge()
    for i in range(0,problem.data_tot()):
        j.main(runfile,problem.get_file_config(i),problem.get_limit_config(i),problem.diff_tool,point_information=str(i)+":",testing_path=base.temp_directory)


