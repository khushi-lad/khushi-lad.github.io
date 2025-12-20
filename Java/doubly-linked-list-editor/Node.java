public class Node {
    public int value;
    public Node next;
    public Node prev;

    public Node(int value) {
        this.value = value; // Set value to given value parameter
        this.next = null; // Set next pointer to null
        this.prev = null; // Set prev pointer to null
    }
}
