/*
 * Hacker Rank problem found on: 
 * https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
 * 
 * Assumptions:
 * each index in the array contains 1 and only one element
 * things that don't matter in this problem: what data is in the array (is it sorted, are there duplicates, etc.)
 * 
 * Test Input: 
 * int d = 4; // number of rotations to perform)
 * int[] arr = { 1, 2, 3, 4, 5 }; // the array that is being rotated
 * 
 * Expected Output:
 * arr = [ 5, 1, 2, 3, 4 ]
 * 
 * What I notice about the problem:
 * as described in the problem, all a left rotation describes is an operation in which:
 *      each element in the array shifts over one index position
 *      when an element reaches the first index position, it moves over into the end index position
 * 
 * Brainstorming solutions:
 *      1. Iteration from right to left - O(n * d)
 *          A: for as many as d passes:
 *              B: start from the end of the array
 *             C:  using a temp variable, we copy over the value from each array index, into the index
 *                  that is left of it
 *              D: when we reach the first index, we copy over the value into the greatest index position
 *      2. Negative Indexing - O(n)
 *        A:  iterate over the arr
 *             B: calculate the change in each element's index - it will equal the difference between 
 *                  arr.length and d
 *             C: if the change is positive, keep a refernce to the element that is 1 left of the currElement (starting at 0)
 *                if the change is negative, keep a refernce to the element that is 1 right of the currElement (starting at 0)
 *             D: on each iteration:
 *                  calculate the newIndex for both the index being iterated on, as well as its neighbor
 *                  store the value currently being stored in the newIndex of the iterated over index, in a temp variable
 *                  move over the item at the index being iterated over, then its neighbor
 *        E: return the new array
 *              arr             neighborIndex          currentIndex  
 *          [1, 2, 3, 4, 5]         4                       0
 *          []
 *          
 * /

