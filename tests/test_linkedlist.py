import pytest

from datastructure.linkedlist import LinkedList


@pytest.fixture
def sample_linked_list():
    l = LinkedList()

    l.append(1)
    l.append(2)
    l.append(3)

    return l


def test_append(sample_linked_list):
    sample_linked_list.append(4)
    assert sample_linked_list.get() == [1, 2, 3, 4]


def test_prepend(sample_linked_list):
    sample_linked_list.prepend(0)
    assert sample_linked_list.get() == [0, 1, 2, 3]


def test_insertAt(sample_linked_list):
    assert sample_linked_list.get() == [1, 2, 3]
