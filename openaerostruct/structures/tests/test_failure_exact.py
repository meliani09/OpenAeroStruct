import unittest

from openaerostruct.structures.failure_exact import FailureExact
from openaerostruct.utils.testing import run_test, get_default_surf_dict


class Test(unittest.TestCase):

    def test(self):
        surface = get_default_surf_dict()

        comp = FailureExact(surface=surface)

        run_test(self, comp)


if __name__ == '__main__':
    unittest.main()