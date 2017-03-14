import java.io.IOException;

import javax.swing.JFrame;
import javax.swing.JPanel;

@SuppressWarnings("serial")
public class GuiMaker extends JFrame {

	private static GuiMaker frame;
	private JPanel contentPane;
	
	private int windowState = 0;
	
	private static final int WIDTH = 450;
	private static final int HEIGHT = 350;
	
	private static void run(){
		try {
			frame = new GuiMaker();
			frame.setTitle("Group 28 - Application");
			frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
			frame.setSize(WIDTH, HEIGHT);
			frame.setLocationRelativeTo(null);
			frame.setVisible(true);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	//Create the frame.
	public GuiMaker() throws IOException {
		super();
		if (windowState == 0) {
			contentPane = new MainMenu();
		} else if (windowState == 1) {
			
		}
		setContentPane(contentPane);
	}

	public static void main(String[] args) {
		run();
	}
}