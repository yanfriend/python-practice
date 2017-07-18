import Queue
import collections


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counter=collections.Counter(tasks)
        qu=Queue.PriorityQueue()
        for k,v in counter.items():
            qu.put((-v, k))  # -cout, char
        ret=0

        while not qu.empty():
            org_size=qu.qsize()
            tmp=[]
            for i in range(min(qu.qsize(),n+1)):
                minus_cnt, ch=qu.get()
                minus_cnt+=1
                if minus_cnt!=0:
                    tmp.append((minus_cnt,ch))

            for tt in tmp:
                qu.put(tt)

            if qu.qsize()>0:
                ret+=n+1
            else:
                ret+=org_size

        return ret

print Solution().leastInterval(['A','A','A','B','B','B'],2) # output 8: a,b,-,a,b,-,a,b
print Solution().leastInterval(['A','A','A','B','B','B','C','C'],2) # output 8
print Solution().leastInterval(['A','A','A','B','B','B'],0) # output 6
