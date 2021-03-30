import java.util.ArrayDeque;
import java.util.HashSet;
import java.util.Hashtable;
import java.util.Set;


public class Graph {
    public boolean isDirected;
    Hashtable<String, Vertex> vertices;

    public Graph(boolean isDirected) {
        this.isDirected = isDirected;
        this.vertices = new Hashtable<String, Vertex>();
    }

    public Graph() {
        this.isDirected = false;
        this.vertices = new Hashtable<String, Vertex>();
    }

    public void addEdge(Vertex v1, Vertex v2) {
        if (v1 != null && v2 != null) {
            // add the vertex and its new neighbor
            if (this.vertices.keySet().contains(v1.getId()) == false) {
                this.addVertex(v1);
            }
            v1.addNeighbor(v2);
            // for undirected graphs, do it in the other direction as well
            if (this.isDirected == false) {
                if (this.vertices.keySet().contains(v2.getId()) == false) {
                    this.addVertex(v2);
                }
                v2.addNeighbor(v1);
            }
        }
    }

    public void addVertex(Vertex v) {
        // add the vertex if not already in the graph
        Set<String> vertices = this.vertices.keySet();

        if (vertices.contains(v.getId()) == false) {
            this.vertices.put(v.getId(), v);
        }
    }

    public void bfsIterative() {
        /* print the id of each Vertex. 
         * Assumes graph is fully-connected, and that cycles are possible 
         */
        // init a queue
        ArrayDeque<Vertex> q = new ArrayDeque<Vertex>();
        HashSet<Vertex> visited = new HashSet<Vertex>();
        // enqueue the first node - put all vertices in an array, get the first
        Vertex first = this.vertices.values().toArray(new Vertex[this.vertices.size()])[0];
        q.addLast(first);
        // TRAVERSE
        while (q.size() > 0) {
            // dequeue a node
            Vertex node = q.removeFirst();
            // visit it
            System.out.println(node);
            visited.add(node);
            // enqueue its neighbors
            for (Vertex neighbor: node.neighbors.values().toArray(new Vertex[node.neighbors.size()])) {
                if (visited.contains(neighbor) == false) {
                    q.addLast(neighbor);
                }
            }
        }
    }

    public static void main(String[] args) {
        // make the graph
        Vertex v1 = new Vertex("a"), v2 = new Vertex("b"), v3 = new Vertex("c");
        Graph g = new Graph();
        g.addEdge(v1, v2);
        g.addEdge(v1, v3);
        g.bfsIterative();
        g.dfsIterative();

        /* 
            v1 = {
                id: "a",
                neighbors: {
                    "b": v2,
                    "c": v3,
                }
            }
            v2 = {
                id: "b",
                neighbors: {
                    "a": v1,
                }
            }
            v3 = {
                id: "c",
                neighbors: {
                    "a": v1,
                }
            }
            g = {
                isDirected: false,
                vertices: {
                    "a": v1,
                    "b": v2, 
                    "c": v3,
                }
            }

            q = []
            visited = {}
            
        */ 
    }

    public void dfsIterative() {
        // A: init collections
        HashSet<Vertex> visited = new HashSet<Vertex>();
        ArrayDeque<Vertex> stack = new ArrayDeque<Vertex>();
        // B: push the first vertex on the stack
        Vertex first = this.vertices.values().toArray(new Vertex[this.vertices.size()])[0];
        stack.addLast(first);
        // C: traverse
        while (stack.size() > 0) {
            // D: pop a node
            Vertex node = stack.removeLast();
            // E: visit it
            System.out.println(node);
            visited.add(node);
            // F: push the unvisited neighbors onto the stack
            Vertex[] neighbors = node.neighbors.values().toArray(new Vertex[node.neighbors.size()]);
            for (Vertex neighbor: neighbors) {
                if (visited.contains(neighbor) == false) {
                    stack.addLast(neighbor);
                }
            }
        }
    }
    
    public void dfsIterativeTwo() {
        /* Prints each vertex. Assumes all vertices are connected, 
         * and cycles possible. 
         */
        // A: init collections
        HashSet<Vertex> visited = new HashSet<Vertex>();
        ArrayDeque<Vertex> stack = new ArrayDeque<Vertex>();
        // B: get the first vertex
        Vertex first = this.vertices.values().toArray(new Vertex[this.vertices.size()])[0];
        stack.addLast(first);
        // C: traverse
        while (stack.size() > 0) {
            // D: pop a node
            Vertex node = stack.removeLast();
            // E: visit it
            System.out.println(node);
            visited.add(node);
            // F: push the neighboring nodes
            Vertex[] neighbors = node.neighbors.values().toArray(new Vertex[node.neighbors.size()]);
            for (Vertex neighbor: neighbors) {
                if (visited.contains(neighbor) == false) {
                    stack.addLast(neighbor);
                }
            }
        }
    }
}

public class Vertex {
    String id;
    Hashtable<String, Vertex> neighbors;

    public Vertex(String id) {
        this.id = id;
        this.neighbors = new Hashtable<String, Vertex>();
    }

    public String getId() {
        return this.id;
    }

    public void addNeighbor(Vertex neighbor) {
        if (neighbor != null) {
            this.neighbors.put(neighbor.getId(), neighbor);
        }
    }

    public String toString() {
        return "Visiting vertex w/ id: " + this.id;
    }
}
