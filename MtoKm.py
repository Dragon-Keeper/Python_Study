#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def MtoKm(m):
    Km=float(m)*0.001
    return str(Km)+"Km"
minput=float(input('请输入要转换的长度(m):'))
print('你要转换的长度为'+str(minput)+'m')
print('转换后的长度为(Km):'+MtoKm(minput))
