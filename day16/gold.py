

def solve(d):

    offset = int(''.join(map(str, d[:7])))

    data = d * 10000

    iterations = 100

    for it in range(iterations):
        print(it)
        new_data = [0] * offset

        acum = sum(data[offset:])

        acum = acum * -1 if acum < 0 else acum
        t = acum % 10
        new_data.append(t)

        for idx in range(offset + 2, len(data) + 1):
            acum -= data[idx - 2]
            acum = acum * -1 if acum < 0 else acum
            t = acum % 10
            new_data.append(t)
        data = list(new_data)

    return ''.join(str(i) for i in data[offset:(offset + 8)])


def main():

    with open('input') as in_f:
        data = [int(x) for x in in_f.readline().strip()]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
