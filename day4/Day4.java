import java.io.File; // Import the File class
import java.io.FileNotFoundException; // Import this class to handle errors
import java.util.ArrayList;
import java.util.Scanner; // Import the Scanner class to read text files

public class Day4 {
    public static void main(String[] args) {
        ArrayList<String> lines = new ArrayList<String>();
        try {
            File myObj = new File("input.txt");
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                lines.add(data);
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }

        // start here
        int numberOfFullOverlaped = 0;
        int numberOfOverlaped = 0;
        for (String line : lines) {
            String[] pairStrings = line.split(",");
            ArrayList<Pair> pairs = new ArrayList<>();
            for (String data : pairStrings) {
                pairs.add(new Pair(data));
            }

            if (pairs.get(0).fullOverlaps(pairs.get(1)))
                numberOfFullOverlaped++;
            else if (pairs.get(1).fullOverlaps(pairs.get(0)))
                numberOfFullOverlaped++;
            
            if (pairs.get(0).overlaps(pairs.get(1)))
                numberOfOverlaped++;
            else if (pairs.get(1).overlaps(pairs.get(0)))
                numberOfOverlaped++;
        }
        
        System.out.println("Number of full overlaps is " + numberOfFullOverlaped);
        System.out.println("Number of overlaps is " + numberOfOverlaped);

    }
}