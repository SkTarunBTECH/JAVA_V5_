import java.util.*;

public class c1 {
    public static void main(String[] args) {
        String[] students = { "Rahul", "Priya", "Arun", "Sneha", "Kiran" };
        Scanner scanner = new Scanner(System.in);

        System.out.print("Search: ");
        String searchName = scanner.nextLine();

        boolean found = false;
        for (String student : students) {
            if (student.equalsIgnoreCase(searchName)) {
                found = true;
                break;
            }
        }

        if (found) {
            System.out.println("Student Found");
        } else {
            System.out.println("Student Not Found");
        }

        scanner.close();
    }
}
