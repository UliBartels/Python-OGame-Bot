from OGameAPI import _Resource
from OGameAPI import _Storage
import math #I need this one in order to be able to use a single pow over in the Terraformer. -.-

##############################
#Resource Producing Buildings#
##############################
class Metal_mine(_Resource):
	def __init__(self, browser):
		print "Initializing Metal Mine"
		_Resource.__init__(self, browser, 1.5, [60,15,0], 'button1', 'http://s115-us.ogame.gameforge.com/game/index.php?page=resources', 30, 10)

		
class Crystal_mine(_Resource):
	def __init__(self, browser):
		print "Initializing Crystal Mine"
		_Resource.__init__(self, browser, 1.6, [48,24,0], 'button2', 'http://s115-us.ogame.gameforge.com/game/index.php?page=resources', 20, 10)

		
class Deuterium_synthesizer(_Resource):
	def __init__(self, browser):
		print "Initializing Deuterium Synthesizer"
		_Resource.__init__(self, browser, 1.5, [225,75,0], 'button3', 'http://s115-us.ogame.gameforge.com/game/index.php?page=resources', 10, 20)

		
class Solar_plant(_Resource):
	def __init__(self, browser):
		print "Initializing Solar Power Plant"
		_Resource.__init__(self, browser, 1.5, [75,30,0], 'button4', 'http://s115-us.ogame.gameforge.com/game/index.php?page=resources', 20, 0)

		
class Fusion_reactor(_Resource):
	def __init__(self, browser):
		print "Initializing Fusion Reactor"
		_Resource.__init__(self, browser, 1.5, [900,360,180], 'button5', 'http://s115-us.ogame.gameforge.com/game/index.php?page=resources', 30, -10)

	#def _production(self, energy_technology): #Production in Hours ### Commented out for now as I don't have Research yet ###
	#	return self.base_production * self.level * pow((1.05 + energy_technology) * 0.01, self.level)

		
class Solar_sattelites(_Resource):
	
	def __init__(self, browser):
		print "Initializing Solar Sattelites"
		_Resource.__init__(self, browser, 0, [0,2000,500], 'button6', 'http://s115-us.ogame.gameforge.com/game/index.php?page=resources', 0, 0)
		self._planet_overview = 'http://s115-us.ogame.gameforge.com/game/index.php?page=overview'
		
		self.production = self._solar_production(browser)
		
	def _calculate_build_cost(self, base_cost, cost_increase_factor): #Solar Satellites are special in that their cost never goes up.
		return base_cost
		
	def _solar_production(self, browser):
		try:
			if self._planet_overview not in browser.geturl():
				_Entity.html = browser.open(self._planet_overview).read()
		except:
			self._login(browser)
			_Entity.html = browser.open(self._planet_overview).read()
		
		html = _Entity.html
		html_crawler = BeautifulSoup(html)
		html_level_string = str(html_crawler.find('span',{'id':'resources_metal'})).replace("\xc2","")
		max_temperature = int(re.search('\d+(?=.C)', html_level_string).group(1))
		
		return int(self.level * int(max_temperature + 140))


#############################
#Resource Storing Facilities#
#############################
class Metal_storage(_Storage):
	def __init__(self, browser):
		print "Initializing Metal Storage"
		_Storage.__init__(self, browser, 2, [1000,0,0], 'button7', 'http://s115-us.ogame.gameforge.com/game/index.php?page=resources')

		
class Crystal_storage(_Storage):
	def __init__(self, browser):
		print "Initializing Crystal Storage"
		_Storage.__init__(self, browser, 2, [500,250,0], 'button8', 'http://s115-us.ogame.gameforge.com/game/index.php?page=resources')

		
class Deuterium_storage(_Storage):
	def __init__(self, browser):
		print "Initializing Deuterium Storage"
		_Storage.__init__(self, browser, 2, [1000,1000,0], 'button9', 'http://s115-us.ogame.gameforge.com/game/index.php?page=resources')
		
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
	def __init__(self, browser)
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
		