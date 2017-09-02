# -*- coding: utf-8 -*-
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty

from kivy.clock import Clock
from time import sleep

class WidAlfa(BoxLayout):
	contador_1 = StringProperty("0")
	contador_2 = StringProperty("0")
	pos_pelota = ListProperty([0,0])
	vx = 6
	vy = 3
	def __init__(self):
		super(WidAlfa,self).__init__()
		self.obj1 = Clock.schedule_interval(self.contar_1,1)
		Clock.schedule_once(self.contar_2,2)
		Clock.schedule_interval(self.mover_pelota,1/60.0)
	
	def contar_1(self,dt):
		self.contador_1 = str(int(self.contador_1)+1)
		if self.contador_1 == "5":
			self.obj1.cancel()
			sleep(5)
			
	def contar_2(self,dt):
		self.contador_2 = str(int(self.contador_2)+1)
		Clock.schedule_once(self.contar_2,2)
		
	def mover_pelota(self,dt):
		self.pos_pelota[0] += self.vx
		self.pos_pelota[1] += self.vy
		if self.pos_pelota[0]<0 or self.pos_pelota[0]>700:
			self.vx = self.vx*-1
		if self.pos_pelota[1]<0 or self.pos_pelota[1]>500:
			self.vy = self.vy*-1
		
class MainApp(App):
	def build(self):
		return WidAlfa()
		
if __name__ == "__main__":
	MainApp().run()
