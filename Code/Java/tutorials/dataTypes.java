public class dataTypes {
  public static void main(String[] args) {
    byte numByte = -100; //bytes hold from -128 to 127
    short numShort = -5000; //shorts hold from -32768 to 32767
    int numInt = 100000; //ints hold from -2147483648 to 2147483647
    long numLong = 1500000000000000000L; //Longs are from -9223372036854775808 to 9223372036854775807 and should be ended with the "L"
    float numFloat = 5.75f; // can store fractional numbers from 3.4e−038 to 3.4e+038 and should be ended with the "f"
    double numDouble = 19.99d; // can store fractional numbers from 1.7e−308 to 1.7e+308 and should be ended with the "d"
    System.out.println(numByte);
    System.out.println(numShort);
    System.out.println(numInt);
    System.out.println(numLong);
    System.out.println(numFloat);
    System.out.println(numDouble);

    //A floating point number can also be a scientific number with an "e" to indicate the power of 10:
    float f1 = 35e3f;
    double d1 = 12E4d;
    System.out.println(f1);
    System.out.println(d1);

    //bools are true or false just like in any other language
    boolean isJavaFun = true;
    boolean isFishTasty = false;
    System.out.println(isJavaFun);     // Outputs true
    System.out.println(isFishTasty);   // Outputs false

    //char is used to store a single character us single quotes for char ''
    char myGrade = 'B';
    System.out.println(myGrade);

    //Alternatively, you can use ASCII values to display certain characters:
    char a = 65, b = 66, c = 67;
    System.out.println(a);
    System.out.println(b);
    System.out.println(c);

    //String needs a capital for String when initialization, also you need to use double quotes ""
    String greeting = "Hello World";
    System.out.println(greeting);
  }
}
