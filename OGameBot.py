from FacilityImplementation import *
from ResourceImplementation import *
from StorageImplementation import *
from ResearchImplementation import *
import mechanize
import time

####################
#Logging into OGame#
####################
browser = mechanize.Browser()
html = None #All classes share a global HTML variable. This way I can avoid making multiple calls to the website if we already have the correct HTML loaded.

##############################
#Setting up all the buildings#
##############################

metal_mine = Metal_mine(browser)
crystal_mine = Crystal_mine(browser)
deuterium_synthesizer = Deuterium_synthesizer(browser)

solar_plant = Solar_plant(browser)
fusion_reactor = Fusion_reactor(browser)
solar_sattelites = Solar_sattelites(browser)

metal_storage = Metal_storage(browser)
crystal_storage = Crystal_storage(browser)
deuterium_storage = Deuterium_storage(browser)

robotics_factory = Robotics_factory(browser)
shipyard = Shipyard(browser)
research_lab = Research_lab(browser)
alliance_depot = Alliance_depot(browser)
missile_silo = Missile_silo(browser)
nanite_factory = Nanite_factory(browser)
terraformer = Terraformer(browser)

energy_technology = Energy_technology(browser)
laser_technology = Laser_technology(browser)
ion_technology = Ion_technology(browser)
hyperspace_technology = Hyperspace_technology(browser)
plasma_technology = Plasma_technology(browser)
combustion_drive = Combustion_drive(browser)
impulse_drive = Impulse_drive(browser)
hyperspace_drive = Hyperspace_drive(browser)
espionage_technology = Espionage_technology(browser)
computer_technology = Computer_technology(browser)
astrophysics = Astrophysics(browser)
intergalactic_research_network = Intergalactic_research_network(browser)
graviton_technology = Graviton_technology(browser)
weapons_technology = Weapons_technology(browser)
shielding_technology = Shielding_technology(browser)
armor_technology = Armor_technology(browser)

###########
#Main Loop#
###########
'''
while True:
	sleep_time = 0
	sleep_cmpr = 0
	
	if metal_mine.buildable(browser) and not metal_mine.level > crystal_mine.level + 1:
		print "Building Metal Mine"
		sleep_time = metal_mine.build(browser)
		if sleep_time == 0:
			print "Couldn't build Metal Mine"
			sleep_time = 120
	elif crystal_mine.buildable(browser) and not crystal_mine.level > metal_mine.level + 1:
		print "Building Crystal Mine"
		sleep_cmpr = crystal_mine.build(browser)
		if sleep_cmpr == 0:
			print "Couldn't build Crystal Mine"
			sleep_cmpr = 120
		if sleep_cmpr > sleep_time:
			sleep_time = sleep_cmpr
	elif deuterium_synthesizer.buildable(browser):
		print "Building Deuterium Synthesizer"
		sleep_cmpr = deuterium_synthesizer.build(browser)
		if sleep_cmpr == 0:
			print "Couldn't build Deuterium Synthesizer"
			sleep_cmpr = 120
		if sleep_cmpr > sleep_time:
			sleep_time = sleep_cmpr
	elif solar_plant.buildable(browser):
		print "Building Solar Plant"
		sleep_cmpr = solar_plant.build(browser)
		if sleep_cmpr == 0:
			print "Couldn't build Solar Power Plant"
			sleep_cmpr = 120
		if sleep_cmpr > sleep_time:
			sleep_time = sleep_cmpr

	time.sleep(sleep_time + 5)
'''