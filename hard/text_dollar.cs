/* CodeEval - Text Dollar
 * https://www.codeeval.com/open_challenges/52/
 */

using System.IO;
using System.Text;
using System.Collections.Generic;

class Program
{
    static string[] singleDigits = new string[]{"", "One", "Two", "Three", "Four", "Five", 
        "Six", "Seven", "Eight", "Nine"};
    static string[] teens = new string[]{"Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
        "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"};
    static string[] doubleDigits = {"", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty",
        "Seventy", "Eighty", "Ninety"};

    // Convert 3 digit numbers to English equivelant
    static string ConvertNumber(string numberString)
    {
        numberString = numberString.PadLeft(3, '0');
        StringBuilder number = new StringBuilder();
        if (numberString[0] != '0')
        {
            int hundreds = int.Parse(numberString[0].ToString());
            string hundredsString = singleDigits[hundreds] + "Hundred";
            number.Append(hundredsString);
        }

        if (numberString[1] == '0')
        {
            int index = int.Parse(numberString[2].ToString());
            string singleDigit = singleDigits[index];
            number.Append(singleDigit);
        }
        else if (numberString[1] == '1')
        {
            int index = int.Parse(numberString[2].ToString());
            string teen = teens[index];
            number.Append(teen);
        }
        else 
        {
            string secondDigit = doubleDigits[ int.Parse(numberString[1].ToString()) ];
            string thirdDigit = singleDigits[ int.Parse(numberString[2].ToString()) ];
            number.Append(secondDigit);
            number.Append(thirdDigit);
        }
        return number.ToString();
    }

    static string TextNumber(string numberString)
    {
        numberString = numberString.PadLeft(9, '0');
        StringBuilder number = new StringBuilder();
        if (int.Parse(numberString.Substring(0,3)) != 0 )
        {
            string millionsString = ConvertNumber(numberString.Substring(0,3)) + "Million";
            number.Append(millionsString);
        }

        if (int.Parse(numberString.Substring(3,3)) != 0)
        {
            string thousands = ConvertNumber(numberString.Substring(3,3)) + "Thousand";
            number.Append(thousands);
        }

        if (int.Parse(numberString.Substring(6,3)) != 0)
        {
            string hundreds = ConvertNumber(numberString.Substring(6,3));
            number.Append(hundreds);
        }
        return number.ToString();
    }

    static void Main(string[] args)
    {
        using (StreamReader reader = File.OpenText(args[0]))
        while (!reader.EndOfStream)
        {
            string line = reader.ReadLine();
            if (null == line)
                continue;
            string numberString = line.Trim();
            string dollars = TextNumber(numberString);
            System.Console.WriteLine(dollars + "Dollars");
        }
    }
}

