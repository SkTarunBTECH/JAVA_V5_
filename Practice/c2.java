public class c2 {
    public static void main(String[] args) {
        String[] cities = {"Delhi", "Mumbai", "Bengaluru", "Pune", "Chennai"};
        String longest = "";
        
        for (String city : cities) {
            if (city.length() > longest.length()) {
                longest = city;
            }
        }
        
        System.out.println("Longest City = " + longest);
    }
}
