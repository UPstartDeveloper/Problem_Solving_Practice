def is_valid(num):
    # check if num is an num
    try:
        num = int(num)  # "12" --> 12
        # see it's 0-255
        return 0 <= num <= 255
    except ValueError:
        return False


def validateIP(ip):
    # edge case for no periods
    if "." not in ip:
        return False
    # A: split the address amongst the periods
    nums = ip.split(".")
    # B: count up the number of valid addresses
    valid = 0
    # validate each num
    for num in nums:
        if is_valid(num) is True:
            valid += 1
    # C: return if we have a valid IP address
    return valid == 4


"""
time: O(n)
Space: O(n)

 ip = '123.24.059.99'  -> return True
"""


if __name__ == "__main__":
    # TODO: this test case should actually FAIL, b/c of leading 0's
    ip = "123.24.059.99"
    print(validateIP(ip))
