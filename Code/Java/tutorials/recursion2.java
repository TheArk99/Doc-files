public class recursion2 {
  public static void main(String[] args) {
    int result = sum(5, 10);
    System.out.println(result);
  }
  public static int sum(int start, int end) {
    if (end > start) {
      //System.out.println(start);
      //System.out.println(end);
      System.out.println("\n" + end + "+" + sum(start, end - 1));
      int var = end + sum(start, end - 1);
      //System.out.println(var);
      return var;
         } else {
           //System.out.println(end);
      return end;
    }
  }
}
