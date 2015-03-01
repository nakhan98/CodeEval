/* CodeEval - Reverse Groups
 * https://www.codeeval.com/public_sc/71/ 
 */

using System.IO;
using System.Collections.Generic;

class Program
{
    static void ReverseArrayParts(string[] array, int x, int y)
    {
        for (int i = x; i <= (x+y)/2; i++){
            int j = i-x;
            string a = array[i];
            string b = array[y-j];
            array[i] = b;
            array[y-j] = a;
        }
    }

    static void ReverseGroup(string[] array, int k)
    {
        int max = array.Length/k * k;        
        int i = 0;
        int j = k -1;
        while (j < max)
        {
            ReverseArrayParts(array, i, j);
            i = j + 1;
            j = i + k - 1;
        }
    }

    static void Main(string[] args)
    {
        using (StreamReader reader = File.OpenText(args[0]))
        while (!reader.EndOfStream)
        {
            string line = reader.ReadLine();
            if (null == line)
                continue;
            string[] tokens = line.Trim().Split(';');
            int k = int.Parse(tokens[1]);
            string[] numberArray = tokens[0].Split(',');
            ReverseGroup(numberArray, k);
            string output = string.Join("," , numberArray);
            System.Console.WriteLine(output);
        }
    }
}
