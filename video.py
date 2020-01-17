import cv2
import numpy as np
import csv
import pytesseract

bb = []
with open('bounding_boxes.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
      temp=[]
      for r in row:
        temp.append(int(r))
      bb.append(temp)

cap = cv2.VideoCapture('C:/WorkSpace/goalPrediction/temp_vids/FIFA 19 2020-01-11 16-34-44-1.m4v')
 
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out_radar = cv2.VideoWriter('temp_vids/radar.avi',fourcc, 60, (bb[0][2],bb[0][3]))
# out_time = cv2.VideoWriter('temp_vids/time.avi',fourcc, 60, (2*bb[1][2],2*bb[1][3]))
# out_on = cv2.VideoWriter('temp_vids/on.avi',fourcc, 60, (3*bb[2][2],3*bb[2][3]))
# out_opl = cv2.VideoWriter('temp_vids/opl.avi',fourcc, 60, (bb[3][2],bb[3][3]))
# out_mn = cv2.VideoWriter('temp_vids/mn.avi',fourcc, 60, (3*bb[4][2],3*bb[4][3]))
# out_mpl = cv2.VideoWriter('temp_vids/mpl.avi',fourcc, 60, (bb[5][2],bb[5][3]))
# out_oteam = cv2.VideoWriter('temp_vids/oteam.avi',fourcc, 60, (bb[6][2],bb[6][3]))
# out_mteam = cv2.VideoWriter('temp_vids/mteam.avi',fourcc, 60, (bb[7][2],bb[7][3]))
# out_board = cv2.VideoWriter('temp_vids/board.avi',fourcc, 60, (bb[8][2],bb[8][3]))

with open('ouput.csv','w') as f1:
  writer=csv.writer(f1, delimiter='\t',lineterminator='\n',)
  while True:
      ret, frame = cap.read()
      if ret == True:
        if bb:
          # radar = frame[int(bb[0][1]):int(bb[0][1]+bb[0][3]), int(bb[0][0]):int(bb[0][0]+bb[0][2])]
          # out_radar.write(radar)

          time = frame[int(bb[1][1]):int(bb[1][1]+bb[1][3]), int(bb[1][0]):int(bb[1][0]+bb[1][2])]
          time = pytesseract.image_to_string(time, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789:')

          oteam = frame[int(bb[6][1]):int(bb[6][1]+bb[6][3]), int(bb[6][0]):int(bb[6][0]+bb[6][2])]
          oteam = pytesseract.image_to_string(oteam, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ')

          mteam = frame[int(bb[7][1]):int(bb[7][1]+bb[7][3]), int(bb[7][0]):int(bb[7][0]+bb[7][2])]
          mteam = pytesseract.image_to_string(mteam, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ')

          board = frame[int(bb[8][1]):int(bb[8][1]+bb[8][3]), int(bb[8][0]):int(bb[8][0]+bb[8][2])]
          board = pytesseract.image_to_string(board, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789-')

          on = frame[int(bb[2][1]):int(bb[2][1]+bb[2][3]), int(bb[2][0]):int(bb[2][0]+bb[2][2])]
          on = pytesseract.image_to_string(on, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')

          opl = frame[int(bb[3][1]):int(bb[3][1]+bb[3][3]), int(bb[3][0]):int(bb[3][0]+bb[3][2])]
          opl = pytesseract.image_to_string(opl, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ')        

          mn = frame[int(bb[4][1]):int(bb[4][1]+bb[4][3]), int(bb[4][0]):int(bb[4][0]+bb[4][2])]
          mn = pytesseract.image_to_string(mn, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')

          mpl = frame[int(bb[5][1]):int(bb[5][1]+bb[5][3]), int(bb[5][0]):int(bb[5][0]+bb[5][2])]
          mpl = pytesseract.image_to_string(mpl, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ')

          writer.writerow([time, oteam, mteam, board, on, opl, mn, mpl])
          # print([time, oteam, mteam, board, on, opl, mn, mpl])
        else:
            break
      
  cap.release()

# on = pytesseract.image_to_string(frame_on, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
# mn = pytesseract.image_to_string(frame_mn, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
# mpl = pytesseract.image_to_string(frame_mpl, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ')
# mteam = pytesseract.image_to_string(frame_mteam, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ')
# opl = pytesseract.image_to_string(frame_opl, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ')
# oteam = pytesseract.image_to_string(frame_oteam, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ')
# time = pytesseract.image_to_string(frame_time, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789:')