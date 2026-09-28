// Question 1 – Constructor
// Develop a Java program to create a Student class with Student ID, Name, and CGPA.
// Initialize the object using a constructor and display the student details.

class Student1 {

    int studentId;
    String name;
    double cgpa;

    Student1(int studentId, String name, double cgpa) {
        this.studentId = studentId;
        this.name = name;
        this.cgpa = cgpa;
    }

    void display() {
        System.out.println("Student ID: " + studentId);
        System.out.println("Student Name: " + name);
        System.out.println("CGPA: " + cgpa);
        System.out.println("Student Details Displayed");
    }
}

public class d1 {
    public static void main(String[] args) {
        // TC1
        Student1 s1 = new Student1(101, "Rahul", 8.5);
        s1.display();
        System.out.println();

        // TC2
        Student1 s2 = new Student1(102, "Priya", 9.2);
        s2.display();
        System.out.println();

        // TC3
        Student1 s3 = new Student1(103, "Aman", 7.8);
        s3.display();
    }
}
