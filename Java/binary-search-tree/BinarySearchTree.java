import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class BinarySearchTree {
    public TreeNode root;

    public void addNode(int value) {
        root = addRecursive(root, value); // Recursively add the root with the given value
    }

    private TreeNode addRecursive(TreeNode root, int value) {
            if (root == null) {
                root = new TreeNode(value); // If root is null, give the new value to the root
                return root; // Return root
            }
            else if (value < root.value) {
                root.leftChild = addRecursive(root.leftChild, value); // If value is less than root value, recursively go through the left subtree and add the nodes
            }
            else if (value > root.value) {
                root.rightChild = addRecursive(root.rightChild, value); // If value is greater than root value, recursively go through the right subtree and add the nodes
            }
            return root; // Return root
    }

    public int getNodeCount() {
        return countRecursive(root); // Recursively count the nodes
    }

    private int countRecursive(TreeNode root) {
        int total = 0; // Set total to zero
        if (root == null) {
            return 0; // If root is null, return zero
        }
        else {
            total += countRecursive(root.leftChild) + countRecursive(root.rightChild) + 1; // Otherwise, recursively count the nodes of the left subtree and right subtree and add one for the root
            return total; // Return total
        }
    }

    public ArrayList<Integer> bfsTraversal() {
        ArrayList<Integer> numbers = new ArrayList<>(); // Create new integer ArrayList numbers
        Queue<TreeNode> queue = new LinkedList<>(); // Create new TreeNode Queue queue
        queue.add(root); // Add root to queue
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll(); // While queue is not empty, remove the head of the queue and save it to the variable node
            numbers.add(node.value); // Add the value of node to numbers
            if (node.leftChild != null) {
                queue.add(node.leftChild); // If leftChild of node is not null, recursively traverse the left subtree and add the nodes to the queue
            }
            if (node.rightChild != null) {
                queue.add(node.rightChild); // If rightChild of node is not null, recursively traverse the right subtree and add the nodes to the queue
            }
        }
        return numbers; // Return numbers
    }

    public boolean containsNode(int value) {
        if (value == root.value) { 
            return true; // If the value is the root value, return true
        }
        else if (value < root.value) {
            containsNode(root.leftChild.value); // If the value is less than the root value, recursively check the values of the left subtree to check if the value is there
        }
        else if (value > root.value) {
            containsNode(root.rightChild.value); // If the value is greater than the root value, recursively check the values of the right subtree to check if the value is there
        }
        return false; // Otherwise, return false
    }

    public int getHeight() {
        if (root == null) { 
            return -1; // If root is null, return -1
        }
        else {
            int leftHeight = getHeight(); // Get the height of the left subtree
            int rightHeight = getHeight(); // Get the height of the right subtree
            int height = Math.max(leftHeight, rightHeight) + 1; // Find the max height and add one for the root
            return height; // Return height
        }
    }
}
