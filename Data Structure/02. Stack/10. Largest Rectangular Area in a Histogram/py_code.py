'''
Largest Rectangular Area in a Histogram.

Find the largest rectangular area possible in a given histogram where the 
largest rectangle can be made of a number of contiguous bars. For simplicity, 
assume that all bars have same width and the width is 1 unit.

For example, consider the following histogram with 7 bars of heights {6, 2, 5, 4, 5, 1, 6}. 
The largest possible rectangle possible is 12.
'''

def find_max_area(histogram):
    '''
    Function to calculate largest rectangular area in a histogram.

    Arguments:
    histogram -- list, containing height of each histogram.

    Returns:
    max_area -- int, the max area of the ranctangle in the histogram.
    '''
    max_area = 0
    stack = []
    index = 0

    while index < len(histogram):
        if (not stack) or histogram[index] >= histogram[stack[-1]]:
            stack.append(index)
            index += 1
        
        else:
            top_index = stack.pop()

            area = histogram[top_index] * (index - stack[-1] - 1) if stack else index

            max_area = max(area, max_area)

            print(index, top_index, area, max_area)
    
    while stack:
        top_index = stack.pop()

        area = histogram[top_index] * (index - stack[-1] - 1) if stack else index

        max_area = max(area, max_area)
        print(max_area)

    return max_area

histogram = [6, 2, 5, 4, 5, 1, 6]
print(find_max_area(histogram))
