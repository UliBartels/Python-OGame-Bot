from OGameAPIFacility import _Facility
from OGameAPI import _Entity

import math #I need this one in order to be able to use a single pow over in the Terraformer. -.-
		
#####################
#Research Facilities#
#####################

class Robotics_factory(_Facility):
	def __init__(self, browser):
		print "initializing Robotics Facility"
		_Facility.__init__(self, browser, 2, [400,120,200], 'button0', 'http://s115-us.ogame.gameforge.com/game/index.php?page=station')
	
	def _set_level(self):
		_Entity.robotics_level = self.level
		
class Shipyard(_Facility):
	def __init__(self, browser):
		print "Initializing Shipyard"
		_Facility.__init__(self, browser, 2, [200,400,200], 'button2', 'http://s115-us.ogame.gameforge.com/game/index.php?page=station')
	
	def _set_level(self):
		_Entity.shipyard_level = self.level
		
class Research_lab(_Facility):
	def __init__(self, browser):
		print "Initializing Research Lab"
		_Facility.__init__(self, browser, 2, [200,400,200], 'button2', 'http://s115-us.ogame.gameforge.com/game/index.php?page=station')
	
	def _set_level(self):
		_Entity.research_level = self.level
		
class Alliance_depot(_Facility):
	def __init__(self, browser):
		print "Initializing Alliance Depot"
		_Facility.__init__(self, browser, 2, [20000,40000,0], 'button3', 'http://s115-us.ogame.gameforge.com/game/index.php?page=station')
	
	def _set_level(self):
		_Entity.alliance_level = self.level
		
class Missile_silo(_Facility):
	def __init__(self, browser):
		print "Initializing Missile Silo"
		_Facility.__init__(self, browser, 2, [20000,20000,10000], 'button4', 'http://s115-us.ogame.gameforge.com/game/index.php?page=station')
		
	def _set_level(self):
		_Entity.missile_level = self.level
		
class Nanite_factory(_Facility):
	def __init__(self, browser):
		print "Initializing Nanite Factory"
		_Facility.__init__(self, browser, 2, [1000000,500000,100000], 'button5', 'http://s115-us.ogame.gameforge.com/game/index.php?page=station')
		
	def _set_level(self):
		_Entity.nanite_level = self.level
		
class Terraformer(_Facility):
	def __init__(self, browser):
		print "Initializing Terraformer"
		_Facility.__init__(self, browser, 2, [0,100000,0], 'button6', 'http://s115-us.ogame.gameforge.com/game/index.php?page=station')
		
	
	def _set_level(self):
		_Entity.terraformer_level = self.level
		
	def buildable(self, browser):
		self._update_costs(browser)
		
		[metal_available, crystal_available, deuterium_available, energy_available] = _fetch_resources_available(self)
		
		if 1000*math.pow(2,self.level) <= energy_available and self.crystal_upgrade_cost <= crystal_available:
				return 1
		return 0
		