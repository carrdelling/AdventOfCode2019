
def fuel(m):
    f = (m//3) - 2
    return f + fuel(f) if f > 0 else 0


def solve(data):

    return sum(fuel(f) for f in data)


def main():

    with open('input') as in_f:
        data = [int(row.strip()) for row in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
