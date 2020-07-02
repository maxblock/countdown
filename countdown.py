from argparse import ArgumentParser
from itertools import (
    chain,
    combinations,
    combinations_with_replacement,
    zip_longest,
    permutations)

# 843 100 75 10 2 8 5
# 842 = (100+5)*8+2


def powerset(iterable):
    "powerset([1,2,3]) --> () (1) (2) (3) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def add_brackets(iterable):
    yield iterable
    for (fst, snd) in combinations(range(len(iterable)), 2):
        bracketed = list(iterable).copy()
        bracketed[fst] = "("+bracketed[fst]
        bracketed[snd] = bracketed[snd]+")"
        yield bracketed
        # TODO: yield and try adding brackets to sub expressions longer than 2


def solve(target, numbers):
    best_distance = target
    # For each subset
    for subset in powerset(numbers):
        # For each permuation
        for permutation in permutations(subset):
            operators = ["+", "-", "*"]

            if len(subset) <= 1:
                continue  # TODO: Handle

            # TODO: Add brackets
            for with_brackets in add_brackets(permutation):
                # For each assignment of operators between
                o_a = combinations_with_replacement(
                    operators, len(with_brackets) - 1)
                for combination in o_a:
                    zipped = zip_longest(with_brackets, combination)
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
