class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
		numDict={}
		for idx, val in enumerate(nums):
		    if numDict.get(val, True) == True:
		        numDict[val]=idx
		    else:
		    	# print "test"
		        preValue=numDict[val]
		        # newlist=[preValue+1, idx+1]
		        if not isinstance(preValue, list):
					newlist=[preValue+1, idx+1]
					numDict[val]=newlist
		        else:
		        	preValue.append(idx)
		        	numDict[val]=preValue
		        # newlist=preValue+idx
		        # print newlist
		        
		# numSet=set(nums)
		print numDict
		while nums:
			fristNum = nums.pop()
			# print "########"
			# print fristNum
			secondNum = target - fristNum
			# print secondNum
			testEle=numDict.get(secondNum, "NoEle")
			# print testEle
			# if fristNum == secondNum:
			# 	print "succe"
			if testEle != "NoEle" and not isinstance(testEle, list) and fristNum != secondNum:
				# print "test1"
			# if index2 in numDict.keys():
				index1 = numDict[fristNum]
				index2 = numDict[secondNum]
				if index1 > index2:
					return [index2+1, index1+1]
				else:
					return [index1+1, index2+1]
			elif isinstance(testEle, list) and secondNum == fristNum:
				# print "test"
				return testEle
		return None

# class Solution:
#     # @return a tuple, (index1, index2)
#     def twoSum(self, num, target):
#         index1, index2, total = 0, len(num)-1, 0
#         sortedNum = sorted(enumerate(num), key=lambda x:x[1])
#         print sortedNum
#         while index1 != index2:
#         	print sortedNum[index1][0]
#             print sortedNum[index1][1]
#             total = sortedNum[index1][1] + sortedNum[index2][1]
#             if total == target:
#                 if sortedNum[index1][0] > sortedNum[index2][0] :
#                     return (sortedNum[index2][0]+1, sortedNum[index1][0]+1)
#                 else:
#                     return (sortedNum[index1][0]+1, sortedNum[index2][0]+1)
#             elif total > target:
#                 index2 -= 1
#             else:
#                 index1 += 1

#         return (-1, -1)

if __name__ == '__main__':
	print Solution().twoSum([2,1,6], 8)