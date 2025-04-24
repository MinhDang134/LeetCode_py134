class Solution(object):
    def findNumbers(nums):
        count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
        return count

    nums1 = [555, 901, 482, 1771]
    n1 = findNumbers(nums1)
    print(n1)
    nums2 = [12, 345, 2, 6, 7896]
    n2 = findNumbers(nums2)
    print(n2)








