# Given
# a
# string
# s,
# return the
# longest
# palindromic
#
# substring
# in s.
# Example
# 1:
#
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also
# a
# valid
# answer.
# Example
# 2:
#
# Input: s = "cbbd"
# Output: "bb"
#
# Constraints:
#
# 1 <= s.length <= 1000
# s
# consist
# of
# only
# digits and English
# letters.
#
# Nếu s1 là xâu đối xứng thì bỏ 2 gtri 2 bên vẫn được 1 xâu đối xứng
# Vậy ta coi các phần từ là nhân, mở rộng ra 2 been với điều kiện s[left] = s[right] đ đc xâu lớn nhất

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    maxlen = 0
    maxPS = ""
    n = len(s)
    #Dxung loai 1, phan tu giua la 1 phan tu
    for i in range(n):
        step = 0
        while i-step >= 0 and i+step < n :
            if s[i-step] == s[i+step] :
                if maxlen < 2*step + 1:
                    maxlen = 2*step+1
                    maxPS = s[i - step: i + step + 1]
                step += 1
                continue
            else :
                # maxlen = max(maxlen, 2*step - 1)
                # maxPS = s[i-step+1 : i+step]
                break
      #Dxung loai 2: Phan tu trung tam la 2 phan tu
    for i in range(n-1) :
        if(s[i] == s[i+1]) :
            mid_l = i
            mid_r = i+1
            step = 0
            if maxlen < 2:
                maxlen = 2
                maxPS = s[i : i+2]
            while mid_l - step >= 0 and mid_r + step < n :
                if s[mid_l-step] == s[mid_r+step] :
                    if maxlen < 2*step + 2:
                        maxlen  = 2*step+2
                        maxPS = s[mid_l-step : mid_r + step +1]
                    step+=1
                    continue
                else:
                    break
    return maxPS




def longestPalindrome2(s : str) -> str :
    n = len(s)
    if n <= 1 :
        return s
    def expand_from_center(left, right) :
        while left >= 0 and right < n and s[left] == s[right] :
            left -= 1
            right += 1
        return s[left+1 : right]
    maxlen = 1
    maxS = s[0]
    for i in range(n-1) :
        oddS = expand_from_center(i, i)
        evenS = expand_from_center(i, i+1)

        if len(oddS) > maxlen :
            maxlen  = len(oddS)
            maxS = oddS
        if len(evenS) > maxlen :
            maxlen = len(evenS)
            maxS = evenS
    return maxS


#Dynamic Programming
"""
Lấy dp[l][r] thể hiện chuỗi s[l : r+1] có phải chuỗi đối xứng hay không
Điều kiệnể d[l][r] = 1 <=> s[l] = s[r] and d[l+1 : r] = 1
Khởi tạo d[i][i] = 1 với mọi i in range(len(s))
"""
def longestPalindrome3(s : str) -> str :
    n = len(s)
    if n < 2 :
        return s

    dp = [[0 for i in range(n)] for i in range(n)]
    maxlen = 1
    maxS = s[0]
   #init

    for l in range(n):
        dp[l][l] = 1

    for l in range(n-1, -1, -1) :
        for r in range(n-1, l, -1) :
            if s[l] == s[r] and (r-l <2 or dp[l+1][r-1]==1) :
                dp[l][r] = 1
                if maxlen <= r-l+1 :
                    maxlen  = r-l+1
                    maxS = s[l:r+1]
    return maxS






s = "aaaa"
print(longestPalindrome(s))
print(longestPalindrome2(s))
print(longestPalindrome3(s))
