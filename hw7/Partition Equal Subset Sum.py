class Solution:
    @staticmethod
    def canPartition(nums):
        total_sum = sum(nums)
        # If the total sum is odd, it cannot be divided evenly
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        # Create a DP array that tracks possible sums
        dp = [False] * (target + 1)
        dp[0] = True  # There is always a way to make sum 0, which is by taking no elements

        # Process each number in the array
        for num in nums:
            # Update the dp array from right to left
            for j in range(target, num - 1, -1):
                if dp[j - num]:
                    dp[j] = True

        # The result is whether the target can be achieved
        return dp[target]

# Example usage
sol = Solution()
print(sol.canPartition([1, 5, 11, 5]))  # Output: true
print(sol.canPartition([1, 2, 3, 5]))  # Output: false
