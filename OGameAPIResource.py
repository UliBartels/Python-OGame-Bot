from OGameAPI import _Entity

#This is a more specialized class for the resource producing buildings.
#These are the differences (apart from the more obvious production and consumption
#_buildime: Buildtime for Resource buildings depends on the level of my Robotics or Nanite Factory
#buildable: Resource buildings consume energy. This needs to be taken into account when looking to build them.

class _Resource(_Entity):
	
	robotics_level = 0
	nanite_level = 0
	
	def __init__(self, browser, cost_increase_factor, base_costs, id, link, base_production, base_consumption):
		_Entity.__init__(self, browser, cost_increase_factor, base_costs, id, link)
		self.base_production = base_production
		self.base_consumption = base_consumption
		
		self.power_cost = self._consumption() #In case of the Fusion Reactor this translates into Deuterium_cost
		self.production = self._production()
	
	def _consumption(self):
		return self.base_consumption * ((self.level * pow(1.1, self.level)) - (self.level - 1) * pow(1.1, (self.level - 1)))
	
	def _production(self): #Production in Hours
		return self.base_production * self.level * pow(1.1, self.level)
	
	def _buildtime(self): #Buildtime in Seconds
		buildtime = int(60*60*(self.metal_upgrade_cost + self.crystal_upgrade_cost) / (2500 * max(4 - self.level / 2, 1) * (1 + self.robotics_level) * pow(2,self.nanite_level)))
		print "Projected Buildtime is: " + str(int(buildtime/60)) + "m and " + str(buildtime%60) + "s. (or: " +str(buildtime) + " seconds)"		
		return buildtime
	
	def buildable(self, browser): #Function is redefined for resource buildings to also take into consideration their energy consumption.
		self._change_browser(browser)
		[metal_available, crystal_available, deuterium_available, energy_available] = self._fetch_resources_available()

		if self.metal_upgrade_cost <= metal_available and self.crystal_upgrade_cost <= crystal_available and self.deuterium_upgrade_cost <= deuterium_available and self.power_cost <= energy_available:
				return 1
		return 0