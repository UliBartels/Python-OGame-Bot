from OGameAPIStorage import _Storage

#############################
#Resource Storing Facilities#
#############################
class Metal_storage(_Storage):
	def __init__(self, browser):
		print "Initializing Metal Storage"
		_Storage.__init__(self, browser, 2, [1000,0,0], 'button7', 'http://s115-us.ogame.gameforge.com/game/index.php?page=resources')

		
class Crystal_storage(_Storage):
	def __init__(self, browser):
		print "Initializing Crystal Storage"
		_Storage.__init__(self, browser, 2, [500,250,0], 'button8', 'http://s115-us.ogame.gameforge.com/game/index.php?page=resources')

		
class Deuterium_storage(_Storage):
	def __init__(self, browser):
		print "Initializing Deuterium Storage"
		_Storage.__init__(self, browser, 2, [1000,1000,0], 'button9', 'http://s115-us.ogame.gameforge.com/game/index.php?page=resources')