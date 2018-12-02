from enum import Enum
from skimage.feature import hessian_matrix, hessian_matrix_eigvals
import cv2


class DetectionType(Enum):
    CUSTOM = 1
    OPENCV = 2


class RidgeDetector:

    def detect_ridges(self, image, detection_type):
        if detection_type == DetectionType.CUSTOM:
            out_image = self.__detect_using_custom(image)
        elif detection_type == DetectionType.OPENCV:
            out_image = self.__detect_using_opencv(image)
        else:
            out_image = self.__detect_using_opencv(image)

        return out_image

    def __detect_using_custom(self, image):
        return image

    def __detect_using_opencv(self, image):
        ridge_filter = cv2.ximgproc.RidgeDetectionFilter_create()
        ridges = ridge_filter.getRidgeFilteredImage(image)
        return ridges