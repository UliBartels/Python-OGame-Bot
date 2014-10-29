import math
import re
	
def resource_building_level_extraction(name, html_crawler, energy_technology):
		
		enumerator = ['metal_mine','crystal_mine','deuterium_synth','solar_plant','fusion_reactor','solar_sattelites','metal_storage','crystal_storage','deuterium_storage','metal_den','crystal_den','deuterium_den']
		#To get the level of all my buildings I look at the buttons in the Resource tab. Those buttons are numbered, which is why I'm using the 
		#array's index so I can call the function with something more useful than 'button1'
		building_number = enumerator.index(name) + 1
		html_level_string = str(html_crawler.find(id= 'button'+str(building_number)).find('span',{'class':'level'})).split()
		
		#Can't figure out how to fetch the temperature of the planet quite yet.
		#min_temp = int(re.compile("([^-_a-zA-Z0-9!@#%&=,/'\";:~`\$\^\*\(\)\+\[\]\.\{\}\|\?\<\>\\]+|[^\s]+)").search('\d+(?=C)', html_crawler).group(0)) #Deuterium Production depends on the Planet's temperature
		#max_temp = int(re.compile("([^-_a-zA-Z0-9!@#%&=,/'\";:~`\$\^\*\(\)\+\[\]\.\{\}\|\?\<\>\\]+|[^\s]+)").search('\d+(?=C)', html_crawler).group(1)) #So I'm using regular expressions to fetch all integers between
		min_temp = 64
		max_temp = 106
		
		try:
			for string in html_level_string:
				try:
					building_level = int(string)		

					if(building_number == 1): #Metal Mine
						metal_cost = 60 * pow(1.5,building_level)
						crystal_cost = 15 * pow(1.5,building_level)
						power_cost = 10  * ((building_level + 1) * pow(1.1,building_level + 1) - (building_level * pow(1.1,building_level)))
						production = 30 * (building_level + 1) * pow(1.1,building_level + 1)
						return [building_level, metal_cost, crystal_cost, power_cost, production]
					
					if(building_number == 2): #Crystal Mine
						metal_cost = 48 * pow(1.5,building_level)
						crystal_cost = 24 * pow(1.5,building_level)
						power_cost = 10 * ((building_level + 1) * pow(1.1,building_level + 1) - (building_level * pow(1.1,building_level)))
						production = 20 * (building_level + 1) * pow(1.1,building_level + 1)
						return [building_level, metal_cost, crystal_cost, power_cost, production]
					
					if(building_number == 3): #Deuterium Synthesizer
						metal_cost = 225 * pow(1.5,building_level)
						crystal_cost = 75 * pow(1.5,building_level)
						power_cost = 20 * ((building_level + 1) * pow(1.1,building_level + 1) - (building_level * pow(1.1,building_level)))
						production = 10 * ((building_level + 1) * pow(1.1,building_level + 1) * (1.36 - 0.004 * (max_temp + min_temp)/2)) 
						return [building_level, metal_cost, crystal_cost, power_cost, production]
					
					if(building_number == 4): #Solar Plant
						metal_cost = 75 * pow(1.5, building_level)
						crystal_cost = 30 * pow(1.5, building_level)
						production = 20 * (building_level + 1) * pow(1.1, building_level + 1)
						production_increase = production - 20 * building_level * pow(1.1, building_level)
						return [building_level, metal_cost, crystal_cost, production, production_increase]
					
					if(building_number == 5): #Fusion Reactor
						metal_cost = 900 * pow(1.8, building_level)
						crystal_cost = 360 * pow(1.8, building_level)
						deuterium_cost = 180 * pow(1.8, building_level)
						production = 30 * building_level * pow(1.5 + (0.01 * energy_technology),building_level)
						production_increase = production - 30 * building_level * pow(1.5 + (0.01 * (energy_technology - 1)),building_level)
						deuterium_consumption = math.ceil(+10 * building_level * pow(1.1, building_level))
						return [building_level, metal_cost, crystal_cost, deuterium_cost, deuterium_consumption, production, production_increase]
					
					if(building_number == 6): #Solar Satellites
						metal_cost = 0
						crystal_cost = 2000
						deuterium_cost = 500
						production = building_level * math.floor(max_temp/2 + 20)
						production_increase = math.floor(max_temp/2 + 20)
						return [building_level, metal_cost, crystal_cost, deuterium_cost, production, production_increase]
					
					if(building_number == 7): #Metal Storage
						metal_cost = 500 * pow(2,building_level + 1)
						crystal_cost = 0
						current_storage_capacity = 5000 * math.floor(2.5 * pow(math.exp(1),20 * building_level/33))
						next_storage_capacity = 5000 * math.floor(2.5 * pow(math.exp(1),20 * (building_level + 1)/33))
						return [building_level, metal_cost, crystal_cost, current_storage_capacity, next_storage_capacity]
					
					if(building_number == 8): #Crystal Storage
						metal_cost = 500 * pow(2,building_level +1)
						crystal_cost = 250 * pow(2, building_level + 1)
						current_storage_capacity = 5000 * math.floor(2.5 * pow(math.exp(1),20 * building_level/33))
						next_storage_capacity = 5000 * math.floor(2.5 * pow(math.exp(1),20 * (building_level + 1)/33))
						return [building_level, metal_cost, crystal_cost, current_storage_capacity, next_storage_capacity]
					
					if(building_number == 9): #Deuterium Tank
						metal_cost = 1000 * pow(2,building_level +1)
						crystal_cost = 1000 * pow(2, building_level + 1)
						current_storage_capacity = 5000 * math.floor(2.5 * pow(math.exp(1),20 * building_level/33))
						next_storage_capacity = 5000 * math.floor(2.5 * pow(math.exp(1),20 * (building_level + 1)/33))
						return [building_level, metal_cost, crystal_cost, current_storage_capacity, next_storage_capacity]
					
					if(building_number == 10):
						return building_level
					
					if(building_number == 11):
						return building_level
					
					if(building_number == 12):
						return building_level

				except ValueError:
					pass

		except Exception as e:
			print e
			return -1

def facilities_level_extraction(name,html_crawler):
	
	enumerator = ['robotics_factory','shipyard','research_lab','alliance_depot','missile_silo','nanite_factory','terraformer']
	building_number = enumerator.index(name)
	html_level_string = str(html_crawler.find(id= 'button'+str(building_number) ).find('span',{'class':'level'})).split()
	
	#The resulting list contains only one number, the current building level but the position changes every now and then.
	#Thus I cycle through the entire list, looking for the lone integer.
	for string in html_level_string:
		try:
			building_level = int(string)
			
			if(building_number == 0): #Robotics Factory
				metal_cost = 400 * pow(2, building_level)
				crystal_cost = 120 * pow(2, building_level)
				deuterium_cost = 200 * pow(2, building_level)
				return [building_level, metal_cost, crystal_cost, deuterium_cost]
		
			if(building_number == 2): #Shipyard
				metal_cost = 400 * pow(2, building_level)
				crystal_cost = 200 * pow(2, building_level)
				deuterium_cost = 100 * pow(2, building_level)
				return [building_level, metal_cost, crystal_cost, deuterium_cost]
		
			if(building_number == 3): #Research Lab
				metal_cost = 200 * pow(2, building_level)
				crystal_cost = 400 * pow(2, building_level)
				deuterium_cost = 200 * pow(2, building_level)
				return [building_level, metal_cost, crystal_cost, deuterium_cost]
		
			if(building_number == 4): #Alliance Depot
				metal_cost = 20000 * pow(2, building_level)
				crystal_cost = 40000 * pow(2, building_level)
				return [building_level, metal_cost, crystal_cost]
		
			if(building_number == 5): #Missile Silo
				metal_cost = 20000 * pow(2, building_level)
				crystal_cost = 20000 * pow(2, building_level)
				deuterium_cost = 1000 * pow(2, building_level)
				return [building_level, metal_cost, crystal_cost, deuterium_cost]
		
			if(building_number == 6): #Nanite Factory
				metal_cost = 20000 * pow(2, building_level)
				crystal_cost = 20000 * pow(2, building_level)
				deuterium_cost = 1000 * pow(2, building_level)
				return [building_level, metal_cost, crystal_cost, deuterium_cost]

			if(building_number == 7): #Terraformer
				metal_cost = 1000000 * pow(2, building_level)
				crystal_cost = 500000 * pow(2, building_level)
				deuterium_cost = 100000 * pow(2, building_level)
				return [building_level, metal_cost, crystal_cost, deuterium_cost]
			
		except ValueError:
			pass
	
	return -1
		
def research_level_extraction(name,html_crawler):

	dictionary = {'energy_technology':'research113',
				'laser_technology':'research120',
				'ion_technology':'research121',
				'hyperspace_technology':'research114',
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

	html_level_string = str(html_crawler.find('div',{'class':dictionary[name]}).find('span',{'class':'level'})).split()
	for string in html_level_string:
		try:
			num = int(string)
			return num
		except IndexError:
			html_level_string = html_level_string[1].replace('class=\"level\">','')
			num = int(html_level_string)
			return num
		except ValueError:
			pass
			
	return -1