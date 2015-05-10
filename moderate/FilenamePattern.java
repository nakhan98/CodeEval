/* CodeEval: Filename Pattern
 * https://www.codeeval.com/open_challenges/169/
 */

import java.io.*;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;
import java.lang.StringBuilder;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class FilenamePattern {
    
    static String join(String delimiter, List<String> stringList){
        StringBuilder joinedString = new StringBuilder();
        for (String string : stringList)
            joinedString.append(string + delimiter);

        joinedString.deleteCharAt(joinedString.length() - 1);
        return joinedString.toString();
    }

    static String convertGlobToRegex(String globPattern){
        String regex = "^";
        for (int i = 0; i < globPattern.length(); i++){
            char c = globPattern.charAt(i);
            if (c == '*')
                regex += ".*";
            else if (c == '?')
                regex += ".";
            else if (c == '.')
                regex += "\\.";
            else
                regex += c;
        }
        regex += '$';
        return regex;
    }

    static List<String> matchString(String globPattern, String[] filenames){
        List<String> matchedFilenames = new ArrayList<String>();
        String regex = convertGlobToRegex(globPattern);
        Pattern pattern = Pattern.compile(regex);
        for (String filename : filenames){
            Matcher matcher = pattern.matcher(filename);
            if (matcher.matches())
                matchedFilenames.add(filename);
        }
        return matchedFilenames;
    }

    public static void main (String[] args) throws IOException {
        File file = new File(args[0]);
        BufferedReader buffer = new BufferedReader(new FileReader(file));
        String line;
        while ((line = buffer.readLine()) != null) {
            line = line.trim();
            String[] tokens = line.split(" ");
            String pattern = tokens[0];
            String[] filenames = Arrays.copyOfRange(tokens, 1, tokens.length);
            List<String> matchedFilenames = matchString(pattern, filenames);
            if (matchedFilenames.size() == 0)
                System.out.println('-');
            else {
                String output = join(" ", matchedFilenames);
                System.out.println(output);
            }
        }
    }
}
