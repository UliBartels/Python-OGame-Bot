#Custom Libraries
import mechanize #Can fill and submit forms
from bs4 import BeautifulSoup #Simplifies searching the HTML, might be included in mechanize already.

#Python Libraries
import time
import re
import cookielib
from random import randint, seed
from urllib import quote

#Function Libraries
from resource_data import *
from building_data import *
from build_functions import *

#################
#LOGIN VARIABLES#
#################
myUsername = 'Redacted'
myPassword = 'Redacted'
mySystem = 's115-us.ogame.gameforge.com'

############################
#Setting up Server spoofing#
############################
user_agent = 'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0'
seed() #Seeding random number gen

####################
#Logging into OGame#
####################
browser = mechanize.Browser()
cookie_jar = cookielib.LWPCookieJar()
browser.set_cookiejar(cookie_jar)
browser.set_handle_robots(False)#Ignore any Robot.txt's

browser.addheaders = [('User-agent', user_agent)] #OGame doesn't want Bots to traverse its HTML, so we change our TCP header to mask ourselves as a Mozilla Browser

request = mechanize.Request('http://us.ogame.gameforge.com/')
browser.open(request)

time.sleep(0.5 * randint(2,4)) #Delays to prevent setting off any bot-detection scripts

browser.select_form('loginForm')

control = browser.form.find_control('uni') #Small workaround to deal with the dropdown menu.
for item in control.items:
	if item.name == mySystem:
		item.selected = True

browser.form['login'] = myUsername
browser.form['pass'] = myPassword

time.sleep(0.5 * randint(2,4)) #Delays to prevent setting off any bot-detection scripts

browser.submit() #And we're in.

###########################
#Gathering Resource Levels#
###########################
print 'Gathering Resource Levels'
time.sleep(0.5 * randint(2,4)) #Delays to prevent setting off any bot-detection scripts
html = browser.open('http://s115-us.ogame.gameforge.com/game/index.php?page=resourcesSettings')
html_crawler = BeautifulSoup(html.read())

#Gathering Resource Data. Function returns a List [Amount in Storage, Storage Capacity, Current Production, Den Capacity]
metal_results = resource_level_gathering('metal_box', html_crawler)
crystal_results = resource_level_gathering('crystal_box', html_crawler)
deuterium_results = resource_level_gathering('deuterium_box', html_crawler)

#Energy and Darkmatter are special and thus get their own functions.
energy_results = energy_level_gathering(html_crawler)
darkmatter_results = darkmatter_level_gathering(html_crawler)

def update_resource_levels():
	html = browser.open('http://s115-us.ogame.gameforge.com/game/index.php?page=resourcesSettings')
	html_crawler = BeautifulSoup(html.read())

	#Gathering Resource Data. Function returns a List [Amount in Storage, Storage Capacity, Current Production, Den Capacity]
	metal_results = resource_level_gathering('metal_box', html_crawler)
	crystal_results = resource_level_gathering('crystal_box', html_crawler)
	deuterium_results = resource_level_gathering('deuterium_box', html_crawler)

	#Energy and Darkmatter are special and thus get their own functions.
	energy_results = energy_level_gathering(html_crawler)
	darkmatter_results = darkmatter_level_gathering(html_crawler)

###########################
#Gathering Research Levels#
###########################
        
print 'Gathering Research Levels'
time.sleep(0.5 * randint(2,4)) #Delays to prevent setting off any bot-detection scripts
html = browser.open('http://s115-us.ogame.gameforge.com/game/index.php?page=research')
html_crawler = BeautifulSoup(html.read())

energy_technology = research_level_extraction('energy_technology',html_crawler)
laser_technology = research_level_extraction('laser_technology',html_crawler)
ion_technology = research_level_extraction('ion_technology',html_crawler)
hyperspace_technology = research_level_extraction('hyperspace_technology',html_crawler)
plasma_technology = research_level_extraction('plasma_technology',html_crawler)
combustion_drive = research_level_extraction('combustion_drive',html_crawler)
impulse_drivel = research_level_extraction('impulse_drive',html_crawler)
hyperspace_drive = research_level_extraction('hyperspace_drive',html_crawler)
espionage_technology = research_level_extraction('espionage_technology',html_crawler)
computer_technology = research_level_extraction('computer_technology',html_crawler)
astrophysics_technology = research_level_extraction('astrophysics',html_crawler)
intergalactic_technology = research_level_extraction('intergalactic_research_network',html_crawler)
graviton_technology = research_level_extraction('graviton_technology',html_crawler)
weapons_technology = research_level_extraction('weapons_technology',html_crawler)
shielding_technology = research_level_extraction('shielding_technology',html_crawler)
armor_technology = research_level_extraction('armor_technology',html_crawler)

def update_technologies():
	time.sleep(0.5) #Delays to prevent setting off any bot-detection scripts
	html = browser.open('http://s115-us.ogame.gameforge.com/game/index.php?page=research')
	html_crawler = BeautifulSoup(html.read())
	
	energy_technology = research_level_extraction('energy_technology',html_crawler)
	laser_technology = research_level_extraction('laser_technology',html_crawler)
	ion_technology = research_level_extraction('ion_technology',html_crawler)
	hyperspace_technology = research_level_extraction('hyperspace_technology',html_crawler)
	plasma_technology = research_level_extraction('plasma_technology',html_crawler)
	combustion_drive = research_level_extraction('combustion_drive',html_crawler)
	impulse_drivel = research_level_extraction('impulse_drive',html_crawler)
	hyperspace_drive = research_level_extraction('hyperspace_drive',html_crawler)
	espionage_technology = research_level_extraction('espionage_technology',html_crawler)
	computer_technology = research_level_extraction('computer_technology',html_crawler)
	astrophysics_technology = research_level_extraction('astrophysics',html_crawler)
	intergalactic_technology = research_level_extraction('intergalactic_research_network',html_crawler)
	graviton_technology = research_level_extraction('graviton_technology',html_crawler)
	weapons_technology = research_level_extraction('weapons_technology',html_crawler)
	shielding_technology = research_level_extraction('shielding_technology',html_crawler)
	armor_technology = research_level_extraction('armor_technology',html_crawler)


######################################
#Gathering Resource Production Levels#
######################################				

print 'Gathering Resource Production Levels'
time.sleep(0.5 * randint(2,4)) #Delays to prevent setting off any bot-detection scripts
html = browser.open('http://s115-us.ogame.gameforge.com/game/index.php?page=resources')
html_crawler = BeautifulSoup(html.read())

metal_level = resource_building_level_extraction('metal_mine',html_crawler,0)
crystal_level = resource_building_level_extraction('crystal_mine',html_crawler,0)
deuterium_level = resource_building_level_extraction('deuterium_synth',html_crawler,0)
energy_level = resource_building_level_extraction('solar_plant',html_crawler,0)
fusion_reactor_level = resource_building_level_extraction('fusion_reactor',html_crawler,energy_technology) #The fusion reactor is special in that its efficiency depends on the level of Energy Technology
solar_sattelite_level = resource_building_level_extraction('solar_sattelites',html_crawler,0)
metal_storage_level = resource_building_level_extraction('metal_storage',html_crawler,0)
crystal_storage_level = resource_building_level_extraction('crystal_storage',html_crawler,0)
deuterium_storage_level = resource_building_level_extraction('deuterium_storage',html_crawler,0)
metal_den_level = resource_building_level_extraction('metal_den',html_crawler,0)
crystal_den_level = resource_building_level_extraction('crystal_den',html_crawler,0)
deuterium_den_level = resource_building_level_extraction('deuterium_den',html_crawler,0)

def update_resource_production():
	time.sleep(0.5) #Delays to prevent setting off any bot-detection scripts
	html = browser.open('http://s115-us.ogame.gameforge.com/game/index.php?page=resources')
	html_crawler = BeautifulSoup(html.read())


	metal_level = resource_building_level_extraction('metal_mine',html_crawler,0)
	crystal_level = resource_building_level_extraction('crystal_mine',html_crawler,0)
	deuterium_level = resource_building_level_extraction('deuterium_synth',html_crawler,0)
	energy_level = resource_building_level_extraction('solar_plant',html_crawler,0)
	fusion_reactor_level = resource_building_level_extraction('fusion_reactor',html_crawler,energy_technology) #The fusion reactor is special in that its efficiency depends on the level of Energy Technology
	solar_sattelite_level = resource_building_level_extraction('solar_sattelites',html_crawler,0)
	metal_storage_level = resource_building_level_extraction('metal_storage',html_crawler,0)
	crystal_storage_level = resource_building_level_extraction('crystal_storage',html_crawler,0)
	deuterium_storage_level = resource_building_level_extraction('deuterium_storage',html_crawler,0)
	metal_den_level = resource_building_level_extraction('metal_den',html_crawler,0)
	crystal_den_level = resource_building_level_extraction('crystal_den',html_crawler,0)
	deuterium_den_level = resource_building_level_extraction('deuterium_den',html_crawler,0)

#############################
#Gathering Facilities Levels#
#############################

print 'Gathering Facilities Levels'
time.sleep(0.5 * randint(2,4)) #Delays to prevent setting off any bot-detection scripts
html = browser.open('http://s115-us.ogame.gameforge.com/game/index.php?page=station')
html_crawler = BeautifulSoup(html.read())

robotics_factory_level =  facilities_level_extraction('robotics_factory',html_crawler)
shipyard_level =  facilities_level_extraction('shipyard',html_crawler)
research_lab_level =  facilities_level_extraction('research_lab',html_crawler)
alliance_depot_level =  facilities_level_extraction('alliance_depot',html_crawler)
missile_silo_level =  facilities_level_extraction('missile_silo',html_crawler)
nanite_factory_level =  facilities_level_extraction('nanite_factory',html_crawler)
terraformer_level =  facilities_level_extraction('terraformer',html_crawler)

def update_facilities():
	time.sleep(0.5) #Delays to prevent setting off any bot-detection scripts
	html = browser.open('http://s115-us.ogame.gameforge.com/game/index.php?page=station')
	html_crawler = BeautifulSoup(html.read())

	robotics_factory_level =  facilities_level_extraction('robotics_factory',html_crawler)
	shipyard_level =  facilities_level_extraction('shipyard',html_crawler)
	research_lab_level =  facilities_level_extraction('research_lab',html_crawler)
	alliance_depot_level =  facilities_level_extraction('alliance_depot',html_crawler)
	missile_silo_level =  facilities_level_extraction('missile_silo',html_crawler)
	nanite_factory_level =  facilities_level_extraction('nanite_factory',html_crawler)
	terraformer_level =  facilities_level_extraction('terraformer',html_crawler)

def buildtime(level,metal, crystal):
	return int(60*60*(metal + crystal) / (2500 * max(4 - level / 2, 1)))
	
######################
#Make first Decisions#
######################
print '\n\n'
while True:
	update_resource_levels()
	update_resource_production()
	if(metal_level[0] < energy_level[0] - 1):
		print "Building Metal Mine"
		build_resources('metal_mine', browser)
		time.sleep(buildtime(metal_level[0], metal_level[1], metal_level[2]))
	elif(crystal_level[0] < energy_level[0] - 1):
		print "Building Crystal Mine"
		build_resources('crystal_mine', browser)
		time.sleep(buildtime(crystal_level[0], crystal_level[1], crystal_level[2]))
	elif(energy_results[1] >= deuterium_level[3]):
		print "Building Deuterium Synth"
		build_resources('deuterium_synth', browser)
		time.sleep(buildtime(deuterium_level[0], deuterium_level[1], deuterium_level[2]))
	else:
		print "Building Solar Power Plant"
		build_resources('solar_plant', browser)
		time.sleep(buildtime(energy_level[0], energy_level[1], energy_level[2]))
	
	
