//https://www.codewars.com/kata/583203e6eb35d7980400002a/train/java

import java.util.regex.*;
import java.util.List;
import java.util.Arrays;

public class Smiley {
    public static void main (String[] args) {
        List<String> smileyArray = Arrays.asList(":)", ";(", ";}", ":-D");
        System.out.println(countSmileys(smileyArray));
    }

    public static int countSmileys(List<String> input){
        String pattern = "[:;][-~]?[D)]";

        int count = 0;

        for (String face : input) {
            if (face.matches(pattern)) {
                count++;
            }
        }
        return count;

    }
}
