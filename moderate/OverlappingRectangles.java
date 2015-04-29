/* 
 * - CodeEval: Overlapping Triangles
 * - https://www.codeeval.com/open_challenges/70/
 */

import java.io.*;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;

public class OverlappingRectangles {

    static boolean rectanglesOverlap(Rectangle r1, Rectangle r2){
        // Check if any points in rectangle 1 fall in 2
        List<int[]> pointsOfInterest = new ArrayList<int[]>();
        for (int[] i : r1.getPoints())
            for (int[] j : r2.getPoints())
                if (i[0] >= j[0] && i[1] >= j[1])
                    pointsOfInterest.add(i);                    

        if (!pointsOfInterest.isEmpty())
            for (int[] i : pointsOfInterest)
                for (int[] j : r2.getPoints())
                    if (i[0] <= j[0] && i[1] <= j[1])
                        return true;

        // Check if any points in rectangle 2 fall in 1
        //List<int[]> pointsOfInterest = new ArrayList<int[]>();
        pointsOfInterest.clear();
        for (int[] i : r2.getPoints())
            for (int[] j : r1.getPoints())
                if (i[0] >= j[0] && i[1] >= j[1])
                    pointsOfInterest.add(i);                    

        if (!pointsOfInterest.isEmpty())
            for (int[] i : pointsOfInterest)
                for (int[] j : r1.getPoints())
                    if (i[0] <= j[0] && i[1] <= j[1])
                        return true;
        
        return false;
    } 

    public static void main (String[] args) throws IOException {
        File file = new File(args[0]);
        BufferedReader buffer = new BufferedReader(new FileReader(file));
        String line;
        while ((line = buffer.readLine()) != null) {
            line = line.trim();
            // Process line of input Here
            String[] points = line.split(",");
            Rectangle r1 = new Rectangle(points[0], points[1], points[2], points[3]);
            Rectangle r2 = new Rectangle(points[4], points[5], points[6], points[7]);
            //System.out.println( String.format("Rectangle two, point a: %d, %d", r2.getPoints()[0][0], r2.getPoints()[0][1]) );
            if (rectanglesOverlap(r1, r2))
                System.out.println("True");
            else
                System.out.println("False");
        }
    }
}

class Rectangle {
    int[] a;
    int[] b;
    int[] c;
    int[] d;
    int[][] points = new int[4][];

    Rectangle(String p1X, String p1Y, String p2X, String p2Y){
        int aX = Integer.parseInt(p1X);
        int aY = Integer.parseInt(p1Y);
        int bX = Integer.parseInt(p2X);
        int bY = Integer.parseInt(p2Y);

        a = new int[] {aX, aY};
        b = new int[] {bX, aY};
        c = new int[] {bX, bY};
        d = new int[] {aX, bY};

        points[0] = a.clone();
        points[1] = b.clone();
        points[2] = c.clone();
        points[3] = d.clone();
    }

    int[][] getPoints(){
        return points;
    }
}

    
