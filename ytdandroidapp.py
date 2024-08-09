import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from pytube import YouTube


kivy.require('1.9.0')


class YTDownloader(App):
    def build(self):
        return BoxLayout()

## Still trying to figure the GUI out. ##
## Will work on downloading after that. ##
    #def download(self, instance):
     #   url = self.url.text
      #  download_video(url)

    #def download_video(self, url):
     #   yt = YouTube(url)
      #  stream = yt.streams.get_highest_resolution()
       # steam.download(/storage/emulated/0/Download/)

if __name__ == "__main__":
    YTDownloader().run()
