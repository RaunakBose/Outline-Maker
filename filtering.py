import numpy as np


class Filtering:

    def __init__(self, image):
        self.image = image

    def get_laplacian_filter(self):
        result = np.ones((3, 3))
        result[1, 1] = -8
        return result

    def addPadding(self, filter_size):
        result = np.ones((len(self.image) + (filter_size - 1), len(self.image[0]) + (filter_size - 1)))
        for i in range(filter_size - 1, len(result)):
            for j in range(filter_size - 1, len(result[0])):
                result[i, j] = self.image[i - (filter_size - 1), j - (filter_size - 1)]

        return result

    def invertImage(self, image):
        return 255 - image

    def getOutline(self):
        filter_size = 3
        specifiedfilter = self.get_laplacian_filter()
        padded = self.addPadding(filter_size)
        result_img = np.zeros(self.image.shape)
        for i in range(len(result_img)):
            for j in range(len(result_img[0])):
                sum = 0
                for u in range(i, i + filter_size):
                    for v in range(j, j + filter_size):
                        sum += specifiedfilter[u - i, v - j] * padded[u][v]
                result_img[i, j] = round(sum)
        return self.invertImage(result_img)
