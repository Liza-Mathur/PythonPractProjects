def merge_intervals(intervals):
    intervals.sort()  
    merged = []

    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)  # No overlap
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])  # Merge

    return merged

print(merge_intervals([[1,3], [2,6], [8,10], [15,18]]))
# [[1,6], [8,10], [15,18]]
