import java.util.ArrayList;
import java.util.Collections;

public class BinarySearchTreeCollection {
    private ArrayList<BinarySearchTree> trees;

    public BinarySearchTreeCollection() {
        this.trees = new ArrayList<>(); // Initialize BinarySearchTree ArrayList trees
    }

    public void addTree(BinarySearchTree tree) {
        trees.add(tree); // Add tree to trees ArrayList
    }

    public BinarySearchTree getTree(int index) throws IllegalArgumentException {
        if (index < 0) {
            throw new IllegalArgumentException("Invalid argument!"); // If index is less than 0, throw IllegalArgumentException
        }
        else if (index >= trees.size()) {
            throw new IllegalArgumentException("Invalid argument!"); // If index is greater than or equal to the size of trees, throw IllegalArgumentException
        }
        else {
            BinarySearchTree tree = trees.get(index); // Use the index to find the tree
            return tree; // Return the tree
        }
    }

    public void deleteTree(int index) {
        if (index < 0) {
            throw new IllegalArgumentException("Invalid argument!"); // If index is less than 0, throw IllegalArgumentException
        }
        else if (index >= trees.size()) {
            throw new IllegalArgumentException("Invalid argument!"); // If index is greater than or equal to the size of trees, throw IllegalArgumentException
        }
        else {
            trees.remove(index); // Use the index to find the tree and remove it from trees
        }
    }

    public int getNumberOfTrees() {
        int size = trees.size(); // Get the size of trees
        return size; // Return the size
    }

    public boolean areStructurallyEquivalent(int[] indices) throws IllegalArgumentException {
        if (indices.length < 2) {
            throw new IllegalArgumentException("Invalid argument!"); // If length of indices is less than 2, throw IllegalArgumentException
        }
        for (int i = 0; i < indices.length; i++) {
            if (indices[i] < 0) {
                throw new IllegalArgumentException("Invalid argument!"); // For each element in indices, if the element is less than 0, throw IllegalArgumentException
            }
            else if (indices[i] > trees.size() - 1) {
                throw new IllegalArgumentException("Invalid argument!"); // For each element in indices, if the element is greater than or equal to the size of trees, throw IllegalArgumentException
            }
        }
        for (int j = 0; j < indices.length - 1; j++) {
            BinarySearchTree tree1 = getTree(indices[j]); // Get the tree at the first index of indices
            BinarySearchTree tree2 = getTree(indices[j+1]); // Get the tree at the next index of indices
            if (!((tree1.getNodeCount()) == (tree2.getNodeCount())) && ((tree1.bfsTraversal()) == (tree2.bfsTraversal())) && ((tree1.getHeight()) == (tree2.getHeight()))) {
                return false; // If the node count, bfsTraversal, and height of the first tree and second tree are all not equal, then return false
            }
        }
        return true; // Otherwise, return true
    }

    public void merge(int[] indices) throws IllegalArgumentException {
        if (indices.length < 2) {
            throw new IllegalArgumentException("Invalid argument!"); // If length of indices is less than 2, throw IllegalArgumentException
        }
        for (int i = 0; i < indices.length; i++) {
            if (indices[i] < 0) {
                throw new IllegalArgumentException("Invalid argument!"); // For each element in indices, if the element is less than 0, throw IllegalArgumentException
            }
            else if (indices[i] > trees.size() - 1) {
                throw new IllegalArgumentException("Invalid argument!"); // For each element in indices, if the element is greater than or equal to the size of trees, throw IllegalArgumentException
            }
        }
        ArrayList<Integer> values = new ArrayList<>(); // Create a new integer ArrayList values
        for (int i : indices) {
            BinarySearchTree tree = trees.get(i); // For each element in indices, get the tree at that index from trees
            collectValues(tree.root, values); // Collect the values from that tree
        }
        Collections.sort(values); // Sort the values
        ArrayList<Integer> unique = new ArrayList<>(); // Crete a new integer ArrayList unique
        if (!values.isEmpty()) {
                unique.add(values.get(0)); // If values is not empty, add the first value to unique
            }
        for (int i = 1; i < values.size(); i++) {
            if ((values.get(i) != null) && (!values.get(i).equals(values.get(i-1)))) { // For each value in values, if the value is not null and the first value and next value are not the same
                unique.add(values.get(i)); // Get the value at that index and add it to unique
            }
        }
        for (int i = indices.length - 1; i >= 0; i--) {
            trees.remove(indices[i]); // For each element in indices, remove it from trees
        }
        BinarySearchTree merged = new BinarySearchTree(); // Create a new BinarySearchTree called merged
        for (int i : unique) {
            merged.addNode(i); // For each element in unique, add it to merged
        }
        trees.add(merged); // Add merged to trees
    }

    private void collectValues(TreeNode root, ArrayList<Integer> values) {
        if (root != null) {
            collectValues(root.leftChild, values); // If root is not null, recursively collect values from the left subtree
            values.add(root.value); // Add the root value to values
            collectValues(root.rightChild, values); // Recursively collect values from the right subtree
        }
    }

    public int getTotalNodes() {
        int total = 0; // Set total to zero
        for (BinarySearchTree i : trees) {
            total += i.getNodeCount(); // For each tree in trees, count the nodes and add it to the total
        }
        return total; // Return total
    }
}
