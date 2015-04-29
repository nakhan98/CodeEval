/* 
 * - CodeEval: Number of Ones
 * - https://www.codeeval.com/open_challenges/16/
 */

import java.io.*;

public class NumberOfOnes {

    static int numberOfOnes(String binary){
        int count = 0;
        for (char c : binary.toCharArray())
            if (c == '1')
                count++;
        return count;
    }

    public static void main (String[] args) throws IOException {
        File file = new File(args[0]);
        BufferedReader buffer = new BufferedReader(new FileReader(file));
        String line;
        while ((line = buffer.readLine()) != null) {
            line = line.trim();
            int number = Integer.parseInt(line);
            String binary = Integer.toBinaryString(number);
            System.out.println( numberOfOnes(binary) );
        }
    }
}
