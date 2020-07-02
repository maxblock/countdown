from argparse import ArgumentParser
from itertools import (
    chain,
    combinations,
    combinations_with_replacement,
    zip_longest,
    permutations)


def powerset(iterable):
    "powerset([1,2,3]) --> () (1) (2) (3) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def solve(target, numbers):
    best_distance = target
    # TODO: For each subset
    for subset in powerset(numbers):
        # print("Evaluating subset {}".format(
        #     ", ".join(subset)))

        # TODO: For each permuation
        for permutation in permutations(subset):
            operators = ["+", "-", "*"]

            if len(subset) <= 1:
                continue  # TODO: Handle

            # For each assignment of operators between
            # TODO: Add brackets
            o_a = combinations_with_replacement(operators, len(subset) - 1)
            for combination in o_a:
                zipped = zip_longest(subset, combination)
                foo = list(chain(*[list(x) for x in zipped]))
                bar = [x for x in foo if x]
                candidate_expression = "".join(bar)
                candidate_value = eval(candidate_expression)
                candidate_distance = abs(candidate_value - target)

                if candidate_distance < best_distance:
                    print("\tNew best: {}={}, distance: {}".format(
                        candidate_expression,
                        candidate_value,
                        candidate_distance))
                    best_distance = candidate_distance
                    if best_distance == 0:
                        return


def main():
    parser = ArgumentParser(description="Tries to reach the goal")
    parser.add_argument("target")
    parser.add_argument("numbers", nargs="+")
    args = parser.parse_args()
    print(args)

    print("Trying to reach {} using {}".format(
        args.target, ", ".join(args.numbers)))

    solve(int(args.target), args.numbers)


if __name__ == "__main__":
    main()
