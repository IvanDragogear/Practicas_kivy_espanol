import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import NoTransition 
from kivy.uix.screenmanager import SlideTransition 
#from kivy.uix.screenmanager import CardTransition 
from kivy.uix.screenmanager import SwapTransition 
from kivy.uix.screenmanager import FadeTransition 
from kivy.uix.screenmanager import WipeTransition 
from kivy.uix.screenmanager import FallOutTransition 
from kivy.uix.screenmanager import RiseInTransition 

class MainWid(ScreenManager):
    #transition = NoTransition()
    #transition = SlideTransition()
    #transition = SwapTransition()
    #transition = FadeTransition()
    #transition = WipeTransition()
    #transition = FallOutTransition()
    #transition = RiseInTransition()
    pass
    
class UnaScreen(Screen):
    pass
    
class MainApp(App):
    title = "Screen Manager"
    def build(self):
        return MainWid()
        
if __name__ == "__main__":
    MainApp().run()
