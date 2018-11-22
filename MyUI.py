from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.graphics import Color, Rectangle # 为背景添加颜色，画矩形
from kivy.config import Config

def on_touch_down(self, touch):
    if self.collide_point(*touch.pos):

        #如果触摸检测来自我们自己的部件，让我们捕获它。
        touch.grab(self)
        # 并响应这次触摸.
        return True

def on_touch_up(self, touch):
    #这里，你不用检测触摸碰撞或类似操作，
    #你仅需要检测是否它是一个捕获的触摸事件
    if touch.grab_current is self:
        #OK，当前触摸事件被派发给我们
        #做一些感兴趣的操作
        print('Hello world!')
        #不要忘记释放掉，否则可能会有副作用
        touch.ungrab(self)
        #最后响应这次触摸
        return True

Builder.load_string('''
<MyLayout>: #  kv代码中被<>包裹住的是某个class的名字，这个class需在python代码中声明，它们代表同一个class。
#    FloatLayout:
#        Label:
#            id: my_label #设定Label的名称
#            text: my_textinput1.text + '-' + my_textinput2.text #  直接调用my_textinput的text属性
#            font_size: 80
#            size_hint_y: None
#            on_text: root.color_change() #当文本变化时，调用函数。root表示最上层的类，本例中就是指MyLayout类。

    orientation: 'vertical' #  定义竖直排布
#  以下为背景画布
    FloatLayout:
        canvas:
            Color:
                rgba: 1, 1, 1, 1 # 前面三个对应红、绿、蓝，最后一个为透明度80%，所有值为0-1之间
            Rectangle:
                pos:0, 0
                size:337.5, 600

#  标题画布上面留白20的高度给电量、时间导航栏

#  以下为显示标题画布
    FloatLayout:
        canvas:
            Color:
                rgba: 0.08, 0.41, 0.76, 1 # 前面三个对应红、绿、蓝，最后一个为透明度80%，所有值为0-1之间
            Rectangle:
                pos:7, 554
                size: 324, 21
            #  用矩形函数画一条线来填补下面画圆角时上面两个角弧度为零时出现的两个缺口
            Rectangle:
                pos:2, 534
                size: 334, 25
            Line: #  画线函数画一个圆角
                #  前两位表示矩形的左下角位置，三四位表示宽度和高度，5-8是两个边框之间的像素数（圆角度数），最后一位用于在每个角绘制圆弧的线段数（默认为30），越大越圆润
                rounded_rectangle:7, 554, 324, 21, 0, 0, 3, 3, 30
                #  宽度设置为以宽度为1时为中心，向两边扩展，如果width为50的话，就是向线两边扩展50的宽度
                width:5

#  以下为显示历史数据画布，为了指纹按钮能浮现在历史数据画布上，需要将指纹按钮所在的随机数结果画布拍到后面，拥有更高的显示优先级
    FloatLayout:
        canvas.before:
            Color:
                rgba: 0.05, 0.29, 0.64, 1 # 前面三个对应红、绿、蓝，最后一个为透明度80%，所有值为0-1之间
            Rectangle:
                pos:2, 30
                size: 334, 173
        canvas.after:
            Color:
                rgba: 1, 1, 1, 1 # 前面三个对应红、绿、蓝，最后一个为透明度100%，所有值为0-1之间
            #  功能键上面的的线条
            Line:
                points: [30, 192, 308, 192]
                width:1.5

#  以下为显示随机数结果画布
    FloatLayout:
        canvas:
            Color:
                rgba: 0.13, 0.61, 0.96, 1 # 前面三个对应红、绿、蓝，最后一个为透明度80%，所有值为0-1之间
            Rectangle:
                pos:2, 193
                size: 334, 346

        #  导入图片
        Button:
            background_normal: '2.png'
            background_down: '2.png'
            #pos:137, 170
            pos_hint:{'x':.172, 'y':.42}
            size_hint:None,None #  要使用确定的像素大小的话就要将大小比例参数关闭
            size:60, 60
        Label:
            text: 'RAN             DOM'
            font_size:22
            #pos:94, 202
            #  pos_hint是一个字典，默认为空。正如size_hint, 布局对使用pos_hint分别对待，通常你可以添加任何pos特征值(x, y, left, top, center_x, center_y)
            pos_hint:{'x':.15, 'y':.3}
            #size_hint: .19, .055
            size_hint:None,None #  要使用确定的像素大小的话就要将大小比例参数关闭
            color: 1, 1, 1, 1

#  以下为按钮、输入区画布
    FloatLayout:

#  按钮、输入区画布白色背景
        canvas.before:
            Color:
                rgba: 0.05, 0.29, 0.64, 1 # 前面三个对应红、绿、蓝，最后一个为透明度100%，所有值为0-1之间

            #  用矩形函数画一条线来填补下面画圆角时上面两个角弧度为零时出现的两个缺口
            Rectangle:
                pos:2, 55
                size: 334, 25
            Line: #  画线函数画一个圆角
                #  前两位表示矩形的左下角位置，三四位表示宽度和高度，5-8是两个边框之间的像素数（圆角度数），最后一位用于在每个角绘制圆弧的线段数（默认为30），越大越圆润
                rounded_rectangle:7, 25, 324, 30, 3, 3, 0, 0, 30
                #  宽度设置为以宽度为1时为中心，向两边扩展，如果width为50的话，就是向线两边扩展50的宽度
                width:5

#  用画布来生成一条线
        canvas:
            Color:
                rgba: 1, 1, 1, 1 # 前面三个对应红、绿、蓝，最后一个为透明度100%，所有值为0-1之间
            #  Random按钮旁的线条
            Line:
                points: [30, 60, 308, 60]
                width:1.2

#  在输入框下生成一根线提示输入，Line函数必须在canvas画布函数下才行
            Line: #  Min_No
                points: [120, 27, 172, 27]
                width:1.2
            Line: #  Max_No
                points: [226, 27, 278, 27]
                width:1.2
        Label:
            text: 'Clear'
            font_size:18
            pos:25, 38
            #size_hint: .06, .01
            size_hint:None,None #  要使用确定的像素大小的话就要将大小比例参数关闭
            size:20.28, 0.5
            color: 1, 1, 1, 1

        Label:
            text: 'Min:'
            font_size:18
            pos:86, 38
            #size_hint: .06, .01
            size_hint:None,None #  要使用确定的像素大小的话就要将大小比例参数关闭
            size:20.28, 0.5
            color: 1, 1, 1, 1

# 通过设置background_normal和background_active为空将输入框边框取消
        TextInput:
            id: my_textinput1 #  设定id为my_textinput，方便后续调用
            font_size:18
            pos:115, 27
            #size_hint: .07, .18
            size_hint:None,None #  要使用确定的像素大小的话就要将大小比例参数关闭
            size:62, 30
            #  text: 'Min' #  定义默认的文本内容
            multiline: False #  设置输入框为单行，不能换行
            background_normal:'' #  输入框未激活时TextInput的背景图像，用空图片来屏蔽输入框边框
            background_active:'' #  输入框激活时TextInput的背景图像，用空图片来屏蔽输入框边框
            background_color:0.05, 0.29, 0.64, 1
            padding_x:[1,0] #  设置X轴方向的对齐位移，后面的0没什么用
            padding_y:[8,0] #  设置Y轴方向的对齐位移，后面的0没什么用
            on_text: self.foreground_color = (1,1,1,1) #  当点击输入框时，将输入文字颜色设置为白色

        Label:
            text: 'Max:'
            font_size:18
            pos:192, 38
            #size_hint: .06, .01
            size_hint:None,None #  要使用确定的像素大小的话就要将大小比例参数关闭
            size:20.28, 0.5
            color: 1, 1, 1, 1

        TextInput:
            id: my_textinput2 #  设定id为my_textinput，方便后续调用
            font_size:18
            pos:220, 27
            #size_hint: .07, .18
            size_hint:None,None #  要使用确定的像素大小的话就要将大小比例参数关闭
            size:62, 30
            #  text: 'Max' #  定义默认的文本内容
            multiline: False
            background_normal:'' #  输入框未激活时TextInput的背景图像，用空图片来屏蔽输入框边框
            background_active:'' #  输入框激活时TextInput的背景图像，用空图片来屏蔽输入框边框
            background_color:0.05, 0.29, 0.64, 1
            padding_x:[1,0] #  设置X轴方向的对齐位移，后面的0没什么用
            padding_y:[8,0] #  设置Y轴方向的对齐位移，后面的0没什么用
            on_text: self.foreground_color = (1,1,1,1) #  当点击输入框时，将输入文字颜色设置为白色

        Label:
            text: 'Set'
            font_size:18
            pos:300, 38
            #size_hint: .06, .01
            size_hint:None,None #  要使用确定的像素大小的话就要将大小比例参数关闭
            size:20.28, 0.5
            color: 1, 1, 1, 1
''')

class MyLayout(BoxLayout): #  声明MyLayout，否则会报错：MyFloatLayout未定义
    pass

class TutorialApp(App):
    def build(self):
        return MyLayout()

TutorialApp().run()
