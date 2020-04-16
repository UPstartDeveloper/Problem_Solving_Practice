import unittest
"""
RNA Transcription
Problem found on Exercism. Description can be found at the following URL:
https://exercism.io/my/solutions/a8890252f83a47848618974c0adb725f

Notes:
DNA A, C, G, T
RNA A, C, G, U

test case:
string, no spaces, all upper case
'ACTGT'

RNA:
'UGACA'

{    D    R
    'A': 'U'
}

Idea #1
make an empty string for the RNA sequence
traverse the DNA strand:
    enqueue the letter from the front
    add corresponding letter in RNA to RNA seq

return string

"""


def get_complement(dna):
    # map DNA letters to RNA letters
    rna_key = {
        'A': 'U',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    rna_seq = ''
    for letter in dna:  # O(n) space and time
        rna_seq += rna_key[letter]

    return rna_seq


# Test Cases
class RNATranscriptionTests(unittest.TestCase):
    def test_get_complement_on_good_inputs(self):
        dna = 'GCTA'
        assert get_complement(dna) == 'CGAU'

        dna = 'CTAG'
        assert get_complement(dna) == 'GAUC'

    def test_get_complement_on_bad_inputs(self):
        pass

    def test_get_complement_on_edge_cases(self):
        pass


if __name__ == '__main__':
    unittest.main()
