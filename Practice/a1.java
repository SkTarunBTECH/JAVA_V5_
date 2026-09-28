// import java.util.*;
// // 1.only one week
// // Attendance Report

// class a1 {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);

//         System.out.print("Enter id: ");
//         int eid = sc.nextInt();
//         sc.nextLine(); // consume leftover newline

//         System.out.print("Enter name: ");
//         String ename = sc.nextLine();

//         int[] att = new int[7];
//         int p = 0, a = 0;

//         System.out.println("Enter attendance (1=Present, 0=Absent): ");
//         for (int i = 0; i < 7; i++) {
//             System.out.print("Day " + (i + 1) + ": ");
//             att[i] = sc.nextInt();

//             if (att[i] == 1) {
//                 p++;
//             } else {
//                 a++;
//             }
//         }

//         double per = (p / 7.0) * 100;
//         boolean eli = per >= 90;

//         System.out.println("\n--- Attendance Report ---");
//         System.out.println("Employee ID: " + eid);
//         System.out.println("Employee Name: " + ename);
//         System.out.println("Present: " + p);
//         System.out.println("Absent: " + a);
//         System.out.println("Percentage: " + per + "%");
//         System.out.println("Eligible: " + eli);
//     }
// }


// first program 

import java.util.*;

public class a1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] marks = new int[N];
        char[] grades = new char[N];

        int countA = 0, countB = 0, countC = 0, countD = 0, countF = 0;
        double sum = 0;

        for (int i = 0; i < N; i++) {
            marks[i] = sc.nextInt();
            sum += marks[i];

            if (marks[i] >= 90 && marks[i] <= 100) {
                grades[i] = 'A';
                countA++;
            } else if (marks[i] >= 80) {
                grades[i] = 'B';
                countB++;
            } else if (marks[i] >= 70) {
                grades[i] = 'C';
                countC++;
            } else if (marks[i] >= 60) {
                grades[i] = 'D';
                countD++;
            } else {
                grades[i] = 'F';
                countF++;
            }
        }

        System.out.print("Grades: ");
        for (char g : grades) {
            System.out.print(g + " ");
        }
        System.out.println();

        System.out.println("A=" + countA + ", B=" + countB + ", C=" + countC + ", D=" + countD + ", F=" + countF);
        System.out.printf("Average = %.1f\n", sum / N);

        sc.close();
    }
}
