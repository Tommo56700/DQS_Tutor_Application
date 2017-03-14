public class Member {

	private String ID, name;
	private int courseID;
	
	public Member(String ID, String name, int courseID) {
		this.ID = ID;
		this.name = name;
		this.courseID = courseID;
	}

	public String getID() {
		return ID;
	}

	public String getName() {
		return name;
	}
	
	public int getCourseID() {
		return courseID;
	}
}
