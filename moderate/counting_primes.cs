/* CodeEval - Counting Primes
 * https://www.codeeval.com/open_challenges/63/
 */

using System.IO;
using System.Collections.Generic;

class Program
{
    static bool IsPrime(int some_int)
    {
        if (some_int < 2)
            return false;
        int limit = (int)System.Math.Sqrt(some_int) + 1;        
        for (int i = 2; i < limit; i++)
            if (some_int % i == 0)
                return false;
        return true;
    }

    static void Main(string[] args)
    {
        using (StreamReader reader = File.OpenText(args[0]))
        while (!reader.EndOfStream)
        {
            string line = reader.ReadLine();
            if (null == line)
                continue;
            string[] numbers = line.Trim().Split(',');            
            int x = int.Parse(numbers[0]);
            int y = int.Parse(numbers[1]);
            int count = 0;
            for (int i = x; i <= y; i++)
                if (IsPrime(i))
                    count++;
            System.Console.WriteLine(count);
        }
    }
}
