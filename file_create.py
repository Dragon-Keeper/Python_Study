#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def file_create(name,msg):
    file_path='d://users/desktop/'
    file_path_name=file_path+name+'.txt'
    file=open(file_path_name,'w')
    print('准备写入的内容是：'+msg)
    file.write(msg)
    file.close()
    print('写入完毕')
file_create('TheOne',input('请输入你想写入的内容：'))
     
    