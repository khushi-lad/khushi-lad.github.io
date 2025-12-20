public class DoublyLinkedList {
    private Node head;
    private Node tail;

    public void add(int value) {
        Node newNode = new Node(value); // Create new Node object called newNode
        if (head == null) {
            head = newNode; // If list is empty, set head to newNode
            tail = newNode; // If list is empty, set tail to newNode
        }
        else {
            tail.next = newNode; // Otherwise, set next of tail to newNode
            newNode.prev = tail; // Set prev of newNode to tail
            tail = newNode; // Update tail to newNode
        }
    }

    public boolean remove(int value) {
        Node current = head; // Set current to head
        while (current != null) {
            if (current.value == value) { // Check if the value is the same
                if (current == head) {
                    head = current.next; // If current is head, set head to the next of current
                    if (head != null) {
                        head.prev = null; // If head is not null, set prev of head to null
                    }
                }
                else if (current == tail) {
                    tail = current.prev; // If current is tail, set tail to the prev of current
                    if (tail != null) {
                        tail.next = null; // If tail is not null, set next of tail of null
                    }
                }
                else {
                    current.next.prev = current.prev; // If current is in the middle, set the prev of current.next to prev of current
                    current.prev.next = current.next; // Set the next of current.prev to next of current
                }
                return true; // Value was found and removed so return true
            }
            current = current.next; // Update current to the next of current
        }
        return false; // Value was not found so return false
    }

    public void reverse() {
        Node current = head; // Set current to head
        Node temp = null; // Set temp to null
        while (current != null) {
            temp = current.prev; // If current is not null, set temp to prev of current
            current.prev = current.next; // Set prev of current to next of current
            current.next = temp; // Set next of current to temp
            current = current.prev; // Set current to prev of current
        }
        if (temp != null) {
            head = temp.prev; // If temp is not null, set head to prev of temp
        }
    }

    public void print() {
        Node current = head; // Set current to head
        while (current != null) {
            System.out.println(current.value + " "); // If current is not null, print the value of current
            current = current.next; // Set current to the next of current
        }
        System.out.println();
    }

    public void deleteList() {
        head = null; // Set head to null
        tail = null; // Set tail to null
    }

    // helper method to print to a StringBuilder (for testing purposes) 
    public void printToString(StringBuilder sb) { 
        Node current = head; // Set current to head
        while (current != null) { 
            sb.append(current.value).append(" ");  // If current is not null, append the value to StringBuilder object
            current = current.next; // Set current to the next of current
        } 
    }
}
