/*
 * Hacker Rank Problem found here:
 * https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
 */

 public class repeatedString {
     //-----------------------------------------------------
     // pre: String s, and long n
     // post: return the number of times "a" appears in
     //       first n letters of s, repeated over and over
     //------------------------------------------------------
     public static long repeatString(String s, long n){
        // count the number of times "a" appears in s
        long numAsInOne = 0;
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == 'a'){
                numAsInOne += 1;
            }
        }
        // obtain roughly the number of "a" appearances in n letters
        long total = numAsInOne * (n / s.length());
        // store the remainder, the letters of s that partially fit in n letters
        long remS = n % s.length();
        // count number of times "a" appears in first r letters of s
        long numAsInRest = 0;
        for(int i = 0; i < remS; i++){
            if (s.charAt(i) == 'a'){
                numAsInRest += 1;
            }
        }
        // return the total
        return (total + numAsInRest);
    }
     //--------------------------------------------------
     // pre: None
     // post: Solution to the "Repeated String" problem.
     //--------------------------------------------------
     public static void main(String[] args){
         // execute repeatedString on a reasonable test input
         String s = "aba";
         long n = 10;
         long As = repeatString(s, n);
         System.out.println("The correct ouput for the above is: " + As);
     }
 }
