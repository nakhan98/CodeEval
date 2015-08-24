/* CodeEval: URI Comparison
 * https://www.codeeval.com/open_challenges/80
 */

using System.IO;

class URIComparison
{
    static void Main(string[] args)
    {
        using (StreamReader reader = File.OpenText(args[0]))
        while (!reader.EndOfStream)
        {
            string line = reader.ReadLine();
            if (null == line)
                continue;
            string[] urls = line.Trim().Split(';');
            string url1 =  DecodeUrl(urls[0]);
            string url2 =  DecodeUrl(urls[1]);
            if (url1 == url2)
                System.Console.WriteLine("True");
            else
                System.Console.WriteLine("False");
        }
    }

    static string DecodeUrl(string url)
    {
        string newUrl = url.ToLower();
        newUrl = newUrl.Replace(":80", "");
        newUrl = System.Uri.UnescapeDataString(newUrl); 
        return newUrl;
    }
}
