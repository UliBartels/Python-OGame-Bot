from OGameAPI import _Entity

class _Storage(_Entity):
	
	def __init__(self, browser, cost_increase_factor, base_costs, id, link):
		_Entity.__init__(self, browser, cost_increase_factor, base_costs, id, link)
		self.storage_capacity = int(2.5 * pow(2.7182818284590451,(20 * self.level/33)) * 5000)