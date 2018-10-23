#!/usr/bin/python
import random
a=1;#代表包
b=2;#代表剪
c=3;#代表锤
d=random.choice((a,b,c));
#以上为随机abc其中一个并赋值给d，然后等待与人输入数据比较大小

e=int(input("玩家1:请输入1/2/3，分别代表包/剪/锤："));#实际程序中以按键分别代表a/b/c按键输入
f=int(input("玩家2:请输入1/2/3，分别代表包/剪/锤："));#实际程序中以按键分别代表a/b/c按键输入

#调试的时候根据数字显示包剪锤
if d==1:
  print("程序出了包");
elif d==2:
  print("程序出了剪");
elif d==3:
  print("程序出了锤");

if e==1:
  print("玩家1你出了包");
elif e==2:
  print("玩家1你出了剪");
elif e==3:
  print("玩家1你出了锤");
  
if f==1:
  print("玩家2你出了包");
elif f==2:
  print("玩家2你出了剪");
elif f==3:
  print("玩家2你出了锤");


if (d==1 and e==3):#这里有问题
  print("包VS锤：抱歉玩家1，你输了!");
elif (d==3 and e==1):
  print("锤VS包：恭喜玩家1，你赢了!");
elif d==e:
  print("玩家1：啊噢，平局!");
elif d>e:
  print("玩家1：抱歉，你输了!!");
elif d<e:
  print("玩家1：恭喜，你赢了!!");
  
if (d==1 and f==3):#这里有问题
  print("包VS锤：抱歉玩家2，你输了!");
elif (d==3 and f==1):
  print("锤VS包：恭喜玩家2，你赢了!");
elif d==f:
  print("玩家2：啊噢，平局!");
elif d>f:
  print("玩家2：抱歉，你输了!!");
elif d<f:
  print("玩家2：恭喜，你赢了!!");
