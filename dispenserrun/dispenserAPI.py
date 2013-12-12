#!/usr/bin/evn python
#
# Interface for the dispenser. This contains everything needed for this to work

from printrun.printcore import printcore
from printrun.printrun.pronsole import pronsole

class dispenserAPI:
	"""Methods needed for constructing gCode to do following things"""
	
	baud = 115200

	def __init__(self, numX, numY):
		""" initiates a instance of size given """
		ps = pronsole()
		port = ps.scanserial()

		if len(port) > 1:
			print ("Too many devices detected")
			return
		if len(port) < 1:
			print ("no device detected")
			return

		self.printer = printcore(port[0], self.baud)
		self.nX = numX
		self.nY = numY

	def parallellSqirt(self, xPos, amount):
		"""  the parrallel dispenser on row "xPos" """
		print ("dispensing in parrallel " + str(amount) 
			+ " to " + str(xPos))
		return [""]

	def singleSquirt(self, xPos, yPos, dispenserAmount):
		""" dispenses certain amount into xPos, yPos. dispenserAmount is a list of tupples
		where the first is the dispenser and the second element the amount """
		
		operations = [""]

		for disps in dispenserAmount :
			dispenser = disps[0]
			amount = disps[1]
			operations
			print ("dispensing " + str(amount) + " from " + str(dispenser) 
				+ " to " + "(" + str(xPos) + "," + str(yPos) + ")")
			
		return [""]

	def watch(self, xPos, yPos):
		""" Moves the camera to look at (xPos, yPos) """
		print ("watching " + "(" + str(xPos) + "," + str(yPos) + ")")
		return [""]

	def home(self):
		""" Homes the moving unit, makes it possible for the big camera to 
		see eveything """
		print("homing")
		return self.exe(["G28 X0 Y0"])

	def setLight(self, xPos, yPos, level):
		""" Sets the level for given for position level in int procent"""
		print ("light " + "(" + str(xPos) + "," + str(yPos) + ") at level " + str(level))
		pass

	def getQueue():
		""" return the current queue of gCodes """
		return ["TODO"]


	def exe(self, commands):
		""" Sends a list of arguments to the printer """
		for cmd in commands:
			self.printer.send(cmd)
