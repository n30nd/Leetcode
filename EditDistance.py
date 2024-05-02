# Given
# two
# strings
# word1 and word2,
# return the
# minimum
# number
# of
# operations
# required
# to
# convert
# word1
# to
# word2.
#
# You
# have
# the
# following
# three
# operations
# permitted
# on
# a
# word:
#
# Insert
# a
# character
# Delete
# a
# character
# Replace
# a
# character
#
# Example
# 1:
#
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse(replace
# 'h'
# with 'r')
# rorse -> rose(remove
# 'r')
# rose -> ros(remove
# 'e')
# Example
# 2:
#
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation:
# intention -> inention(remove
# 't')
# inention -> enention(replace
# 'i'
# with 'e')
# enention -> exention(replace
# 'n'
# with 'x')
# exention -> exection(replace
# 'n'
# with 'c')
# exection -> execution(insert
# 'u')


def minDistance(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    m = len(word1) + 1
    n = len(word2) + 1

    dp = [[0]*n for _ in range(m)] #dp[i][j] is number of step to change from word1[0..i-1] to word2[0..j-1]

    for i in range(m):
        dp[i][0] = i #delete
    for j in range(n):
        dp[0][j] = j #insert

    for i in range(1, m) :
        for j in range(1, n) :
            if word1[i-1] == word2[j-1] :
                dp[i][j] = dp[i-1][j-1]
            else :
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    return dp[m-1][n-1]

word1 = "intention"
word2 = "execution"
print(minDistance(word1, word2))
