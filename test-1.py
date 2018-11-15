from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics.vertex_instructions import Rectangle, Ellipse, Line #导入矩形、椭圆、直线
from kivy.graphics.context_instructions import Color #导入颜色控件
from kivy.lang import Builder
import random

Builder.load_string('''
<ScatterTextWidget>:
    orientation: 'vertical'
    canvas: #创建画板
        Color:
            rgba: 0,0,1,1 #设置rgba色值
        Ellipse: #椭圆
            pos: 0, 400
            size: 200, 100
        Line: #直线段
            points: [0,0,500,600,400,300]
            close: True #直线闭合
            width: 3 #线条宽度
    TextInput:
        id: my_textinput
        font_size:150
        size_hint_y: None
        height: 200
        text: 'default'
    FloatLayout:
        Scatter:
            Label:
                id: my_label
                text: my_textinput.text
                font_size: 150
                on_text: root.color_change()
    BoxLayout:
        orientation: 'horizontal'
        size_hint_y: None
        height: 150
        Label:
            text: my_textinput.text[:3][::-1]
            font_size: 100
        Label:
            text: my_textinput.text[-3:][::-1]
            font_size: 100
''')
class ScatterTextWidget(BoxLayout):
    def color_change(self):
        label = self.ids['my_label']
        label.color = [random.random() for _ in range(3)] + [1]

class TutorialApp(App):
    def build(self):
        return ScatterTextWidget()

TutorialApp().run()
