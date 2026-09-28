import java.util.Scanner;

public class f2 {

    public static void accessElement(int n, int index) {
        try {
            int[] arr = new int[n];
            // Access element at given index
            int element = arr[index];
            System.out.println("Element Displayed Successfully");
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("ArrayIndexOutOfBoundsException");
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter array size (N): ");
        int n = sc.nextInt();

        System.out.print("Enter index: ");
        int index = sc.nextInt();

        accessElement(n, index);

        sc.close();
    }
}
