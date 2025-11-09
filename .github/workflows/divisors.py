import sys

def get_divisors(n: int):
    return [i for i in range(1, n + 1) if n % i == 0]

def main():
    if len(sys.argv) < 2:
        print("Usage: python divisors.py <positive-integer>")
        return
    n = int(sys.argv[1])
    if n <= 0:
        print("")
        return
    print(" ".join(map(str, get_divisors(n))))

if __name__ == "__main__":
    main()

