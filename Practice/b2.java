import java.util.*;

public class b2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String feedback = sc.nextLine();

        if (feedback.trim().isEmpty()) {
            System.out.println("Invalid Feedback Message");
        } else if (feedback.length() > 500) {
            System.out.println("Feedback Exceeds Maximum Length");
        } else {
            System.out.println("Characters = " + feedback.length());
        }

        sc.close();
    }
}
