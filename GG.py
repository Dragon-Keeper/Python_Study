#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def gg(a,b):
    c = (a**2+b**2)**0.5
    return round(c,2);
aa=float(input('第一条直角边::'));
bb=float(input('第二条直角边::'));
da=gg(aa,bb);
print('三角形斜边长为::', da);