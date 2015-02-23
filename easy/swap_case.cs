/* CodeEval - Swap Case
 * https://www.codeeval.com/open_challenges/96/
 */

using System.IO;
using System.Collections.Generic;

class Program
{
    static char ChangeCase(char x)
    {
        if(char.IsUpper(x))
            return char.ToLower(x);
        else
            return char.ToUpper(x);
    }

    static void Main(string[] args)
    {
        using (StreamReader reader = File.OpenText(args[0]))
        while (!reader.EndOfStream)
        {
            string line = reader.ReadLine();
            if (null == line)
                continue;

            foreach (char x in line)
            {
                char newChar = ChangeCase(x);
                //putchar(newChar);
                System.Console.Out.Write(newChar);
            }
            System.Console.Out.WriteLine("");
        }
    }
}
