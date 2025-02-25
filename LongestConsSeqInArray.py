def find_longest_streak(nums):
    if not nums:
        return 0, []

    nums = sorted(set(nums)) 
    longest_streak = 0
    longest_sequence = []

    def find_streak(nums):
        if not nums:
            return 0, []

        min1 = nums.pop(0)  
        streak = 1
        sequence = [min1]

        while nums and nums[0] == min1 + 1:
            min1 = nums.pop(0)  
            streak += 1
            sequence.append(min1)

        next_streak, next_sequence = find_streak(nums)
        
        if streak > next_streak:
            return streak, sequence
        else:
            return next_streak, next_sequence

    return find_streak(nums)


length, sequence = find_longest_streak([100, 4, 200, 1, 3, 2])
print(f"Longest consecutive sequence length: {length}")
print(f"Longest consecutive sequence: {sequence}")
