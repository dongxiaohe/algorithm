class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            start, last = 0, len(image[0]) - 1
            while start <= last:
                image[i][start], image[i][last] = image[i][last] ^ 1, image[i][start] ^ 1
                start += 1
                last -= 1
        return image
