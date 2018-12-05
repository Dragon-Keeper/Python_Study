from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import BooleanProperty
from kivy.uix.popup import Popup


class SelectButton(Button):
    selected = BooleanProperty(False)

    def set_selection(self):
        self.selected = True


class SelectPopup(Popup):
    pass


class MainBox(BoxLayout):
    pass


class SelectButtonApp(App):
    def build(self):
        return MainBox()


if __name__ == "__main__":
    SelectButtonApp().run()
