def find_all_pairs_with_sum(nums, target):
    # Create an empty set to store the elements we've already seen
    seen = set()
    found_pairs = []  # List to store all pairs found
    
    # Iterate through the array
    for num in nums:
        # Calculate the complement of the current number
        complement = target - num
        
        # If the complement is already in the set, we have found a pair
        if complement in seen:
            found_pairs.append((num, complement))
        
        # Add the current number to the set
        seen.add(num)
    
    # If we found any pairs, print them
    if found_pairs:
        for pair in found_pairs:
            print(f"Pair found {pair}")
    else:
        print("Pair not found.")

# Example test cases
nums1 = [8, 7, 2, 5, 3, 1]
target1 = 10
find_all_pairs_with_sum(nums1, target1)  # Output: Pair found (8, 2) or (7, 3)

nums2 = [5, 2, 6, 8, 1, 9]
target2 = 12
find_all_pairs_with_sum(nums2, target2)  # Output: Pair not found.
