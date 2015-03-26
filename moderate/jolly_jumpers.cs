/* CodeEval: Jolly Jumpers
 * https://www.codeeval.com/open_challenges/43/
 */

using System;
using System.IO;
using System.Collections.Generic;

class JollyJumpers
{

    static List<int> ConvertToInts(List<string> stringList)
    {
        List<int> numbers = new List<int>();
        foreach (string str in stringList)
        {
            int number = int.Parse(str);
            numbers.Add(number);
        }
        return numbers;
    }

    static bool IsJolly(int n, List<int> numbers)
    {
        List<int> jollyNumbers = new List<int>();
        for (int i = 0; i < n-1; i++)
        {
            int diff = numbers[i] - numbers[i+1];
            if (diff < 0)
                diff = diff * -1;
            if (diff >= n)
                return false;
            jollyNumbers.Add(diff);
        }
        
        for (int i=1; i < n; i++)
        {
            if (jollyNumbers.IndexOf(i) < 0)
                return false;
        }

        return true;
    }

    static void Main(string[] args)
    {
        using (StreamReader r = new StreamReader(args[0]))
        {
            while (!r.EndOfStream)
            {
                string line = r.ReadLine();
                List<string> stringList = new List<string>(line.Split(' '));
                //stringList.RemoveAt();
                List<int> numbers = ConvertToInts(stringList);
                int n = numbers[0];
                numbers.RemoveAt(0);
                if (IsJolly(n, numbers))
                    Console.WriteLine("Jolly");
                else
                    Console.WriteLine("Not jolly");
            }
        }
    }
}
