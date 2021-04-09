/* 
 * Given an m x n 2D binary grid grid which 
 * represents a map of '1's (land) and '0's (water), return the number of islands.
 * An island is surrounded by water and is formed by 
 * connecting adjacent lands horizontally or vertically. 
 * 
 * You may assume all four edges of the grid are all surrounded by water.
 * 
 * Clarifications:
 * 1. guaranteed to have at least 1 element 
 * 2. rectangular island
 * 3. input is mutable
 * 4. diagonal connections don't count
 * 
 * Example: 
 * Input: grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
   ]
 * Output: 1
 */

import java.util.ArrayList;


class NumberoOfIslands {
    public static int solution(String[][] grid) {
        // A: init ouput
        int islands = 0;
        // B: validate input
        if (grid != null && grid[0].length > 0) {
            // C: define the 4 directions
            final int[][] DIRECTIONS = {
                {-1, 0}, // up
                {1, 0}, // down
                {0, -1}, // left
                {0, 1}  // right
            };
            // D: init a stack
            ArrayList<int[]> stack = new ArrayList<int[]>();
            // E: traverse the grid
            for (int rowIndex = 0; rowIndex < grid.length; rowIndex++) {
                String[] row = grid[rowIndex];
                for (int colIndex = 0; colIndex < row.length; colIndex++) {
                    String element = row[colIndex];
                    // F: island found
                    if (element.equals("1")) {
                        // G: traverse the island
                        int[] firstCoordinates = {rowIndex, colIndex};
                        stack.add(firstCoordinates);
                        while (stack.size() > 0) {
                            // get the piece of land
                            int[] coordinates = stack.remove(stack.size() - 1);
                            // mark it as visited
                            int landRow = coordinates[0], landCol = coordinates[1];
                            grid[landRow][landCol] = "0";
                            // traverse the neighbor land spaces
                            for (int[] directionVector: DIRECTIONS) {
                                int neighborRow = landRow + directionVector[0];
                                int neighborCol = landCol + directionVector[1];
                                // avoid out of bounds errors
                                if (neighborRow < grid.length && neighborRow > -1) {
                                    if (neighborCol > -1 && neighborCol < grid[0].length) {
                                        // pushing neighboring land onto the stack
                                        String neighbor = grid[neighborRow][neighborCol];
                                        if (neighbor.equals("1")) {
                                            int[] neighborCoordinates = { neighborRow, neighborCol };
                                            stack.add(neighborCoordinates);
                                        }
                                    }
                                }

                            }
                        }
                        // H: increment number of islands
                        islands += 1;
                    }
                }
            }
        }
        return islands;
    }

    public static void main(String[] args) {
        String[][] grid = {
            {"1","1","1","1","0"},
            {"1","1","0","1","0"},
            {"1","1","0","0","0"},
            {"0","0","0","0","0"}
        };
        System.out.println(solution(grid));
    }
}