import java.util.Scanner;

public class f1 {

    public static void getReciprocal(int number) {
        try {
            if (number == 0) {
                // Division by zero triggers ArithmeticException
                int error = 1 / 0;
            }
            double reciprocal = 1.0 / number;
            System.out.println("Reciprocal = " + reciprocal);
        } catch (ArithmeticException e) {
            System.out.println("ArithmeticException");
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter an integer: ");
        int number = sc.nextInt();

        getReciprocal(number);

        sc.close();
    }
}
