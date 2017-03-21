from tkinter import *
class MainMenu(Frame):
	def __init__(self, master):
		Frame.__init__(self, master, background="white")
		self.initUI()
		
	def initUI(self):
		self.grid()
		
		lblTitle = Label(self, text = "Main Menu", font=("Helvetica", 40,"bold"), background="white")
		lblTitle.grid(row=1, column=0, columnspan=3, padx=(50, 50), pady=(20,20))
		
		butImport = Button(self, text="Import CSV file", font=("Helvetica", 10))
		butImport.grid(row=3, column=1, pady=(2, 0))
		
		butSearch = Button(self, text="Search for Student", font=("Helvetica", 10))
		butSearch.grid(row=4, column=1, pady=(2, 0))
		
		butDisplay = Button(self, text="Display Students by Tutor", font=("Helvetica", 10))
		butDisplay.grid(row=5, column=1, pady=(2, 0))
		
		butFind = Button(self, text="Find Tutor Quota", font=("Helvetica", 10))
		butFind.grid(row=6, column=1, pady=(2, 0))
		
		butDelete = Button(self, text="Delete Student", font=("Helvetica", 10))
		butDelete.grid(row=9, column=1, pady=(2, 0))
		
		butTransfer = Button(self, text="Transfer Student", font=("Helvetica", 10))
		butTransfer.grid(row=8, column=1, pady=(2, 0))
		
		butQuit = Button(self, text="Quit", font=("Helvetica", 10), command=self.quit)
		butQuit.grid(row=10, column=1, pady=(20, 10))
def main():
	root = Tk()
	root.title("Tutor Management Software")
	app = MainMenu(root)
	root.mainloop()


if __name__ == "__main__":
	main()
