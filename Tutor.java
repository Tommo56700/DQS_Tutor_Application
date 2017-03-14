public class Tutor extends Member {
	
	private boolean senior;

	public Tutor(String ID, String name, int courseID, boolean senior) {
		super(ID, name, courseID);
		this.senior = senior;
	}
	
	public boolean isSenior(){
		return senior;
	}
	
}