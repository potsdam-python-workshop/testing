def pytest_addoption(parser):
    parser.addoption("--seed", type=int, help="random generator seed")
