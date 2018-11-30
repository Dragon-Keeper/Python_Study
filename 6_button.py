from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line


class MyPaintWidget(Widget):  # 定义一个类

    def on_touch_down(self, touch):  # 定义一个事件的处理办法
        color = (random(), 1, 1)
        with self.canvas:
            Color(*color, mode='hsv')
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


class MyPaintApp(App):  # 定义一个类，继承App类

    def build(self):  # 实现它的build()方法，它能返回一个部件的实例（你的部件树的根部件）
        parent = Widget()  # 定义父空间为Widget()
        self.painter = MyPaintWidget()  # 定义painter承接MyPaintWidget()这个类的内容
        clearbtn = Button(text='Clear')  # 定义一个按键，并且上面文字为Clear，将它连接到clearbtn上
        # 将类clear_canvas(self, obj)被点击（on_release）事件绑定到按键Clear上
        clearbtn.bind(on_release=self.clear_canvas)
        parent.add_widget(self.painter)  # 在父空间里添加MyPaintWidget()这个类的内容
        parent.add_widget(clearbtn)  # 在父空间里添加Clear按钮
        return parent  # 返回父空间内容并显示

    def clear_canvas(self, obj):  # 定义了一个类用于清空画布
        self.painter.canvas.clear()  # 每当调用这个函数时，清空画布内容


if __name__ == '__main__':
    MyPaintApp().run()  # 实例化该类，同时调用它的run()方法
