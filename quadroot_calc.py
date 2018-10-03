#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
a=int(input('a: '))
b=int(input('b: '))
c=int(input('c: '))

x1= (-b+ math.sqrt(b*b-4*a*c))/2*a
x2= (-b- math.sqrt(b*b-4*a*c))/2*a
if (math.sqrt(b*b-4*a*c)<0):
    print('complex roots')
else:
    print (x1,',',x2)
"""
Created on Mon Sep 17 19:07:10 2018

@author: mayank
"""

