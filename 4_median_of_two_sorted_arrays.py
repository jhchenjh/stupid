# 23 Jan, 2020
# Runtime: 96 ms, faster than 15.15% of Python online submissions for Median of Two Sorted Arrays.
# Memory Usage: 11.8 MB, less than 100.00% of Python online submissions for Median of Two Sorted Arrays.

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        mid = (m+n)/2 + 1
        even = 0
        if (m+n)%2==0:
            even = 1
        id1 = 0
        id2 = 0
        this_num = 0
        last_num = 0
        for i in range(mid):
            last_num = this_num
            if id1<m and id2<n:
                if(nums1[id1]<nums2[id2]):
                    this_num = nums1[id1]
                    id1 += 1
                else:
                    this_num = nums2[id2]
                    id2 += 1
            else:
                if(id1>=m):
                    this_num = nums2[id2]
                    id2 += 1
                else:
                    this_num = nums1[id1]
                    id1 += 1
        if even==1:
            return (this_num+last_num)/2.0
        else:
            return this_num
