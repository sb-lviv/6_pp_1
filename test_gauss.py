import pytest
from Gauss import Matrix


@pytest.fixture
def M():
    return Matrix(500)


def test_simple(M):
    M.gauss()


def test_parallel(M):
    M.gauss_parallel()
