import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock

Window.clearcolor = (0.5, 0.5, 0.5, 1)
Window.size = (400, 100)

Builder.load_string('''
<MyLayout>:
    BoxLayout:
        orientation: "vertical"
        padding : 20, 20
        BoxLayout:
            orientation: "horizontal"
            padding: 10, 10 #  padding:控制的是widget和窗口边缘的间隔
            spacing: 10, 10 #  spacing: 控制的是各个widget之间的间隔
            size_hint_x: .6

            Label:
                text: "Number"
                text_size: self.size
                valign: 'bottom'
                halign: 'right'
                size_hint_x: .2

            TextInput:
                size_hint_x: .2
                id : test
                #padding_x:[10,0]
                #padding_y:[10,0]
''')

class MyLayout(BoxLayout): #  声明MyLayout，否则会报错：MyFloatLayout未定义
    pass

class Testing(Screen):

    def __init__(self, **kwargs):
        super(Testing, self).__init__(**kwargs)
        Clock.schedule_once(lambda dt: setattr(self.test, 'text', str(100)))

class Test(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    Test().run()
