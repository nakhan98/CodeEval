/* CodeEval: URI Comparison
 * https://www.codeeval.com/open_challenges/80
 */

import java.io.*;
import java.net.URLDecoder;
import java.net.URLEncoder;

public class UriComparison {
    public static void main (String[] args) throws IOException {
        File file = new File(args[0]);
        BufferedReader buffer = new BufferedReader(new FileReader(file));
        String line;
        while ((line = buffer.readLine()) != null) {
            line = line.trim();
            String[] urls = line.split(";");
            String url1 = urls[0].replaceAll("%(?![0-9a-fA-F]{2})", "%25");
            String url2 = urls[1].replaceAll("%(?![0-9a-fA-F]{2})", "%25");
            url1 = URLDecoder.decode(url1);
            url2 = URLDecoder.decode(url2);
            url1 = processUrl(url1);
            url2 = processUrl(url2);
            if (url1.equals(url2))
                System.out.println("True");
            else
                System.out.println("False");
        }
    }

    public static String processUrl(String url) {
        String newUrl = url.toLowerCase();
        newUrl = newUrl.replaceAll(":80", "");
        newUrl = URLEncoder.encode(newUrl);
        return newUrl;
    }
}
