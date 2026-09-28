// Question 2 – this Keyword
// Develop a Java program to demonstrate the use of the this keyword to distinguish
// local variables from instance variables while updating employee details.

class Employee {

    int employeeId;
    String name;

    Employee(int employeeId, String name) {
        this.employeeId = employeeId;
        this.name = name;
    }

    void updateEmployee(int employeeId, String name) {
        this.employeeId = employeeId;
        this.name = name;
        System.out.println("Employee Record Updated");
    }

    void display() {
        System.out.println("Employee ID: " + employeeId);
        System.out.println("Employee Name: " + name);
    }
}

public class d2 {
    public static void main(String[] args) {
        // TC1
        Employee e1 = new Employee(201, "Arjun");
        e1.updateEmployee(201, "Arjun");
        e1.display();
        System.out.println();

        // TC2
        Employee e2 = new Employee(202, "Meera");
        e2.updateEmployee(202, "Meera");
        e2.display();
        System.out.println();

        // TC3
        Employee e3 = new Employee(203, "Kiran");
        e3.updateEmployee(203, "Kiran");
        e3.display();
    }
}
