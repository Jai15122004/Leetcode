class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxi= values[0]  
        maxj = -10000000000
        
        for j in range(1, len(values)):
            maxj = max(maxj, maxi + values[j] - j)
            maxi = max(maxi, values[j] + j)
        return maxj
# TIME COMPLEXITY : O(N)
# SPACE COMPLEXITY : O(1)
