import java.util.Scanner;

public class c4 {
    public static void main(String[] args) {
        String[] books = {"Java", "Python", "C", "HTML", "SQL"};
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Search: ");
        String search = sc.next();
        
        boolean found = false;
        for (String book : books) {
            if (book.equalsIgnoreCase(search)) {
                found = true;
                break;
            }
        }
        
        if (found) {
            System.out.println("Book Found");
        } else {
            System.out.println("Book Not Found");
        }
        
        sc.close();
    }
}
