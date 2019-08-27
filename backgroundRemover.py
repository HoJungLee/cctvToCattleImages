# 원래 한 파일에 추적기 저장기 배경지우기 모여있어서 
# 코드를 짠 나도 잘 못알보겠어서 따로 정리 중
# 오류나 느린 부분을 다른 함수나 
# GPU로 처리할 수 있을 것 같은데 
# 지금은 시간이 없다.


# 패키지가 이것이 맞는지 잘 모르겠음
import matplotlib.pyplot as plt
import cv2
import sys
import PIL.Image


# 지우는 코드 1
# 이미지와 마스크 정보를 받아서 
# 마스크외에 전부 파란색으로 바꿔줍니다.
def apply_mask(image, mask):
    image[:, :, 0] = np.where(
        mask == 0,
        125,
        image[:, :, 0]
    )
    image[:, :, 1] = np.where(
        mask == 0,
        12,
        image[:, :, 1]
    )
    image[:, :, 2] = np.where(
        mask == 0,
        15,
        image[:, :, 2]
    )
    return image


# 지우는 코드 2
# 사용 시 주의사항
# 지우는 코드 1을 바로 보내면 오류 남
# 이미지 형식 바꾸기 위해 cv2쓰면 사진들이 푸른색을 띄는 오류 남
# 그래서 지우는 코드 1을 png파일로 저장했다가 다시 읽는 방법을 사용해야 합니다. 

def transparent_back(image):

    image = image.convert("RGBA")

    L,H = image.size
    color_0 = (15,12,125,255)
    for h in range(H):
        for l in range(L):
            dot = (l, h)
            color_1 = image.getpixel(dot)
            if color_1 == color_0:
                color_1 = color_1[:-1] + (0,)
                image.putpixel(dot, color_1)

    return image
