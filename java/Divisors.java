public class Divisors {
    public static void main (String[] args){
        System.out.println(countDivisors(100));

    }
public static int countDivisors (int n){
        int count = 0;
        int sqrtN = (int) Math.sqrt(n);

        for (int i = 1; i <= sqrtN; i++) {
            if (n % i == 0) {
                count += 2;
            }}

            if (sqrtN * sqrtN == n) {
                count -= 1;
            }

            return count;
        }
}

