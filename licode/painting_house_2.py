class Solution:
    # @param {int[][]} costs n x k cost matrix
    # @return {int} an integer, the minimum cost to paint all houses
    def minCostII(self, costs):
        # Write your code here
        n=len(costs)
        k=len(costs[0])

        pre_cost=0
        pre_ind=0
        second_cost=0
        for i in range(n):
            for j in range(k):
                costs[i][j]+=(pre_cost if j!=pre_ind else second_cost)

            curr_cost=float('inf'); curr_sec_cost=float('inf'); curr_ind=0
            for j in range(k):
                if costs[i][j]<curr_cost:
                    curr_sec_cost,curr_cost=curr_cost,costs[i][j]
                    curr_ind=j
                elif costs[i][j]<curr_sec_cost:
                    curr_sec_cost=costs[i][j]

            pre_cost,second_cost,pre_ind=curr_cost,curr_sec_cost,curr_ind
        return min(costs[-1])

print Solution().minCostII([[14,2,11],[11,14,5],[14,3,10]])

