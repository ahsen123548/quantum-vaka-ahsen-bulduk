import os
import cv2
import numpy as np


def detect_red_squares(image_path, output_path='detected_result.jpg'):
  img = cv2.imread(image_path)
  if img is None:
    print(f'Görüntü yüklenemedi: {image_path}')
    return

  hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

  lower_red1 = np.array([0, 120, 70])
  upper_red1 = np.array([10, 255, 255])
  lower_red2 = np.array([170, 120, 70])
  upper_red2 = np.array([180, 255, 255])

  mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
  mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
  mask = cv2.bitwise_or(mask1, mask2)

  kernel = np.ones((5, 5), np.uint8)
  mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

  contours, _ = cv2.findContours(
      mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
  )

  for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > 300:
      peri = cv2.arcLength(cnt, True)
      approx = cv2.approxPolyDP(cnt, 0.04 * peri, True)

      if len(approx) == 4:
        x, y, w, h = cv2.boundingRect(approx)
        M = cv2.moments(cnt)
        if M['m00'] != 0:
          cX = int(M['m10'] / M['m00'])
          cY = int(M['m01'] / M['m00'])
        else:
          cX, cY = x + w // 2, y + h // 2

        cv2.drawContours(img, [approx], -1, (0, 255, 0), 3)
        cv2.circle(img, (cX, cY), 5, (0, 0, 255), -1)
        print(
            f'[TESPİT BAŞARILI] Alan: {int(area)} px | Merkez: (X: {cX}, Y:'
            f' {cY})'
        )

  cv2.imwrite(output_path, img)
  print(f'Sonuç kaydedildi: {output_path}')


if __name__ == '__main__':
  detect_red_squares('input_file_0.png')
