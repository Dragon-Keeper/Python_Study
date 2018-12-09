import kivy
import random
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.storage.jsonstore import JsonStore
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.uix.textinput import TextInput
from kivy.base import EventLoop
kivy.require('1.10.1')
# coding: UTF-8

#  Kivy文件内注释不能用python的格式
#  from kivy.lang import Builder
#  from kivy.uix.label import Label
#  from kivy.uix.boxlayout import BoxLayout
#  from kivy.graphics import Color, Rectangle  # 为背景添加颜色，画矩形
#  from kivy.config import Config

store = JsonStore('data.json')  # 建立数据文件data.json
if store.exists('SaveData'):
    store.get('SaveData')
    ran_no = store.get('SaveData')['ran_no']
    his_no_sort = store.get('SaveData')['his_no_sort']
    his_no = store.get('SaveData')['his_no']
    min_show = store.get('SaveData')['min_show']
    max_show = store.get('SaveData')['max_show']
# -----------------------------以下为监测输入框内容等待赋值-----------------------
# 为了使用属性，你必须在一个类里面声明它们，注意是直接写在类里面，而不是写在任何的类的方法里，它是一个类属性。每一个属性都默认提供了一个on_<propertyname>事件；当属性值的状态和属性值发生改变时该事件均会被调用。


class TextInput_No(TextInput):  # 这个类用于接收输入的变化然后赋值
    testtext = StringProperty()  # 将testtext定义为一个字符属性

    def __init__(self, **kwargs):  # （此句格式固定）要创建一个自定义事件，需要在一个类中注册事件名，并创建一个同名的方法
        # （此句格式固定）只需这里的TextInput_No与上面类名TextInput_No同名即可
        super(TextInput_No, self).__init__(**kwargs)
        EventLoop.window.bind(on_textedit=self._on_textedit)  # 添加下面_on_textedit事件的处理方法：on_textedit
        # 触屏消息的处理是在函数开始的 EventLoop.idle() 里进行的
        # bind:将一个方法绑定到一个消息类型,用于保存方法的是一个list类型

    def _on_textedit(self, window, text):  # 这个是这个属性里的textedit（文件编辑）事件
        self.testtext = text  # 每次发生文件编辑事件时，将text的值赋值给testtext
# -----------------------------以上为监测输入框内容等待赋值------------------------
# -----------------------------以下为将输入框内容赋值给具体函数--------------------


class RootWidget(FloatLayout):  # 这个类用于接收输入的赋值然后显示出来
    min_no_input = StringProperty()  # 将text定义为一个字符属性
    max_no_input = StringProperty()
    min_show = StringProperty()
    max_show = StringProperty()
    ran_no = StringProperty()
    his_no = StringProperty()
    his_no_sort = StringProperty()
    clearnot_color = NumericProperty()
    container = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.min_no_input = ''  # 创建一个自定义事件,设定min_no_input的值为空，等待赋值
        self.max_no_input = ''
        self.min_show = ''
        self.max_show = ''
        self.ran_no = ''
        self.his_no_sort = ''
        self.his_no = ''
        self.clearnot_color = 0.5
        self.set_no = set()

    def confim(self):  # 用来将输入的内容显示在label上，关联button的on_press
        # ----------------------判断输入是否为空，空的话弹出提示要求输入内容--------
        # 使用ids来访问带id标识的对象，将text_box赋值给text，而text_box取值自输入栏
        self.min_no_input = self.ids["textinput_min"].text
        self.max_no_input = self.ids["textinput_max"].text
        # 将输入的内容传递给函数以保存
        self.min_show = self.ids["textinput_min"].text
        self.max_show = self.ids["textinput_max"].text

        # 加入判断输入是否为空的语句，如果是空的话，重新载入主页面等待输入
        while self.min_show == '' or self.max_show == '' or self.min_show == ' ' or self.max_show == ' ':
            Builder.load_file('randomno.kv')
            break
        else:
            # 由于input函数输入的是str字符串型，必须转换为整数型才能进行随机运算
            min = int(self.min_no_input)
            max = int(self.max_no_input)
            # 下面这段判断语句用来将输入数据按大小赋值给随机函数，输入框不限制哪个输入大/小
            if min < max:
                min_no = min
                max_no = max
            else:
                max_no = min
                min_no = max
# ------------------------------以下为随机数生成过程------------------------------
            random_no = random.randint(min_no, max_no)  # 产生范围内的随机数
            if random_no not in self.set_no:  # 判断随机数是否已存在，如果不存在则写入集合
                print('新的随机数生成：' + str(random_no))  # 调试用的输出
            else:
                Random_Times = 1  # 定义函数用来计算随机次数
                while random_no in self.set_no:  # 判断随机数是否已存在，如果存在则重新产生随机数直到不存在
                    print(str(random_no) + '：已经存在')  # 调试用的输出
                    random_no = random.randint(min_no, max_no)  # 产生范围内的随机数
                    Random_Times = Random_Times + 1  # 每次循环次数加一
                    Max_Random_Times = max_no**2  # 循环输入数值最大数的平方次数
                    if Random_Times > Max_Random_Times:  # 当循环次数大于输入数值最大数的平方次数时
                        break  # 退出循环，要求从新输入范围
                    else:  # 经过循环重新产生不存在的随机数，然后写入集合
                        print('新的随机数经过循环生成：' + str(random_no))  # 调试用的输出
# ------------------------------以上为随机数生成过程------------------------------
            r_n = random_no
            self.set_no.add(r_n)  # 随机数写入集合
            list_set = list(self.set_no)  # 将集合转换成列表
            self.ran_no = str(r_n)  # 显示随机数
            self.his_no = self.his_no + str(r_n) + '->'  # 按随机数产生顺序显示随机结果
            list_set.sort()  # 列表按小到大排序，这样输出到数据文件就是顺序的了
            self.his_no_sort = str(list_set).replace(
                '[', '').replace(']', '').replace(',', ' ').replace('\'', '')
            # 通过计算列表内容的数量和"max"对比，相等时在非排序历史数据栏提示随机完毕
            no_len = max_no - min_no + 1
            if len(list_set) >= no_len:
                self.his_no = self.his_no + 'My Lord! Random Finish ^_^'
            else:
                pass
                # 建立字典SaveData，将值self.ran_no存在键ran_no下面。。。已起效
            store.put('SaveData', ran_no=self.ran_no, his_no=self.his_no,
                      his_no_sort=self.his_no_sort, max_show=self.max_show, min_show=self.min_show)

    def confim2(self):  # 用来将输入的内容显示在label上，关联button的on_press
        self.ran_no = ' '
        self.his_no_sort = ' '
        self.his_no = ' '
        self.min_show = ' '
        self.max_show = ' '
        self.set_no.clear()  # 通过清除集合内容来达到清除历史数据排序显示
        store.put('SaveData', ran_no=self.ran_no, his_no=self.his_no,
                  his_no_sort=self.his_no_sort, max_show=self.max_show, min_show=self.min_show)
        screen = Builder.load_file('randomno.kv')
        self.container.clear_widgets()  # 清除所有页面，防止通过点击激活旧的数据页面
        self.container.add_widget(screen)
        # 至此，Clear键大功告成，点击即刻返回空白的randomno.kv主页面

    def next_screen(self, screen):
        '''Clear container and load the given screen object from file in kv
        folder.

        :param screen: name of the screen object made from the loaded .kv file
        :type screen: str
        :rtype: none
    '''
        filename = screen + '.kv'
        # unload the content of the .kv file
        # reason: it could have data from previous calls
        # Builder.unload_file(filename)
        # clear the container
        self.container.clear_widgets()
        # 多次点击back而不clear时读取数据显示在next_screen-----下面代码可能没有，还可能会导致在clearnot2页面出现空赋值传递而导致出错
        # store = JsonStore('data.json')
        # if store.exists('SaveData'):
        #    store.get('SaveData')
        #    self.ran_no = store.get('SaveData')['ran_no']
        #    self.his_no_sort = store.get('SaveData')['his_no_sort']
        #    self.his_no = store.get('SaveData')['his_no']
        #    self.min_show = store.get('SaveData')['min_show']
        #    self.max_show = store.get('SaveData')['max_show']
        # 如果检测到载入判断返回/清除页面，将底色调黑
        if screen == 'clearnot':
            self.clearnot_color = 0.5
        else:
            self.clearnot_color = 0
        # load the content of the .kv file
        screen = Builder.load_file(filename)
        # add the content of the .kv file to the container
        self.container.add_widget(screen)
# -----------------------------以上为将输入框内容赋值给具体函数--------------------


class RandomNoApp(App):
    def __init__(self, **kwargs):
        super(RandomNoApp, self).__init__(**kwargs)


if __name__ == '__main__':
    RandomNoApp().run()
