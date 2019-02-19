import numpy as np
import pytest

from maxima import find_maxima

@pytest.mark.xfail
def test_empty():
    out = find_maxima([])
    assert out == [-1]

test_cases = [
([0, 1, 2, 1, 2, 1, 0], [2, 4]),
([-i**2 for i in range(-3, 4)], [3]),
([np.sin(2*alpha) for alpha in np.linspace(0.0, 5.0, 100)], [16,78]),
([4, 2, 1, 3, 1, 2], [0, 3, 5]),
([4, 2, 1, 3, 1, 5], [0, 3, 5]),
([4, 2, 1, 3, 1], [0, 3]),
([1, 2, 2, 1], [2]),
([1, 2, 2, 3, 1], [3]),
([1, 3, 2, 2, 1], [1]),
([3, 2, 2, 3], [0, 3])
]

@pytest.mark.parametrize('inp,exp', test_cases)
def test_maxima(inp, exp):
    out = find_maxima(inp)
    assert exp == out

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
    out      = find_maxima(test_vec)

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
