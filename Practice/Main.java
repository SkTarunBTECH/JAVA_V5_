import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String[] restaurants = new String[10];
        int count = 0;

        System.out.println("Enter 5 restaurant names:");
        for (int i = 0; i < 5; i++) {
            System.out.print("Restaurant " + (i + 1) + ": ");
            String name = sc.nextLine();
            if (name.length() > 50) {
                System.out.println("Invalid Restaurant Name");
                return;
            }
            restaurants[count++] = name;
        }

        System.out.print("Enter restaurant name to search: ");
        String search = sc.nextLine();

        boolean found = false;
        for (int i = 0; i < count; i++) {
            if (restaurants[i].equalsIgnoreCase(search)) {
                found = true;
                break;
            }
        }

        if (found) {
            System.out.println("Restaurant Found");
        } else {
            System.out.println("Restaurant Not Found");
        }

        String longest = restaurants[0];
        for (int i = 1; i < count; i++) {
            if (restaurants[i].length() > longest.length()) {
                longest = restaurants[i];
            }
        }

        System.out.println("Total Restaurants = " + count + ", Longest Name = " + longest);

        System.out.println("Available Restaurants:");
        for (int i = 0; i < count; i++) {
            System.out.println(restaurants[i]);
        }

        sc.close();
    }
}
