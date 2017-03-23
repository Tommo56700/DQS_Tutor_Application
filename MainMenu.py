from tkinter import *
from NewStudents import *
#from SearchByTutor import *
#from SearchStudents import *
from StudentManagement import *
from Classes import *

bufferCounter = 0

class MainMenu(Frame):
	def __init__(self, master):
		Frame.__init__(self, master, background="white")
		self.initUI()
		
	def initUI(self):
		self.grid()
		
		lblTitle = Label(self, text = "Main Menu", font=("Helvetica", 40,"bold"), background="white")
		lblTitle.grid(row=1, column=0, columnspan=3, padx=(50, 50), pady=(20,20))
		
		butImport = Button(self, text="Import CSV file", font=("Helvetica", 10), command=csv_import("students.csv", "tutors.csv"))
		butImport.grid(row=3, column=1, pady=(2, 0))
		
		butSearch = Button(self, text="Search for Student", font=("Helvetica", 10), command = self.searchWindow)
		butSearch.grid(row=4, column=1, pady=(2, 0))
		
		butDisplay = Button(self, text="Display Students by Tutor", font=("Helvetica", 10), command = self.searchTutorWindow)
		butDisplay.grid(row=5, column=1, pady=(2, 0))
		
		butFind = Button(self, text="Find Tutor Quota", font=("Helvetica", 10), command=self.quotaWindow)
		butFind.grid(row=6, column=1, pady=(2, 0))

		butTransfer = Button(self, text="Transfer Student", font=("Helvetica", 10), command = managementWindow)
		butTransfer.grid(row=8, column=1, pady=(2, 0))
		
		butQuit = Button(self, text="Quit", font=("Helvetica", 10), command=self.quit)
		butQuit.grid(row=10, column=1, pady=(20, 10))

	def quotaWindow(self):
		global Tutors
		labels = []
		buttons = []

		t = Toplevel(self)
		t.wm_title("Quota Info")

		t.grid()
	
		lblTitle = Label(t, text = "Tutor Quota", font=("Helvetica", 40,"bold"), background="white")
		lblTitle.grid(row=1, column=0, columnspan=1, padx=(50, 50), pady=(20,20))
		
		for tutor in Tutors:
			myString = ("Name: " + tutor.getFName() + " " + tutor.getSName() + "   |   Total Students: " + str(len(tutor.getStudents())) + "/" + str(tutor.getStudentNum()) + "   |   Email Address: " + tutor.getEmail())
			labels.append(Label(t, text = myString, font=("Helvetica", 10, "bold"), background="white"))
			labels[-1].grid(row=(3 + Tutors.index(tutor)), column=0, columnspan=1, padx=(50, 50), pady=(20, 20))

	def searchWindow(self):
		t = Toplevel(self)
		t.wm_title("Search Student")
		t.grid()

		lblTitle = Label(t, text = "Search for Students by ID", font=("Helvetica", 20,"bold"), background="white")
		lblTitle.grid(row=0, column=0, columnspan=2, padx=(20, 20), pady=(20,20))

		entID = Entry(t, font=("Helvetica", 10))
		entID.grid(row = 1, column = 0)

		butSearch = Button(t, text="Search", font=("Helvetica", 10), command = lambda: SearchByID(entID.get(), t))
		butSearch.grid(row=1, column=1, pady=(0, 0))

		butQuit = Button(t, text="Quit", font=("Helvetica", 10), command=t.quit)
		butQuit.grid(row=3, column=0, columnspan = 2, pady=(20, 10))

	def searchTutorWindow(self):
		t = Toplevel(self)
		t.wm_title("Search Tutor")
		t.grid()

		lblTitle = Label(t, text = "Search for Students by Tutor", font=("Helvetica", 20,"bold"), background="white")
		lblTitle.grid(row=0, column=0, columnspan=5, padx=(20, 20), pady=(20,20))

		t.listTutor = Listbox(t, height= 3, width = 30)
		scroll = Scrollbar(t, command= t.listTutor.yview)
		t.listTutor.configure(yscrollcommand=scroll.set)
		
		t.listTutor.grid(row=1, column=0, columnspan = 2)
		scroll.grid(row=1, column=2, columnspan = 1, sticky = W)
		
		for Tutor in Tutors:
			t.listTutor.insert(END, Tutor.getFName() + " " + Tutor.getSName())
		t.listTutor.selection_set(END)

		t.listProg = Listbox(t, height= 3, width = 30)
		scroll = Scrollbar(t, command= t.listProg.yview)
		t.listProg.configure(yscrollcommand=scroll.set)
		
		t.listProg.grid(row=1, column=4, columnspan = 2)
		scroll.grid(row=1, column=5, columnspan = 1, sticky = E)
		
		for Student in Students:
			t.listProg.insert(END, Student.getFName() + " " + Student.getSName())
		t.listProg.selection_set(END)

		butSearch = Button(t, text="Search", font=("Helvetica", 10), command = lambda: SearchByID(int(entID.get())))
		butSearch.grid(row=1, column=3, pady=(0, 0))

		butQuit = Button(t, text="Quit", font=("Helvetica", 10), command=t.quit)
		butQuit.grid(row=2, column=3, columnspan = 1, pady=(20, 10))



def SearchByID(student_id, t):
	global Students
	global bufferCounter
	bufferCounter += 1
	for student in Students:
		if student_id == student.getId():
			lblTrue = Label(t, text = student.output(), font=("Helvetica", 8,"bold"), background="white")
			lblTrue.grid(t, row=3 + bufferCounter, column=0, columnspan=2, padx=(20, 20), pady=(20,20))

def main():
	root = Tk()
	root.title("Tutor Management Software")
	app = MainMenu(root)
	root.mainloop()


if __name__ == "__main__":
	main()