import java.util.Scanner;

class BaseProduct {
    protected String productId;
    protected String productName;
    protected double price;

    public BaseProduct(String productId, String productName, double price) {
        this.productId = productId;
        this.productName = productName;
        this.price = price;
    }

    public void displayCategoryInfo() {
        if (price <= 0) {
            System.out.println("Invalid Product Price");
        } else {
            System.out.println("Product Details Displayed");
        }
    }
}

class Electronics extends BaseProduct {
    public Electronics(String productId, String productName, double price) {
        super(productId, productName, price);
    }

    @Override
    public void displayCategoryInfo() {
        if (price <= 0) {
            System.out.println("Invalid Product Price");
        } else {
            System.out.println("Electronics Product Displayed");
        }
    }
}

class HomeAppliance extends BaseProduct {
    public HomeAppliance(String productId, String productName, double price) {
        super(productId, productName, price);
    }

    @Override
    public void displayCategoryInfo() {
        if (price <= 0) {
            System.out.println("Invalid Product Price");
        } else {
            System.out.println("Home Appliance Product Displayed");
        }
    }
}

public class e3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter Category (Electronics/Home Appliance): ");
        String category = sc.nextLine();

        System.out.print("Enter Product Name: ");
        String productName = sc.nextLine();

        System.out.print("Enter Price: ");
        double price = sc.nextDouble();

        if (price <= 0) {
            System.out.println("Invalid Product Price");
        } else if (category.equalsIgnoreCase("Electronics")) {
            Electronics p = new Electronics("P101", productName, price);
            p.displayCategoryInfo();
        } else if (category.equalsIgnoreCase("Home Appliance") || category.equalsIgnoreCase("HomeAppliance")) {
            HomeAppliance p = new HomeAppliance("P102", productName, price);
            p.displayCategoryInfo();
        } else {
            BaseProduct p = new BaseProduct("P100", productName, price);
            p.displayCategoryInfo();
        }

        sc.close();
    }
}
