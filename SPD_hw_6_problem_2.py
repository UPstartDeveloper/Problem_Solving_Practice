"""
Given a RNA

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
    for letter in dna:  # O(n)
        rna_seq += rna_key[letter]

    return rna_seq

# space and time - O(n)


if __name__ == '__main__':
    print(get_complement('GCTA'))  # CGAU
