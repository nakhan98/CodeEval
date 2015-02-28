/* CodeEval - Reverse and Add
 * https://www.codeeval.com/open_challenges/45/
 */

using System.IO;
using System.Collections.Generic;

class Program
{
    static string ReverseString(string someString)
    {
        char[] reversedCharArr = new char[someString.Length];
        int j = 0;
        for (int i = someString.Length-1; i >= 0; i--)
        {
            reversedCharArr[j] = someString[i];
            j++;
        }
        string reversedString = string.Join("" , reversedCharArr);
        return reversedString;
    }

    static string ReverseAdd(string intString)
    {
        string reversedString = ReverseString(intString);
        uint sum = uint.Parse(intString) + uint.Parse(reversedString);
        return sum.ToString();
    } 

    static bool IsPalindrome(string intString)
    {
        if (intString == ReverseString(intString))
            return true;
        else
            return false;
    }

    static void Main(string[] args)
    {
        using (StreamReader reader = File.OpenText(args[0]))
        while (!reader.EndOfStream)
        {
            string line = reader.ReadLine();
            if (null == line)
                continue;
            string intString = line.Trim();
            int iterations = 0;
            while (true)
            {
                intString = ReverseAdd(intString);
                //System.Console.WriteLine(intString);
                iterations++;
                if (IsPalindrome(intString))
                {
                    System.Console.WriteLine(iterations + " " + intString);
                    break;
                }
            }
        }
    }
}
