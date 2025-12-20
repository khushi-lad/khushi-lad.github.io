import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.ArrayList;

public class Scrabble {
    private Tile[] tiles;

    public Scrabble() {
        Tile[] tiles = {new Tile(), new Tile(), new Tile(), new Tile(), new Tile(), new Tile(), new Tile()}; // Creates an array called tiles with 7 new Tile objects
    }

    public Scrabble(Tile[] tiles) throws IllegalArgumentException {
        if (tiles.length != 7) {
            throw new IllegalArgumentException(); // If the length of the tiles array is less than 7, throw an IllegalArgumentException
        }
        else {
            this.tiles = tiles; // Otherwise initialize the tiles array
        }
    }

    public String getLetters() {
        String strLetters = ""; // Create an empty String called strLetters
        if (tiles != null) { 
            for (Tile i : tiles) { // Loop through each tile object in the tiles array
                if (i != null) { 
                    strLetters += Character.toString(i.getLetter()); // If the tiles array and the current tile object are not null, get the letter and turn it into a string, and concatenate it to strLetters
                }
            }
        }
        return strLetters; // Then return strLetters
    }

    public ArrayList<String> getWords() throws FileNotFoundException {
        ArrayList<String> spellableWords = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader("CollinsScrabbleWords2019.txt"))) {
            String word; // stores the word that we are currently looking at
            while ((word = br.readLine()) != null) { // loops through each individual word in the CollinsScrabbleWords2019.txt file
                String myLetters = getLetters(); // Set myLetters to the string returned from the getLetters() method
                for (int i = 0; i < word.length(); i++) { // Loop through each letter in the word
                    char c = word.charAt(i); // Get the character at index i in word
                    if (myLetters.contains(Character.toString(c))) { // Turn the character into a string and check if it is in myLetters
                        myLetters = myLetters.replaceFirst(Character.toString(c), ""); // If it is, then remove the string of the character and continue to the next letter
                    }
                }
                if (myLetters.length() == (7 - word.length())) { // If this is true the word is spellable
                    spellableWords.add(word); // Add the word to the spellableWords array list
                    myLetters = getLetters(); // Set myLetters back to the string returned from the getLetters() method
                }
            }
        } catch (IOException e) { // Catch the exception
            e.printStackTrace(); // Print the error message
        }
        return spellableWords; // Return the spellableWords array list
    }

    public int[] getScores() throws FileNotFoundException {
        ArrayList<String> spellableWords = this.getWords();
        int[] wordScores = new int[spellableWords.size()];

        for (String i : spellableWords) { // Loop through each word in spellableWords array list
            int score = 0; // Set score to 0
            for (int j = 0; j < i.length(); j++) { // Loop through each letter in each word
                char c = i.charAt(j); // Get the character at index j in word i
                score += getLetterValue(c); // Add the score of each letter to the score
            }
            wordScores[spellableWords.indexOf(i)] = score; // Set the index of wordScores to the index of word i in the spellableWords array list, then set it equal to the score
        }
        Arrays.sort(wordScores); // Sort the wordScores array
        return wordScores; // Return the wordScores array
    }

    private int getLetterValue(char letter) { // Return the scores for each letter
        if (letter == 'A' || letter == 'E' || letter == 'I' || letter == 'L' || letter == 'N' || letter == 'O' || letter == 'R' || letter == 'S' || letter == 'T' || letter == 'U') {
            return 1;
        } else if (letter == 'D' || letter == 'G') {
            return 2;
        } else if (letter == 'B' || letter == 'C' || letter == 'M' || letter == 'P') {
            return 3;
        } else if (letter == 'F' || letter == 'H' || letter == 'V' || letter == 'W' || letter == 'Y') {
            return 4;
        } else if (letter == 'K') {
            return 5;
        } else if (letter == 'J' || letter == 'X') {
            return 8;
        } else if (letter == 'Q' || letter == 'Z') {
            return 10;
        } else {
            throw new IllegalArgumentException("Invalid Scrabble letter: " + letter);
        }
    }

    public boolean equals(Scrabble s) {
        char[] thisCharArray = this.getLetters().toCharArray(); // Turn the string returned from getLetters() method to a char array and set it to thisCharArray
        char[] otherCharArray = s.getLetters().toCharArray(); // Turn the string returned from getLetters() method to a char array and set it to otherCharArray
        Arrays.sort(thisCharArray); // Sort thisCharArray
        Arrays.sort(otherCharArray); // Sort otherCharArray
        if (Arrays.equals(thisCharArray, otherCharArray)) {
            return true; // If thisCharArray and otherCharArray are equal then return true
        }
        else {
            return false; // Otherwise return false
        }
    }
}
