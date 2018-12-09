from kivy.app import App
# from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label


class MyLabel(Image):
    text = StringProperty('')

    def on_text(self, *_):
        # Just get large texture:
        l = Label(text=self.text)
        l.font_size = '1000dp'  # something that'll give texture bigger than phone's screen size
        l.texture_update()
        # Set it to image, it'll be scaled to image size automatically:
        self.texture = l.texture


class RootWidget(BoxLayout):
    pass


class TestApp(App):
    def build(self):
        return MyLabel(text='Test test test')


if __name__ == '__main__':
    TestApp().run()
