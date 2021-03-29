public class Experiments {

    static int returnAndFinally() {
        try {
            int a = 5, b = 1;
            return a / b;
        } catch (Exception e) {
            return 5;
        } finally {
            return -1;  // "Will this code get run?"
        }
    }
    public static void main(String[] main) {
        System.out.print(returnAndFinally());
    }
}
