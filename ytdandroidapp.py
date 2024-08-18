import time

import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from pytube import YouTube


kivy.require('1.9.0')

Builder.load_file('ytdownloader.kv')


class MyLayout(Widget):

    url = ObjectProperty(None)


    #def press(self):
        #try:
            #url = self.url.text
            #print("Das ist dein Link: ", url)

        #except:
         #   self.add_widget(Label(text="Das war wohl kein YouTube Link!"))
          #  self.url.text = ""

            #self.url.text = ""

        #try:
         #   path = "/storage/emulated/0/Download/"
#
 #           yt = YouTube(url)
  #          stream = yt.streams.get_highest_resolution()
   #         stream.download(path)
#
 #       except:
  #          self.add_widget(Label(text="Das war wohl kein YouTube Link!"))
   #         self.url.text = ""


class YTD(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    YTD().run()
