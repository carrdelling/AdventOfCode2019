import math


def compute_angle(v1, v2):

    try:
        dot = v1[0] * v2[0] + v1[1] * v2[1]  # dot product between [x1, y1] and [x2, y2]
        det = v1[0] * v2[1] - v1[1] * v2[0]  # determinant
        rad = math.atan2(det, dot)
        angle = rad / math.pi * 180
        return angle + 360.0 if angle < 0.0 else angle
    except:
        return 0


def distance(v1, v2):

    return math.sqrt(((v1[0]-v2[0]) * (v1[0]-v2[0])) + ((v1[1]-v2[1]) * (v1[1]-v2[1])))


def solve(m):

    asteroids = [k for k, v in m.items() if v]

    max_score = 0
    location = None
    for a in asteroids:

        vectors = [(a[0] - b[0], a[1] - b[1]) for b in asteroids if a != b]

        unique_vectors = []

        for v in vectors:
            for vv in unique_vectors:

                angle = compute_angle(v, vv)

                if abs(angle) < 1E-5:
                    break
            else:
                unique_vectors.append(v)

        if len(unique_vectors) > max_score:
            max_score = len(unique_vectors)
            location = a

    # prep for vaporize
    targets = [((location[0] - b[0], location[1] - b[1]), b) for b in asteroids if location != b]
    targets = [(compute_angle(x[0], (1, 0)), distance(x[1], location), x[1]) for x in targets]
    targets.sort(key=lambda x: (x[0], x[1]))

    # vaporize!
    destroyed = []

    while targets:
        saved = []
        seen = set()

        for a, d, p in targets:

            if a not in seen:
                seen.add(a)
                destroyed.append((p, len(destroyed) + 1))
            else:
                saved.append((a, d, p))
        targets = list(saved)

    solution = destroyed[199][0]
    # our coordinates system is reversed vs AoC
    signature = 100 * solution[1] + solution[0]

    return signature


def main():

    with open('input') as in_f:
        area = {}
        for i, row in enumerate(in_f, 0):
            data = row.strip()
            for j, d in enumerate(data):
                area[(i, j)] = True if d == '#' else False

    solution = solve(area)

    print(solution)


if __name__ == "__main__":

    main()
