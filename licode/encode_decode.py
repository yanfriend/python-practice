class Codec(object):
    def encode(self,strs):
        return ''.join('{}:'.format(len(s))+s for s in strs)

    def decode(self,s):
        i=0; ret=[]
        while i<len(s):
            end=s.find(':',i)
            str_len=int(s[i:end])
            word=s[end+1:(end+1+str_len)]
            ret.append(word)
            i=end+str_len+1
        return ret

encoded=Codec().encode(['abc','ee','a','ddd'])
print encoded
print Codec().decode(encoded)

