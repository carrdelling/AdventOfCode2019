from functools import reduce


def vel_fwd(asteroids, axis):

    v_axis = axis+3

    min_v = -999999
    grav = 0
    size = 0
    for c, x in enumerate(asteroids):
        if x[axis] > min_v:
            grav += 1 + size
            min_v = x[axis]
            size = 0
        else:
            size += 1
        asteroids[c][v_axis] -= grav


def vel_bwd(asteroids, axis):

    v_axis = axis+3

    max_x = 999999
    grav = 0
    size = 0
    for c, x in list(enumerate(asteroids))[::-1]:
        if x[axis] < max_x:
            grav += 1 + size
            max_x = x[axis]
            size = 0
        else:
            size += 1
        asteroids[c][v_axis] += grav


def energy(asteroids):

    def _single(x):
        potential = sum(abs(x[i]) for i in range(3))
        kinetic = sum(abs(x[i + 3]) for i in range(3))

        return potential * kinetic

    return sum(_single(x) for x in asteroids)


def generation(asteroids, axis):

    # velocity

    asteroids.sort(key=lambda x: x[axis])
    vel_fwd(asteroids, axis)
    vel_bwd(asteroids, axis)

    # position
    for x in asteroids:
        x[axis] += x[3 + axis]


def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x


def lcm(x, y):
    m = (x*y)//gcd(x, y)
    return m


def solve(positions):

    asteroids = [[x, y, z, 0, 0, 0] for x, y, z in positions]

    steps = []

    for ax in range(3):
        state = tuple([x[ax] for x in asteroids] + [x[ax+3] for x in asteroids])
        seen = {state}

        found = False
        gen = -1

        while not found:
            generation(asteroids, ax)
            gen += 1
            state = tuple([x[ax] for x in asteroids] + [x[ax + 3] for x in asteroids])

            if state in seen:
                found = True
                steps.append(gen)
            else:
                seen.add(state)

        print(f"Axis {ax}: Period {gen}")

    return reduce(lcm, steps)


def main():

    positions = []
    with open('input') as in_f:
        for line in in_f:
            dim_value_pairs = [i.strip() for i in line.strip()[1:-1].split(',')]
            x, y, z = [int(i.split('=')[1]) for i in dim_value_pairs]
            positions.append((x, y, z))

    solution = solve(positions)

    print(solution)


if __name__ == "__main__":

    main()
