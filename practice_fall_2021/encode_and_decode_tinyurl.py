class Codec:
    
    """
    1:1 mapping
    can't repeat tiny URLs
    
    Intution:
        mapping problems
        
    Approach:
        dict (tiny URLs --> input )
        
        1) Encode Func
            - same hash_code ---> Different Input
            Idea:
            1) Map tinyURl
            2) split 
            
            
            - hash --> randomized short string, same I/O
            - TODO: MORE scalable
            A: get a hashcode(input)
            B: cast as a string
            C: BASE_URL = https://tinyurl.com/ + hash_code
            D: add an new entry to the dict
            E: return the tiny URL
            
        2) Decode
            A: retrive the long urL from the dict
            B: if not found -> raise KeyError 
    EC:
        - no empty url 
        - URL validation
        
    Intuition:
        deteministic
        maps unique I/O
        
    Approach: 
        ord(str) -> Unicode value
        A: call the func on the path: ord('design-tinyurl') = 57005657666
        B: modulo div w/ 26 = 57005657666 ---> 45
        C: 
    
    """
    def __init__(self):
        self.data_store = dict()
        self.BASE_URL = "http://tinyurl.com/"
        
        

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        # A: get a hashcode(input)
        code = hash(longUrl)
        # B: cast as a string
        str_code = str(code)[:5]
        # C: BASE_URL = https://tinyurl.com/ + hash_code
        tiny = self.BASE_URL + str_code
        # D: add an new entry to the dict
        self.data_store[tiny] = longUrl
        # E: return the tiny URL
        return tiny
        
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        if shortUrl not in self.data_store:
            raise KeyError("This is not valid tiny URL")
        return self.data_store[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
