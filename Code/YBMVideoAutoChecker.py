import pyautogui
import time
import os

os.system('mode con cols=60 lines=4')

i = 0
click_count = 0

while True:
    window_title = "title [" + str(click_count) + "] YBM 강의 영상 자동체크 프로그램 v0.1.2"
    os.system(window_title)
    try:
        original_btn_ok = pyautogui.locateOnScreen('ybmYellowYesBtn.png')
        center_btn_ok = pyautogui.center(original_btn_ok)
        print('>> Found!', center_btn_ok, '<<')
        time.sleep(1.1)
        pyautogui.click(center_btn_ok)
        x, y = center_btn_ok.x + 100, center_btn_ok.y
        pyautogui.moveTo(x, y)  #  마우스 커서가 이미지 인식을 방해하지 않게하기위해 마우스 커서 이동
        click_count += 1
        
        # 클릭이 안된 경우를 대비하여 동일 작업 반복
        original_btn_ok = pyautogui.locateOnScreen('ybmYellowYesBtn.png')
        center_btn_ok = pyautogui.center(original_btn_ok)
        pyautogui.click(center_btn_ok)
        x, y = center_btn_ok.x + 100, center_btn_ok.y
        pyautogui.moveTo(x, y)
        
        original_btn_ok = pyautogui.locateOnScreen('ybmYellowYesBtn.png')
        center_btn_ok = pyautogui.center(original_btn_ok)
        pyautogui.click(center_btn_ok)
        x, y = center_btn_ok.x + 100, center_btn_ok.y
        pyautogui.moveTo(x, y)
    except:
        print(str(i) + ': \'예\'버튼 Not Found.')
        i += 1
        time.sleep(0.5)