import java.util.Scanner;

interface PaymentMethod {
    void processPayment();
}

class UPIPayment implements PaymentMethod {
    @Override
    public void processPayment() {
        System.out.println("Payment Successful");
    }
}

class CreditCardPayment implements PaymentMethod {
    @Override
    public void processPayment() {
        System.out.println("Payment Successful");
    }
}

class DebitCardPayment implements PaymentMethod {
    @Override
    public void processPayment() {
        System.out.println("Payment Successful");
    }
}

class NetBankingPayment implements PaymentMethod {
    @Override
    public void processPayment() {
        System.out.println("Payment Successful");
    }
}

class PaymentService {
    public static void makePayment(String paymentMode) {
        PaymentMethod paymentMethod = null;

        if (paymentMode.equalsIgnoreCase("UPI")) {
            paymentMethod = new UPIPayment();
        } else if (paymentMode.equalsIgnoreCase("Credit Card")) {
            paymentMethod = new CreditCardPayment();
        } else if (paymentMode.equalsIgnoreCase("Debit Card")) {
            paymentMethod = new DebitCardPayment();
        } else if (paymentMode.equalsIgnoreCase("Net Banking")) {
            paymentMethod = new NetBankingPayment();
        } else {
            System.out.println("Invalid Payment Mode");
            return;
        }

        paymentMethod.processPayment();
    }
}

public class e4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter Payment Mode: ");
        String paymentMode = sc.nextLine();

        PaymentService.makePayment(paymentMode);

        sc.close();
    }
}
