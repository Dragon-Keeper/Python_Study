import kivy

from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock

Window.clearcolor = (0.5, 0.5, 0.5, 1)
Window.size = (400, 100)

class Testing(Screen):

    def __init__(self, **kwargs):
        super(Testing, self).__init__(**kwargs)
        Clock.schedule_once(lambda dt: setattr(self.test, 'text', str(100)))

class Test(App):

    def build(self):
        self.root = Builder.load_file('test.kv')
        return self.root


if __name__ == '__main__':
    Test().run()
