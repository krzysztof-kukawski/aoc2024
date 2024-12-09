import java.util.ArrayList;


public class Main {
    public static void main(String[] args) throws Exception {
        Guard guard = new Guard();
        guard.move();
        ArrayList<String> newMap = new ArrayList<>(guard.map);
        int c = 0;
        for (int row = 0; row < guard.map.size(); row++) {
            for (int col = 0; col < guard.map.get(row).length(); col++) {
                int[] proposedObst = {row, col};
                if (Guard.isInArrayList(guard.visited, proposedObst)) {
                    String firstPart = newMap.get(row).substring(0, col);
                    String secondPart = newMap.get(row).substring(col + 1);
                    String newRow = firstPart + "#" + secondPart;
                    newMap.set(row, newRow);
                    Guard newGuard = new Guard();
                    newGuard.map = new ArrayList<>(newMap);
                    try {
                        newGuard.move();

                    } catch (Exception e) {
                        c++;
                    }
                    newMap = new ArrayList<>(guard.map);
                }

            }
        }
        System.out.println("Part 1: " + guard.visited.size());
        System.out.println("Part 2: " + c);
    }

}

