/* CodeEval - Overlapping Rectangles
 * https://www.codeeval.com/open_challenges/70/
 */

using System.IO;
using System.Collections.Generic;

class Program
{
    static List<int[]> GetCoordinates(string p1X, string p1Y, string p2X, string p2Y)
    {
        List<int[]> rectangleCoords = new List<int[]>
        {
            new int[]{ int.Parse(p1X), int.Parse(p1Y) }, 
            new int[]{ int.Parse(p2X), int.Parse(p1Y) },
            new int[]{ int.Parse(p2X), int.Parse(p2Y) },
            new int[]{ int.Parse(p1X), int.Parse(p2Y) },
        };
        return rectangleCoords;
    }

    static bool RectanglesOverlap(List<int[]> r1, List<int[]> r2)
    {
        List<int[]> pointsOfInterest = new List<int[]>();
        foreach (int[] i in r1)
            foreach (int[] j in r2)
                if (i[0] >= j[0] && i[1] >= j[1])
                   pointsOfInterest.Add(i);
        if (pointsOfInterest.Count > 0)
            foreach (int[] i in pointsOfInterest)
                foreach (int[] j in r2)
                    if (i[0] <= j[0] && i[1] <= j[1])
                        return true;                

        pointsOfInterest.Clear();
        foreach (int[] i in r2)
            foreach (int[] j in r1)
                if (i[0] >= j[0] && i[1] >= j[1])
                   pointsOfInterest.Add(i);
        if (pointsOfInterest.Count > 0)
            foreach (int[] i in pointsOfInterest)
                foreach (int[] j in r1)
                    if (i[0] <= j[0] && i[1] <= j[1])
                        return true;                

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
            string[] points = line.Trim().Split(',');
            List<int[]> r1 = GetCoordinates(points[0], points[1], points[2], points[3]);
            List<int[]> r2 = GetCoordinates(points[4], points[5], points[6], points[7]);
            if (RectanglesOverlap(r1, r2))
                System.Console.WriteLine("True");
            else
                System.Console.WriteLine("False");
        }
    }
}
