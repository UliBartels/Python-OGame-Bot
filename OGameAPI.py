#Downloaded Libraries
import mechanize
from bs4 import BeautifulSoup

#Built in Libraries
from math import pow
import re
import time

#################
#LOGIN VARIABLES#
#################
myUsername = 'Redacted'
myPassword = 'Redacted'
mySystem = 's115-us.ogame.gameforge.com' #Orion

#This is the base class for all research, resource, and facility objects
#This class holds an object's upgrade costs, can check if that object can be built and send a build command to the server.
#Furthermore every object in this script has the ability to login to the website again as well as change sites to fetch
#the relevant HTML.
class _Entity: 
	
	#These variables are variables shared between all instances of Entity.
	#I use html to reduce the number of times I need to request a website from the OGame servers by keeping a local copy.
	html = None
	
	#The facilities and research levels are also stored globally to deal with dependencies.
	#FACILITIES
	robotics_level = 0
	shipyard_level = 0
	research_level = 0
	alliance_level = 0
	missile_level = 0
	nanite_level = 0
	terraformer_level = 0
	
	#RESEARCH
	energy_technology = 0
	laser_technology = 0
	ion_technology = 0
	hyperspace_technology = 0
	plasma_technology = 0
	combustion_drive = 0
	impulse_drive = 0
	hyperspace_drive = 0
	espionage_technology = 0
	computer_technology = 0
	astrophysics = 0
	intergalactic_research_network = 0
	graviton_technology = 0
	weapons_technology = 0
	shielding_technology = 0
	armor_technology = 0
	
	def __init__(self, browser, cost_increase_factor, base_costs, id, link):
		self.id = id
		self.link = link #Link needs to be established before the call to update_level.
		self.level = 0
		
		self._update_level(browser)
		
		self.base_cost_metal = base_costs[0]
		self.base_cost_crystal = base_costs[1]
		self.base_cost_deuterium = base_costs[2]
		self.cost_increase_factor = cost_increase_factor
		
		self.metal_upgrade_cost = self._calculate_build_cost(self.base_cost_metal, self.cost_increase_factor)
		self.crystal_upgrade_cost = self._calculate_build_cost(self.base_cost_crystal, self.cost_increase_factor)
		self.deuterium_upgrade_cost = self._calculate_build_cost(self.base_cost_deuterium, self.cost_increase_factor)
	
	#Login is called whenever a request to browser.open fails. This function takes a browser object,
	#configures so that the OGame server won't immediately recognize it as a script and then login to the
	#game using the Login data provided above.
	def _login(self, browser):
		browser.set_handle_robots(False)
		user_agent = 'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0'
		
		browser.addheaders = [('User-agent', user_agent)] #OGame doesn't want Bots to traverse its HTML, so we change our TCP header to mask ourselves as a Mozilla Browser

		request = mechanize.Request('http://us.ogame.gameforge.com/')
		_Entity.html = browser.open(request)

		print "Processing Login."
		browser.select_form('loginForm')

		control = browser.form.find_control('uni') #Small workaround to deal with the dropdown menu.
		for item in control.items:
			if item.name == mySystem:
				item.selected = True

		browser.form['login'] = myUsername
		browser.form['pass'] = myPassword

		browser.submit() #And we're in.
	
	#For the script to work we need to fetch the HTML from the different tabs available
	#i.e. Resource, Facilities, Research etc...
	def _change_browser(self, browser):
		try:
			if self.link not in browser.geturl():
				_Entity.html = browser.open(self.link).read()
			if not _Entity.html:
				_Entity.html = browser.open(self.link).read()
		except:
			self._login(browser)
			_Entity.html = browser.open(self.link).read()
	
	def _calculate_build_cost(self, base_cost, cost_increase_factor):
		return int(base_cost * pow(cost_increase_factor, self.level))
	
	def _update_costs(self, browser):
		self._update_level(browser)
		self.metal_upgrade_cost = self._calculate_build_cost(self.base_cost_metal, self.cost_increase_factor)
		self.crystal_upgrade_cost = self._calculate_build_cost(self.base_cost_crystal, self.cost_increase_factor)
		self.deuterium_upgrade_cost = self._calculate_build_cost(self.base_cost_deuterium, self.cost_increase_factor)
	
	def _update_level(self, browser):
		self._change_browser(browser)
		
		html = _Entity.html
		html_crawler = BeautifulSoup(html)
		html_level_string = str(html_crawler.find(id = self.id).find('span',{'class':'level'})).replace(".","")
		self.level =  int(re.search('\d+', html_level_string).group(0)) #Using regular expressions, I can strip out the solitary level decimal
	
	#Whenever we want to build something we need to first test if we have the resources available.
	def _fetch_resources_available(self):
		html = _Entity.html
		html_crawler = BeautifulSoup(html)
		html_level_string = str(html_crawler.find('span',{'id':'resources_metal'})).replace(".","")
		metal_available = int(re.search('\d+', html_level_string).group(0))
		
		html_level_string = str(html_crawler.find('span',{'id':'resources_crystal'})).replace(".","")
		crystal_available = int(re.search('\d+', html_level_string).group(0))
		
		html_level_string = str(html_crawler.find('span',{'id':'resources_deuterium'})).replace(".","")
		deuterium_available = int(re.search('\d+', html_level_string).group(0))
		
		html_level_string = str(html_crawler.find('span',{'id':'resources_energy'})).replace(".","")
		energy_available = int(re.search('\d+', html_level_string).group(0))
		
		return [metal_available, crystal_available, deuterium_available, energy_available]
		
	def build(self, browser):
		self._change_browser(browser)
		html = _Entity.html
		
		html_crawler = BeautifulSoup(html)
		html_level_string = str(html_crawler.find(id = self.id))
		try:
			upgrade_link = re.search('Request\(\'(.+?)\',',html_level_string).group(1).replace("amp;","")
			if upgrade_link:
				print "for " + str(self.metal_upgrade_cost) + "metal, " + str(self.crystal_upgrade_cost) + "crystal, " + str(self.deuterium_upgrade_cost) + "deuterium"
				
				try:
					html = browser.open(upgrade_link)
				except:
					print upgrade_link
					
				html_crawler = BeautifulSoup(html.read())
				html_level_string = str(html_crawler.find(id = self.id))
				try:
					build_check = re.search('class="on"',html_level_string).group(0) #When a building is built the corresponding class is set to 'on', this is how we know that our upgrade is working properly.
					if build_check:
						return self._buildtime()
				except AttributeError:	
					return 0
		except AttributeError:
			return 0
			
		return 0
		
	def buildable(self, browser):
		self._update_costs(browser)
		
		[metal_available, crystal_available, deuterium_available, energy_available] = self._fetch_resources_available()
		
		if self.metal_upgrade_cost <= metal_available and self.crystal_upgrade_cost <= crystal_available and self.deuterium_upgrade_cost <= deuterium_available and self.power_cost <= energy_available:
				return 1
		return 0