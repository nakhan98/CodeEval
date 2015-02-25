/* CodeEval - Minimum Coins
 * https://www.codeeval.com/browse/74/
 */

using System.IO;
using System.Collections.Generic;

class Program
{

    static int[] coins = new int[3]{5,3,1};

    static List<int> CalcNumbCoins(int amount)
    {
        List<int> coinsToReturn = new List<int>();
        foreach (int coin in coins)
        {
            float quotient = amount / (float)coin;
            if (quotient >= 1)
            {
                int numberOfCoins = (int)quotient;
                for (int i=0; i < numberOfCoins; i++)
                    coinsToReturn.Add(coin);
                amount -= numberOfCoins * coin;
            }

            if (amount == 0)
                return coinsToReturn;
        }
        return coinsToReturn;
    }

    static void Main(string[] args)
    {
        using (StreamReader reader = File.OpenText(args[0]))
        while (!reader.EndOfStream)
        {
            string line = reader.ReadLine();
            if (null == line)
                continue;

            int amount = int.Parse(line.Trim());
            List<int> numberCoins = CalcNumbCoins(amount);
            System.Console.WriteLine(numberCoins.Count);
        }
    }
}
