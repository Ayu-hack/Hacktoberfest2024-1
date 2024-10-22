def three_sum(nums):
    # Sort the array to simplify the problem
    nums.sort()
    result = []
    n = len(nums)
    
    # Iterate over the array
    for i in range(n):
        # Skip duplicates for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Early termination
        if nums[i] > 0:
            break
        
        # Two pointers approach
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                # Found a valid triplet
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for the second element
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicates for the third element
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            
            elif total < 0:
                # Move the left pointer to increase the sum
                left += 1
            else:
                # Move the right pointer to decrease the sum
                right -= 1
    
    return result
