import itertools as it


def naive_grouper(inputs, n):
    num_groups = len(inputs) // n
    return [tuple(inputs[i*n:(i+1)*n]) for i in range(num_groups)]


# Working with iterators
def better_grouper(inputs, n):
    #  creates a list of n references to the same iterator
    iters = [iter(inputs)] * n
    # returns an iterator over pairs of corresponding elements of each iterator in iters.
    return zip(*iters)


def grouper(inputs, n, fillvalue=None):
    iters = [iter(inputs)] * n
    return it.zip_longest(*iters, fillvalue=fillvalue)


def main():
    # Naive_grouper takes lot of memory

    #  Better_grouper less memory used than naive

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(list(grouper(nums, 4)))


if __name__ == '__main__':
    main()
