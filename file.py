## new file

class Good(Object):
	def __init__(self,name):
		self.name = name

class FactoryProto(Object):
	def __init__(self,name,inputList,product):
		self.name = name
		self.inputGood = inputList
		self.outputGood = product
		self.size = 1000

class PopProto(Object):
	def __init__(self,name,need):
		self.name = name
		self.need = need

class Factory(Object):
	def __init__(self,proto):
		self.proto = proto
		self.employment = []

class Pop(Object):
	def __init__(self,proto):
		self.proto = proto

class WorldMarket(Object):
	pass

class LabourMarket(Object):
	pass

class World(Object):
	pass
