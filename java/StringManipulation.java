public class StringManipulation {
    public static void main(String[] args){
        System.out.println(stringManipulation("JUST GETTING BACK FROM LUNCH!"));
    }

    public static String stringManipulation(String input) {
        if (!input.isEmpty()) {
            char firstChar = Character.toUpperCase(input.charAt(0));
            String restOfSentence = input.substring(1).toLowerCase();
            return firstChar + restOfSentence;
        } else {
            return "";
        }
    }

}
