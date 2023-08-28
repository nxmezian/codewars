public class StringEndsWith {
    public static void main(String[] args) {

        String str = "abc";
        String ending = "a";
        if (solution(str, ending)) {
            System.out.println("True");

        }
    }

    public static boolean solution(String str, String ending) {
        if (str.startsWith(ending)) {
            return true;
        }
        else {
            return false;
        }
    }

}
