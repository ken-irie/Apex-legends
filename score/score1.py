import cv2
import matplotlib.pyplot as plt
import os
import os.path
import math
import openpyxl
import youtube_dl
import sys

args = sys.argv
#args[0]:score.py
#args[1]:url
url  = args[1]

def movie(url):
    ydl = youtube_dl.YoutubeDL({'outtmpl':'%(title)s.%(ext)s','format':'best'})
    # print('URL')
    # url = input()

    with ydl:
        result = ydl.extract_info(
        url,
        download=True
        )

movie(url)

# def save_all_frames(video_path, dir_path, basename, ext='jpg'):
#     cap = cv2.VideoCapture(video_path)

#     if not cap.isOpened():
#         return

#     os.makedirs(dir_path, exist_ok=True)
#     base_path = os.path.join(dir_path, basename)

#     digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

#     n = 0

#     while True:
#         ret, frame = cap.read()
#         if ret:
#             cv2.imwrite('{}_{}.{}'.format(base_path, str(n).zfill(digit), ext), frame)
#             n += 1
#         else:
#             return

# def get_distance(x1, y1, x2, y2):
    
#     d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
#     return d


# def score_shooting(start, end):
#     summation = 0
#     num = 0
#     points = 0
    
#     for i in range(int(start),int(end)):
#         i = str(i)
#         i = i.zfill(3)
#         name_iamge = name + i + types
#         image_path = os.path.join(img_dir_path, name_iamge)
#         img = cv2.imread(image_path)
#         print(image_path)
#     #     cv2.imshow('image_000', img)
#     #     cv2.waitKey(0)
#     #     cv2.destroyAllWindows()
#         print(name_iamge)
#         height, width = img.shape[:2]
#         img_x_center = width / 2#画像の中心（ｘ）
#         img_y_center = height / 2#画像の中心（y）
#         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         mato = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))
#         new_name = 'result_' + i +'.jpg'
#         mato_path = os.path.join(result_img_path, new_name)
#     #    print(mato_path)
#         #顔領域を赤色の矩形で囲む
#         for (x, y, w, h) in mato:
#             if 500 < x < 700 and 300 < y < 390:#真中のマトだけ抽出

#                 cv2.rectangle(img, (x, y), (x + w, y+h), (0,0,200), 3)
#     #            print(x,y)
#                 x_center = int(x) + int(w)/2
#                 y_center = int(y) + int(h)/2
#     #            print(int(x) + int(w)/2, int(y) + int(h)/2)
#                 #print(w,h)
#                 cv2.imwrite(mato_path, img)


#     #           if __name__ == '__main__':
#                 d = get_distance(x_center, y_center, img_x_center, img_y_center)
# #                print(d)
#                 d = round(d)
#                 num += 1 
#                 if 0 < d <w/10:
#                     point = 5
#                 elif w/10 < d <= w/5:
#                     point = 4
#                 elif w/5 < d <= w/3:
#                     point = 3
#                 elif w/3 < d <= w/2:
#                     point = 2
#                 elif w/2 < d <= w:
#                     point = 1
#                 else:
#                     point = 0






#                 print('{}個目のデータ'.format(num))
#                 summation = summation + d
#                 print('距離：{}'.format(d))
#                 print('距離の合計：{}'.format(summation))
#                 points = points + point
#                 average = points / num
#                 print('ポイント：{}'.format(point))
#                 print('合計ポイント：{}'.format(points))
#                 print('平均：{}'.format(average))
#                 print('-----------------')
#                 return points, average


# def main(movie_name,base_img_name):

#     file_path = 'C:\\Users\\kenta\\Desktop\\apex\\jissou\\score'
#     movie_path = os.path.join(file_path,movie_name)
#     #img_path = os.path.join(file_path,'data_jpg')
#     img_dir_path = os.path.join(file_path, base_img_name)
#     img_dir = os.makedirs(img_dir_path, exist_ok=True)
#     result_img = 'reslult_' + base_img_name
#     result_img_path = os.path.join(file_path, result_img)
#     result_img_dir = os.makedirs(result_img_path, exist_ok=True)
#     save_all_frames(movie_path, img_dir_path, base_img_name)

#     path = 'C:\\Users\\kenta\\Desktop\\apex\\jissou\\score'
#     name = base_img_name +'_'
#     types = '.jpg'
#     cascade = cv2.CascadeClassifier("C:\\Users\\kenta\\Desktop\\apex\\jissou\\opencvcascade2\\cascade\\cascade.xml")



#     points, average = score_shooting(start, end)

#     print('------------------------------------------')
#     print('------------------------------------------')
#     print('合計ポイント：{}'.format(points))
#     final_average = round(average)
#     print('最終結果：{}'.format(final_average))

#     # if average < 3:
#     #     print('スコア(0~5):5')
        
#     # elif 5 <= average < 8:
#     #     print('スコア(0~5):4')
        
#     # elif 8 <= average < 11:
#     #     print('スコア(0~5):3')
        
#     # elif 11 <= average < 14:
#     #     print('スコア(0~5):2')
        
#     # elif 14 <= average < 15:
#     #     print('スコア(0~5):1')

#     # else:
#     #     print('スコア(0~5):0')
                    



#     #     # 結果画像を保存
#     #           cv2.imwrite(mato_path, img)


#     # #結果画像を表示
#     # #         cv2.imshow('image_000', img)
#     # #         cv2.waitKey(0)
#     # #         cv2.destroyAllWindows()