public class Student extends Member {
	
	private int year, tutorID;

	public Student(String ID, String name, int courseID, int year) {
		super(ID, name, courseID);
		this.year = year;
		this.tutorID = assignToTutor();
	}
	
	public int getYear() {
		return year;
	}
	
	public int getTutorID() {
		return tutorID;
	}
	
	private int assignToTutor() {
		//to do
		return 1;
	}
	
}
