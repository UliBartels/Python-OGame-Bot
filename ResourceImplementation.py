from OGameAPIResource import _Resource
from OGameAPI import _Entity

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

	def _production(self, ): #Production in Hours ### Commented out for now as I don't have Research yet ###
		return self.base_production * self.level * pow((1.05 + _Entity.energy_technology) * 0.01, self.level)

		
class Solar_sattelites(_Resource):
	
	def __init__(self, browser):
		print "Initializing Solar Sattelites"
		_Resource.__init__(self, browser, 0, [0,2000,500], 'button6', 'http://s115-us.ogame.gameforge.com/game/index.php?page=resources', 0, 0)
		self._planet_overview = 'http://s115-us.ogame.gameforge.com/game/index.php?page=overview'
		
		#self.production = self._solar_production(browser)
		
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