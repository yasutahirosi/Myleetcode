#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s.strip())>0:
            last=s.split()[-1]
            return len(last)
        else:
            return 0
# @lc code=end


