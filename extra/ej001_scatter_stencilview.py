# -*- coding: utf-8 -*-
import kivy
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stencilview import StencilView
from kivy.properties import ListProperty
from kivy.clock import Clock

Builder.load_string('''
<Grafica>:
    canvas:
        Color:
            rgb: .3,.3,1
        Line:
            width: .5
            points: self.eje_y
        Color:
            rgb: 1,.3,.3
        Line:
            width: 2
            points: self.lista_de_puntos_01

<ContenedorPricipal>:
    canvas:
        Color:
            rgb: .2,.2,.2
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        orientation: "vertical"
        padding: [10,10,10,10]
        spacing: 5
        VistaLimitada:
            id: panel_grafico
            size_hint: 1,0.8
            canvas:
                Color:
                    rgb: 1,1,1
                Rectangle:
                    pos: self.pos
                    size: self.size
            Scatter:
                id: lienzo
                size: panel_grafico.size
                do_rotation: False
                do_translation: False
                Grafica:
                    id: grafica
        GridLayout:
            cols: 4
            raws: 2
            size_hint: [1,0.2]
            spacing: 2
            Button:
                text: 'f(x) 1'
                on_press: root.funcion_de_seno()
            Button:
                text: 'Centrar'
                on_press: root.centrar_cero_eje_y(lienzo.height/2.,lienzo.width)
            Button:
                text: "Acecar"
                on_press: root.acercar()
            Button:
                text: "Alejar"
                on_press: root.alejar()
            Button:
                text: "+X"
                on_press: root.escalar_x(2)
            Button:
                text: "-X"
                on_press: root.escalar_x(-2)
            Button:
                text: "+Y"
                on_press: root.escalar_y(2)
            Button:
                text: "-Y"
                on_press: root.escalar_y(-2)
''')

from math import sin,cos,pi

def frange(start, stop, step):
    i = start
    while i < stop:
        yield i  # yield es como "return" pero no interrumpe el ciclo
        i += step

class ContenedorPricipal(FloatLayout):
    escala_grafica_x = 10
    escala_grafica_y = 50
    altura_cero_eje_y = 0

    def __init__(self):
        super(ContenedorPricipal, self).__init__()
        Clock.schedule_once(self.adaptar_grafica)

    def adaptar_grafica(self,dt):
        h = self.ids.lienzo.height
        w = self.ids.lienzo.width
        self.centrar_cero_eje_y(h/2.0,w)

    def acercar(self): # Aquí usamos el atributo "scale" de "Scatter"
        self.ids.lienzo.scale += .05

    def alejar(self):# Aquí también usamos el atributo "scale" de "Scatter"
        self.ids.lienzo.scale -= .05

    def escalar_x(self,escala):
        self.escala_grafica_x += escala
        self.funcion_de_seno()

    def escalar_y(self,escala):
        self.escala_grafica_y += escala
        self.funcion_de_seno()

    def centrar_cero_eje_y(self,altura,ancho):
        self.ids.grafica.eje_y = [0,altura,ancho,altura]
        self.altura_cero_eje_y = altura
        self.funcion_de_seno()

    def funcion_de_seno(self):
        points = []
        for x in frange(0,100,0.1):
            y = (2*cos(x+(pi/2.)))+1
            points.append(x*self.escala_grafica_x)
            points.append(y*self.escala_grafica_y+self.altura_cero_eje_y)
        self.ids.grafica.lista_de_puntos_01 = points

class VistaLimitada(BoxLayout,StencilView):
    # La StencilView es para que los que se dibuje dentro de este widget
    # no se salga del mismo
    pass

class Grafica(BoxLayout):
    lista_de_puntos_01 = ListProperty([])
    eje_y = ListProperty([0,0,1000,0])

class MainApp(App):
    def build(self):
        return ContenedorPricipal()

if __name__ == "__main__":
    MainApp().run()