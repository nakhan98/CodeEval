/* CodeEval - Pangrams
 * https://www.codeeval.com/open_challenges/37/
 */

using System.IO;
using System.Text;
using System.Collections.Generic;

class Program
{
    static string alphabets = "abcdefghijklmnopqrstuvwxyz";

    static string GetMissingAlphas(string string1, string string2)
    {
        string1 = string1.ToLower();        
        string2 = string2.ToLower();
        StringBuilder missingChars = new StringBuilder();
        
        foreach (char letter in string1)
            if (string2.IndexOf(letter) < 0)
                missingChars.Append(letter);

        return missingChars.ToString();
    }


    static void Main(string[] args)
    {
        using (StreamReader reader = File.OpenText(args[0]))
        while (!reader.EndOfStream)
        {
            string line = reader.ReadLine();
            if (null == line)
                continue;
            string missingChars = GetMissingAlphas(alphabets, line);
            if (missingChars.Length > 0)
                System.Console.WriteLine(missingChars);
            else 
                System.Console.WriteLine("NULL");
        }
    }
}
