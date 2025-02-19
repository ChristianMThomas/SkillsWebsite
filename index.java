import java.util.Scanner;
public class index {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        System.out.println("What is your name");
        String name = input.next();



        // variables

    String firstName = "Bobby";      // declared a String firstName  with the value of Bobby
    char middleInitial = 'R';        // declared a Char middleInitial  with the value of R
    String lastName = "Hill";        // declared a String lastName  with the value of Hill
    int age = 16;                    // declared an int age with the value of 16
    boolean isAStudent = true;        // declared a boolean isAStudent  with the value of true
    boolean hasAJob = false;          // declared a boolean hasAJob  with the value of false


        // Final 

        final double PI = 3.145159;     //declared a final constant named PI

        int radius = 20;                //declared an int called radius
        radius = 21;                     //reassigned  radius



        byte b = 99;
        short s = 9999;
        int i = 999999999;
        long l = 999999999;
        float f = 4.7333434f;
        double d = 4984.355453532;

        boolean isCold = true;
        char c = 'c';

        String namet = "Chris";
        String kids[];


        Car car1 = new Car("Toyota", 1999);


        // Arithmetic

        int friends = 20;

    friends = friends + 1;    // adding 1  this will give you 21
    friends = friends - 1;    // subtracting 1  this will give you 20
    friends = friends * 2;    // multiplying by 2  this will give you 40
    friends = friends / 2;   // diving by 2  this will give you 20

    // augment assingment operator  (shortcut)

    friends +=1;        // adding 1  this will give you 21
    friends -=1;        // subtracting 1  this will give you 20
    friends *=2;        // multiplying by 2  this will give you 40
    friends /=2;        // diving by 2  this will give you 20

    // String concatenation 
    String str1 = "Hello";
    String str2 = "World";
    String result = str1 + " " + str2; // Using + operator
    String result2 = str1.concat(" ").concat(str2); // Using concat() method
    

    // SubString
    String str = "Hello World";
    String subStr = str.substring(0, 5); // Extracts "Hello"
    

    //Length
    String strn = "Hello World";
    int length = strn.length(); // Length of the string
        
    //String Comparison
        String strng = "Hello";
        String strng2 = "hello";
        
        boolean isEqual = strng.equals(strng2); // Case-sensitive comparison
        boolean isEqualIgnoreCase = strng.equalsIgnoreCase(strng2); // Case-insensitive comparison
        int comparison = strng.compareTo(strng2); // Lexicographical comparison
        
    //String Replacement
        String st1 = "Hello World";
        String replacedStr = st1.replace('o', 'a'); // Replaces 'o' with 'a'
        // replacedStr: "Hella Warld"
        
        String replacedAllStr = st1.replaceAll("World", "Java"); // Replaces "World" with "Java"
        // replacedAllStr: "Hello Java"
        

    //String Splitting
        String string = "Hello World Java";
        String[] words = string.split(" "); // Splits by space
        // words: ["Hello", "World", "Java"]
        




        // Arrays

        //declaring arrays
        String[] cars;
        String[] carBrands = {"Volvo", "BMW", "Ford", "Mazda"};
        int[] myNum = {10, 20, 30, 40};

        //access elements of arrays
        System.out.println(carBrands[0]); // Outputs Volvo


        //change elements of array

        carBrands[0] = "Lexus";

        //length of array
       String fruits[] = {"Orange", "Apple", "Grape"};
        System.out.println(fruits.length);  // Outputs 4
            
        // Using for loop
        for(String fruit : fruits){
            System.out.println(fruit);
        }

    } 

}
