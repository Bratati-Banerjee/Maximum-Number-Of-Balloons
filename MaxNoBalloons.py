class Solution(object):
    	def maxNumberOfBalloons(self, text):
		"""
		:type text: str
		:rtype: int
		"""
		target='balloon'
		ch_num=dict.fromkeys(target,0)

		for ch in text:
			if ch in target:
				ch_num[ch]+=1
		ch_num['l']=int(ch_num['l']/2)
		ch_num['o']=int(ch_num['o']/2)

		return min(ch_num.values())


sol = Solution()

text = "nlaebolko"
text = "loonbalxballpoon"
text = "leetcode"

res = sol.maxNumberOfBalloons(text)
print(res)