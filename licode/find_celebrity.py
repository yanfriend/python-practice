"""
Find the Celebrity
Suppose you are at a party with n people (labeled from 0 ton - 1) and among them, there may exist one celebrity.
The definition of a celebrity is that all the othern - 1 people know him/her but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one.
The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B.
You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a functionint findCelebrity(n),
your function should minimize the number of calls toknows.
Note: There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party.
If there is no celebrity, return-1.
"""

class Sulution(object):
    def findCelebrity(self, n):
        if not n: return -1
        ret=0
        for i in range(1,n):
            if knows(ret, i):
                ret=i
        for i in range(n):
            if i==ret: continue
            if not knows(i,ret) or knows(ret,i): return -1
        return ret
