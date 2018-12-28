import collections


class Solution(object):
    def wordsAbbreviation(self, words):
        """
        :param self:
        :param words: a list of string
        :return:
        """
        self.gmap={}
        self.helper(words,0)
        return [self.gmap[w] for w in words]

    def helper(self, words, size):
        word_abbr=collections.defaultdict(list)
        for w in words:
            word_abbr[self.abbr(w, size)].append(w)

        for k, v in word_abbr.iteritems():
            if len(v)==1:
                self.gmap[v[0]]=k
            else:
                self.helper(v, size+1)

    def abbr(self,word, size): # return abbreviated word
        if len(word)<=size+3: return word
        return word[0:size+1] + str(len(word)-size-2) + word[-1]


print Solution().wordsAbbreviation(["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"])
# ['l2e', 'god', 'internal', 'me', 'i6t', 'interval', 'inte4n', 'f2e', 'intr4n']

