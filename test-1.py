from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.graphics import Color, Rectangle # 为背景添加颜色



Builder.load_string('''
<MyLayout>:
    FloatLayout:
        canvas:
            Color:
                rgba: 0.38, 0.49, 0.55, 1 # 前面三个对应红、绿、蓝，最后一个为透明度80%，所有值为0-1之间
            Rectangle:
                pos:7, 205
                size: 324, 388
            Line:
                #  前两位表示矩形的左下角位置，三四位表示宽度和高度，5-8是两个边框之间的像素数（圆角度数），最后一位用于在每个角绘制圆弧的线段数（默认为30），越大越圆润
                rounded_rectangle:7, 205, 324, 388, 3, 3, 3, 3, 30
                #  宽度设置为以宽度为1时为中心，向两边扩展，如果width为50的话，就是向线两边扩展50的宽度
                width:5

''')

class MyLayout(BoxLayout): #  声明MyLayout，否则会报错：MyFloatLayout未定义
    pass

class TutorialApp(App):
    def build(self):
        return MyLayout()

TutorialApp().run()
