from kivent_core.managers.resource_managers import texture_manager
#texture_manager.load_atlas('Sprites/Ejemplo.atlas')
texture_manager.load_atlas('Sprites/ProtoSprite_Estar.atlas')

class Animatron():
	def __init__(self,Nux,Modelo):
		self.Nux = Nux
		self.Mod = Modelo
		self.EstadoActual = 'DePie'
		self.EstadoAnterior = 'DePie'
		self.DireccionActual = 'Derecha'
		self.DireccionAnterior = 'Derecah'
		self.C01 = 0
		self.C02 = 0
		self.C03 = 0
		self.C04 = 0
		self.Retraso = 0
		self.RT = 4
		self.Invertir = False
		
	def Anim001(self):
		self.Retraso += 1
		if self.Retraso >= self.RT:
			self.Retraso = 0
			self.C01 += 1
			if self.C01 > 7:
				self.C01 = 0
			self.Mod.renderer.texture_key='Ejemplo_Paso0'+str(self.C01)
		
	def Anim002(self):
		self.Retraso += 1
		if self.Retraso >= self.RT:
			self.Retraso = 0
			if self.Invertir :
				self.C01 -= 1
				if self.C01 < 0:
					self.C01 = 0
					self.Invertir = False 
			else:
				self.C01 += 1
				if self.C01 > 4:
					self.C01 = 4
					self.Invertir = True
			self.Mod.renderer.texture_key='Anim'+str(self.C01)

	def Restaurar_Contadores(self):
		self.C01 = 0
		self.C02 = 0
		self.C03 = 0
		self.C04 = 0
		
	def Actualizar(self):
		if self.EstadoActual == 'DePie':
			self.Anim002()
