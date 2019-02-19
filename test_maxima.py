import numpy as np
import pytest
from maxima_good import find_maxima_1

test_cases = [(3, 1),
              (10, 1),
              (7, 1)]

@pytest.mark.parametrize('numel,seedval', test_cases)
def test_randomized(numel, seedval):
    rand_gen = np.random.RandomState(seed=seedval)

    test_vec = rand_gen.random_integers(low=1,high=20,size=numel)
    out      = find_maxima_1(test_vec)

    numMax = len(out)

    for i in range(0,numMax):
        iE = out[i]
        if iE == 0:
            assert test_vec[0] > test_vec[1]
        elif iE == numel - 1:
            assert test_vec[numel-1] > test_vec[numel-2]
        else:
            assert test_vec[iE-1] < test_vec[iE] and test_vec[iE+1] < test_vec[iE]
