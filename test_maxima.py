import numpy as np
import pytest
from maxima_good import find_maxima_1

def test_randomized():
    seedval = pytest.config.getoption('seed')
    if seedval is None:
        seedval = np.random.randint(2**32)
    print()
    print(f'seedval: {seedval}')

    # given
    rand_gen = np.random.RandomState(seed=seedval)
    numel = rand_gen.randint(0, 1000)
    print(f'numel: {numel}')

    test_vec = rand_gen.random_integers(low=1, high=20, size=numel)
    print(f'test_vec: {test_vec}')

    # when
    out      = find_maxima_1(test_vec)

    # then
    numMax = len(out)
    for i in range(0,numMax):
        iE = out[i]
        if iE == 0:
            assert test_vec[0] > test_vec[1]
        elif iE == numel - 1:
            assert test_vec[numel-1] > test_vec[numel-2]
        else:
            assert test_vec[iE-1] < test_vec[iE] and test_vec[iE+1] < test_vec[iE]
