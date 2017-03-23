from Classes import *

def csv_import(filename, header=True):
	import csv
	student_details = []

	with open(filename) as csvfile:
			rdr = csv.reader(csvfile)
			next(csvfile)
			for row in rdr:
				student_details.append(Student(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
	close(filename)
	return student_details

def assign_students(students):
	for student in students:
		if student.getCourse() == "UFBSCMSA":
			testtutor.addStudent(student)
		elif student.getCourse() == "UFBSCMSB":
			testtutor2.addStudent(student)
		elif student.getCourse() == "UFBSCSFA":
			testtutor3.addStudent(student)
		elif student.getCourse() == "UFBSCSFB":
			testtutor4.addStudent(student)
		elif student.getCourse() == "UFBSCSHA":
			testtutor5.addStudent(student)
		elif student.getCourse() == "UFBSCSHB":
			testtutor6.addStudent(student)
		elif student.getCourse() == "UFBSCVCA":
			testtutor7.addStudent(student)
		elif student.getCourse() == "UFBSCVCB":
			testtutor8.addStudent(student)
		elif student.getCourse() == "UFBSASEA":
			testtutor9.addStudent(student)
		else:
			ValueError #Throw error stating too many students for number of tutors??????
			print("Too many students to be mentored by this few tutors") #??????????