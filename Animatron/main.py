import kivy
import kivent_core

import kivy
import kivent_core

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.factory import Factory

from kivent_core.systems.gamesystem import GameSystem

from Configuracion import Animatron

class Sis_Animacion(GameSystem):
	None

Factory.register('Sis_Animacion', cls=Sis_Animacion)

class MotorJuego(Widget):
	L_KEYS = []
	L_Comandos = []
	def __init__(self, **kwargs):
		super(MotorJuego, self).__init__(**kwargs)
		Window.bind(on_key_down=self.Key_Down)
		Window.bind(on_key_up=self.Key_Up)
		self.gameworld.init_gameworld(
			['renderer','position','color'],
			callback=self.init_game)

	def init_game(self):
		self.setup_states()
		self.set_state()
		self.load_models()
		self.draw_some_stuff()
		Clock.schedule_interval(self.update,0.033)
		
	def load_models(self):
		None

	def draw_some_stuff(self,*args):
		ie = self.gameworld.init_entity
		p = [150,175]
		#t = 'Ejemplo_Paso00'
		t = 'Anim0'
		cd = {'color':[255,255,255,255],'position': p,
		'renderer': {'texture': t,'size':[300,350]}}
		ID=ie(cd,['color','position','renderer'])
		self.Jugador = self.gameworld.entities[ID]
		self.Animatron = Animatron(self,self.Jugador)

	def setup_states(self):
		self.gameworld.add_state(state_name='main',
			systems_added=['color','renderer'],
			systems_removed=[], 
			systems_paused=[],
			systems_unpaused=['color','renderer'],
			screenmanager_screen='main')

	def set_state(self):
		self.gameworld.state = 'main'
	
	def Key_Down(self, window, key,*args):
		if not key in self.L_KEYS:
			self.L_KEYS.append(key)
			if key == 32:
				self.Comando_Agr("Acc_1")
			if key == 114:
				self.Comando_Agr("Acc_2")
			if key == 273:
				self.Comando_Agr("Mov_N")
			if key == 274:
				self.Comando_Agr("Mov_S")
			if key == 275:
				self.Comando_Agr("Mov_E")
			if key == 276:
				self.Comando_Agr("Mov_O")
		return True

	def Key_Up(self, window, key,*args):
		if key in self.L_KEYS:
			self.L_KEYS.remove(key)
			if key == 32:
				self.Comando_Qui("Acc_1")
			if key == 114:
				self.Comando_Qui("Acc_2")
			if key == 273:
				self.Comando_Qui("Mov_N")
			if key == 274:
				self.Comando_Qui("Mov_S")
			if key == 275:
				self.Comando_Qui("Mov_E")
			if key == 276:
				self.Comando_Qui("Mov_O")
		return True
		
	def Comando_Agr(self,Comando):
		# Coamndos: Mov_N, Mov_S, Mov_O, Mov_E, Acc_1, Acc_2, Acc_3, Pausa
		if not Comando in self.L_Comandos:
			self.L_Comandos.append(Comando)
			print Comando
			if Comando == "Mov_N":
				None
			if Comando == "Mov_S":
				None
			if Comando == "Mov_O":
				None
			if Comando == "Mov_E":
				None
			if Comando == "Acc_1":
				self.VX += 1
				self.ElArquitecto.Dibujar(self.VX)
			if Comando == "Acc_2":
				self.VX = 0
			if Comando == "Acc_3":
				None
			if Comando == "Pausa":
				None

	def Comando_Qui(self,Comando):
		# Coamndos: Mov_N, Mov_S, Mov_O, Mov_E, Acc_1, Acc_2, Acc_3, Pausa
		if Comando in self.L_Comandos:
			self.L_Comandos.remove(Comando)
			if Comando == "Mov_N":
				None
			if Comando == "Mov_S":
				None
			if Comando == "Mov_O":
				None
			if Comando == "Mov_E":
				None
			if Comando == "Acc_1":
				None
			if Comando == "Acc_2":
				None
			if Comando == "Acc_3":
				None
			if Comando == "Pausa":
				None
				
	def update(self,dt):
		self.Animatron.Actualizar()

class DebugPanel(Widget):
	fps = StringProperty(None)

	def __init__(self, **kwargs):
		super(DebugPanel, self).__init__(**kwargs)
		Clock.schedule_once(self.update_fps)

	def update_fps(self,dt):
		self.fps = str(int(Clock.get_fps()))
		Clock.schedule_once(self.update_fps, .05)

class MainApp(App):
	def build(self):
		Window.clearcolor = (0, 0, 0, 1.)

if __name__ == '__main__':
	MainApp().run()
