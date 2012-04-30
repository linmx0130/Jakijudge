# -*- coding:utf-8 -*-
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

the list of classes the base module supported:
    Diff_config
"""
class Diff_config:
    """
    The tester will use a object of Diff_config to tell what diff program
    the judge should to use.
    It has two members: 
        1.standard: the standard which the diff to follow
        2.filename: the path of the diff program
    """
    def __init__(self,standard=1,file_name="oidiff"):
        self.standard=1;
        self.file_name=1;

if __name__=="__main__":
    print("This file can't be called by user directly.")
    print(base.__doc__)

