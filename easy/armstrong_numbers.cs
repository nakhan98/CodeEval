/* CodeEval - ARMSTRONG NUMBERS
 * https://www.codeeval.com/open_challenges/82/
 */

using System.IO;
using System.Collections.Generic;

class Program
{
    static int power(int x, int power)
    {
        if (power == 0) return 1;
        if (power == 1) return x;

        int result = 1;
        for (int i = 0; i < power; i++)
        {
            result = result * x;
        }
        return result;
    }

    static void Main(string[] args)
    {
        using (StreamReader reader = File.OpenText(args[0]))
        while (!reader.EndOfStream)
        {
            string line = reader.ReadLine();

            if (null == line)
                continue;

            int sum = 0;
            string numberString = line.Trim();
            int stringLength = numberString.Length;

            foreach(char c in numberString){
                int val = c - '0';
                sum += power(val, stringLength);
            }

            if (sum.ToString() == numberString)
                System.Console.Out.WriteLine("True");
            else
            {
                System.Console.Out.WriteLine("False");
            }
            
        }
        //System.Console.ReadKey();      
    }
}
