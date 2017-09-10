# -*- coding: utf-8 -*-

import cv2
import sys

if __name__ == '__main__':
	image = cv2.imread(sys.argv[1])
	image = cv2.cvtColor(image,cv2.COLOR_BGR2LAB)
	image[:,:,1] = 127
	image = cv2.cvtColor(image,cv2.COLOR_LAB2BGR)
	cv2.imwrite('out.jpg',image)
