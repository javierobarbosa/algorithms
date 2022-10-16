# The following code computes the [integer] square root of a number.
# If the number is not a perfect square (there is no integer square root), then it returns -1.

def calculate_square(n: int):
    return square_helper(n, 1, n)


def square_helper(n: int, min: float, max: float):
    if max < min:
        return -1
    guess = (min + max) // 2
    square = guess * guess
    if square == n:
        return guess
    elif square < n:
        return square_helper(n, guess+1, max)
    else:
        return square_helper(n, min, guess-1)


if __name__ == "__main__":
    number = 100
    print(calculate_square(number))