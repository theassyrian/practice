import math
import unittest


def get_permutations_aux(l, c, res):
    if not l:
        # Copy c here
        res.append(c[:])
    else:
        for i in range(len(l)):
            c.append(l[i])
            get_permutations_aux(l[:i] + l[i + 1:], c, res)
            c.pop()


def get_permutations(l):
    """Get permutations of a list (of integers)"""
    res = []
    c = []
    get_permutations_aux(l, c, res)
    return res


def get_string_permutations(s):
    """
    Get permutations of a given string `s`
    Return a list of strings
    """
    if len(s) == 0:
        return ['']
    else:
        perms = []
        for i, char in enumerate(s):
            rest_chars = s[:i] + s[i + 1:]
            rest_perms = get_string_permutations(rest_chars)
            for _perm in rest_perms:
                perms.append(_perm + char)
        return perms


def get_string_permutations_alt_aux(s, c, res):
    """
    :param s: source string
    :param c: candidate extension sequence
    :param res: a list for storing permutations (list of strings)
    """
    if not s:
        res.append(''.join(c[:]))
    else:
        for i in range(len(s)):
            c.append(s[i])
            get_string_permutations_alt_aux(s[:i] + s[i + 1:], c, res)
            c.pop()


def get_string_permutations_alt(s):
    res = []
    c = []
    get_string_permutations_alt_aux(s, c, res)
    return res


class TestPermutation(unittest.TestCase):
    def _test_get_string_permutations(self, func=get_string_permutations):
        s1 = ''
        perms1 = func(s1)
        self.assertEqual(len(perms1), 1)
        assert '' in perms1
        s2 = 'abcd'
        f = math.factorial(len(s2))
        perms2 = func(s2)
        self.assertEqual(len(perms2), f)
        current = perms2[0]
        assert len(current) == len(s2)
        for i in range(1, f):
            _current = perms2[1]
            assert len(_current) == len(s2)
            for c in s2:
                assert c in _current
            assert _current != current
            _current = current

    def test_get_string_permutations(self):
        self._test_get_string_permutations(get_string_permutations)

    def test_get_string_permutations_alt(self):
        self._test_get_string_permutations(get_string_permutations_alt)


if __name__ == '__main__':
    #unittest.main()
    a = [1, 2, 3, 4]
    print get_permutations(a)
