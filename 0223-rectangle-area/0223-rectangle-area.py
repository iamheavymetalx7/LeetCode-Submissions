class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        x_left = max(ax1,bx1)
        x_right=min(ax2,bx2)

        y_left=max(ay1,by1)
        y_right=min(ay2,by2)

        x_ = x_right - x_left
        y_ = y_right - y_left

        comm=0
        area = abs((ax1-ax2)*(ay1-ay2))+abs((bx1-bx2)*(by1-by2))

        if x_>0 and y_>0:
            comm = x_*y_
            area-=comm
        return area
