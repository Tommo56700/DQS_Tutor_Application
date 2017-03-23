from tkinter import *
from classes import *

class TutorQuota(Frame):
	def __init__(self, master):
		Frame.__init__(self, master, background="white")
		self.initUI()
	
	def getQuotaInfo(self):
		global tutors
		labels = []
		for t in tutors:
			myString = ("Name: " + t.getFName() + " " + t.getSName() + "   |   Total Students: " + str(len(t.getStudents())) + "   |   Email Address: " + t.getEmail())
			labels.append(Label(self, text = myString, font=("Helvetica", 10, "bold"), background="white"))
			labels[-1].grid(row=(3 + tutors.index(t)), column=0, columnspan=1, padx=(50, 50), pady=(20, 20))

	def initUI(self):
		self.grid()
		
		lblTitle = Label(self, text = "Tutor Quota", font=("Helvetica", 40,"bold"), background="white")
		lblTitle.grid(row=1, column=0, columnspan=1, padx=(50, 50), pady=(20,20))
		
		butQuota = Button(self, text="Display Quota", font=("Helvetica", 10), command=self.getQuotaInfo)
		butQuota.grid(row=2, column=0, pady=(2, 0))

def main():
	root = Tk()
	root.title("Tutor Management Software")
	app = TutorQuota(root)
	root.mainloop()


if __name__ == "__main__":
	main()