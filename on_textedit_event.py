# -*- coding: utf-8 -*-

'''
on_textedit event sample.
'''
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.textinput import TextInput
from kivy.base import EventLoop


# 为了使用属性，你必须在一个类里面声明它们，注意是直接写在类里面，而不是写在任何的类的方法里，它是一个类属性。每一个属性都默认提供了一个on_<propertyname>事件；当属性值的状态和属性值发生改变时该事件均会被调用。
class TextInputIME(TextInput):  # 这个类用于接收输入的变化然后赋值
    testtext = StringProperty()  # 将testtext定义为一个字符属性

    def __init__(self, **kwargs):  # （此句格式固定）要创建一个自定义事件，需要在一个类中注册事件名，并创建一个同名的方法
        # （此句格式固定）只需这里的TextInputIME与上面类名TextInputIME同名即可
        super(TextInputIME, self).__init__(**kwargs)
        EventLoop.window.bind(on_textedit=self._on_textedit)  # 添加下面_on_textedit事件的处理方法：on_textedit
        # 触屏消息的处理是在函数开始的 EventLoop.idle() 里进行的
        # bind:将一个方法绑定到一个消息类型,用于保存方法的是一个list类型

    def _on_textedit(self, window, text):  # 这个是这个属性里的textedit（文件编辑）事件
        self.testtext = text  # 每次发生文件编辑事件时，将text的值赋值给testtext

    # 好，上面这个类注册了消息类型和消息的处理过程，按下来就要等消息上门了。


class MainWidget(Widget):  # 这个类用于接收输入的赋值然后显示出来
    text = StringProperty()  # 将text定义为一个字符属性

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.text = ''  # 创建一个自定义事件,设定text的值为空，等待赋值

    def confim(self):  # 用来将输入的内容显示在label上，关联button的on_press
        self.text = self.ids["text_box"].text  # 使用ids来访问带id标识的对象，将text_box赋值给text，而text_box取值自输入栏


class TextEditTestApp(App):
    def __init__(self, **kwargs):
        super(TextEditTestApp, self).__init__(**kwargs)

    def build(self):
        return MainWidget()


if __name__ == '__main__':
    Builder.load_string('''
<MainWidget>:
    BoxLayout:
        orientation: 'vertical'
        size: root.size

        BoxLayout:
            Label:
                size_hint_x: 3
                text: "Enter text ->"
            TextInputIME:
                id: text_box  # 设定id，用来给confim函数取值
                size_hint_x: 7
                focus: True
        BoxLayout:
            Button:
                size_hint_x: 3
                text: "Confirm text property"
                on_press: root.confim()  # 如果点击，则调用confim函数
            Label:
                size_hint_x: 7
                text: root.text  # 从根层次取值text，就是上面confim函数的作用
                canvas.before:
                    Color:
                        rgb: 0.5765 ,0.5765 ,0.5843
                    Rectangle:
                        pos: self.pos
                        size: self.size
    ''')
    TextEditTestApp().run()
