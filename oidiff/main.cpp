/*
 * oidiff/main.cpp
 *
 * Jaki Judge: Offline OI Judger in Linux
 * Copyright (c) by Sweetdumplings<linmx0130@163.com> 
 * 
 *    Jakijudge is free software: you can redistribute it and/or modify
 *   it under the terms of the GNU General Public License as published by
 *   the Free Software Foundation, either version 3 of the License, or
 *   (at your option) any later version.
 *
 *   This program is distributed in the hope that it will be useful,
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *   GNU General Public License for more details.
 *
 *   You should have received a copy of the GNU General Public License
 *   along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

/* Jaki oidiff is built to suit old jaki special judge standard at first.I
 * didn't think I should use Python to rewrite it because it's very simple.
 * It could be use as a normal diff program. But in the new standard,
 * I have to change it. 
 * From Formosa, Jaki started to support 2 kinds of "diff program standard".
 * Of couese new jaki advises users to use the new kind of standard, so the
 * special score system of old standard hasn't been supported.
 * 
 * Sweeedumplings<linmx0130@163.com> 
 */

/* Usage: oidiff File1 File2
 * File1 is the standard answer file.
 * File2 is the answer file that the judger should to test.
 * oidiff only compares the data in two files but it won't care about
 * return or space characters.
 */
#include <string>
#include <fstream>
#include <iostream>
using namespace std;
int main(int argc,char ** argv){
	if (argc!=3) {
		cerr<<"The wrong argument!"<<endl;
		return 255;
	}
	ifstream fstd(argv[1]);
	if (!fstd) {
		cerr<<"Couldn't open the standard answer file!"<<endl;
		return 254;
	}
	ifstream fans(argv[2]);
	string Tmp1,Tmp2;
	while (fstd >>Tmp1){
		fans>>Tmp2;
		if (Tmp1!=Tmp2) return 1;
	}
	if (fans >> Tmp2) return 1;
	return 0;
}
