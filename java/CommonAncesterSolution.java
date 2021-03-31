/* 
 * First Common Ancestor: 
 * 
 * "Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. 
 * Avoid storing additional nodes in a data structure. 
 * 
 * NOTE: This is not necessarily a binary search tree."
 * 
 * Clarifications:
 * 1. So all the nodes in the tree are connected? yes
 * 2. Are the nodes guaranteed to have common ancester? yes (for now)
 * 3. What does "first" mean? 
 *  is it the earliest occuring ancestor, 
 *  or the first that that they share when going up? --- yes
 * 4. Any assumptions we can make about the tree?
 *      - balanced? nope
 *      - complete? nope
 *      - full? nope
 *      - M-way
 * 5. can travel different lengths to go up the tree
 * 6. if no tree - return None
 * 7. ASSUME the node keys are unique (or at least object addresses unqiue)
 * 8. Could one node be descendant of other? - yes, then return grandparent
 * 9. What to return? --a MwayTreeNode
 * 
 * 
 * Example
 *               A  ---> F + G, G + V, F + V
 *           /     \
 *         F        G
 *                 /  \
 *                V    X
 * 
  *             A 
 *          /     \
 *        F        G
 *                /  \
 *               V    X
 * 
 * Intuition:
 *  - given the root of a tree, and 2 nodes in the tree --> find last shared ancestor
 * Approach:
 *  1. Straightforward, use of memory
 *      - traverse down the tree to find the two nodes
 *          - return the list of nodes including everything from root to specific node, no including extras
 *      - traverse back up, 
 *      - when pointers equal, return that node (finding intersection of two linked lists)
 * 
 * 2. 3 pointers
 * 
 * 3. Brute force
 *      - store a list of all nodes I traverse to find node1
 *      - do same for node2
 *      - return last common element in those lists
 * 
 * 4. Subtrees
 *      - DFS the tree
 *          - bool helper function - contains() 
 *              --> if both nodes can be found in the subtrees
 *              -- DFS
 *          - BASE: if not true --> return the parent node
 *          - RECURSIVE - if true --> keep going
 * 
 * 
 */

import java.util.ArrayList;


public class MwayTreeNode {
    ArrayList<MwayTreeNode> children;
    int key;

    public MwayTreeNode(int key) {
        this.key = key;
        this.children = new ArrayList<MwayTreeNode>();
    }
}

public class MwayTree {
    MwayTreeNode root;

    public MwayTree(){ 
        this.root = null;
    }

    public setRoot(MwayTreeNode root) {
        this.root = root;
    }

    public MwayTreeNode getRoot() {
        return this.root;
    }

    public boolean isParent(MwayTreeNode otherNode) {
        // make sure this isn't the otherNode - FALSE
        if (this == otherNode) {
            return false;
        } 
        else {
            // recurisively check all subtrees
            boolean found = false;
            for (MwayTreeNode child: this.children) {
                // see if it can be true
                found = child.isParentRecursive(otherNode);
                if (found == true) break;  // end early
            }
            // return the answer
            return found;
        }
    }
    
    public boolean isParentRecursive(MwayTreeNode otherNode) {
        // check if otherNode found 
        if (this == otherNode) {
            return true;
        }
        // recursively check all the subtrees
        for (MwayTreeNode child : this.children) {
            // see if it can be true
            return child.isParentRecursive(otherNode);
        }
        // reached a leaf, never found the otherNode
        return false;
    }
}


public class CommonAncestorSolution {

    public static MwayTreeNode findCommonAncestor(MwayTreeNode parent, MwayTreeNode node, 
                                                  MwayTreeNode node1, MwayTreeNode node2) {
        // A: calculate if the node is parent of both node and node 2
        boolean isAncestor = node.isParent(node1) && node.isParent(node2);
        // B: BASE: if false
        if (isAncestor == false) {
            return parent;
        }
        // C: RECURSE: for each children, call the same func
        for (MwayTreeNode child : node.children) {
            return findCommonAncestor(node, child, node1, node2);
        }

    }

    public static MwayTreeNode findCommonAncestor(MwayTree tree, MwayTreeNode node1, MwayTreeNode node2) {
        MwayTreeNode ancestor = null;
        // validate input
        if (tree != null && tree.root != null) {
            // A: see if the root contains both nodes in its subtrees
            if (tree.root.isParent(node1) && tree.root.isParent(node2)) {
                // RECURSIVE case: if true, then continue the search
                for (MwayTreeNode child : tree.root.children) {
                    ancestor = findCommonAncestor(tree.root, child, node1, node2);
                }
            }
        }
        return ancestor;
    }
}