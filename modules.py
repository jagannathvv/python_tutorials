#Modules is a way to resuse a code written by someone else

import math #import modules written by someone else using import command. 

print(math.sqrt(16)) #use math modules squareroot function to find the square root of a number
print(math.pi)
print(math.log10(100))

print(dir(math)) #dir function lists the functions available in a module. 

import calendar

cal = calendar.month(2021,1)
print(cal)

print(calendar.isleap(2022))
print(calendar.isleap(2020))

# pip is used to install modules from internet
# pip - pip installs packages
# syntax - pip install/uninstall <<package_name>>
# pip uses pypi index. google pypi to know more about packages available online. 

#writing your own module
import geoareas #import your module by using filename without .py extension. 
                #File should be in the same directory as your program

print(geoareas.cal_sq_area(5))
print(geoareas.cal_tri_area(10,6))

import librarym.geoareasm as garea #import your module by using foldername.filename without .py extension. 
                                   # you can also import file in some random directory. first import sys
                                   # then use function sys.path.append("fully qualified module path")
print(garea.cal_sq_area(5))
print(garea.cal_tri_area(10,6))

