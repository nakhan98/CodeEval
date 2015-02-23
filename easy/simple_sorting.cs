/* CodeEval - Simple Sorting
 * https://www.codeeval.com/open_challenges/91/
 */

using System.IO;
using System.Collections.Generic;

class Program
{
    static void Main(string[] args)
    {
        using (StreamReader reader = File.OpenText(args[0]))
        while (!reader.EndOfStream)
        {
            string line = reader.ReadLine();
            if (null == line)
                continue;

            line = line.Trim();
            string[] float_strings = line.Split(' ');
            List<float> floats = new List<float>();

            foreach (string float_string in float_strings)
            {
                float fl = System.Convert.ToSingle(float_string);
                //System.Console.Out.WriteLine(fl);
                floats.Add(fl);
            }

            floats.Sort();

            foreach (float fl in floats) 
            {
                System.Console.Write(fl.ToString("N3") + " ");
            }
            System.Console.Write("\n");
        }
    }
}
