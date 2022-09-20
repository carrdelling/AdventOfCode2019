from collections import defaultdict


def solve(rules):

    recipes = {name: (pre, am) for pre, name, am in rules}

    targets = {'FUEL': 1}
    ore_used = 0
    kitchen = defaultdict(int)
    while len(targets) > 0:
        next_target = next(iter(targets.keys()))
        next_need = targets[next_target]

        # ORE usage
        if next_target == 'ORE':
            ore_used += next_need
            del targets[next_target]
            continue

        # check kitchen first
        in_kitchen = 0 if kitchen[next_target] < 0 else kitchen[next_target]
        if in_kitchen > 0:
            to_use = min(in_kitchen, next_need)
            kitchen[next_target] -= to_use
            targets[next_target] -= to_use
            next_need = targets[next_target]

        if next_need < 1:
            del targets[next_target]
            continue

        # prepare a new recipe
        req, amount = recipes[next_target]
        if next_need <= amount:
            del targets[next_target]
            kitchen[next_target] += amount - next_need
        else:
            targets[next_target] -= amount

        # we need the ingredients of the new recipe
        for rr, nn in req.items():
            targets[rr] = targets.get(rr, 0) + nn

    return ore_used


def main():

    rules = []
    with open('input') as in_f:
        for line in in_f:
            pre, post = line.strip().split('=>')
            prec = {}
            for comp in pre.split(','):
                am, name = comp.strip().split()
                prec[name] = int(am)
            am, name = post.strip().split()

            rule = [prec, name, int(am)]
            rules.append(rule)

    solution = solve(rules)

    print(solution)


if __name__ == "__main__":

    main()
