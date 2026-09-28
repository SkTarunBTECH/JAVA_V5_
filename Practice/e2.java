import java.util.Scanner;

class PricingCalculator {

    // Method to display original price
    public void calculatePrice(double price) {
        if (price <= 0) {
            System.out.println("Invalid Product Price");
            return;
        }
        System.out.printf("Original Price = ₹%,.0f%n", price);
    }

    // Overloaded method to calculate and display discounted price
    public void calculatePrice(double price, double discount) {
        if (price <= 0) {
            System.out.println("Invalid Product Price");
            return;
        }
        if (discount < 0 || discount > 100) {
            System.out.println("Invalid Discount");
            return;
        }

        double finalPrice = price - (price * discount / 100);
        System.out.printf("Final Price = ₹%,.0f%n", finalPrice);
    }
}

public class e2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter Price: ");
        double price = sc.nextDouble();

        System.out.print("Enter Discount: ");
        double discount = sc.nextDouble();

        PricingCalculator calculator = new PricingCalculator();
        calculator.calculatePrice(price, discount);

        sc.close();
    }
}
