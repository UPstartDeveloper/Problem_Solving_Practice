/* 
 * Is Unique: Implement an algorithm to determine if a string has all unique characters. 
 * What if you cannot use additional data structures?
 * 
 * "abc" ---> True
 * "aaa" --> False
 * 
 * Assume no spaces in the string
 * the function is case sensitive 
 * is the string mutable? yes
 * 
 * Idea 1:
 * iterate over the string
 *      keep a running tally of how many times each individual char appears
 * iterate over all types of chars
 *      if any char has > 1 token (appearances) --> return False
 * return True
 * 
 * linear time and space ---> but what if we can't use the additional space?
 * 
 * Idea 2: trade space for more time
 * keep track of the letter seen, and see if it appears again
 *    v
 * "abc"
 *    ^
 * 
 * abdecb
 * 
 * Idea 3: Use a HashSet:
 * make a set of all the chars in the string
 * return T/F if lengths differ
 * linear time and space
 * 
 * Idea 4: Sorting
 * sort the chars in the string lexicogrpahically 
 * linear pass over the string, see if any adj chars match
 * am I allowed to use the built-in sort function
 * linearithmic time, more chars, and linear space
 * 
 */
import java.util.Arrays;

public class UniqueString {
    public static boolean isUnique(String str) {
        // 1: iterate over the string's chars
        for (int charIndex = 0; charIndex  < str.length(); charIndex  += 1) {
            // a): for each char, check every other char
            char currentChar = str.charAt(charIndex);
            for (int otherIndex = 0; otherIndex < str.length(); otherIndex += 1) {
                char otherChar = str.charAt(otherIndex);
                // b): if there's a duplicate char, the string's not unique
                if (currentChar == otherChar && charIndex != otherIndex) {
                    return false;
                }
            }
        }
        // 2: otherwise, the string's unique
        return true;
    }


    public static boolean isUnique2(String str) {
        // 1: create an array of the sorted characters of the string
        char[] characters = str.toCharArray();
        Arrays.sort(characters);
        // 1: iterate over the string's chars with 2 pointers
        for (int charIndex = 0; charIndex < str.length() - 1; charIndex += 1) {
            // a): check adjacent characters at each iteration
            char currentChar = characters[charIndex];
            char otherChar = characters[charIndex + 1];
            // b): if there's a duplicate char, the string's not unique
            if (currentChar == otherChar) {
                return false;
            }
        }
        // 2: otherwise, the string's unique
        return true;
    }

    public static void main(String[] args) {
        // posiive test case
        System.out.println(isUnique("abc"));
    }
}


/*        012
 * str = "abc"
 * 
 * cI = 2
 * cC = c
 * oI = 2
 * oC = c
 * --> True
 * Time: O(n^2)
 * Space: O(1)
 * 
 * Best Conceivable Runtime: O(n)
 * Bottleneck: linear search for each letter - nested O(n)
 * 
 */