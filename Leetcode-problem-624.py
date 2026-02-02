# problem- 624(medium level)

# solution

# Memory Trick to Remember:-

# When problem says:

# sorted arrays

# max distance

# pick from different arrays

# Think:

# “Only edges matter.”
# “Track global min and max.”

def maxDistance(arrays):
    min_val = arrays[0][0]
    max_val = arrays[0][-1]
    max_dist = 0

    for i in range(1, len(arrays)):
        curr_min = arrays[i][0]
        curr_max = arrays[i][-1]

        max_dist = max(
            max_dist,
            abs(curr_max - min_val),
            abs(max_val - curr_min)
        )

        min_val = min(min_val, curr_min)
        max_val = max(max_val, curr_max)

    return max_dist