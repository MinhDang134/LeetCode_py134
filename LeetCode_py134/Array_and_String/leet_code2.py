# Đầu vào: l1 = [2,4,3], l2 = [5,6, 4]
#  Đầu ra: [7,0,8]
#  Giải thích: 342 + 465 = 807.
# Ví dụ 2:
#
# Đầu vào: l1 = [0], l2 = [0]
#  Đầu ra: [0]
# Ví dụ 3:
#
# Đầu vào: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
#  Đầu ra: [8,9,9,9,0,0,0,1]


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        mang_array =[]
        count = 0
        i = 0
        j = 0
        while i< len(l1) or j<len(l2):
            total = l1[i] + l2[j] + count
            count = total // 10
            mang = total % 10
            mang_array.append(mang)
            i +=1
            j +=1
        return mang_array



l1 = [2,4,3]
l2 = [5,6,4]
s = Solution()
minhdang=s.addTwoNumbers(l1,l2)
print(minhdang)
