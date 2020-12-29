# Praca z obrazami - OpenCV + Python

Ładowanie i wyświetlanie obrazu
```
image = cv2.imread("images/car.jpg")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))

cv2_imshow(image)
```
![car](https://github.com/patryktk/175IC-machine-learning-21176/blob/main/LAb9/images/images/car.jpg)<br>
Otrzymywanie danych na temat poszczególnego piksela
```
(B, G, R) = image[150, 150]
print("R={}, G={}, B={}".format(R, G, B))
```
Zmiana rozmiaru obrazy bez uwzględniania ratio
```
resized = cv2.resize(image, (300, 300))
cv2.imwrite("images/resized-car.jpg", resized)
cv2_imshow(resized)
```
![resized-car](https://github.com/patryktk/175IC-machine-learning-21176/blob/main/LAb9/images/images/resized-car.jpg)<br>
Obliczanie ratio i resize poprawny
```
r = 300.0 / w
dim = (300, int(h * r))
fixed_resized = cv2.resize(image, dim)
cv2.imwrite("images/ratio-resized-car.jpg", fixed_resized)
cv2_imshow(fixed_resized)
```
![ratio-resized-car](https://github.com/patryktk/175IC-machine-learning-21176/blob/main/LAb9/images/images/ratio-resized-car.jpg)<br>

Resize obrazu z wykorzystaniem imutils
```
imutils_fixed_resized = imutils.resize(image,width=300)
cv2.imwrite("images/imutils-fixed-resize.jpg",imutils_fixed_resized)
cv2_imshow(imutils_fixed_resized)
```
![imutils-fixed-resize](https://github.com/patryktk/175IC-machine-learning-21176/blob/main/LAb9/images/images/imutils-fixed-resize.jpg)<br>
Obracanie obrazu
```
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, -45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imwrite("images/rotate-car.jpg",rotated)
cv2_imshow(rotated)
```
![car-rotate](https://github.com/patryktk/175IC-machine-learning-21176/blob/main/LAb9/images/images/rotate-car.jpg) <br>

Obracanie obrazu z wykorzstaniem imutils
```
rotated = imutils.rotate(image, -45)
cv2.imwrite("images/imutils-rotate-car.jpg",rotated)
cv2_imshow(rotated)
```
![imutils-rotate-car](https://github.com/patryktk/175IC-machine-learning-21176/blob/main/LAb9/images/images/imutils-rotate-car.jpg)<br>

Obracanie obrazu z wykorzstaniem imutils.rotate_bound
```
rotated = imutils.rotate_bound(image, 45)
cv2.imwrite("images/imutils-rotate-bound-car.jpg",rotated)
cv2_imshow(rotated)
```
![imutils-rotate-bound-car](https://github.com/patryktk/175IC-machine-learning-21176/blob/main/LAb9/images/images/imutils-rotate-bound-car.jpg)<br>

Rozmycie obrazu
```
blurred = cv2.GaussianBlur(image, (11, 11), 0)
cv2.imwrite("images/blurred-car.jpg",blurred)
cv2_imshow(blurred)
```
![blurred-car](https://github.com/patryktk/175IC-machine-learning-21176/blob/main/LAb9/images/images/blurred-car.jpg) <br>

Rysowanie po obrazie (kwadrat)
```
output = image.copy()
cv2.rectangle(output, (320, 60), (420, 160), (0, 0, 255), 2)
cv2.imwrite("images/car-draw-rectangle.jpg",output)
cv2_imshow(output)
```
![rectangle-draw-car](https://github.com/patryktk/175IC-machine-learning-21176/blob/main/LAb9/images/images/car-draw-rectangle.jpg) <br>

#Rysowanie po obrazie cz.2 (koło)
```
output_2 = image.copy()
cv2.circle(output_2, (300, 150), 20, (255, 0, 0), -1)
cv2.imwrite("images/car-draw-circle.jpg",output_2)
cv2_imshow(output_2)
```
![circle-draw-car](https://github.com/patryktk/175IC-machine-learning-21176/blob/main/LAb9/images/images/car-draw-circle_1.jpg) <br>

Rysowanie po obrazie cz.3 (linia)
```
output_3 = image.copy()
cv2.line(output_3, (60, 20), (400, 200), (0, 0, 255), 5)
cv2.imwrite("images/car-draw-line.jpg",output_3)
cv2_imshow(output_3)
```
![car-draw-line](https://github.com/patryktk/175IC-machine-learning-21176/blob/main/LAb9/images/images/car-draw-line.jpg)<br>

Dodawnie tekstu do obrazu
```
output_4 = image.copy()
cv2.putText(output_4, "OpenCV + 1970 Charger", (10, 25), 
	cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv2.imwrite("images/car-add-text.jpg",output_4)
cv2_imshow(output_4)
```
![car-add-text](https://github.com/patryktk/175IC-machine-learning-21176/blob/main/LAb9/images/images/car-add-text.jpg) <br>
Konwertowanie obrazu do odcieni szarości
```
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("images/car-gray.jpg",gray)
cv2_imshow(gray)
```
![car-gray](https://github.com/patryktk/175IC-machine-learning-21176/blob/main/LAb9/images/images/car-gray.jpg)
<br>
Wykrywanie krawędzi
```
edged = cv2.Canny(gray, 30, 150)
cv2.imwrite("images/car-edged.jpg",edged)
cv2_imshow(edged)
```
![car-edged](https://github.com/patryktk/175IC-machine-learning-21176/blob/main/LAb9/images/images/car-edged.jpg)
<br>
Progowanie - wyznaczanie poziomu jasności dla zdjęcia
```
thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]
cv2.imwrite("images/car-thresh.jpg",thresh)
cv2_imshow(thresh)
```
![car-thresh](https://github.com/patryktk/175IC-machine-learning-21176/blob/main/LAb9/images/images/car-thresh.jpg)
<br>
Znajdowanie oraz oznaczenie kontur
```
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
output_5 = image.copy()

for c in cnts:
  cv2.drawContours(output_5, [c], -1, (240, 0, 159), 10)
  
cv2.imwrite("images/car-drawContours.jpg", output_5)
cv2_imshow(output_5)
```
![car-conturs](https://github.com/patryktk/175IC-machine-learning-21176/blob/main/LAb9/images/images/car-drawContours.jpg)<br>
Erozja i dylatacja
```
mask = thresh.copy()
mask_2 = thresh.copy()
mask = cv2.erode(mask, None, iterations=2)
mask_2 = cv2.dilate(mask_2, None, iterations=5)
cv2.imwrite("images/car-eroded.jpg", mask)
cv2.imwrite("images/car-eroded.jpg", mask_2)
cv2_imshow(mask)
cv2_imshow(mask_2)
```
![car-eroded](https://github.com/patryktk/175IC-machine-learning-21176/blob/main/LAb9/images/images/car-eroded.jpg)<br>

Operacje maskowe i bitowe
```
mask_3 = thresh.copy()
output_6 = cv2.bitwise_and(image, image, mask=mask)
cv2.imwrite("images/car2-mask.jpg", output_6)
cv2_imshow(output_6)
```
![car-mask](https://github.com/patryktk/175IC-machine-learning-21176/blob/main/LAb9/images/images/car2-mask.jpg)
<br>
