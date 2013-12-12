import wx
import wx.lib.splitter as splitter

class dispenserFrame(wx.Frame):
	def __init__(self, title, numX, numY, app):
		""" Initialise graphical output """
		self.app = app
		self.numX = numX
		self.numY = numY
		wx.Frame.__init__(self, None, title=title, size=(1024, 768))
		"""self.Bind(wx.EVT, self.onClose)"""
		MainPanel(self, numX, numY)
		#bind all click events to the same eventhandler
		self.Bind(wx.EVT_BUTTON, self.onButtonClick)

	def onButtonClick(self, event):
		""" The handler for all clicks """
		id = event.Id
		if (id == -1000):
			self.app.clickHome()
			return

		if(id < 0):
			id = -(id+2)
			self.app.clickRow(id, self.readVal(1))
		else:
			x = id % self.numX
			y = id / self.numX
			self.app.clickGrid(x, y, [(2, self.readVal(2)), (3, self.readVal(3))])

	def readVal(self, valId):
		""" read input values """
		if(valId == 1):
			return float(self.e1.GetValue())
		if(valId == 2):
			return float(self.e2.GetValue())
		if(valId == 3):
			return float(self.e3.GetValue())
		return -0.42

class MainPanel(wx.Panel):
	def __init__ (self, parent, nx, ny):
		""" The main Panel """
		self.parent = parent
		wx.Panel.__init__(self, parent)
		multisplitter = splitter.MultiSplitterWindow(self, 0, (0,0), (1024, 768));
		multisplitter.AppendWindow(rowPanel(self, ny))
		multisplitter.AppendWindow(gridPanel(self, nx, ny))

class rowPanel(wx.Panel):
	""" Panel showing rows for parallel squiting """
	def __init__(self, parent, numY):
		wx.Panel.__init__(self, parent)
		for y in range(numY):
			wx.Button(self, -(y+2), "row " + str(y), (0, 10+y*40))

		wx.Button(self, -1000, "Home", (0, 10+numY*40))

class gridPanel(wx.Panel):
	""" The grid representing all wells """
	def __init__(self, parent, numX, numY):
		wx.Panel.__init__(self, parent)
		for x in range(numX):
			for y in range(numY):
				wx.Button(self, x+(y*numX), "(" + str(x) + "," + str(y) + ")" , (10+x*90,10+y*40))
		wx.StaticText(self, label="extrusion1 (parallel) uL:", pos=(10, (numY * 40 + 30)))
		wx.StaticText(self, label="extrusion2 uL:", pos=(210, (numY * 40 + 30)))
		wx.StaticText(self, label="extrusion3 uL:", pos=(410, (numY * 40 + 30)))
		parent.parent.e1 = wx.TextCtrl(self, size=(140, -1), pos=(10, (numY * 40 + 50)), id=-1010)
		parent.parent.e2 = wx.TextCtrl(self, size=(140, -1), pos=(210, (numY * 40 + 50)), id=-1010)
		parent.parent.e3 = wx.TextCtrl(self, size=(140, -1), pos=(410, (numY * 40 + 50)), id=-1010)
