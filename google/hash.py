from list import LinkedList


class HashTable:
    """An associative array that uses separate chaining to resolve hash collections.
       For now we don't rely on dynamic resizing.
    """

    def __init__(self, num_buckets=8):
        self.buckets = [LinkedList() for _ in range(num_buckets)]

    def _get_bucket_index(self, key):
        hash_code = hash(key)
        index = hash_code % len(self.buckets)
        return index

    def set(self, key, value):
        """Add or update a key-value pair in an bucket."""
        index = self._get_bucket_index(key)
        new_pair, bucket = (key, value), self.buckets[index]
        pairs = bucket.items()
        for bucket_key, value in pairs:
            if key == bucket_key:
                bucket.delete((bucket_key, value))
        bucket.add(new_pair)

    def get(self, key):
        """Return the associated value for a given key."""
        index = self._get_bucket_index(key)
        bucket = self.buckets[index]
        pairs = bucket.items()
        for bucket_key, value in pairs:
            if key == bucket_key:
                return value

    def delete(self, key):
        """Remove a pair which is known to be stored somewhere."""
        index = self._get_bucket_index(key)
        bucket = self.buckets[index]
        pairs = bucket.items()
        for bucket_key, value in pairs:
            if key == bucket_key:
                bucket.delete((bucket_key, value))
