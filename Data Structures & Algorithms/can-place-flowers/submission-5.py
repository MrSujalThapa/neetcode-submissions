class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:    
        nextElement = 0
        for i, flower in enumerate(flowerbed):
            if n == 0:
                return True
            elif flower == 0:
                if i + 1 < len(flowerbed):
                    nextElement = flowerbed[i+1]
                if i == 0:
                    if nextElement == 0:
                        flowerbed[i] == 1
                        n -= 1
                else:
                    prev = flowerbed[i-1]
                    if prev == 0 and nextElement == 0:
                        flowerbed[i] == 1
                        n -= 1
        
        return n == 0