from tkinter import *
from NewStudents import *
#from SearchByTutor import *
#from SearchStudents import *
#from StudentManagement import *
from Classes import *

class Window(Frame):
	def __init__(self, master):
		Frame.__init__(self, master, background="white")
		self.menuWindow()
		
	def menuWindow(self):
		self.grid()
		buttonList = []
		
		lblTitle = Label(self, text = "Main Menu", font=("Helvetica", 40,"bold"), background="white")
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

		lblTrue = Label(t, text = "", font=("Helvetica", 8,"bold"))
		lblTrue.grid(row=4, column=0, columnspan=2, padx=(20, 20), pady=(20,20))

		butSearch = Button(t, text="Search", font=("Helvetica", 10), command = lambda: searchByStudentID(entID.get(), lblTrue))
		butSearch.grid(row=1, column=1, pady=(0, 0))

		butQuit = Button(t, text="Quit", font=("Helvetica", 10), command=t.quit)
		butQuit.grid(row=3, column=0, columnspan = 2, pady=(20, 10))
		

	def searchTutorWindow(self):
		t = Toplevel(self)
		t.wm_title("Search Tutor")
		t.grid()

		lblTitle = Label(t, text = "Search for Students by Tutor", font=("Helvetica", 20,"bold"), background="white")
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

		butQuit = Button(t, text="Quit", font=("Helvetica", 10), command=t.quit)
		butQuit.grid(row=2, column=3, columnspan = 1, pady=(20, 10))

	def managementWindow(self):
		t = Toplevel(self)
		t.wm_title("Student Management")
		t.grid()

		lblTitle = Label(t, text = "Student Management", font=("Helvetica", 30,"bold"), background="white")
		lblTitle.grid(row=1, column=0, columnspan=3, padx=(50, 50), pady=(20,20))
		
		lblProg = Label(t, text='Students:', background="white", font=('Helvetica', 12))
		lblProg.grid(row=3, column=0, sticky = E, columnspan = 1)
		
		t.listStudent = Listbox(t, height= 3, width = 30)
		scroll = Scrollbar(t, command= t.listStudent.yview)
		t.listStudent.configure(yscrollcommand=scroll.set)
		
		t.listStudent.grid(row=3, column=1)
		scroll.grid(row=3, column=2, sticky = W)
		
		for Student in Students:
			t.listStudent.insert(END, Student.getFName() + " " + Student.getSName())
		t.listStudent.selection_set(END)
		
		lblProg = Label(t, text='Degree Programme:', font=('Helvetica', 10,'bold'))
		
		butReassign = Button(t, text="Reassign Student", font=("Helvetica", 10))
		butReassign.grid(row=5, column=1, pady=(2, 0))
		
		butDelete = Button(t, text="Delete Student", font=("Helvetica", 10))
		butDelete.grid(row=4, column=1, pady=(2, 0))
		
		butQuit = Button(t, text="Quit", font=("Helvetica", 10), command=t.quit)
		butQuit.grid(row=6, column=1, pady=(10, 10))


def SearchByTutorID(tutor_id, lst):
	global Tutors
	lst.delete(0, END)
	for tutor in Tutors:
		if tutor_id == tutor.getId():
			students = tutor.getStudents()
			for student in students:
				lst.insert(END, student.getFName() + " " + student.getSName())
				lst.selection_set(END)


def searchByStudentID(student_id, lbl):
	global Students
	for student in Students:
		if student_id == student.getId():
			lbl.config(text = student.output())
			break
		else:
			lbl.config(text = "NOT FOUND")
				
def importFunc(fileName, btnList):
	try:
		csv_import(fileName, "tutors.csv")
	except FileNotFoundError:
		pass
	else:
		for btn in btnList:
			btn.config(state="normal")



def main():
	root = Tk()
	root.title("Tutor Management Software")
	app = Window(root)
	root.mainloop()


if __name__ == "__main__":
	main()