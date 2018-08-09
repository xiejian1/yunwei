import cv2 as cv

#读取图像，支持 bmp、jpg、png、tiff 等常用格式
#cv.putText(img="sightseen01.jpg",text="I love you",org=(0,10),fontFace=cv.FONT_HERSHEY_SCRIPT_SIMPLEX,fontScale=2,color='red')
#cv.getTextSize()
img = cv.imread("sightseen01.jpg")
#创建窗口并显示图像
cv.namedWindow("Image",cv.WINDOW_AUTOSIZE)
cv.imshow("Image",img)
cv.waitKey(0)
#释放窗口
cv.destroyAllWindows()