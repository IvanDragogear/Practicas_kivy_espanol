# -*- coding: utf-8 -*-
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.lang.builder import Builder

STRING_STYLE = '''
<MyButton@Button>:
    background_normal: "Imagenes/Boton_verde.png"
    background_down: "Imagenes/Boton_verde.png"
    bold: True
    font_size: self.width/10

<WidStyle>:
    canvas:
        Color:
            rgb: .01,.2,.01
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        size_hint: .2,1
    BoxLayout:
        orientation: 'vertical'
        MyButton:
            text: 'Estilo 1'
            on_press: app.root.change_style(1)
        MyButton:
            text: 'Estilo 2'
            on_press: app.root.change_style(2)
        MyButton:
            text: 'Estilo 3'
            on_press: app.root.change_style(3)
    BoxLayout:
        size_hint: .2,1
'''

Builder.load_string(STRING_STYLE)
Builder.load_file("Estilos/Estilo01.kv")
#Builder.unload_file("Estilos/Estilo01.kv")
Builder.load_file("Estilos/Estilo02.kv")

class WidAlfa(BoxLayout):
    def __init__(self):
        super(WidAlfa,self).__init__()
        self.add_widget(WidStyle())
    
    def change_style(self,int_style):
        self.clear_widgets()
        if int_style == 1:
            self.add_widget(WidStyle())
        elif int_style == 2:
            self.add_widget(WidStyle1())
        elif int_style == 3:
            self.add_widget(WidStyle2())
    
class WidStyle(BoxLayout):
    None
    
class WidStyle1(BoxLayout):
    None
    
class WidStyle2(BoxLayout):
    None
    
class MainApp(App):
    def build(self):
        return WidAlfa()
        
if __name__ == '__main__':
    MainApp().run()
