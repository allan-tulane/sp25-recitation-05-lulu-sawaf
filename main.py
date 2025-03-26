import random
import time
import tabulate
import matplotlib.pyplot as plt

def ssort(L):
    ### selection sort
    if (len(L) == 1):
        return (L)
    else:
        m = L.index(min(L))
        print('selecting minimum %s' % L[m])
        L[0], L[m] = L[m], L[0]
        print('recursively sorting L=%s\n' % L[1:])
        return [L[0]] + ssort(L[1:])


def qsort(a, pivot_fn):
    if (len(a) <= 1):
        return a

    p = pivot_fn(a)                    #select pivot using the provided pivot function
    left = [x for x in a if x < p]     #elements less than pivot
    right = [x for x in a if x > p]    #elements greater than pivot
    return qsort(left, pivot_fn) + [p] + qsort(right, pivot_fn)


def time_search(sort_fn, mylist):
    """
    Return the number of milliseconds to run this
    sort function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds.
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start) * 1000
    ###

def compare_sort(sizes=[100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]):
    """
    Compare the running time of different sorting algorithms.

    Returns:
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """
    qsort_fixed_pivot = lambda L: qsort(L, lambda L: L[0]    #first element as pivot
                                        )
    qsort_random_pivot = lambda L: qsort(L, lambda L: random.choice(L)    #random pivot
                                         )
    tim_sort = sorted    #python's built-in Timsort (optimized hybrid sort)
    result = []
    for size in sizes:
        # create list in ascending order
        mylist = list(range(size))     #create a list of size `size`
        # shuffles list if needed
        random.shuffle(mylist)    #shuffle to ensure average-case input
        result.append([
            len(mylist),
            time_search(qsort_fixed_pivot, mylist), #time fixed-pivot quicksort
            time_search(qsort_random_pivot, mylist),    #time random-pivot quicksort
            time_search(tim_sort, mylist)    #time Python's built-in `sorted`
        ])
    return result
    ###


def print_results(results):
    """ change as needed for comparisons """
    print(
        tabulate.tabulate(
            results,
            headers=['n', 'qsort-fixed-pivot', 'qsort-random-pivot', 'tim_sort'],
            floatfmt=".3f",
            tablefmt="github"))


def test_print():
    print_results(compare_sort())


def plot_results(results, title="Pivot Timing Results"):
    sizes = [row[0] for row in results]    #extract input sizes (n)
    fixed_times = [row[1] for row in results]    #fixed-pivot quicksort times
    random_times = [row[2] for row in results]    #random-pivot quicksort times

    plt.plot(sizes, fixed_times, label='qsort-fixed-pivot')
    plt.plot(sizes, random_times, label='qsort-random-pivot')
    plt.xlabel("List size (n)")
    plt.ylabel("Time (ms)")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()


random.seed()
results = compare_sort()
test_print()
plot_results(results)