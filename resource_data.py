def resource_level_gathering(resource_id, html_crawler):
	resource_results_html = html_crawler.find(id= resource_id)
	
	#The issue with gathering the resource data is that the information is placed within a <li #Here be stuff#></li> tag.
	#So we treat the search result as a string, strip out anything we don't want, then search the remainders.
	resource_results_string = str(resource_results_html).replace('tr&gt;','').replace('th&gt;','').replace('td&gt;','').replace('&lt;','').replace('&gt','').replace('/','').replace(';','').replace('span','').replace('undermark','').replace('overermark','').replace('class=','').replace('\""','').replace('+','').replace('.','')
	
	if 'overmark' in resource_results_string: #If Deuterium is 0 the game adds an "overmark" to the HTML
		resource_results_string = resource_results_string.replace('\"overmark\"','')
	if 'middlemark' in resource_results_string: #If Deuterium is 0 the game adds an "overmark" to the HTML
		resource_results_string = resource_results_string.replace('\"middlemark\"','')
	
	resource_results_string_split = resource_results_string.split()
	
	resource_available = int(resource_results_string_split[8])
	resource_storage = int(resource_results_string_split[11])
	resource_production = int(resource_results_string_split[14])
	resource_den = int(resource_results_string_split[17])
	
	return [resource_available, resource_storage, resource_production, resource_den] #[Amount in Storage, Storage Capacity, Current Production, Den Capacity]
	
def energy_level_gathering(html_crawler):
	energy_results_html = html_crawler.find(id='energy_box')
	energy_results_string = str(energy_results_html).replace('tr&gt;','').replace('th&gt;','').replace('td&gt;','').replace('&lt;','').replace('&gt','').replace('/','').replace(';','').replace('span','').replace('undermark','').replace('overermark','').replace('class=','').replace('\""','').replace('+','').replace('.','')

	if 'overmark' in energy_results_string: #Energy can be negative, which adds another string to the HTML
		energy_results_string = energy_results_string.replace('\"overmark\"','')

	energy_results_string_split = energy_results_string.split()	
	energy_available = int(energy_results_string_split[8])
	energy_production = int(energy_results_string_split[11])
	
	return [energy_available, energy_production]

def darkmatter_level_gathering(html_crawler):
	darkmatter_results_html = html_crawler.find(id='darkmatter_box')
	darkmatter_results_string = str(darkmatter_results_html).replace('tr&gt;','').replace('th&gt;','').replace('td&gt;','').replace('&lt;','').replace('&gt','').replace('/','').replace(';','').replace('span','').replace('undermark','').replace('overermark','').replace('class=','').replace('\""','').replace('+','').replace('.','')
	darkmatter_results_string_split = darkmatter_results_string.split()

	darkmatter_available = int(darkmatter_results_string_split[13])
	darkmatter_purchased = int(darkmatter_results_string_split[15])
	darkmatter_found = int(darkmatter_results_string_split[17])
	
	return [darkmatter_available, darkmatter_purchased, darkmatter_found]