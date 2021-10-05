def decode_variations(S):
    """
    A letter can be encoded to a number in the following way:

    'A' -> '1', 'B' -> '2', 'C' -> '3', ..., 'Z' -> '26'
    A message is a string of uppercase letters, and it is encoded first using this scheme.
    For example, 'AZB' -> '1262'

    Given a string of digits S from 0-9 representing an encoded message,
    return the number of ways to decode it.

    Assumptions:
    - none of the inputs have leading zeros
    - the input is a string representing a nonnegative integer

    Time: O(2^n), in the case each subsequent pair of integers
                  has two variations (e.g. '262626262626')
    Space: O(n), b/c in the worst case input that's how many stack frames
                   we push onto the call stack at any one time

    """

    def is_valid(string):
        """returns T/F on whether the 2-digit string is a letter by itself"""
        if 1 <= int(string) <= 26:
            return True
        return False

    def get_variations(current_string, input_string):
        """Top-Down DP for finding the number of ways to decode a string"""
        # Base Case - if input if empty
        if len(input_string) == 0:
            # assume we add 1 variations
            adding = 1
            # check if it's appropiate to add 1
            last_token = current_string.split("-")[-1]
            if not is_valid(last_token):
                # if not, then don't increase the num of variations
                adding = 0
            return adding
        # Recursive case: check if >= 2 letters
        if len(input_string) >= 1:
            variations = 0
            # take a look at the next 2 letters
            if len(input_string) >= 2:
                # if they are valid together
                if is_valid(input_string[:2]) is True:
                    # call the function again, w/ both of them added
                    new_string = "".join([current_string, "-", input_string[:2]])
                    variations += get_variations(new_string, input_string[2:])
            # call the function again w/ just the next
            new_string = "".join([current_string, "-", input_string[:1]])
            variations += get_variations(new_string, input_string[1:])
            # return the answer for the subproblem
            return variations

    return get_variations("", S)


"""
  Brainstorming: 

  # A: init the list of strings
  strings = list()
	# letter by letter (1 digit)
  first = 0
  second = 1
  # window of 2, move it across the whole word
      # check if the number is between 1-26
      # if it is, decode the number, and move both indices
      # if not, use 1 digit
      # always check if 2 or 1 numbers left
  # append the new variation to a list
  # return the length of the list of strings
      
    
    import java.io.*;
import java.util.*;

class Solution {
 
  
  private static int res ;
  
	static int decodeVariations(String S) {
     res = 0;
		// your code goes here
    if(S.length() < 1 || S.charAt(0) == '0'){
      return 0;
    }
    
    fun(S, 0 );
    return res;
	}
  
  
  static void fun(String str, int index){
  
     if(index > str.length()){
       return;
     }
   
     if(index == str.length()){
      res++;
      return;
     }
      
   
   
    int first = Character.getNumericValue(str.charAt(index));
   
    if(first == 0){
      return;
    }
    
    if(first > 2){
      System.out.println("first  >2 -- "+ first);
       fun(str, index+1);
      
    }else{
        
      if( (index +1)  < str.length()){ 
       
        int val = Integer.parseInt(str.substring(index, index+2));
       
        if(val <=26){ // "6", ""
            fun(str, index+1 );
          
            fun(str, index+2);
         }else{
           fun(str, index+1);
        }
      }else{
       
        fun(str, index+1);
     }
     
   }
  
 }

	public static void main(String[] args) {
	
	}
}



/*

// "" ,
 String str = "30"; A
 String str = "101";
 
 
 
 fun(String str , index){
 if(index == str.length()){
 res++;
 }
 
 char ch = str.chartAt(index);
 
 if(Charcter.getNumericValue(ch) > 2){
  fun(str, index+1);
 }else{
    
    int val = Ineger.parseInt(str.subString(index, index+1))
    if(val< 26){
    fun(str, index+1);
    fun(str, index+2);
    }else{
    fun(str, index+1);
    }
    
 }
 
 }


*/

  
	
	@param S: str
	@return: int
  
  Inutuition:
  enumerate all uppercase English letters 
  A - > 1
  B -> 2
  
  Example:
  1, 26, 2': 'AZB', 
  1, 2, 6, 2 : 'ABFB', and 
  12, 6, 2 :'LFB'
  
  return 3
  
  Brainstorming:
  
  1 or 2 digit number, 3 
  
  1 - A
  2 - B
  11 - AA, L
  
  Approach
  # letter by letter (1 digit)
  # window of 2, move it across the whole word
      # check if the number is between 1-26
      # if it is, decode the number, and move both indices
      # if not, use 1 digit
      # always check if 2 or 1 numbers left
  # append the new variation to a list
  # return the length of the list of strings
      
  
      
      
  1262 - ABFB
  
  12626 - LFB, 
  
  12 - A B, 'L'
  ^^
  
  Edge Case: no leading zeroes
  09
  
  10 - J
  101 - JA
  
  '1262'
  each digit, or pair of digits is a subproblem
  
  1     12     1
  2     6      26
  6     2      2
  2
  
  1 -> fun(262) -
            2 -> fun(62)
                     6 -> fun(2);
            26 -> fun(2) -1
  12 -> fun(62)
            6  -> fun(2)
            
  
  // String  str = "0"  // res =0;
  // str = 01 // 0
  // str == 335345340000
  
  0 - 0
  1 - 1 variation
  11 - 2 variation
  
  
  
  int  res =0;
  fun(String  str , int  index){
  
  if(index > str.length()){
  retrun.
  }
  
  if(index == str.length())
     res++;
  }
  
  int first = //first character of string
  
  if(first == 0){
  return ;
  }
  
  if(first >2){
     fun(str, index+1);
  }else{
  
      
      // int  val ////check two digit number
      
      if(val >=10 && val <=26){
          fun(str, index+1);
          fun(str, index+2);
      }else{
           fun(str, index+1);
      }
  }
  
  
  1262
  
  # A: look at first 1 (if not 2) chars in the string:
  DP table to match substrings w/ number of variations
  
  # A: map all 1 digit numbers to the number of vairations
  num_ = dict()
  num_variations['0'] = 0
  for i in range(1, 11):
    num_variations[str(i)] = 1
  
"""


if __name__ == "__main__":
    # Test Cases
    assert decode_variations("1") == 1
    assert decode_variations("10") == 1, f"The answer is {decode_variations('10')}"
    assert decode_variations("60") == 0
    assert decode_variations("11") == 2
    assert decode_variations("1262") == 3
