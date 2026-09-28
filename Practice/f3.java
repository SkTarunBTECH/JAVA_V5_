import java.util.Scanner;

class InvalidAgeException extends Exception {
    public InvalidAgeException(String message) {
        super(message);
    }
}

public class f3 {

    public static void validateAge(int age) {
        try {
            if (age < 18) {
                throw new InvalidAgeException("Invalid Age Exception");
            }
            System.out.println("Eligible to Vote");
        } catch (InvalidAgeException e) {
            System.out.println(e.getMessage());
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter Age: ");
        int age = sc.nextInt();

        validateAge(age);

        sc.close();
    }
}
