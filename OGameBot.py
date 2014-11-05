from OGameImplementation import *
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

###########
#Main Loop#
###########
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