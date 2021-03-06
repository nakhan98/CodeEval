/* CodeEval: URI Comparison
 * https://www.codeeval.com/open_challenges/80
 */

import java.io.*;
import java.net.URLDecoder;
import java.net.URLEncoder;

public class URIComparison {
    public static void main (String[] args) throws IOException {
        File file = new File(args[0]);
        BufferedReader buffer = new BufferedReader(new FileReader(file));
        String line;
        while ((line = buffer.readLine()) != null) {
            line = line.trim();
            String[] urls = line.split(";");
            String url1 = convertPercentSigns(urls[0]);
            String url2 = convertPercentSigns(urls[1]);
            url1 = decodeUrl(url1);
            url2 = decodeUrl(url2);
            if (url1.equals(url2))
                System.out.println("True");
            else
                System.out.println("False");
        }
    }

    /**
     * Deal with stray percent signs that aren't in hex codes
     */
    public static String convertPercentSigns(String url){
        url = url.replaceAll("%(?![0-9a-fA-F]{2})", "%25");
        return url;
    }
    
    public static String decodeUrl(String url) {
        String newUrl = url.toLowerCase();
        newUrl = newUrl.replaceAll(":80", "");
        newUrl = URLDecoder.decode(newUrl);
        return newUrl;
    }
}
