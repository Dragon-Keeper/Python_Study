from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# from kivy.properties import ObjectProperty
# from kivy.uix.label import Label
# from kivy.factory import Factory
from kivy.uix.screenmanager import ScreenManager, Screen


class MainScreen(Screen):
    pass


class SubScreen(Screen):
    pass


class ScreenApp(App):

    def build(self):
        sm = ScreenManager()
        scm = MainScreen(name="main")
        scs = SubScreen(name="sub")
        sm.add_widget(scm)
        sm.add_widget(scs)
        return sm


ScreenApp().run()
