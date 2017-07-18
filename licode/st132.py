"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        dp=[[False]*len(s) for _ in range(len(s))]
        cut=[i for i in range(len(s))]

        for i in range(len(s)):
            for j in range(i+1):
                if s[i]==s[j] and (i-j<=1 or dp[j+1][i-1]):
                    dp[j][i]=True

                    import ipdb;ipdb.set_trace()

                    if j==0: cut[i]=0
                    else: cut[i]=min(cut[i],cut[j-1]+1)
        return cut[len(s)-1]

print Solution().minCut('aab')


""" # too good

public int minCut(String s) {
    int n = s.length();

	boolean dp[][] = new boolean[n][n];
	int cut[] = new int[n];

	for (int j = 0; j < n; j++) {
		cut[j] = j; //set maximum # of cut
		for (int i = 0; i <= j; i++) {
			if (s.charAt(i) == s.charAt(j) && (j - i <= 1 || dp[i+1][j-1])) {
				dp[i][j] = true;

				// if need to cut, add 1 to the previous cut[i-1]
				if (i > 0){
					cut[j] = Math.min(cut[j], cut[i-1] + 1);
				}else{
				// if [0...j] is palindrome, no need to cut
					cut[j] = 0;
				}
			}
		}
	}

	return cut[n-1];
}
"""


""" Palindrome Partition one
public static List<String> palindromePartitioning(String s) {

	List<String> result = new ArrayList<String>();

	if (s == null)
		return result;

	if (s.length() <= 1) {
		result.add(s);
		return result;
	}

	int length = s.length();

	int[][] table = new int[length][length];

	// l is length, i is index of left boundary, j is index of right boundary
	for (int l = 1; l <= length; l++) {
		for (int i = 0; i <= length - l; i++) {
			int j = i + l - 1;
			if (s.charAt(i) == s.charAt(j)) {
				if (l == 1 || l == 2) {
					table[i][j] = 1;
				} else {
					table[i][j] = table[i + 1][j - 1];
				}
				if (table[i][j] == 1) {
					result.add(s.substring(i, j + 1));
				}
			} else {
				table[i][j] = 0;
			}
		}
	}

	return result;
}
"""
