from tkinter import *
from Classes import *


Students = []
Tutors = []

def csv_import(filename1, filename2, header=True): #The import once the csv file is located
	import csv
	global Students
	global Tutors

	with open(filename1) as csvfile: #reads the students.csv
			rdr = csv.reader(csvfile)
			next(csvfile)
			for row in rdr:
				Students.append(Student(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

	with open(filename2) as csvfile: #reads the tutors.csv
			rdr = csv.reader(csvfile)
			next(csvfile)
			for row in rdr:
				Tutors.append(Tutor(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

	assign_students(Students, Tutors)

def assign_students(students, tutors): #Auto assigns students to tutors depending on their module code, a one to one match
	global Tutors
	global Students

	assigned=[]	

	for tutor in Tutors:
		for student in Students:
			if (student not in assigned) and (student.getCourse() == tutor.getCourse()):
				tutor.addStudent(student)
				student.setTutor(tutor)
				break