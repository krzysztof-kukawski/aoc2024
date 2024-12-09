import java.io.File;
import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Guard {
    int row;
    int column;
    int[] start;
    ArrayList<int[][]> path = new ArrayList<>();
    ArrayList<int[]> visited = new ArrayList<>();
    ArrayList<String> map = new ArrayList<>();
    int[] direction = {-1, 0};
    int[][] order = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};


    public Guard() throws FileNotFoundException {
        readFile();
        this.start = findStart();
        this.row = this.start[0];
        this.column = this.start[1];

    }

    public static boolean isInArrayList(ArrayList<int[]> listOfItems, int[] item) {
        for (int[] i : listOfItems) {
            if (Arrays.equals(i, item)) {
                return true;
            }
        }
        return false;
    }

    public void move() throws Exception {
        int maxIndex = this.order.length;
        int c = 0;
        try {
            while (true) {
                if (c > maxIndex) {
                    c = 0;
                }
                if (!step()) {
                    this.direction = this.order[c];
                    c++;

                }
            }
        } catch (IndexOutOfBoundsException e) {
            System.out.println(this.visited.size());
        }
    }

    private int[] findStart() {
        for (int i = 0; i < this.map.size(); i++) {
            String line = this.map.get(i);
            for (int j = 0; j < line.length(); j++) {
                String letter = line.substring(j, j + 1);
                if (letter.equals("^")) {
                    return new int[]{i, j};
                }
            }
        }
        return new int[0];
    }

    public void readFile() throws FileNotFoundException {
        Path workingDir = Paths.get(System.getProperty("user.dir"));
        Path fileDir = Paths.get(workingDir.toString(), "java", "day6", "puzzle_input_day6");
        File puzzleFile = new File(fileDir.toString());
        Scanner puzzleReader = new Scanner(puzzleFile);
        while (puzzleReader.hasNext()) {
            this.map.add(puzzleReader.next());
        }
        puzzleReader.close();
    }

    public boolean step() throws Exception {
        this.row += this.direction[0];
        this.column += this.direction[1];
        String currentRow = this.map.get(this.row);
        String currentSpot = currentRow.substring(this.column, this.column + 1);
        int[] currentLocation = {this.row, this.column};
        if (currentSpot.equals("#")) {
            this.row -= this.direction[0];
            this.column -= this.direction[1];
            return false;
        } else {
            if (!isInArrayList(this.visited, currentLocation)) {
                this.visited.add(currentLocation);

            }
            addTrace();

            return true;
        }
    }

    private void addTrace() throws Exception {
        int[][] trace = {{this.row, this.column}, this.direction};

        for (int[][] i : this.path) {
            if (Arrays.deepEquals(i, trace)) {
                throw new Exception("infinite loop");
            }
        }

        this.path.add(trace);
    }

}
