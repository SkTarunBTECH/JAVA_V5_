import java.util.*;

class Patient {
    private int age;
    int patientId;
    String patientName;
    String diagnosis;

    static String hospitalName = "Apollo Hospitals";
    final int MAX_PATIENTS = 100;

    public Patient(int patientId, String patientName, int age, String diagnosis) {
        this.patientId = patientId;
        this.patientName = patientName;
        this.age = age;
        this.diagnosis = diagnosis;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
}

public class appollo4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Map<Integer, Patient> records = new HashMap<>();

        System.out.print("Enter Patient ID: ");
        int id = sc.nextInt();
        sc.nextLine();
        System.out.print("Enter Patient Name: ");
        String name = sc.nextLine();
        System.out.print("Enter Age: ");
        int age = sc.nextInt();
        sc.nextLine();
        System.out.print("Enter Diagnosis: ");
        String diag = sc.nextLine();

        if (age < 1 || age > 100) {
            System.out.println("Invalid Age");
            return;
        }

        if (!records.containsKey(id)) {
            Patient p = new Patient(id, name, age, diag);
            records.put(id, p);
            System.out.println("Patient Record Created");
        } else {
            Patient p = records.get(id);
            p.patientName = name;
            p.setAge(age);
            p.diagnosis = diag;
            System.out.println("Patient Record Updated");
        }

        if (records.containsKey(id)) {
            System.out.println("Patient Details Displayed");
        }

        sc.close();
    }
}
