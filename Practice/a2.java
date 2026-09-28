import java.util.*;

public class a2 {
    public static int a2(int[] arr) {
        int largest = Integer.MIN_VALUE;
        int secondLargest = Integer.MIN_VALUE;

        for (int value : arr) {
            if (value == largest) continue;
            if (value > largest) {
                secondLargest = largest;
                largest = value;
            } else if (value > secondLargest) {
                secondLargest = value;
            }
        }
        return secondLargest;
    }

    public static void main(String[] args) {
        System.out.println("Enter the number of elements and elements  in the array:");
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        int result = a2(arr);
        if (result == Integer.MIN_VALUE) {
            System.out.println("Second largest element does not exist");
        } else {
            System.out.println("Second Largest = " + result);
        }
    }
}
