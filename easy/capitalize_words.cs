/* CodeEval - Capitalize Words
 * https://www.codeeval.com/open_challenges/93/
 */

using System.IO;
using System.Collections.Generic;

class Program
{

    static void Main(string[] args)
    {
        using (StreamReader reader = File.OpenText(args[0]))
        while (!reader.EndOfStream)
        {
            string line = reader.ReadLine();
            if (null == line)
                continue;
            
            string[] words = line.Trim().Split(' '); 
            
            foreach (string word in words)
            {
                System.Console.Out.Write(Capitalize(word) + " ");
            }
            System.Console.Out.WriteLine("");
        }
    }

    static string Capitalize(string word)
    {
        string newWord = char.ToUpper(word[0]) + word.Substring(1);
        return newWord;
    }
}
