import java.util.Scanner;

interface Payment {
    void processPayment(String paymentMode);
}

abstract class Product {
    String productId;
    String productName;
    double price;

    public Product(String productId, String productName, double price) {
        this.productId = productId;
        this.productName = productName;
        this.price = price;
    }

    abstract double calculateFinalPrice();
    
    double calculateFinalPrice(double additionalDiscount) {
        return price - (price * additionalDiscount / 100);
    }
}

class FlipkartProduct extends Product implements Payment {
    double discount;

    public FlipkartProduct(String productId, String productName, double price, double discount) {
        super(productId, productName, price);
        this.discount = discount;
    }

    @Override
    double calculateFinalPrice() {
        return price - (price * discount / 100);
    }

    @Override
    public void processPayment(String paymentMode) {
        if (price > 0) {
            double finalPrice = calculateFinalPrice();
            System.out.printf("Final Price = \u20B9%,d, Payment Successful\n", (long) finalPrice);
        } else {
            System.out.println("Invalid Product Price");
        }
    }
}

public class Flipk5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        String productId = sc.nextLine();
        String productName = sc.nextLine();
        double price = sc.nextDouble();
        double discount = sc.nextDouble();
        sc.nextLine();
        String paymentMode = sc.nextLine();

        Product product = new FlipkartProduct(productId, productName, price, discount);
        Payment paymentProcessor = (Payment) product;
        paymentProcessor.processPayment(paymentMode);
        
        sc.close();
    }
}
