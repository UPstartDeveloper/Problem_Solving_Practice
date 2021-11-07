/* Solution is for this problem found on Hacker Rank at the following link:
 * https://www.hackerrank.com/challenges/compare-the-triplets/problem
 */
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

public class Solution {

    // Complete the compareTriplets function below.
    static List<Integer> compareTriplets(List<Integer> a, List<Integer> b) {
        // init variables to store the comparative scores of Alice and Bob
        int aCompScore = 0;
        int bCompScore = 0;
        // traverse both a and b arrays
        for(int i = 0; i < a.size(); i++)
        {
            // retreive the score of Alice and Bob at this index
            int aScore = a.get(i);
            int bScore = b.get(i);
            // decide whether to award Alice or Bob a point for this index
            if (aScore > bScore)
            {
                aCompScore += 1;
            }
            else if (bScore > aScore)
            {
                bCompScore += 1;
            }
        }
        // return a new List of the comparative scores
        List<Integer> comparativeScores = new ArrayList<Integer>();
        comparativeScores.add(aCompScore);
        comparativeScores.add(bCompScore);
        return comparativeScores;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        List<Integer> a = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
            .map(Integer::parseInt)
            .collect(toList());

        List<Integer> b = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
            .map(Integer::parseInt)
            .collect(toList());

        List<Integer> result = compareTriplets(a, b);

        bufferedWriter.write(
            result.stream()
                .map(Object::toString)
                .collect(joining(" "))
            + "\n"
        );

        bufferedReader.close();
        bufferedWriter.close();
    }
}
