#2.Searching the personal tutor list for individual students 
from tkinter import *


testTutor = Tutor(12, "CM101", "Hailey", "Smiths", "hsmiths@uni.co.uk", True, 10)
testStudent = Student(1, "CM101", "Fred", "Jones", testTutor, "2014/15", "fjones@uni.co.uk")
testStudent2 = Student(2, "CM101", "Fred", "Jones", testTutor, "2014/15", "fjones@uni.co.uk")
Students = [testStudent, testStudent2]
testTutor.addStudent(testStudent)
testTutor.addStudent(testStudent2)

bufferCounter = 0

def SearchByID(student_id):
	global Students
	global bufferCounter
	bufferCounter += 1
	for student in Students:
		if student_id == student.getId():
			lblTrue = Label(text = student.output(), font=("Helvetica", 8,"bold"), background="white")
			lblTrue.grid(row=3 + bufferCounter, column=0, columnspan=2, padx=(20, 20), pady=(20,20))

class SearchStudents(Frame):
	def __init__(self, master):
		Frame.__init__(self, master, background="white")
		self.initUI()
		
	def initUI(self):
		self.grid()

		lblTitle = Label(self, text = "Search for Students by ID", font=("Helvetica", 20,"bold"), background="white")
		lblTitle.grid(row=0, column=0, columnspan=2, padx=(20, 20), pady=(20,20))

		entID = Entry(self, font=("Helvetica", 10))
		entID.grid(row = 1, column = 0)

		butSearch = Button(self, text="Search", font=("Helvetica", 10), command = lambda: SearchByID(int(entID.get())))
		butSearch.grid(row=1, column=1, pady=(0, 0))

		butQuit = Button(self, text="Quit", font=("Helvetica", 10), command=self.quit)
		butQuit.grid(row=3, column=0, columnspan = 2, pady=(20, 10))

def searchWindow():
	root = Tk()
	root.title("Tutor Management Software")
	app = SearchStudents(root)
	root.mainloop()