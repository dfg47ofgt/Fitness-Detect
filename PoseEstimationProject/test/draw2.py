
import cv2
import numpy as np


canvas = np.zeros((480,300,3),dtype="uint8")

cv2.rectangle(canvas,(10,10),(290,94),(79 ,79 ,60), cv2.FILLED)
cv2.rectangle(canvas,(10,104),(290,188),(79 ,79 ,60), cv2.FILLED)
cv2.rectangle(canvas,(10,198),(290,282),(79 ,79 ,60), cv2.FILLED)
cv2.rectangle(canvas,(10,292),(290,376),(79 ,79 ,60), cv2.FILLED)
cv2.rectangle(canvas,(10,386),(290,470),(79 ,79 ,60), cv2.FILLED)     

#sport
cv2.putText(canvas, "Left Lift : " , (40, 45), cv2.FONT_HERSHEY_DUPLEX,0.85, (180,180,180), 2)
cv2.putText(canvas, "Right Lift : " , (40, 139), cv2.FONT_HERSHEY_DUPLEX,0.85, (180,180,180), 2)
cv2.putText(canvas, "Squat : " , (40, 233), cv2.FONT_HERSHEY_DUPLEX,0.85, (180,180,180), 2)
cv2.putText(canvas, "Push up : " , (40, 327), cv2.FONT_HERSHEY_DUPLEX,0.85, (180,180,180), 2)
cv2.putText(canvas, "Step Count:" , (20, 435), cv2.FONT_HERSHEY_DUPLEX,0.85, (180,180,180), 2)

# Curl Count

cv2.putText(canvas, "15", (200, 45), cv2.FONT_HERSHEY_DUPLEX, 0.8, (230,230,230), 2)
cv2.putText(canvas, "15", (200, 139), cv2.FONT_HERSHEY_DUPLEX, 0.8, (230,230,230), 2)
cv2.putText(canvas, "15", (200, 233), cv2.FONT_HERSHEY_DUPLEX, 0.8, (230,230,230), 2)
cv2.putText(canvas, "15", (200, 327), cv2.FONT_HERSHEY_DUPLEX, 0.8, (230,230,230), 2)
cv2.putText(canvas, "10000", (185, 435), cv2.FONT_HERSHEY_DUPLEX, 0.8, (230,230,230), 2)

# Draw Bar
per = 0
go = 190
cv2.rectangle(canvas, (25, 63), (210, 75), (230,230,230), 3)
cv2.rectangle(canvas, (25, 63), (go, 75), (230,230,230), cv2.FILLED)
cv2.putText(canvas, f'{int(per)} %', (225, 75), cv2.FONT_HERSHEY_DUPLEX, 0.6,(230,230,230), 1)

cv2.rectangle(canvas, (25, 157), (210, 169), (230,230,230), 3)
cv2.rectangle(canvas, (25, 157), (go, 169), (230,230,230), cv2.FILLED)
cv2.putText(canvas, f'{int(per)} %', (225, 169), cv2.FONT_HERSHEY_DUPLEX, 0.6,(230,230,230), 1)

cv2.rectangle(canvas, (25, 251), (210, 263), (230,230,230), 3)
cv2.rectangle(canvas, (25, 251), (go, 263), (230,230,230), cv2.FILLED)
cv2.putText(canvas, f'{int(per)} %', (225, 263), cv2.FONT_HERSHEY_DUPLEX, 0.6,(230,230,230), 1)

cv2.rectangle(canvas, (25, 345), (210, 357), (230,230,230), 3)
cv2.rectangle(canvas, (25, 345), (go, 357), (230,230,230), cv2.FILLED)
cv2.putText(canvas, f'{int(per)} %', (225, 357), cv2.FONT_HERSHEY_DUPLEX, 0.6,(230,230,230), 1)


# cv2.rectangle(canvas, (80, 165), (120, 450), (230,230,230), 3)
# cv2.rectangle(canvas, (80, int(bar)), (120, 450), color, cv2.FILLED)
#cv2.putText(canvas, f'{int(per)} %', (60, 155), cv2.FONT_HERSHEY_DUPLEX, 0.75,color, 1)

cv2.imshow('Image', canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()