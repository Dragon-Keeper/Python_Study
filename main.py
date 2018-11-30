
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
import kivy
kivy.require('1.10.1')
# coding: UTF-8

#  Kivy文件内注释不能用python的格式
#  from kivy.lang import Builder
#  from kivy.uix.label import Label
#  from kivy.uix.boxlayout import BoxLayout
#  from kivy.uix.textinput import TextInput
#  from kivy.graphics import Color, Rectangle  # 为背景添加颜色，画矩形
#  from kivy.config import Config

#  声明MyLayout，否则会报错：MyFloatLayout未定义


class TextInput(FloatLayout):  # 这个类用于接收输入的变化然后赋值
    pass


class BackGround(FloatLayout):  # 这个类用于接收输入的赋值然后显示出来
    pass


class RandomNoApp(App):
    def __init__(self, **kwargs):
        super(RandomNoApp, self).__init__(**kwargs)

    def build(self):
        return BackGround()


RandomNoApp().run()
