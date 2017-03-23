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
	foundStudent = False

	for student in Students:
		if student.getId() == StudentID:
			Students.remove(student)
			student.deleteStudent()
			messagebox.showinfo("Success!" , "Student Deleted.")
			foundStudent = True

	if foundStudent == False:
		messagebox.showinfo("ERROR!" , "Student Not Found.")
	
	
def findTutorForStudent(student):
	global Tutors
	matchTutor = []
	tutorFound = False

	for tutor in Tutors:
		if student.getCourse() == tutor.getCourse():
			matchTutor.append(tutor)
			tutorFound = True

	if tutorFound == False:
		messagebox.showinfo("ERROR!" , "No Match Found.")
	else:
		return(matchTutor)
		
def matchTutor(Student, Tutor):
	try:
		Student.deleteStudent()
		Student.Tutor = Tutor
	except:
		messagebox.showinfo("ERROR!" , "Student ID is Incorrect.")
	try:
		Tutor.addStudent(Student)
		messagebox.showinfo("Success!" , "Student Reassigned.")
	except:
		messagebox.showinfo("ERROR!" , "Tutor ID is Incorrect.")
	
		


def getStudentFromID(studentID):
	global Students

	for student in Students:
		if student.getId() == studentID:
			return(student)

def getTutorFromID(tutorID):
	global Tutors

	for tutor in Tutors:
		if tutor.getId() == tutorID:
			return(tutor)