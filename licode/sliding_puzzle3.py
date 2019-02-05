import random


class SlidingGame(object):
    def __init__(self):
        tmp_list=[i for i in range(9)] # 0...8
        for i in range(9):
            ind=random.randint(i, 8)
            tmp_list[i], tmp_list[ind]=tmp_list[ind], tmp_list[i]
        self.board=''.join(map(str,tmp_list))

        self.board='123405678'

        self.col=3
        self.end='123456780'

    def slide(self):
        qu=[self.board]
        cnt=0
        visited=set(self.board)
        # error 1, missed visited. find: check validation before adding is much faster

        def moves(ind):
            # next_inds=[]
            if (ind + 1) % self.col != 0:
                yield ind+1
                # next_inds.append(ind + 1)
            if (ind - 1) % self.col != self.col - 1:
                yield ind-1
                # next_inds.append(ind - 1)
            if (ind + self.col) < len(self.board):
                yield ind+self.col
                # next_inds.append(ind + self.col)
            if (ind - self.col) >= 0:
                yield ind-self.col
                # next_inds.append(ind - self.col)
            # return next_inds

        while len(qu)>0:
            new=[]
            for status in qu:
                ind = status.index('0')
                if status==self.end: return cnt

                next_inds=moves(ind)
                for m in next_inds:
                    tmp=[ch for ch in status] # error 2, used self.board
                    tmp[ind], tmp[m]=tmp[m], tmp[ind]
                    new_status=''.join(tmp)
                    if new_status in visited:
                        continue
                    new.append(new_status)
                    visited.add(new_status)
            qu=new
            cnt+=1 # error 3, had put this in front
        return -1

sol=SlidingGame()
print sol.slide(), sol.board
