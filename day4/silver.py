

def solve(a, b):

    count = 0

    for c in range(a, b+1):
        s = str(c)
        if s[0] <= s[1] <= s[2] <= s[3] <= s[4] <= s[5]:
            if any([(s[0] == s[1]), (s[1] == s[2]), (s[2] == s[3]),
                    (s[3] == s[4]), (s[4] == s[5])
                    ]):
                count += 1

    return count


def main():

    with open('input') as in_f:
        first, second = map(int, in_f.readline().strip().split('-'))

    solution = solve(first, second)

    print(solution)


if __name__ == "__main__":

    main()
