package graph_problems;

public class MinimalTree {
    /* Problem: Given a sorted (increasing order) array with unique integer elements, 
     * write an algorithm to create a binary search tree with minimal height.
     * 
     * [-6, 0, 3, 5, 23, 54]
     * Return the root of the new tree.
     */

    public class Node {
        // declare class attributes
        int key;
        Node left;
        Node right;

        // constructor - children are initialized to null values
        public Node(int key) {
            this.key = key;
            this.left = null;
            this.right = null;
        }

        public void setLeft(Node leftChild) {
            this.left = leftChild;
        }

        public void setRight(Node rightChild) {
            this.right = rightChild;
        }
    }

    // declare the class attributes on the Tree
    Node root;
    int[] numbers;

    public MinimalTree(int[] numbers) {
        this.root = null;
        this.numbers = numbers;
    }

    // solution to the problem
    public Node populateTree() {
        // calculate the middle index
        return this.root;
    }
}
