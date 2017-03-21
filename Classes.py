class Student:
	def __init__(self, studentId, course, fName, sName, Tutor, acadYear, uniEmail):
		self.studentId = studentId
		self.course = course
		self.fName = fName
		self.sName = sName
		self.Tutor = Tutor
		self.acadYear = acadYear
		self.uniEmail = uniEmail
		
	def output(self):
		print(self.studentId)
		print(self.course)
		print(self.fName)
		print(self.sName)
		print(self.Tutor.fName + " " + self.Tutor.sName)
		print(self.acadYear)
		print(self.uniEmail)
		
class Tutor:
	def __init__(self, staffId, course, fName, sName, uniEmail, admin, studentNum):
		self.staffId = staffId
		self.course = course
		self.fName = fName
		self.sName = sName
		self.Students = []
		self.uniEmail = uniEmail
		self.admin = admin
		self.studentNum = studentNum
	
	def displayStudents(self):
		for student in self.Students:
			print(student.fName + " " + student.sName)
		
	def output(self):
		print(self.staffId)
		print(self.course)
		print(self.fName)
		print(self.sName)
		print(self.uniEmail)
		print(self.admin)
		print(self.studentNum)
		self.displayStudents()
		
	def addStudent(self, Student):
		if(len(self.Students) >= self.studentNum):
			ValueError
		else:
			self.Students.append(Student)
	
testTutor = Tutor(12, "CM101", "Hailey", "Smiths", "hsmiths@uni.co.uk", True, 10)
testStudent = Student(1, "CM101", "Fred", "Jones", testTutor, "2014/15", "fjones@uni.co.uk")

testTutor.addStudent(testStudent)

print("Test Student: ")
testStudent.output()
print("")
print("Test Tutor: ")
testTutor.output()