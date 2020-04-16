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


def to_rna(dna):
    # map DNA letters to RNA letters
    rna_key = {
        'A': 'U',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    rna_seq = ''
    for char in dna:  # O(n) space and time
        if isinstance(char, str):
            if char in rna_key.keys():
                # if a DNA character, add the RNA complemet
                rna_seq += rna_key[char]
            else:
                rna_seq += char

    return rna_seq


# Test Cases
class RNATranscriptionTests(unittest.TestCase):
    def test_to_rna_on_good_inputs(self):
        dna = 'GCTA'
        assert to_rna(dna) == 'CGAU'

        dna = 'CTAG GTAC'
        assert to_rna(dna) == 'GAUC CAUG'

    def test_to_rna_on_bad_inputs(self):
        pass

    def test_to_rna_on_edge_cases(self):
        pass


if __name__ == '__main__':
    unittest.main()
