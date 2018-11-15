from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.graphics import Color, Rectangle # 为背景添加颜色


Builder.load_string('''
<MyLayout>: #  kv代码中被<>包裹住的是某个class的名字，这个class需在python代码中声明，它们代表同一个class。
#    FloatLayout:
#        Label:
#            id: my_label #设定Label的名称
#            text: my_textinput1.text + '-' + my_textinput2.text #  直接调用my_textinput的text属性
#            font_size: 80
#            size_hint_y: None
#            on_text: root.color_change() #当文本变化时，调用函数。root表示最上层的类，本例中就是指MyLayout类。
#    BoxLayout:
#        orientation: 'horizontal'
#        size_hint_y: None
#        height: 150
#        Label:
#            text: 'Reset'
#            font_size: 100
#        Label:
#            text: 'Save'
#            font_size: 100
    orientation: 'vertical' #  定义竖直排布
#  以下为背景画布
    FloatLayout:
        canvas:
            Color:
                rgba: 1, 1, 1, 1 # 前面三个对应红、绿、蓝，最后一个为透明度80%，所有值为0-1之间
            Rectangle:
                pos:0, 0
                size:338, 600

#  以下为显示随机数结果画布
    FloatLayout:
        canvas:
            Color:
                rgba: 0.38, 0.49, 0.55, 1 # 前面三个对应红、绿、蓝，最后一个为透明度80%，所有值为0-1之间
            Rectangle:
                pos:2, 200
                size: 334, 398
        Label:
            text: 'Press To Random NO.'
            font_size:16
            pos:90, 210
            size_hint: .19, .055
            color: 1, 1, 1, 1

#  以下为显示历史数据画布
    FloatLayout:
        canvas:
            Color:
                rgba: 0.27, 0.36, 0.4, 1 # 前面三个对应红、绿、蓝，最后一个为透明度80%，所有值为0-1之间
            Rectangle:
                pos:2, 50
                size: 334, 148

#  以下为按钮、输入区画布
    FloatLayout:

#        Button:
#            text: "Reset"
#            font_size:12
#            pos_hint: {'x': .02, 'y': .01}#  与widget最左边边线距离为总长的3%位置，与widget最底边边线距离为总长的1%位置
#            size_hint: .1, .056 # widget最左边边线的1%长，widget最底边边线的5.6%高
#            background_color:0.0, 0.6, 0.66, 1 #  设置按钮text颜色(用手机上的HSV颜色对应找到vec3颜色)
#        Button:
#            text: "Save"
#            font_size:12
#            pos_hint: {'x': .16, 'y': .01}
#            size_hint: .1, .056
#            background_color:0.0, 0.6, 0.66, 1
#        Button:
#            text: "Set"
#            font_size:12
#            pos_hint: {'x': .88, 'y': .01}
#            size_hint: .1, .056
#           background_color:0.0, 0.6, 0.66, 1

#  按钮、输入区画布白色背景
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1 # 前面三个对应红、绿、蓝，最后一个为透明度100%，所有值为0-1之间
            Rectangle:
                pos:0, 0
                size: 338, 50

#  用画布来生成一条线
        canvas:
            Color:
                rgba: 0, 0, 0, 1 # 前面三个对应红、绿、蓝，最后一个为透明度100%，所有值为0-1之间
            Rectangle:
                pos:2, 46
                size: 334, 1

        Label:
            text: 'RESET'
            font_size:13
            pos:15, 20
            size_hint: .06, .01
            color: 0, 0, 0, 1
        Label:
            text: 'Min_No:'
            font_size:13
            pos:78, 20
            size_hint: .06, .01
            color: 0, 0, 0, 1
        TextInput:
            id: my_textinput1 #  设定id为my_textinput，方便后续调用
            font_size:13
            pos:128, 8
            size_hint: .05, .18
            #  text: 'Min' #  定义默认的文本内容
        Label:
            text: 'Max_No:'
            font_size:13
            pos:178, 20
            size_hint: .06, .01
            color: 0, 0, 0, 1
        TextInput:
            id: my_textinput2 #  设定id为my_textinput，方便后续调用
            font_size:13
            pos:228, 8
            size_hint: .05, .18
            #  text: 'Max' #  定义默认的文本内容
        Label:
            text: 'SET'
            font_size:13
            pos:280, 20
            size_hint: .06, .01
            color: 0, 0, 0, 1
''')

class MyLayout(BoxLayout): #  声明MyLayout，否则会报错：MyFloatLayout未定义
    pass

class TutorialApp(App):
    def build(self):
        return MyLayout()

TutorialApp().run()