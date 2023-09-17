def _bs(self, item, left, right):
        """searches for item using `left` and `right` indices instead of slicing"""

        while right - left > 1:
            median = (right + left) // 2
            if item < self._L[median]:
                right = median 
            else:
                left = median
        return right > left and self._L[left] == item