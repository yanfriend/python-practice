def kSmallestPairs(nums1, nums2, k):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :type k: int
    :rtype: List[List[int]]
    """

    """
    the code is not right, as ind can move back.

    Input:
    [1,1,2]
    [1,2,3]
    10
    Output:
    [[1,1],[1,1],[2,1],[2,2],[2,3]]
    Expected:
    [[1,1],[1,1],[2,1],[1,2],[1,2],[2,2],[1,3],[1,3],[2,3]]

    pq:
    (2,0,0),3 0 1,4 0 2, add: 2 1 0,


    correct one:

        if not nums1 or not nums2: return []

        pq=[]
        for i,n1 in enumerate(nums1):
            heapq.heappush(pq, (n1+nums2[0],i, 0))
        ret=[]
        while pq and len(ret)<k:
            _,i,j=heapq.heappop(pq)
            ret.append([nums1[i],nums2[j]])
            if j+1<len(nums2):
                heapq.heappush(pq, ( nums1[i]+nums2[j+1],i,j+1))
        return ret

    """

    if not nums1 or not nums2: return []

    nums1.append(float('inf'))
    nums2.append(float('inf'))
    curr1=curr2=0
    ret=[]

    for ind in range(k):
        ret.append([nums1[curr1],nums2[curr2]])

        if nums1[curr1+1]+nums2[curr2]==nums1[curr1]+nums2[curr2+1]==float('inf'):
            break
        if nums1[curr1+1]+nums2[curr2]>nums1[curr1]+nums2[curr2+1]:
            curr2+=1
        else:
            curr1+=1
    return ret

print kSmallestPairs([1,7,11],[2,4,6],3)
print kSmallestPairs([1,1,2],[1,2,3],2)
print kSmallestPairs([1,2],[3],3)
