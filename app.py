
"""Prime number utilities and simple CLI.

Usage:
  python app.py [limit]

If limit is provided, prints all primes <= limit. Default limit is 100.
"""

import sys
from math import isqrt


def is_prime(n: int) -> bool:
	if n <= 1:
		return False
	if n <= 3:
		return True
	if n % 2 == 0:
		return False
	r = isqrt(n)
	for i in range(3, r + 1, 2):
		if n % i == 0:
			return False
	return True


def sieve(limit: int):
	if limit < 2:
		return []
	sieve = [True] * (limit + 1)
	sieve[0:2] = [False, False]
	for p in range(2, isqrt(limit) + 1):
		if sieve[p]:
			step = p
			start = p * p
			sieve[start: limit + 1: step] = [False] * (((limit - start) // step) + 1)
	return [i for i, val in enumerate(sieve) if val]


def main():
	limit = 100
	if len(sys.argv) > 1:
		try:
			limit = int(sys.argv[1])
		except ValueError:
			print('Invalid limit, using default 100')
	primes = sieve(limit)
	print('Primes up to', limit)
	print(primes)


if __name__ == '__main__':
	main()

