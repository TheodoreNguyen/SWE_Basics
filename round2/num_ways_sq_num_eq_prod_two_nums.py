class Solution:
    def __init__(self):
        pass
    def numType(self, numsX, numsY):
        # square values in numsX
        squared = []
        i = 0
        while i != len(numsX):
            squared.append(numsX[i] * numsX[i])
            i += 1
        print(str(squared))
        
        #multiply values in numsY
        multiplied = []
        j = 0
        while j != len(numsY) - 1:
            k = j + 1
            while k != len(numsY):
                multiplied.append(numsY[j] * numsY[k])
                
                k += 1
            j += 1
        print(str(multiplied))
        
        #compare 
        count = 0
        for square in squared:
            for product in multiplied:
                if square == product:
                    count += 1
        
        return count
        
    def numTriplets(self, nums1, nums2) -> int:
    
        print('nums1=' + str(nums1))
        print('nums2=' + str(nums2))
        
        print('Type1')
        type1 = self.numType(nums1, nums2)
        print('Type2')
        type2 = self.numType(nums2, nums1)
        
        print(type1 + type2)
        return (type1 + type2)
        
        
def main():
    A = Solution()
    nums1 = [7,4]
    nums2 = [5,2,8,9]
    nums1 = [1,1]
    nums2 = [1,1,1]
    nums1 = [7,7,8,3]
    nums2 = [1,2,9,7]
    nums1 = [4,7,9,11,23]
    nums2 = [3,5,1024,12,18]
    A.numTriplets(nums1, nums2)
        
if __name__ == '__main__':
    main()
        