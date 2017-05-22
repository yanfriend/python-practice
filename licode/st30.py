"""
30. Substring with Concatenation of All Words

You are given a string, s, and a list of words, words, that are all of the same length.
Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once
and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
"""
import collections
import copy


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        total_words=len(words)
        if total_words==0: return []
        word_len=len(words[0])
        counter=collections.Counter(words)

        ret=[]
        for i, ch in enumerate(s):
            if i>len(s)-total_words*word_len: break # not enough letters
            if self.check_word(s[i:i+total_words*word_len], counter,total_words,word_len): ret.append(i)
        return ret

    def check_word(self, str_val, counter, total_words,word_len):
        cnt_tmp=collections.Counter() # copy.deepcopy(counter)

        for i in range(total_words):
            tmp_word=str_val[i*word_len: (i+1)*word_len]
            if not tmp_word in counter: return False
            cnt_tmp[tmp_word]+=1
            if cnt_tmp[tmp_word]>counter[tmp_word]: return False

        return True


