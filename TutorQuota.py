from tkinter import *
from NewStudents import *

class TutorQuota(Frame):
	def __init__(self, master):
		Frame.__init__(self, master, background="white")
		self.initUI()
	

	def initUI(self):
		global Tutors
		labels = []
		buttons = []
		self.grid()
		
		lblTitle = Label(self, text = "Tutor Quota", font=("Helvetica", 40,"bold"), background="white")
		lblTitle.grid(row=1, column=0, columnspan=1, padx=(50, 50), pady=(20,20))
		
		for t in Tutors:
			myString = ("Name: " + t.getFName() + " " + t.getSName() + "   |   Total Students: " + str(len(t.getStudents())) + "/" + str(t.getStudentNum()) + "   |   Email Address: " + t.getEmail())
			labels.append(Label(self, text = myString, font=("Helvetica", 10, "bold"), background="white"))
			labels[-1].grid(row=(3 + Tutors.index(t)), column=0, columnspan=1, padx=(50, 50), pady=(20, 20))


def quotaWindow():
	root = Tk()
	root.title("Tutor Management Software")
	app = TutorQuota(root)
	root.mainloop()