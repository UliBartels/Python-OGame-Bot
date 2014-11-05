from OGameAPI import _Entity

class _Facility(_Entity):
	
	def __init__(self, browser, cost_increase_factor, base_costs, id, link):
		_Entity.__init__(self, browser, cost_increase_factor, base_costs, id, link)
		self._set_level()
	
	def _buildtime(self): #Buildtime in Seconds
		buildtime = int(60*60*(self.metal_upgrade_cost + self.crystal_upgrade_cost) / (2500 * max(4 - self.level / 2, 1) * (1 + self.robotics_level) * pow(2,self.nanite_level)))
		print "Projected Buildtime is: " + str(int(buildtime/60)) + "m and " + str(buildtime%60) + "s. (or: " +str(buildtime) + " seconds)"		
		return buildtime

	def _set_level(self):
		raise NotImplementedError("This function needs to be set within the Facility implementations.")
	
	def buildable(self, browser): #Function is redefined for facility buildings to also take into consideration their prerequisites.
		self._change_browser(browser)	
		
		[metal_available, crystal_available, deuterium_available, energy_available] = self._fetch_resources_available()
		
		if self.metal_upgrade_cost < metal_available and self.crystal_upgrade_cost < crystal_available and self.deuterium_upgrade_cost < deuterium_available:
				return 1
		return 0