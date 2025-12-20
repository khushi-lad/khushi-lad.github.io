import java.util.Random;

public class Tile {
    private char letter;

    public Tile() {
        letter = generateLetter(); // Sets letter to be a random letter
    }

    public Tile(char c) {
        this.letter = c; // Initializes letter to be equal to c
    }

    private char generateLetter() {
        Random random = new Random();
        // the ASCII value of ‘A’ is 65 and ‘Z’ is 90
        return (char) (random.nextInt(26) + 'A'); // Randomly generates a number, bounding it so it does not go beyond A to Z, and casting it to char type
    }

    public char getLetter() {
        return letter; // Returns the letter
    }
}