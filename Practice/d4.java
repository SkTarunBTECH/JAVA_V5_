// Day 4: Encapsulation
// This program demonstrates encapsulation by making fields private
// and accessing them through getter and setter methods.

class Product {
    private int productId;
    private double price;

    public void setProductId(int productId) {
        if (productId > 0) {
            this.productId = productId;
        } else {
            System.out.println("Invalid Product ID!");
        }
    }

    public void setPrice(double price) {
        if (price > 0) {
            this.price = price;
        } else {
            System.out.println("Invalid Price!");
        }
    }

    public double getPrice() {
        return price;
    }

    void display() {
        System.out.println("Product ID: " + productId);
        System.out.println("Product Price: " + price);
    }
}

public class d4 {
    public static void main(String[] args) {
        Product p = new Product();

        p.setProductId(101);
        p.setPrice(5000);

        p.display();

        System.out.println("Price (via getter): " + p.getPrice());

        p.setProductId(-5);
        p.setPrice(-100);
    }
}
