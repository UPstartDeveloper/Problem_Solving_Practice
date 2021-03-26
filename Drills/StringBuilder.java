public class StringBuilder {
    protected static final int RESIZE_FACTOR = 2;
    protected String[] chars;

    /***** constructors *******/
    public StringBuilder(String[] characters) {
        this.chars = characters;
    }

    public StringBuilder() {
        this.chars = new String[8];
    }

    /***** instance methods **/
    public int getCurrentLetterCount() {
        // returns the number of letters in the characters array
        int count = 0;
        for (int index = 0; index < this.chars.length; index++) {
            if (this.chars[index] != null) {
                count += 1;
            } else {
                break;
            }
        }
        return count;
    }
    public void concatenate(String newChars) {
        // A: calculate the length of the new characters arr
        int currentLetterCount = this.getCurrentLetterCount();
        int newLengthRequired = currentLetterCount + newChars.length();
        // B: if it's over, find the smallest power of RESIZE_FACTOR 
        // to allocate in the new array
        if (newLengthRequired > this.chars.length) {
            // HELPER FUNC
            // take the log base 2 of newLengthRequired, floor it, +1
            // allocate an array of that size
            // add in everything so far in the current chars array, 
                // and then everything in the new string too
        } 
        // C: otherwise just add in the new characters one by one
        else {
            int charactersIndex = currentLetterCount;
            for (int newCharsIndex = 0; 
                newCharsIndex < newChars.length(); newCharsIndex++) {
                this.chars[charactersIndex] = newChars[newCharsIndex];
                charactersIndex += 1;
            } 
        }

    }

    /* 
     * Other Methods (based on Python str API):
     * upper()
     * lower()
     * pop()
     * find() --> index
     * getChar(index)
     * join --> String
     */

}
