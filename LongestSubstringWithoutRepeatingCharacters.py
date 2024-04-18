# Given a string s, find the length of the longest
# substring
#  without repeating characters.
# Example
# 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The
# answer is "abc",
# with the length of 3.
# Example
# 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The
# answer is "b",
# with the length of 1.
# Example
# 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The
# answer is "wke",
# with the length of 3.
# Notice
# that
# the
# answer
# must
# be
# a
# substring, "pwke" is a
# subsequence and not a
# substring.
#
# Constraints:
#
# 0 <= s.length <= 5 * 104
# s
# consists
# of
# English
# letters, digits, symbols and spaces.

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    n = len(s)
    maxlen = 0
    for i in range(n) :
        dic = {}
        currLen = 0
        for j in range(i, n):
            if  dic.get(s[j]) == None :
                dic[s[j]] = 1
                currLen += 1
            else :
                break
        maxlen = max(maxlen, currLen)

    return maxlen

# l là chỉ mục trái cho phần tử đầu tiên của chuỗi con
# r là chri mục sau phần tử cuối cùng của chuỗi con
# tìm độ dài lớn nhất của các chuỗi con bắt đầu từ l, ta
# tawng dần r cho đến khi gặp phần tử trùng hoặc đã chạy hết chuỗi cha
# Ở đây sau mỗi lần lawjp l, ta 0 làm mới r mà tasi sử dụng
# từ thằng l trước vì chuỗi con dài nhất bắt đầu từ l+1 sẽ có r >= r của chuỗi bắt đầu từ l
# Do đó, nó tiết kiệm thời gian hơn so với cách 1
def lengthOfLongestSubstring2(s):
    """
    :type s: str
    :rtype: int
    """
    n = len(s)
    maxlen = 0
    dic = {}
    r = 0
    for l in range(n) :
        while r < n and dic.get(s[r]) is None:
            dic[s[r]] = 1
            r += 1
        dic.pop(s[l])
        maxlen = max(maxlen, r-l)
    return maxlen

s = "abcabcbb"
print(lengthOfLongestSubstring2(s))
