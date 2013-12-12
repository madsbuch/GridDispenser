try:
	import wx
except:
	print ("wx is not available")

from dispenserrun.dispenserApp import dispenserApp

app = dispenserApp()
app.MainLoop()

