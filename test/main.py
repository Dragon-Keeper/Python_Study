from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# from kivy.properties import ObjectProperty
# from kivy.uix.label import Label
# from kivy.factory import Factory
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.storage.jsonstore import JsonStore
store = JsonStore('data.json')
store.put('SaveData', ran_no="1", his_no="2", his_no_sort="3")


class MainScreen(Screen):
    store = JsonStore('data.json')  # 建立数据文件data.json
    if store.exists('SaveData'):
        store.get('SaveData')
        ran_no = store.get('SaveData')['ran_no']
        his_no_sort = store.get('SaveData')['his_no_sort']
        his_no = store.get('SaveData')['his_no']
    # store.put('SaveData', ran_no=ran_no, his_no=his_no, his_no_sort=his_no_sort)


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
