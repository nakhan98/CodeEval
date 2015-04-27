/**
 * - CodeEval: String Rotation
 * - https://www.codeeval.com/open_challenges/76/
 */

import java.io.*;

public class StringRotation {

    static boolean isRotation(String string1, String string2)
    {
        if (string1.length() != string2.length())
            return false;
        String concatString = string1 + string1;
        if (concatString.contains(string2))
            return true;
        else
            return false;
    }

    public static void main (String[] args) throws IOException {
        File file = new File(args[0]);
        BufferedReader buffer = new BufferedReader(new FileReader(file));
        String line;
        while ((line = buffer.readLine()) != null) {
            line = line.trim();
            // Process line of input Here
            String[] tokens = line.split(",");
            String string1 = tokens[0];
            String string2 = tokens[1];
            if (isRotation(string1, string2))
                System.out.println("True");
            else
                System.out.println("False");
        }
    }
}
