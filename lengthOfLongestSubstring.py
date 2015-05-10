class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
    	largest=0
        for x in xrange(0,len(s)):
        	cSet=set()
        	currentlen=0
        	for y in xrange(x,len(s)):
        		if s[y] not in cSet:
        			cSet.add(s[y])
        			currentlen+=1
        		else:
        			break
        	if currentlen>largest:
        		largest=currentlen
        	if largest == len(s) - x:
        		break
        print largest

if __name__ == '__main__':
    Solution().lengthOfLongestSubstring("bbbbbb")