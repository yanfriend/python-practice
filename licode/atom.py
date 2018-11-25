import collections

class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        cnt_dict = collections.defaultdict(int)
        ind = [0] * 1
        cnt_dict = self.parse_formula(formula, ind)
        ans = []
        for k in sorted(cnt_dict):
            ans.append(k) if cnt_dict[k] == 1 else ans.append(k + str(cnt_dict[k]))
        return ''.join(ans)

    def parse_formula(self, formula, ind):
        cnt_dict = collections.defaultdict(int)
        while ind[0] < len(formula) and formula[ind[0]]!=')':
            if formula[ind[0]] == '(':
                ind[0] += 1  # skip ()
                dict1 = self.parse_formula(formula, ind)
                ind[0] += 1  # skip )
            else:
                atom = self.parse_unit(formula, ind)
                dict1 = {atom: 1}
            num1 = self.parse_num(formula, ind)
            for k in dict1.keys():
                cnt_dict[k] += dict1[k]*num1
        return cnt_dict

    def parse_num(self, formula, ind):
        init_ind = ind[0]
        while ind[0] < len(formula) and formula[ind[0]].isdigit():
            ind[0] += 1
        if init_ind == ind[0]: return 1
        return int(formula[init_ind:ind[0]])

    def parse_unit(self, formula, ind):
        init_ind = ind[0];
        ind[0] += 1
        while ind[0] < len(formula) and formula[ind[0]].islower():
            ind[0] += 1
        return formula[init_ind:ind[0]]

print Solution().countOfAtoms("(OH)2")        #  ("H2O")
