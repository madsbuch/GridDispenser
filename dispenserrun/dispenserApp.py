import wx
import dispenserFrame as f
import dispenserAPI as dAPI

class dispenserApp(wx.App):
	def __init__(self, *args, **kwargs):
		""" initialise the super interface """
		super(dispenserApp, self).__init__(*args, **kwargs)
		self.SetAppName("DispenserRun")
		self.mainwindow = f.dispenserFrame("DispenserRun", 8, 12, self)
		self.mainwindow.Show()
		self.api = dAPI.dispenserAPI(8, 12);

	def clickGrid(self, x, y, amounts):
		""" A button in the grid was clicked, we squirt """
		self.api.singleSquirt(x, y, amounts)

	def clickRow(self, x, amount):
		""" A button from the row was clicked, we use the parallel squirter """
		self.api.parallellSqirt(x, amount)

	def clickHome(self):
		""" The home button was clicked """
		self.api.home()
