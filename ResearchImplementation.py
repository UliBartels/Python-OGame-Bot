from OGameAPIFacility import _Facility #Turns out that Facilities and Research Levels are really similar. We only really care about their levels.
from OGameAPI import _Entity

class Energy_technology(_Facility):
	def __init__(self, browser):
		print "Initializing Energy Technology"
		_Facility.__init__(self, browser, 2, [0,800,400], 'details113', 'http://s115-us.ogame.gameforge.com/game/index.php?page=research')
	
	def _set_level(self):
		_Entity.energy_technology = self.level
		
class Laser_technology(_Facility):
	def __init__(self, browser):
		print "Initializing Laser Technology"
		_Facility.__init__(self, browser, 2, [200,100,0], 'details120', 'http://s115-us.ogame.gameforge.com/game/index.php?page=research')
	
	def _set_level(self):
		_Entity.laser_technology = self.level
		
class Ion_technology(_Facility):
	def __init__(self, browser):
		print "Initializing Ion Technology"
		_Facility.__init__(self, browser, 2, [1000,300,100], 'details121', 'http://s115-us.ogame.gameforge.com/game/index.php?page=research')
	
	def _set_level(self):
		_Entity.ion_technology = self.level
		
class Hyperspace_technology(_Facility):
	def __init__(self, browser):
		print "Initializing Hyperspace Technology"
		_Facility.__init__(self, browser, 2, [0,4000,2000], 'details114', 'http://s115-us.ogame.gameforge.com/game/index.php?page=research')
	
	def _set_level(self):
		_Entity.hyperspace_technology = self.level
		
class Plasma_technology(_Facility):
	def __init__(self, browser):
		print "Initializing Plasma Technology"
		_Facility.__init__(self, browser, 2, [2000,4000, 1000], 'details122', 'http://s115-us.ogame.gameforge.com/game/index.php?page=research')
		
	def _set_level(self):
		_Entity.plasma_technology = self.level

class Combustion_drive(_Facility):
	def __init__(self, browser):
		print "Initializing Combustion Drive"
		_Facility.__init__(self, browser, 2, [400,0, 600], 'details115', 'http://s115-us.ogame.gameforge.com/game/index.php?page=research')
		
	def _set_level(self):
		_Entity.combustion_drive = self.level

class Impulse_drive(_Facility):
	def __init__(self, browser):
		print "Initializing Impulse Drive"
		_Facility.__init__(self, browser, 2, [2000,4000, 600], 'details117', 'http://s115-us.ogame.gameforge.com/game/index.php?page=research')
		
	def _set_level(self):
		_Entity.impulse_drive = self.level

class Hyperspace_drive(_Facility):
	def __init__(self, browser):
		print "Initializing Hyperspace Drive"
		_Facility.__init__(self, browser, 2, [10000,20000, 6000], 'details118', 'http://s115-us.ogame.gameforge.com/game/index.php?page=research')
		
	def _set_level(self):
		_Entity.hyperspace_drive = self.level		

class Espionage_technology(_Facility):
	def __init__(self, browser):
		print "Initializing Espionage Technology"
		_Facility.__init__(self, browser, 2, [200,1000,200], 'details106', 'http://s115-us.ogame.gameforge.com/game/index.php?page=research')
	
	def _set_level(self):
		_Entity.espionage_technology = self.level
		
class Computer_technology(_Facility):
	def __init__(self, browser):
		print "Initializing Computer Technology"
		_Facility.__init__(self, browser, 2, [200,1000,200], 'details108', 'http://s115-us.ogame.gameforge.com/game/index.php?page=research')
	
	def _set_level(self):
		_Entity.computer_technology = self.level
		
class Astrophysics(_Facility):
	def __init__(self, browser):
		print "Initializing Astrophysics"
		_Facility.__init__(self, browser, 2, [4000,8000,4000], 'details124', 'http://s115-us.ogame.gameforge.com/game/index.php?page=research')
	
	def _set_level(self):
		_Entity.astrophysics = self.level
		
class Intergalactic_research_network(_Facility):
	def __init__(self, browser):
		print "Initializing Intergalactic Research Network"
		_Facility.__init__(self, browser, 2, [240000,400000,160000], 'details123', 'http://s115-us.ogame.gameforge.com/game/index.php?page=research')
	
	def _set_level(self):
		_Entity.intergalactic_research_network = self.level
		
class Graviton_technology(_Facility):
	def __init__(self, browser):
		print "Initializing Graviton Technology"
		_Facility.__init__(self, browser, 2, [0,0,0], 'details199', 'http://s115-us.ogame.gameforge.com/game/index.php?page=research')
	
	def _set_level(self):
		_Entity.graviton_technology = self.level
		
	def buildable(self):
		return 0 #Need to implement a check for Energy Levels here, so for now it's just not buildable.
		
class Weapons_technology(_Facility):
	def __init__(self, browser):
		print "Initializing Weapons Technology"
		_Facility.__init__(self, browser, 2, [800,200,0], 'details109', 'http://s115-us.ogame.gameforge.com/game/index.php?page=research')
	
	def _set_level(self):
		_Entity.weapons_technology = self.level
		
class Shielding_technology(_Facility):
	def __init__(self, browser):
		print "Initializing Shielding Technology"
		_Facility.__init__(self, browser, 2, [200,600,0], 'details110', 'http://s115-us.ogame.gameforge.com/game/index.php?page=research')
	
	def _set_level(self):
		_Entity.shielding_technology = self.level
		
class Armor_technology(_Facility):
	def __init__(self, browser):
		print "Initializing Armor Technology"
		_Facility.__init__(self, browser, 2, [1000,600,0], 'details111', 'http://s115-us.ogame.gameforge.com/game/index.php?page=research')
	
	def _set_level(self):
		_Entity.armor_technology = self.level

