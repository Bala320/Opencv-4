from cv2 import *;
import  numpy as np
import matplotlib.pyplot as plt
img=imread("C:\\Users\\HP\\PycharmProjects\\Image_processing\\venv\\image\\opencvlogo.png")
#img=cvtColor(img,COLOR_BGR2RGB)
img2=imread("C:\\Users\\HP\\PycharmProjects\\Image_processing\\venv\\image\\elon_musk_tesla_3036.jpg")
img=resize(img,(400,400))
#img2=resize(img2,(500,500))
(b,g,r)=cv2.split(img)
[b1,g1,r1]=cv2.split(img2)
img_matplotlib =cv2.merge([r,g,b])
img_2=cv2.merge([r1,g1,b1])
img_cog=np.concatenate((img,img_matplotlib),axis=1)
#img_cong2=np.concatenate((img2,img_2),axis=1)
imshow("2 img in same ",img_cog)
#imshow("musk",img_cong2)
plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(img_matplotlib)
plt.show()
waitKey(0)
destroyAllWindows()