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


def solve(m):

    asteroids = [k for k, v in m.items() if v]

    max_score = 0
    for a in asteroids:

        vectors = [(a[0] - b[0], a[1] - b[1]) for b in asteroids if a != b]

        unique_vectors = []

        for v in vectors:
            for vv in unique_vectors:

                angle = compute_angle(v, vv)

                if abs(angle) < 1E-5:
                    print(angle)
                    break
            else:
                unique_vectors.append(v)

        max_score = max(max_score, len(unique_vectors))

    return max_score


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
