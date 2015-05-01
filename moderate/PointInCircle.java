/* CodeEval: Point in a Circle
 * https://www.codeeval.com/open_challenges/98/submit/
 */

import java.io.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.lang.Math;


public class PointInCircle {

    static CirclePoint extractData(String line){
        // regex - Center: \(([\d\-\.]+), ([\d\-\.]+)\); Radius: ([\d\-\.]+); Point: \(([\d\-\.]+), ([\d\-\.]+)\)
        String pattern = "Center: \\(([\\d\\-\\.]+), ([\\d\\-\\.]+)\\); Radius: ([\\d\\-\\.]+);" + 
           " Point: \\(([\\d\\-\\.]+), ([\\d\\-\\.]+)\\)";
        Pattern r = Pattern.compile(pattern);
        Matcher m = r.matcher(line);
        if (m.find()) {
            double[] center = { Double.parseDouble(m.group(1)), Double.parseDouble(m.group(2)) };
            double radius = Double.parseDouble(m.group(3));
            double[] point = { Double.parseDouble(m.group(4)), Double.parseDouble(m.group(5)) };
            CirclePoint p = new CirclePoint(center, radius, point);
            return p;
        }
        throw new RuntimeException("Could not parse line");
    }

    public static void main (String[] args) throws IOException {
        File file = new File(args[0]);
        BufferedReader buffer = new BufferedReader(new FileReader(file));
        String line;
        while ((line = buffer.readLine()) != null) {
            line = line.trim();
            // Process line of input Here
            CirclePoint p = extractData(line);
            if (p.isPointInCircle())
                System.out.println("true");
            else
                System.out.println("false");
        }
    }
}

class CirclePoint {
    private double[] center;
    private double[] point;
    private double radius;

    CirclePoint(double[] c, double r, double[] p){
        center = c;    
        radius = r;
        point = p;
    }

    boolean isPointInCircle(){
        double diffX = point[0] - center[0];
        double diffY = point[1] - center[1];
        double dist_squared = Math.pow(diffX, 2) + Math.pow(diffY, 2);
        double dist = Math.sqrt(dist_squared);
        if (dist < radius)
            return true;
        else
            return false;
    }
}
