"""
Program: salaryGUI.py
Chapter 8 (page 251)
8/13/24

**NOTE: the module breezypyhtongui.py MUST be in the same directory as this file for the app to run correctly!

Application that calculates weekly pay in a GUI with input from user
"""

from breezypythongui import EasyFrame
from tkinter.font import Font
#Other imports can go here

# Class header (class name will change project to project)
class SalaryCalculator(EasyFrame):

	# Definition of our classes' constructor method
	def __init__(self):
		# Call to the Easy Frame constructor class
		EasyFrame.__init__(self, title = "Salary Calculator 2.0", background = "lightgreen")

		# Variable to store a font design to use with multiple labels
		labelFont = Font(size = 14, family = "Georgia")

		# Add the widgets to the window
		self.addLabel(text = "Salary Calculator", row = 0, column = 0, columnspan = 2, sticky = "NSWE", background = "lightgreen", font = Font(size = 22, family = "Impact"))

		self.addLabel(text = "Hourly Wage:", row = 1, column = 0, background = "lightgreen" , font = labelFont)
		self.wageField = self.addFloatField(value = 0.0, row = 1, column = 1)

		self.addLabel(text = "Hours Worked:", row = 2, column = 0, background = "lightgreen", font = labelFont)
		self.hoursField = self.addFloatField(value = 0.0, row = 2, column = 1)
		# Bind the hoursField to the press of the Enter key event
		self.hoursField.bind("<Return>", lambda event: self.compute())

		self.button = self.addButton(text = "Compute", row = 3, column = 0, columnspan = 2, command = self.compute)
		self.button["background"] = "firebrick"
		self.button["foreground"] = "white"
		self.button["width"] = 15

		self.addLabel(text = "Calculated salary is:", row = 4, column = 0, background = "lightgreen", font = labelFont)
		self.outputField = self.addFloatField(value = 0.0, row = 4, column = 1, state = "readonly", precision = 2)

	def compute(self):
		wage = self.wageField.getNumber()
		hours = self.hoursField.getNumber()
		salary = wage * hours
		self.outputField.setNumber(salary)


		#Global definition of the main() method
def main():
	# Instantiate an object from the class into mainloop()
	SalaryCalculator().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':
	main()