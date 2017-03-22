from tkinter import *

class TutorQuota(Frame):
	def __init__(self, master):
		Frame.__init__(self, master, background="white")
		self.initUI()
		
	def initUI(self):
		self.grid()
		
		lblTitle = Label(self, text = "Tutor Quota", font=("Helvetica", 40,"bold"), background="white")
		lblTitle.grid(row=1, column=0, columnspan=3, padx=(50, 50), pady=(20,20))
		
		butQuota = Button(self, text="Display Quota", font=("Helvetica", 10), command=getQuotaInfo())
		butQuota.grid(row=2, column=1, pady=(2, 0))


	def getQuotaInfo(tutors):
		labels = []
		for t in tutors:
			labels.append(Label(self, text = (t.getFName(), t.getSName(), ": Total Students -", t.getStudentNum(), " |  Email Address", t.getEmail()), font=("Helvetica", 20, "bold"), background="white"))
			lables[-1].grid(row=(3 + tutors.index(t)), column=1, columnspan=2, padx=(50, 50), pady=(20,20))