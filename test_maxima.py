import numpy as np
import pytest
from maxima_good import find_maxima_1

test_cases = [([0, 1, 2, 1, 2, 1, 0],[2,4]),([-i**2 for i in range(-3, 4)],[3]),([np.sin(2*alpha) for alpha in np.linspace(0.0, 5.0, 100)],[16,78]),([1,2,3],[1])]

@pytest.mark.parametrize('inp,exp',test_cases)

def test_maxima(inp,exp):
    out = find_maxima_1(inp)
    assert exp == out

