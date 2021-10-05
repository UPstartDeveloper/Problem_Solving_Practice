def FindIntersection(strArr):

    # code goes here
    """
    strArr - > 2 str
    both represt sorted collection of nums (csv)

    Return
    str
    csv numbers shared in both collections

    Clarifiy
    assume integers
    pos/neg
    duplicates in one string
    output IS sorted
    space requirement --> for now, can be out of place

    "1, 3, 4, 7, 13"
                    ^
    "1, 2, 4, 13, 15"
                        ^

    shared = [1, 4, 13]


    CQ:
    1. Brute force:
        - nested loop --> iterate


    Intuition:
        - only care about the unique values in both string
        - "race", where we move pters to be as equal as possible

    Approach:

    let first  = strArr[0]
    let second = strArr[1]

    1. Brute Force:
        - parse both string --> put it a set
        - take the intersection of the set
        - return "false" if empty
        - if not empty --> sort the set, cast as a string

        - linear time and space
        linear time = O(f + s)log(f + s)
        Space = f + s

    2. Inplace Traversal:
        - validate the inputs
        - init a shared array
        - traverse both - f + s
        - when equal -->
            - add to shared
            - move on to the next distinct val in both
        - not equal
            - mpve index in str w/ smaller, until >= val in other
        - return "false" is shared is empty, or cast as a str

    Time: linear - f + s
    Space: f + s

    3. Merge Operation
        - validate the inputs
        - init a shared array
        - traverse both arrays - f + s
        - merge the shared values into shared
        - return "false" is shared is empty, or cast as a str

    Time: linear - f + s
    Space: f + s




    Edge Cases:
    - floating pt. nums --> split by ", "
    - one str is empty --> return "false"
    - heterogenous data --> ValueError
    """

    def validate(arr1, arr2):
        """TODO: implement!!! - raise ValueError if not homogenous data"""
        # represent the array values as bools, if they are strings
        # combine then
        arr1.extend(arr2)
        # validate they alll work as numbers
        for val in arr1:
            try:
                val_num = float(val)
            except ValueError:
                raise ValueError("There can only be numbers in both collections")

    def intersection(arr1, arr2):
        index1 = 0
        index2 = 0
        # - traverse both - f + s
        shared = list()
        while index1 < len(arr1) and index2 < len(arr2):
            num1 = int(arr1[index1])
            num2 = int(arr2[index2])
            #   - when equal -->
            if num1 == num2:
                # add to shared
                shared.append(arr1[index1])
                # - move on to the next distinct val in both
                while index1 < len(arr1) - 1:
                    if arr1[index1] == arr1[index1 + 1]:
                        index1 += 1
                    else:
                        break
                index1 += 1
                while index2 < len(arr2) - 1:
                    if arr2[index2] == arr2[index2 + 1]:
                        index2 += 1
                    else:
                        break
                index2 += 1
            # not equal
            else:
                # - mpve index in str w/ smaller, until >= val in other
                if num1 < num2:
                    index1 += 1
                else:
                    index2 += 1
        return shared

    def parse_intersection(shared):
        """# - return "false" is shared is empty, or cast as a str"""
        if len(shared) == 0:
            return "false"
        return ", ".join(shared)

    # B: traverse both arrays - f + s
    arr1 = strArr[0].split(", ")
    arr2 = strArr[1].split(", ")
    # A: TODO: validate the inputs
    validate(arr1, arr2)  # raise ValueError if hetero data
    # C: merge the shared values into shared
    shared = intersection(arr1, arr2)
    # - return "false" is shared is empty, or cast as a str
    return parse_intersection(shared)


if __name__ == "__main__":
    strArr = ["1, 3, 4, 1.4, 13", "1, 2, 4, 13, 15"]
    print(FindIntersection(strArr))
