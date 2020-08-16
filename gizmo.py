import numpy as np


class Gizmo:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name)


def hello(name, country="Finland"):
    print(f"Hello {name}, how are things in {country}?")


def spell(word):
    print(".".join(word))


def relative_path(subject_identifiers):
    return [
        f"./subjects/mock_recording_{subject_identifier}.rec"
        for subject_identifier in subject_identifiers
    ]


def multiplication_table(zero_out_multiples=None):
    """Returns a multiplication table from 1 to 12

    The table shows you the results of multiplying two numbers. One number is along a row, the other down a column, and the results are shown where a row and column meet.

    Parameters
    ----------
    zero_out_multiples : int, optional
        When this parameter is set to an integer number, then the multiplication table that is returned by the function will have all multiples of the given number set to zero.

    Returns
    -------
    multiplication_table : ndarray
        Multiplication table
    """
    array = np.arange(1, 13)
    if zero_out_multiples:
        array[array % zero_out_multiples == 0] = 0
    return np.outer(array, array)
