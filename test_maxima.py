import numpy as np
import pytest
from maxima_good import find_maxima_1

test_cases = [(3,1),(10,1),(7,1)]

@pytest.mark.parametrize('numEl,SeedVal',test_cases)

def test_randomized(numEl,SeedVal):
 
    RandNumGen = np.random.RandomState(seed=SeedVal)

    test_vec = RandNumGen.random_integers(low=1,high=20,size=numEl)
    out      = find_maxima_1(test_vec)

    numMax = len(out);

    for i in range(0,numMax):

        iE = out[i];

        if iE == 0:

            assert test_vec[0] > test_vec[1]

        elif iE == numEl - 1:

            assert test_vec[numEl-1] > test_vec[numEl-2]

        else:

            assert test_vec[iE-1] < test_vec[iE] and test_vec[iE+1] < test_vec[iE]

