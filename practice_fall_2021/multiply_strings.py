class Solution:    
    def multiply(self, num1: str, num2: str) -> str:
        """
        Leetcode: https://leetcode.com/problems/multiply-strings/
        
        CANNOT int()
        
        inputs ---> nonneg decimal valuwa
        
        ASSUME only positive nums
        
        Intuition:
            Unicode values
            
         ord 
         values 
                48          49         50     51
                .--------------------------------->
          str   "0"        "1"        "2"    "3"
          inputs
          
         "char" = len(str) == 1
         
         num1 = "123"
         
         ["1", "2", "3"]
          factor1 = sum(
            ord("1") * 10**2, 
            ord("20"), 
            ord("3")
          )
          
        _decode(str) --> int:
            A: str --> list[char]
            B: decode by summing ord() of each digit ** pow10
            
        
        prod = (50 - 48) * (51 - 48) = 2 * 3 = 6
        
        prod = "6"
        
        chr(int) --> str
        chr(prod)
  
        A: convert input str ---> corr. Unicode ints
        B: compute the product (int) using ord("0")
        C: output product (int) ---> str?
        """
        ### HELPER
        def _decode(num: str) -> int:
            # A: str --> list[char]
            ZERO, digits = ord("0"), list(num)
            # B: decode by summing ord() of each digit ** pow10
            decoded = 0
            for index, d in enumerate(digits):
                power = 10 ** (len(digits) - (index + 1))
                digit_as_int = ord(d) - ZERO
                decoded += digit_as_int * power
            # C: all done!
            return decoded
        
        ### DRIVER code
        # A&B: compute prod
        factor1, factor2 = _decode(num1), _decode(num2)  # int values
        prod = factor1 * factor2   # int
        # C: output str of prod
        return f"{prod}"  # str
        
