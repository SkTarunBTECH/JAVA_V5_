import java.util.Scanner;

class LowBalanceException extends Exception {
    public LowBalanceException(String message) {
        super(message);
    }
}

public class f4 {

    public static void checkBalance(double balance) {
        try {
            if (balance < 1000) {
                throw new LowBalanceException("LowBalanceException");
            }
            System.out.println("Valid Balance");
        } catch (LowBalanceException e) {
            System.out.println(e.getMessage());
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter Balance: ");
        double balance = sc.nextDouble();

        checkBalance(balance);

        sc.close();
    }
}
