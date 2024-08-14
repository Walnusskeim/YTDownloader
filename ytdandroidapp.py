import time

import kivy
from pytube import YouTube
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout


kivy.require('1.9.0')


class GridLayout(GridLayout):
    # Initialize ifinite keywords
    def __init__(self, **kwargs):
        # Call grid layout constructor
        super(GridLayout, self).__init__(**kwargs)

        # Set columns
        self.cols = 1

        # Add widgets
        self.add_widget(Label(text="YT-Downloader"))

        self.add_widget(Label(text="Gib hier deinen Link ein"))

        self.url = TextInput(multiline=True)
        self.add_widget(self.url)

        self.download = Button(text="Download", font_size=32)
        self.add_widget(self.download)

        #self.download.bind(on_press=self.press)

        self.add_widget(Label(text="(Das Video wird in den Download Ordner gespeichert)"))

    def press(self, instance):
        url = self.url.text
        try:
            path = "/storage/emulated/0/Download/"

            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            stream.download(path)

        except:
            self.add_widget(Label(text="Das war wohl kein YouTube Link!"))
            self.url.text = ""


class YTDownloader(App):
    def build(self):
        return GridLayout()

if __name__ == "__main__":
    YTDownloader().run()
