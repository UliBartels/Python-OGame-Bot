from bs4 import BeautifulSoup

from random import randint, seed
import re
import time

def build_resources(name, browser):

	enumerator = ['metal_mine','crystal_mine','deuterium_synth','solar_plant','fusion_reactor','solar_sattelites','metal_storage','crystal_storage','deuterium_storage','metal_den','crystal_den','deuterium_den']
	try:
		building_number = enumerator.index(name) + 1
	except ValueError:
		print 'Building is not part of resources'
		return
	
	#Stuff is broken left and right. I really need to move over to classes.
	time.sleep(0.5 * randint(2,4)) #Delays to prevent setting off any bot-detection scripts
	html = browser.open('http://s115-us.ogame.gameforge.com/game/index.php?page=resources')
	
	html_crawler = BeautifulSoup(html.read())
	html_level_string = str(html_crawler.find('li',{'id':'button' + str(building_number)}))
	upgrade_link = re.search('Request\(\'(.+?)\',',html_level_string).group(1).replace("amp;","")
	
	if upgrade_link:
		html = browser.open(upgrade_link)
		return 1
	else:
		return 0
	
def build_facility(name, browser):

	enumerator = ['shipyard','research_lab','alliance_depot','missile_silo','nanite_factory','terraformer']
	try:
		building_number = enumerator.index(name) + 1
	except ValueError:
		print 'Building is not part of facilities'
		return
		
	if not'page=station' in browser.geturl():
		time.sleep(0.5 * randint(2,4)) #Delays to prevent setting off any bot-detection scripts
		html = browser.open('http://s115-us.ogame.gameforge.com/game/index.php?page=station')
	
	html_crawler = BeautifulSoup(html.read())
	html_level_string = str(html_crawler.find('li',{'id':'button' + str(building_number)}))
	upgrade_link = re.search('Request\(\'(.+?)\',',html_level_string).group(1).replace("amp;","")
	
	if upgrade_link:
		html = browser.open(upgrade_link)
		return 1
	else:
		return 0
	
def build_research(name, browser):
	
	dictionary = {'energy_technology':'research113',
				'laser_technology':'research120',
				'ion_technology':'research121',
				'plasma_technology':'research122',
				'combustion_drive':'research115',
				'impulse_drive':'research117',
				'hyperspace_drive':'research118',
				'espionage_technology':'research106',
				'computer_technology':'research108',
				'astrophysics':'research124',
				'intergalactic_research_network':'research123',
				'graviton_technology':'research199',
				'weapons_technology':'research109',
				'shielding_technology':'research110',
				'armor_technology':'research111'}
	try:
		dictionary[name]
	except KeyError:
		print 'Building is not part of facilities'
		return
		
	if not'page=research' in browser.geturl():
		time.sleep(0.5 * randint(2,4)) #Delays to prevent setting off any bot-detection scripts
		html = browser.open('http://s115-us.ogame.gameforge.com/game/index.php?page=research')
		
	html_crawler = BeautifulSoup(html.read())
	html_level_string = str(html_crawler.find('div',{'class': str(dictionary[name])}))
	upgrade_link = re.search('Request\(\'(.+?)\',',html_level_string).group(1).replace("amp;","")
	
	if upgrade_link:
		html = browser.open(upgrade_link)
		return 1
	else:
		return 0