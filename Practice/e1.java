import java.util.Scanner;

class Product1 {
    private String productId;
    private String productName;
    private double price;

    public Product1(String productId, String productName, double price) {
        this.productId = productId;
        this.productName = productName;
        setPrice(price);
    }

    public String getProductId() {
        return productId;
    }

    public void setProductId(String productId) {
        this.productId = productId;
    }

    public String getProductName() {
        return productName;
    }

    public void setProductName(String productName) {
        this.productName = productName;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public void displayProduct() {
        if (price <= 0) {
            System.out.println("Invalid Product Price");
        } else {
            System.out.println("Product ID: " + productId);
            System.out.println("Product Name: " + productName);
            System.out.println("Price: " + price);
            System.out.println("Product Details Displayed");
        }
    }
}

public class e1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter Product ID: ");
        String productId = sc.nextLine();

        System.out.print("Enter Product Name: ");
        String productName = sc.nextLine();

        System.out.print("Enter Price: ");
        double price = sc.nextDouble();

        Product1 p = new Product1(productId, productName, price);
        p.displayProduct();

        sc.close();
    }
}
