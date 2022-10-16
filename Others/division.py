# The following code performs integer division

def division (a, b):
    count = 0
    total = b
    while total <= a:
        total += b
        count += 1
    return count


if __name__ == "__main__":
    a, b = (150, 10)
    print(division(a,b))