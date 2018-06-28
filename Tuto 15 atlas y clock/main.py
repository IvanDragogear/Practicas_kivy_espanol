import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.clock import Clock

class WidAlfa(BoxLayout):
    my_source = StringProperty('atlas://media/ejemplo.atlas/paso3')
    frame_count = 0

    my_ruta = 'atlas://media/ejemplo.atlas/'
    frames = ['paso1','paso2','paso3','paso4','paso5','paso6',
              'paso7','paso8']
    frame_control = [0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7]

    #my_ruta = 'atlas://media/Flash.atlas/'
    #frames = ['FlashR_01','FlashR_02','FlashR_03','FlashR_04',
    #    'FlashR_05','FlashR_06','FlashR_07','FlashR_08','FlashR_09',
    #    'FlashR_10',]
    #frame_control = [
    #    0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5,
    #    6,6,7,7,6,6,7,7,6,6,7,7,6,6,7,7,6,6,7,7,6,6,7,7,6,6,7,7,6,6,7,7,6,6,7,7,
    #    6,6,7,7,6,6,7,7,6,6,7,7,6,6,7,7,6,6,7,7,6,6,7,7,6,6,7,7,6,6,7,7,6,6,7,7,
    #    6,6,7,7,6,6,7,7,6,6,7,7,6,6,7,7,6,6,7,7,6,6,7,7,6,6,7,7,6,6,7,7,6,6,7,7,
    #    8,8,8,8,8,9,9,9,9,9,5,5,5,5,5,4,4,4,4,4,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,0]


    def __init__(self):
        super(WidAlfa,self).__init__()
        Clock.schedule_interval(self.animation,1/60.)

    def animation(self,dt):
        self.frame_count += 1
        if self.frame_count >= len(self.frame_control):
            self.frame_count = 0
        key = self.frames[self.frame_control[self.frame_count]]
        self.my_source = self.my_ruta+key

class MainApp(App):
    def build(self):
        return WidAlfa()

if __name__ == '__main__':
    MainApp().run()
