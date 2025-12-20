import java.util.ArrayList;

public class MazeSolver {
    public static boolean solveMaze(char[][] maze, int row, int col, ArrayList<String> path, MazeVisualizer visualizer) {
        // Your solution here
        if (maze[row][col] == 'E') {
            return true; // Return true if at the end of the maze
        }
        else if ((maze[row][col] == '#') || (maze[row][col] == '+') || (row < 0) || (row >= maze.length) || (col < 0) || (col >= maze[0].length)) {
            return false; // Return false if the maze element is a wall, previously visited, or out of bounds
        }
        else {
            maze[row][col] = '+'; // Vist the tile
            visualizer.repaint();
            try {
                Thread.sleep(100);
            }
            catch (InterruptedException e) { // Catch InterruptedExceptions
                e.printStackTrace();
            }
            if (solveMaze(maze, row, col+1, path, visualizer) == true) { // Try to move right
                path.add("right"); // If true, add right to path
                return true; // Return true
            } 
            else if (solveMaze(maze, row, col-1, path, visualizer) == true) { // Try to move left
                path.add("left"); // If true, add left to path
                return true; // Return true
            }
            else if (solveMaze(maze, row-1, col, path, visualizer) == true) { // Try to move up
                path.add("up"); // If true, add up to path
                return true; // Return true
            }
            else if (solveMaze(maze, row+1, col, path, visualizer) == true) { // Try to move down
                path.add("down"); // If true, add down to path
                return true; // Return true
            }
            else {
                maze[row][col] = ' '; // Otherwise, unvisit the tile
                visualizer.repaint();
                try {
                    Thread.sleep(100);
                }
                catch (InterruptedException e) { // Catch InterruptedExceptions
                    e.printStackTrace();
                }
                return false; // Return false
            }
        }
    }

    public static void main(String[] args) {
        Maze maze = new Maze("maze3.txt"); // to change the maze you're solving, change this filename (maze1.txt, maze2.txt, maze3.txt, maze4.txt, or maze5.txt)
        maze.printMaze();

        ArrayList<String> path = new ArrayList<>();

        // create a frame to display the maze
        MazeVisualizer visualizer = new MazeVisualizer(maze.getMaze(), path);
        visualizer.display();

        if (solveMaze(maze.getMaze(), maze.getStartRow(), maze.getStartCol(), path, visualizer)) {
            System.out.println("Maze solved:");
            for (int i = path.size() - 1; i >= 0; i--) {
                System.out.println(path.get(i));
            }
        } else {
            System.out.println("No solution found for the maze.");
        }
    }
}
