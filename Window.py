from tkinter import *
from tkinter import messagebox
from Classes import *
from WindowProcedures import *

class Window(Frame): #Creates the Main Menu, each function from then on creates another window for the user to interact with.
	def __init__(self, master):
		Frame.__init__(self, master)
		self.menuWindow()
		
	def menuWindow(self):
		self.grid()
		buttonList = []
		
		lblTitle = Label(self, text = "Main Menu", font=("Helvetica", 40,"bold"))
		lblTitle.grid(row=1, column=0, columnspan=2, padx=(50, 50), pady=(20,20))

		butImport = Button(self, text="Import CSV file", font=("Helvetica", 10), command= lambda: importFunc(entCSV.get(), buttonList))
		butImport.grid(row=3, column=1, pady=(2, 0))

		entCSV = Entry(self, font=("Helvetica", 10))
		entCSV.grid(row = 3, column = 0)
		
		butSearch = Button(self, text="Search for Student", font=("Helvetica", 10), state=DISABLED, command = self.searchWindow)
		butSearch.grid(row=4, column=0, columnspan = 2, pady=(2, 0))
		
		butDisplay = Button(self, text="Display Students by Tutor", font=("Helvetica", 10), state=DISABLED, command = self.searchTutorWindow)
		butDisplay.grid(row=5, column=0, columnspan = 2, pady=(2, 0))
		
		butFind = Button(self, text="Find Tutor Quota", font=("Helvetica", 10), state=DISABLED, command=self.quotaWindow)
		butFind.grid(row=6, column=0, columnspan = 2, pady=(2, 0))

		butTransfer = Button(self, text="Transfer Student", font=("Helvetica", 10), state=DISABLED, command = self.managementWindow)
		butTransfer.grid(row=8, column=0, columnspan = 2, pady=(2, 0))
		
		butQuit = Button(self, text="Quit", font=("Helvetica", 10), command=self.quit)
		butQuit.grid(row=10, column=0, columnspan = 2, pady=(20, 10))

		buttonList = [butSearch, butDisplay, butFind, butTransfer]

	def quotaWindow(self):
		global Tutors
		labels = []
		buttons = []

		t = Toplevel(self)
		t.wm_title("Quota Info")

		t.grid()
	
		lblTitle = Label(t, text = "Tutor Quota", font=("Helvetica", 40,"bold"))
		lblTitle.grid(row=1, column=0, columnspan=1, padx=(50, 50), pady=(20,20))
		
		for tutor in Tutors:
			myString = ("Name: " + tutor.getFName() + " " + tutor.getSName() + "   |   Total Students: " + str(len(tutor.getStudents())) + "/" + str(tutor.getStudentNum()) + "   |   Email Address: " + tutor.getEmail())
			labels.append(Label(t, text = myString, font=("Helvetica", 10, "bold")))
			labels[-1].grid(row=(3 + Tutors.index(tutor)), column=0, columnspan=1, padx=(50, 50), pady=(20, 20))

	def searchWindow(self):
		t = Toplevel(self)
		t.wm_title("Search Student")
		t.grid()

		lblTitle = Label(t, text = "Search for Students by ID", font=("Helvetica", 20,"bold"))
		lblTitle.grid(row=0, column=0, columnspan=2, padx=(20, 20), pady=(20,20))

		entID = Entry(t, font=("Helvetica", 10))
		entID.grid(row = 1, column = 0)

		lblTrue = Label(t, text = "", font=("Helvetica", 8,"bold"))
		lblTrue.grid(row=4, column=0, columnspan=2, padx=(20, 20), pady=(20,20))

		butSearch = Button(t, text="Search", font=("Helvetica", 10), command = lambda: searchByStudentID(entID.get(), lblTrue))
		butSearch.grid(row=1, column=1, pady=(0, 0))
		

	def searchTutorWindow(self):
		t = Toplevel(self)
		t.wm_title("Search Tutor")
		t.grid()

		lblTitle = Label(t, text = "Search for Students by Tutor ID", font=("Helvetica", 20,"bold"))
		lblTitle.grid(row=0, column=0, columnspan=5, padx=(20, 20), pady=(20,20))

		entID = Entry(t, font=("Helvetica", 10))
		entID.grid(row = 1, column = 0)

		t.listStudent = Listbox(t, height= 3, width = 30)
		scroll = Scrollbar(t, command= t.listStudent.yview)
		t.listStudent.configure(yscrollcommand=scroll.set)
		
		t.listStudent.grid(row=1, column=4, columnspan = 2)
		scroll.grid(row=1, column=5, columnspan = 1, sticky = E)

		butSearch = Button(t, text="Search", font=("Helvetica", 10), command = lambda: SearchByTutorID(entID.get(), t.listStudent))
		butSearch.grid(row=1, column=3, pady=(0, 0))

	def managementWindow(self):
		t = Toplevel(self)
		t.wm_title("Student Management")
		t.grid()

		lblTitle = Label(t, text = "Student Management", font=("Helvetica", 30,"bold"))
		lblTitle.grid(row=1, column=0, columnspan=3, padx=(50, 50), pady=(20,20))
		
		lblProg = Label(t, text='Students:', font=('Helvetica', 12))
		lblProg.grid(row=3, column=0, sticky = E, columnspan = 1)
		
		entID = Entry(t, font=("Helvetica", 10))
		entID.grid(row = 3, column = 1)
		
		butReassign = Button(t, text="Reassign Student", font=("Helvetica", 10), command =lambda: self.reasignWindow(entID.get()))
		butReassign.grid(row=5, column=1, pady=(2, 0))
		
		butDelete = Button(t, text="Delete Student", font=("Helvetica", 10), command = lambda: studentDelete(entID.get()))
		butDelete.grid(row=4, column=1, pady=(2, 0))

	def reasignWindow(self, studentID):
		u = Toplevel(self)
		u.wm_title("Student Management")
		u.grid()

		u.listProg = Listbox(u, height= 3, width = 30)
		scroll = Scrollbar(u, command= u.listProg.yview)
		u.listProg.configure(yscrollcommand=scroll.set)
		
		u.listProg.grid(row=0, column=1, columnspan = 2, rowspan = 2)
		scroll.grid(row=0, column=2, columnspan = 2, sticky = E)
		
		student = getStudentFromID(studentID)

		for Tutor in Tutors:
			u.listProg.insert(END, Tutor.getFName() + " " + Tutor.getSName() + ": " + Tutor.getId())
		u.listProg.selection_set(END)

		entID = Entry(u, font=("Helvetica", 10))
		entID.grid(row = 2, column = 1)

		lblProg = Label(u, text='Available Tutors: ', font=('Helvetica', 10,'bold'))
		lblProg.grid(row=0, column=0, columnspan = 1)
		lblHelp = Label(u, text='Input Staff ID for transfer: ', font=('Helvetica', 10,'bold'))
		lblHelp.grid(row=2, column=0, columnspan = 1)

		butReassign = Button(u, text="Reassign Student", font=("Helvetica", 10), command = lambda: matchTutor(student, getTutorFromID(entID.get())))
		butReassign.grid(row=2, column=2, pady=(0, 0))



def main(): #defining the start of the code and calling Window()
	root = Tk()
	root.title("Tutor Management Software")
	root.resizable(False, False)
	app = Window(root)
	root.mainloop()


if __name__ == "__main__":
	main()