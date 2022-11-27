"""
Time - O(nloglogn) or O(log(log(n)))  Space - O(n)
Given an integer n, return the number of prime numbers that are strictly less than n.
"""
from typing import List


class Solution:
    def count_primes(self, n: int) -> int:
        if n < 3:
            return 0
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        count = n - 2
        # int(math.ceil(math.sqrt(n)))
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for multiple in range(i*i, n, i):
                    if is_prime[multiple]:
                        is_prime[multiple] = False
                        count -= 1
        return count


if __name__ == "__main__":
    so = Solution()
    x = 10
    print(so.count_primes(x))
