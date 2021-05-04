/**
 * From Data Interview Q's:
 * Suppose a company is taxed 20% if earnings for a given quarter are >= $3M
 * USD.
 * 
 * If earnings land < $3M USD for the quarter, the company is taxed at a lower
 * rate of 15%.
 * 
 * Write a function using Python to calculate both the pre-tax and post-tax
 * earnings for a given company, with the ability to feed in the # of widgets
 * sold as well as the average price of the widget as inputs (# of widgets sold
 * * avg. price of widgets = total earnings in this case).
 * 
 * For example, if the company sells 20,000 widgets at an average price of $220
 * USD then your function should return:
 * 
 * Pre-tax earnings were 20,000*220 = 4.4M for the quarter. Post-tax earnings
 * were 3.52M for the quarter [4.4M *.8 (since we fall in higher 20 percent tax
 * bracket here)]
 * 
 * Clarifications:
 * In: # units, unit price
 * Output: float[] --> pre tax earnings, and post tax earnings
 * Rounding:
 *  - ASSUME we must return the earnings to the nearest cent? (2 decimal places)
 *  - ASSUME it's ok to round up:
 *      - revenue: 77,677,777.88888 ---> 77.7M
 *      - but for starters: round to the nearest cent
 *      - stretch: round to the nearest hecta-million
 *      - stretch: round to whatever the "tenth of whatever power of 1000 our revenue is"
 *  - ASSUME the income thresholds are inclusive
 * 
 * Intuition: 
 *      apply a multiplication, then also use a conditional
 * Approach:
 *      - init array for output, a
 *      - calculate revenue ---> pre-tax earnings ---> a[0]
 *      - figure out the tax rate to use (switch + 2d array of revenue thresholds and tax rates)
 *      - calculate post-tax $$ --> a[1]
 *      - return a
 * Edge Cases:
 *      ASSUME that the # units is an integer?
 *      ASSUME that th unit price is a double?
 *      ASSUME both are nonnegative values
 */

import java.lang.Math;
import java.util.ArrayList;

public class QuarterlyEarnings {
    // ASSUME this is an instance variable, and is static in size
    ArrayList<Double[]> taxBrackets;

    public QuarterlyEarnings(ArrayList<Double[]>  incomeTaxBrackets) {
        this.taxBrackets = incomeTaxBrackets;
    }

    public void addTaxBracket(Double[] incomeRate) {
        // TODO:
    }

    public double calculatePreTax(int widgets, double unitPrice) {
        // validate inputs
        if (widgets <= 0 || unitPrice <= 0.00) {
            throw new IllegalArgumentException(
                "Must input non-negative values for no. units sold, and the price per unit."
            );
        }
        // TODO: use the BigDecimal class to be more precise
        double revenue = (double) widgets * unitPrice;
        return revenue;
    }

    public double calculatePostTax(double preTax) {
        /* Planned Time Complexity: O(b log b), where b is the length of this.taxBrackets */
        // find the tax rate
        double taxRate = null;
        // TODO: make sure to SORT the taxBrackets by highest rate first!
        for(Double[] taxBracket: this.taxBrackets) {
            // the first index is the income threshold
            if (preTax >= taxBracket[0]) {
                // the second is the tax rate to us
                taxRate = taxBracket[1];
                break;
            }
        }
        // TODO: calculate the post tax earnings, rounded to nearest cent
        return preTax * taxRate;
    }

    

    public double[] calculatePrePostEarnings(int widgets, double unitPrice) {
        // - init array for output, a
        double[] earnings = new double[2];
        // - calculate revenue ---> pre-tax earnings ---> a[0]
        double preTax = calculatePreTax(widgets, unitPrice);
        earnings[0] = preTax;
        // - TODO: figure out the tax rate to use (switch + 2d array of revenue thresholds and tax rates)
        // - calculate post-tax $$ --> a[1]
        double postTax = calculatePostTax(preTax);
        earnings[1] = postTax;
        // - return a
        return earnings;
    } 
    
}
