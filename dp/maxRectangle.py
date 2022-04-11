import collections
def find_largest_rectangle(heights, widths):
    # heights = heights + [0]
    # widths = widths + [0]
    # num_buildings = len(heights)
    # Candidate = collections.namedtuple('Candidate', ['index', 'height'])
    # left_candidates = []
    # largest_area = 0
    # for right in range(num_buildings):
    #     height = heights[right]
    #     # Left pointer of the next candidate to be created.
    #     next_left = right
    #     while left_candidates and left_candidates[-1].height >= height:
    #         left = left_candidates[-1].index
    #         i, j = left, right
    #         width = sum(widths[i:j])
    #         area = width * left_candidates[-1].height
    #         largest_area = max(largest_area, area)
    #         # Possible next candidate by trimming down the building.
    #         next_left = left
    #         del left_candidates[-1]
    #     left_candidates.append(Candidate(index=next_left, height=height))
    # return largest_area
    
    max_area = 0
    heights, widths = heights + [0], widths + [0]
    Candidate = collections.namedtuple('Candidate', ['index', 'height'])
    stack = []
    for right in range(len(heights)):
        next_left = right
        while stack and heights[right] <= stack[-1].height:
            left, h = stack[-1].index, stack[-1].height
            w = sum(widths[left:right])
            area = h * w
            max_area = max(max_area, area)
            next_left = left
            stack.pop()
        stack.append(Candidate(index=next_left, height=heights[right]))    
    return max_area

if __name__ == '__main__':
    test_cases = [
        # ([5, 6, 8, 1, 5], [1, 2, 1, 1, 1]),
        # ([1],[2]),
        # ([1, 2, 3, 4, 5], [1, 1, 1, 1, 1]),
        # ([5, 4, 3, 2, 1], [1, 1, 1, 1, 1]),
        ([1, 1, 5, 4, 1, 5, 1], [1, 1, 1, 1, 1, 1, 1])
    ]
    ans = []

    for i in range(len(test_cases)):
        output = find_largest_rectangle(test_cases[i][0], test_cases[i][1])
        try:
            # assert output == ans[i]
            print(output)
        except AssertionError:
            print(f"Error: Test {i}, Output is {output}")

#       -
#       -
#   - - -
# - - - -   -
# - - - -   -
# - - - -   -
# - - - -   -
# - - - - - -

#     -
#     -
#   - -
# - - -   -
# - - -   -
# - - -   -
# - - -   -
# - - - - -