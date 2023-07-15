class ClosestMinMax:
    def function(self, array):

        max_value = float("-inf")
        min_value = float("inf")
        size_array = len(array)
        left = -1
        right = -1
        """finding min and max value of the array"""
        for i in range(size_array):
            if array[i] > max_value:
                max_value = array[i]
            if array[i] < min_value:
                min_value = array[i]

        """ check for minvalue assign i to left and check for maxvalue assign i to right"""

        for j in range(size_array):
            if array[j] == min_value :
                left = j
                if right >= 0:
                    return (right - left) + 1

            if array[j] == max_value:
                right = j
                if left >= 0:
                    return (right - left) + 1

array = list(map(int, input().split()))
object = ClosestMinMax()
print(object.function(array))
