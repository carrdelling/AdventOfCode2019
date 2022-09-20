

def solve(rules):

    N = 10007

    deck = list(range(N))

    for action, value in rules:

        if 'new' in action:
            deck = deck[::-1]
            continue

        if 'cut' in action:
            deck = deck[value:] + deck[:value]
            continue

        if 'increment' in action:
            new_deck = [0] * len(deck)
            for i in range(len(deck)):
                new_deck[(i * value) % len(deck)] = deck[i]
            deck = list(new_deck)
            continue

    return deck.index(2019)


def main():

    rules = []
    with open('input') as in_f:
        for line in in_f:
            chunks = line.strip().split(' ')
            pre = ' '.join(chunks[:-1])
            post = int(chunks[-1]) if chunks[-1] != 'stack' else -1
            rule = (pre, post)
            rules.append(rule)

    solution = solve(rules)

    print(solution)


if __name__ == "__main__":

    main()
