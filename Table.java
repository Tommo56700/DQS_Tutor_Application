import java.util.ArrayList;
import java.util.Iterator;

public class Table {

	private ArrayList<Student> students;
	private ArrayList<Tutor> tutors;
	private boolean tableType;
	
	public Table(boolean tableType) {
		this.tableType = tableType;
		
		if (tableType) {
			this.students = new ArrayList<Student>();
		} else {
			this.tutors = new ArrayList<Tutor>();
		}
	}
	
	public void addRow(Member newMember) {
		if (tableType) {
			students.add((Student) newMember);
		} else {
			tutors.add((Tutor) newMember);
		}
	}
	
	public void deleteRow(String memberName) {
		if (tableType) {
			for (Iterator<Student> iter = students.listIterator(); iter.hasNext();) {
				Student s = iter.next();
				if (s.getName().toLowerCase().equals(memberName.toLowerCase())) {
					iter.remove();
				}
			}
			
		} else {
			for (Iterator<Tutor> iter = tutors.listIterator(); iter.hasNext();) {
				Tutor t = iter.next();
				if (t.getName().toLowerCase().equals(memberName.toLowerCase())) {
					iter.remove();
				}
			}
		}
	}
	
	public Member searchByName(String memberName) {
		if (tableType) {
			for (Student s : students) {
				if (s.getName().toLowerCase().equals(memberName.toLowerCase())) {
	                return s;
	            }
			}
			return null;
			
		} else {
			for (Tutor t : tutors) {
				if (t.getName().toLowerCase().equals(memberName.toLowerCase())) {
	                return t;
	            }
			}
			return null;
		}
	}
	
}