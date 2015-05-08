/* CodeEval - Split the Number
 * https://www.codeeval.com/open_challenges/131/
 */

import java.io.*;

public class SplitTheNumber {
    
    static int doCalc(String n, String pattern){
        char sign = '+';        
        int indexOfSign  = pattern.indexOf(sign);
        if (indexOfSign < 0){
            sign = '-';
            indexOfSign  = pattern.indexOf(sign);
        }

        int x = Integer.parseInt(n.substring(0, indexOfSign));
        int y = Integer.parseInt(n.substring(indexOfSign, n.length()));

        if (sign == '+')
            return x+y;
        else
            return x-y;
    }

    public static void main (String[] args) throws IOException {
        File file = new File(args[0]);
        BufferedReader buffer = new BufferedReader(new FileReader(file));
        String line;
        while ((line = buffer.readLine()) != null) {
            line = line.trim();
            // Process line of input Here
            String[] tokens = line.split(" ");
            int result = doCalc(tokens[0], tokens[1]);
            System.out.println(result);
        }
    }
}
