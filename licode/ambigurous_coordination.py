import itertools


class Solution(object):
    def ambiguousCoordinates(self, S):
        def add_point(frag):
            N = len(frag)
            for d in xrange(1, N + 1):
                left = frag[:d]
                right = frag[d:]
                if ((not left.startswith('0') or left == '0')
                        and (not right.endswith('0'))):
                    yield left + ('.' if d != N else '') + right

        S = S[1:-1]  # remove '(', ')'

        # for i in xrange(1, len(S)):
        #     print S[:i], list(add_point(S[:i])), ' ', S[i:], list(add_point(S[i:]))

        return ["({}, {})".format(*cand)
                for i in xrange(1, len(S))
                for cand in itertools.product(add_point(S[:i]), add_point(S[i:]))]


print Solution().ambiguousCoordinates("(0123)")
