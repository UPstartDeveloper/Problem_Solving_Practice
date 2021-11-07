"""
Solving problem listed on Hacker Rank:
https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
"""


def solution(socks):
    """Return an integer representing the number of pairs of matching socks."""
    # build a histogram of the socks
    sock_colors = {}
    for sock in socks:
        if sock not in sock_colors.keys():
            sock_colors[sock] = 1
        else:
            sock_colors[sock] += 1
    # count the amount of pairs
    pairs = 0
    for count in sock_colors.values():
        pairs += count // 2
    return pairs
