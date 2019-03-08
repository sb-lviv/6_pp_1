from Gauss import Matrix


def test_simple():
    Matrix(100).gauss()


def test_parallel():
    Matrix(100).gauss_parallel()
