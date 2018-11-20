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
            #Rectangle:
            #    pos:2, 200
            #    size: 334, 398
            Line:
                rounded_rectangle:100, 100, 200, 200, 10, 10, 10, 10, 30
                width:50

''')

class MyLayout(BoxLayout): #  声明MyLayout，否则会报错：MyFloatLayout未定义
    pass

class TutorialApp(App):
    def build(self):
        return MyLayout()

TutorialApp().run()
