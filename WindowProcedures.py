from NewStudents import *

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
			lbl.config(text = "STUDENT ID NOT FOUND")
				
def importFunc(fileName, btnList):
	try:
		csv_import(fileName, "tutors.csv")
	except FileNotFoundError:
		messagebox.showinfo("Import Error" , "Unable to find specified file.")
	else:
		for btn in btnList:
			btn.config(state="normal")
		messagebox.showinfo("Success!" , "File read successfully.")

def studentDelete(StudentID):
	global Students
	for student in Students:
		if student.getId() == StudentID:
			Students.remove(student)
			student.deleteStudent()
			del(student)
			messagebox.showinfo("Success!" , "Student Deleted.")
	
	
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