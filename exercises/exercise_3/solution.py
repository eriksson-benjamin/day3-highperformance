# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:22:52 2021

@author: bener807
"""

from classroom import Student
from classroom import Teacher

B = Student('Benjamin', 'Eriksson', 'Physics')
B.print_name_subject()

T = Teacher('Filipe', 'Maia', 'Advanced Scientific Programming in Python')
T.print_name_course()
