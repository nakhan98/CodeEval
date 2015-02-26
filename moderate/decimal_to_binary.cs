/* CodeEval - Decimal to Binary
 * https://www.codeeval.com/open_challenges/27/submit/
 */

using System.IO;
using System.Collections.Generic;

class Program
{
    static object Power(int x, int y)
    {
        int orig_y = y;
        if (y < 0)
            y *= -1;
        int a = 1;
        for (int i = 0; i < y; i++) {
            a = a * x;
        }
        if (orig_y < 0)
            return (float)(1 / a);
        else
            return a;
    }

    static string ConvertToBinary(int decimalNumber)
    {
        if (decimalNumber == 0)
            return decimalNumber.ToString();
        List<int> powersCollected = new List<int> ();
        int exponent = 0;
        while (true)
        {
            if ((int)Power(2,exponent) == decimalNumber)
            {
                decimalNumber = 0;
                powersCollected.Add (exponent);
                break;
            }
            else if ((int)Power(2, exponent) > decimalNumber)
            {
                exponent--;
                decimalNumber -= (int)Power(2, exponent);
                powersCollected.Add (exponent);
                exponent = 0;
            }
            else 
                exponent++; 
        }

        char[] binaryNumberArray = new char[powersCollected[0] + 1];
        for (int i =0; i < binaryNumberArray.Length; i++)
            binaryNumberArray [i] = '0';

        foreach (int i in powersCollected){
            int index = powersCollected [0] - i;
            binaryNumberArray [index] = '1';
        }
        string binaryNumberString = new string(binaryNumberArray);
        return binaryNumberString;
    }

    static void Main(string[] args)
    {
        using (StreamReader reader = File.OpenText(args[0]))
        while (!reader.EndOfStream)
        {
            string line = reader.ReadLine();
            if (null == line)
                continue;
            int number = int.Parse (line.TrimEnd ());
            string binaryRep = ConvertToBinary (number);
            System.Console.WriteLine (binaryRep);
        }
    }
}
