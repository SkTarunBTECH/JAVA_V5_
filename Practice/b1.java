import java.util.*;
public class b1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String name = sc.nextLine();

        if (name.trim().isEmpty() || name.length() > 50) {
            System.out.println("Invalid Customer Name");
        } else {
            System.out.println("Customer Name: " + name);
        }

        sc.close();
    }
}
