public class Palindrome {
    public static void main(String[] args) {


        if (isPalindrome("osssdasdadso")) {
            System.out.println("True");
        } else {
            System.out.println("False");
        }
    }

    public static boolean isPalindrome(String input){

        int left = 0;
        int right = input.length() -  1;

        while (left <= right) {
            left ++;
            right --;
            if (input.charAt(left) != input.charAt(right)){
                return false;
            }
        }

        return true;

    }
}
