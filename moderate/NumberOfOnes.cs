/* CodeEval: Number of Ones
 * https://www.codeeval.com/open_challenges/16  
 */

using System.IO;

class Program
{
    static int NumberOfOnes(string binary)
    {
        int count = 0;
        foreach (char c in binary)
            if (c == '1')
                count++;
        return count;
    }

    static void Main(string[] args)
    {
        foreach (string line in File.ReadLines(args[0]))
        {
            int number = int.Parse( line.Trim() );
            string binary = System.Convert.ToString(number, 2);
            System.Console.WriteLine( NumberOfOnes(binary) );
        }
    }
}
