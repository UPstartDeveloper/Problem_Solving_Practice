def two_fer(name):
    """Return message about sharing.
    Time and space complexity are both O(1).
    """
    if name is None:
        name = "you"
    return f"One for {name}, one for me."
