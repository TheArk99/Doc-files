public class methods {
  static void myMethod(String fname) {
    System.out.println(fname + " Refsnes");
  }

// Liam Refsnes
// Jenny Refsnes
// Anja Refsnes

  static int myMethod(int x) {
    return 5 + x;
  }

// Outputs 8 (5 + 3)

  public static void main(String[] args) {
    myMethod("Liam");
    myMethod("Jenny");
    myMethod("Anja");
    System.out.println(myMethod(3));
  }
}
