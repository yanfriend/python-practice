"""
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
"""

class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret=0
        factor=1
        while n/factor>0:
            high_num=n/factor/10
            curr_digit=n/factor%10
            low_num=n%factor

            if curr_digit==0:
                ret+=high_num*factor
            elif curr_digit==1:
                ret+=high_num*factor+low_num+1
            else:
                ret+=(high_num+1)*factor

            factor *= 10
        return ret

"""
对这个数字的每一位求存在1的数字的个数。从个位开始到最高位。

举个例子54215，比如现在求百位上的1，54215的百位上是2。可以看到xx100到xx199的百位上都是1，这里xx从0到54，即100->199, 1100->1199…54100->54199,
这些数的百位都是1，因此百位上的1总数是55*100。

如果n是54125,这时由于它的百位是1，先看xx100到xx199，其中xx是0到53，即54*100, 然后看54100到54125，这是26个。所以百位上的1的总数是54*100 + 26.

如果n是54025，那么只需要看xx100到xx199中百位上的1，这里xx从0到53，总数为54*100

求其他位的1的个数的方法是一样的。


public class Solution {
    public int countDigitOne(int n) {
        if (n<=0) return 0;

        long ret=0;
        long factor=1;
        while (n/factor>0) {
            long currentDigit = n/factor%10;
            long highNum = n/(factor*10);
            long lowNum = n%factor;
            switch ((int)currentDigit) {
                case 0: ret += highNum*factor; break;
                case 1: ret += highNum*factor + lowNum +1; break;
                default: ret += (highNum+1)*factor;
            }
            factor *= 10;
        }
        return (int)ret;
    }
}

n, factor, currD, highN, lowN, ret
13, 1,      3,     1,     0,    (1+1)*1=2,    ?
13, 10,     1,     0,     3,    0*10+3+1=4

"""
