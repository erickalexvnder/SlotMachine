"""
Program: SlotMachine.py
Author: Erick Romero
"""

from breezypythongui import EasyFrame
import random

class Slots(EasyFrame):
	""" Creates a slot-machine type game."""

	def __init__(self):
		"""Sets up the window and the widgets."""
		EasyFrame.__init__(self, title = "Slot Machine", resizable = False, background = "lightgreen")

		self.addLabel(text = "Slot Machine", row = 0, column = 0, columnspan = 3, sticky = "NSEW", background = "lightgreen").config(font = ("Verdana", 24))

		self.field1 = self.addIntegerField(value = 0, row = 1, column = 0)
		self.field2 = self.addIntegerField(value = 0, row = 1, column = 1)
		self.field3 = self.addIntegerField(value = 0, row = 1, column = 2)

		self.button = self.addButton(text = "SPIN", row = 2, column = 0, columnspan = 3, command = self.spin)

		self.resultArea = self.addLabel(text = "", row = 3, column = 0, columnspan = 3, sticky = "NSEW")

		self.addLabel(text = "Points Remaning:", row = 4, column = 0, sticky = "NSEW")

		self.pointsField = self.addIntegerField(value = 100, row = 4, column = 1)

	def spin(self):
		# variables and constants
		num1 = random.randint(1, 9)
		num2 = random.randint(1, 9)
		num3 = random.randint(1, 9)
		result = ""
		points = self.pointsField.getNumber()

		# calculation phase
		
		# Check the game conditions and modify the result
		if num1 == num2 == num3:
			result = "JACKPOT!!"
			points += 30
		elif num1 == num2 or num2 == num3 or num1 == num3:
			result = "Two Of A Kind!"
			points += 10
		else:
			result = "No combination"
			points -= 10

		# Check if the player has any points left to play again
		if points == 0:
			result = "GAME OVER"
			self.button["state"] = "disabled" 

		# output phase
		self.field1.setNumber(num1)
		self.field2.setNumber(num2)
		self.field3.setNumber(num3)
		self.resultArea["text"] = result
		self.pointsField.setNumber(points)
	
# definition of the main() function for program entry
def main():
	"""Instantiates and pops up the window."""
	Slots().mainloop()

main()