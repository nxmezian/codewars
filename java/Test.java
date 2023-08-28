import java.io.File;
import java.io.IOException;

public class Test {
    public static void main(String[] args) {
        // Specify the path and name of the file you want to create
        String filePath = "C:/test.txt";

        // Create a File object
        File file = new File(filePath);

        try {
            // Create a new file at the specified path
            if (file.createNewFile()) {
                System.out.println("File created successfully!");
            } else {
                System.out.println("File already exists.");
            }
        } catch (IOException e) {
            System.out.println("An error occurred: " + e.getMessage());
            e.printStackTrace();
        }
    }
}




