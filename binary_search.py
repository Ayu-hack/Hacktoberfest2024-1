def binary_search(arr, target):
    """
    Binary Search Algorithm - Hacktoberfest 2024 Contribution
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Example usage
if __name__ == "__main__":
    numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 7
    
    result = binary_search(numbers, target)
    
    if result != -1:
        print(f"Element {target} found at index {result}")
    else:
        print(f"Element {target} not found in the array")
