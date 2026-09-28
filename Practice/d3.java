// Question 3 – static Keyword
// Develop a Java program to demonstrate the use of the static keyword by maintaining
// a common College Name shared by all student objects.

class Student3 {

    int studentId;
    String name;

    static String collegeName = "Alliance University";

    Student3(int studentId, String name) {
        this.studentId = studentId;
        this.name = name;
    }

    void display() {
        System.out.println("Student ID: " + studentId);
        System.out.println("Student Name: " + name);
        System.out.println("College Name: " + collegeName);
    }
}

public class d3 {
    public static void main(String[] args) {
        Student3 s1 = new Student3(101, "Rahul");
        Student3 s2 = new Student3(102, "Priya");
        Student3 s3 = new Student3(103, "Aman");

        s1.display();
        System.out.println();
        s2.display();
        System.out.println();
        s3.display();
    }
}
