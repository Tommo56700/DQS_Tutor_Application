def studentDelete(Student):
	Student.deleteStudent()
	del(Student)
	
def findTutorForStudent(Student):
	#import list of tutors
	Tutors = []
	tutorMatch = []
	for Tutor in range(0, len(Tutors)):
		if (Student.getCourse() == Tutor.getCourse()) and (Tutor.getStudentNum() > len(Tutor.Students)):
			tutorMatch.append(Tutor)
			
def matchTutor(Student, Tutor):
	Student.Tutor = Tutor
	Tutor.addStudent(Student)
	
from tkinter import *
class MainMenu(Frame):
	def __init__(self, master):
		Frame.__init__(self, master, background="white")
		self.initUI()
		
	def initUI(self):
		self.grid()
		
		lblTitle = Label(self, text = "Student Management", font=("Helvetica", 30,"bold"), background="white")
		lblTitle.grid(row=1, column=0, columnspan=3, padx=(50, 50), pady=(20,20))
		
		lblProg = Label(self, text='Students:', background="white", font=('Helvetica', 12))
		lblProg.grid(row=3, column=0, sticky = E, columnspan = 1)
		
		self.listProg = Listbox(self, height= 3, width = 30)
		scroll = Scrollbar(self, command= self.listProg.yview)
		self.listProg.configure(yscrollcommand=scroll.set)
		
		self.listProg.grid(row=3, column=1)
		scroll.grid(row=3, column=2, sticky = W)
		
		Students = ["Bob Allen", "Jeff Darlson", "Mick Mack", "Harry Hunderton", "Paul Meynay", "Brian Scorely"]
		
		for Student in Students:
			self.listProg.insert(END, Student)#Student.getFName() + " " + Student.getLName())
		self.listProg.selection_set(END)
		
		lblProg = Label(self, text='Degree Programme:', font=('Helvetica', 10,'bold'))
		
		butReassign = Button(self, text="Reassign Student", font=("Helvetica", 10))#, command = matchTutor(,findTutorForStudent()))
		butReassign.grid(row=5, column=1, pady=(2, 0))
		
		butDelete = Button(self, text="Delete Student", font=("Helvetica", 10))#, command=studentDelete())
		butDelete.grid(row=4, column=1, pady=(2, 0))
		
		butQuit = Button(self, text="Quit", font=("Helvetica", 10), command=self.quit)
		butQuit.grid(row=6, column=1, pady=(10, 10))
		
def main():
	root = Tk()
	root.title("Tutor Management Software")
	app = MainMenu(root)
	root.mainloop()


if __name__ == "__main__":
	main()