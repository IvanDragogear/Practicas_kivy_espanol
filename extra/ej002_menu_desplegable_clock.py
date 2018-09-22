# -*- coding: utf-8 -*-
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.clock import Clock

from kivy.lang import Builder

STRING_STYLE = '''		
<MainWid>:
	size_hint: 1,1
	canvas:
		Color:
			rgb: 1,1,1
		Rectangle:
			size: self.size
			pos: self.pos
	MenuBoton:
		text: "Menu"
		size_hint: None,None
		size: 100,100
		pos: root.width-100,300
		on_press: self.action()
	MenuDesplegable:
		id: md
		size_hint: None,None
		size: 300,400
		pos: root.width,0
			
<MenuDesplegable@BoxLayout>:
	orientation: "vertical"
	Button:
		text: "Botón 1"
	Button:
		text: "Botón 2"
	Button:
		text: "Botón 3"
	Button:
		text: "Botón 4"
	Button:
		text: "Botón 5"

'''

Builder.load_string(STRING_STYLE)
	
class MainWid(RelativeLayout):
	ESCALA = (0.8,0.6)
	def __init__(self,**kwargs):
		super(MainWid,self).__init__(**kwargs)
		
class MenuBoton(Button):
	estado = 0
	velocidad = 800 #Pixeles por segundo
	def action(self):
		if self.estado == 0:
			Clock.schedule_once(self.desplegar)
		elif self.estado == 1:
			Clock.schedule_once(self.ocultar)
			
	def desplegar(self,*args):
		dt = args[0]
		pos_final = mainwid.width-400
		md = mainwid.ids.md
		if self.x > pos_final:
			self.x = self.x - self.velocidad*dt
		if self.x <= pos_final:
			self.x = pos_final
			self.estado = 1
		else:
			Clock.schedule_once(self.desplegar)
		md.x = self.x+100
		
	def ocultar(self,*args):
		dt = args[0]
		pos_final = mainwid.width -100
		md = mainwid.ids.md
		if self.x < pos_final:
			self.x = self.x + self.velocidad*dt
		if self.x >= pos_final:
			self.x = pos_final
			self.estado = 0
		else:
			Clock.schedule_once(self.ocultar)
		md.x = self.x+100

class MainApp(App):
	title = "Menu desplegable con Clock"
	def build(self):
		global app
		global mainwid
		app = self
		mainwid = MainWid()
		return mainwid
        
if __name__ == '__main__':
    MainApp().run()
