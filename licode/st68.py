class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        ret=[]
        line=[]
        words_len=0
        for w in words:
            if words_len+len(line)+len(w)<=maxWidth:
                words_len+=len(w)
                line.append(w)
                continue
            # now line is for one line.
            ret.append(self.format_line(line,words_len,maxWidth))
            line=[w] # dont forget to add current in. note 1
            words_len=len(w)

        # process last line, in line.
        last_line=' '.join(line)
        ret.append(last_line+' '*(maxWidth-len(last_line)))
        return ret

    def format_line(self,line,words_len,maxWidth):
        if len(line)==1: # case for one word only, note 2
            return line[0]+' '*(maxWidth-words_len)
        ret=''
        space=len(line)-1
        rem=maxWidth-words_len
        div=rem/space
        mod=rem%space
        for i in range(len(line)-1): # seperate spaces, note 3
            if i<mod:
                ret+=line[i]+' '*(div+1)
            else:
                ret+=line[i]+' '*div
        ret+=line[-1]
        return ret


# print Solution().fullJustify([""],2)
# print Solution().fullJustify([""],0)
print Solution().fullJustify(["a","b","c","d","e"],3)
