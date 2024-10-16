
INT_MAX = 50000000

def minChocoDistribution(choco :list, num: int) -> int:

    choco.sort()

    min_diff = INT_MAX

    for i in range(len(choco)-num):

        diff = choco[i+num-1] - choco[i]

        if min_diff>diff:
            min_diff = diff

    print(min_diff)

    return min_diff


if __name__ == "__main__":

    arr = [7, 3, 2, 4, 9, 12, 56]

    m = 3

    x = minChocoDistribution(arr, m)