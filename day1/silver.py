

def solve(data):

    return sum((f//3) - 2 for f in data)


def main():

    with open('input') as in_f:
        data = [int(row.strip()) for row in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
