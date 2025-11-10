


import os
import cv2
import numpy as np
import pyautogui
import time
from typing import Optional, Tuple

TEMPLATE_BTN_ATTACK_PATH = os.path.join(os.path.dirname(__file__), "img", "btn_attack.png")
TEMPLATE_BTN_FIND_A_MATCH_PATH = os.path.join(os.path.dirname(__file__), "img", "btn_find_a_match.png")
TEMPLATE_TROOP_BALLOON_PATH = os.path.join(os.path.dirname(__file__), "img", "troop_balloon.png")
TEMPLATE_TROOP_DRAGON_PATH = os.path.join(os.path.dirname(__file__), "img", "troop_dragon.png")
TEMPLATE_BTN_RETURN_HOME_PATH = os.path.join(os.path.dirname(__file__), "img", "btn_return_home.png")
TEMPLATE_TROOP_WARDEN_PATH = os.path.join(os.path.dirname(__file__), "img", "troop_hero_warden.png")
TEMPLATE_TROOP_MINION_PATH = os.path.join(os.path.dirname(__file__), "img", "troop_hero_minion.png")
TEMPLATE_TROOP_QUEEN_PATH = os.path.join(os.path.dirname(__file__), "img", "troop_hero_queen.png")
TEMPLATE_TROOP_ROYAL_PATH = os.path.join(os.path.dirname(__file__), "img", "troop_hero_royal.png")
TEMPLATE_TROOP_BAT_PATH = os.path.join(os.path.dirname(__file__), "img", "spell_bat.png")
TEMPLATE_TROOP_MACHINE_BALLON_PATH = os.path.join(os.path.dirname(__file__), "img", "troop_machine_balloon.png")
TEMPLATE_BTN_FINISH_MATCH_PATH = os.path.join(os.path.dirname(__file__), "img", "btn_finish_match.png")


loc1 = (367, 753)

minion_loc = None
queen_loc = None
royal_loc = None
warden_loc = None


def _screenshot_bgr() -> np.ndarray:
    img = pyautogui.screenshot()
    frame = np.array(img)[:, :, ::-1]
    return frame

def _load_template(path: str) -> np.ndarray:
    if not os.path.isfile(path):
        raise FileNotFoundError(f"Template not found: {path}")
    tmpl = cv2.imread(path, cv2.IMREAD_COLOR)
    if tmpl is None:
        raise RuntimeError(f"Failed to read template: {path}")
    return tmpl

def _match_template(frame_bgr: np.ndarray, template_bgr: np.ndarray, threshold: float = 0.9) -> Optional[Tuple[int, int]]:
    res = cv2.matchTemplate(frame_bgr, template_bgr, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < threshold:
        return None
    h, w = template_bgr.shape[:2]
    cx, cy = max_loc[0] + w // 2, max_loc[1] + h // 2
    return (cx, cy)

def getBtnAttack():
    try:
        isloading = True
        while isloading : 
            time.sleep(1)
            frame = _screenshot_bgr()
            template = _load_template(TEMPLATE_BTN_ATTACK_PATH)
            pt = _match_template(frame, template, threshold=0.7)
            if pt is None:
                print("Btn Attack not found.")
                isloading = True
            else :
                isloading = False
                pyautogui.moveTo(pt[0], pt[1], duration=0.25)
                time.sleep(1)
                print(f"Moved mouse to Btn Attack at {pt}")

    except Exception as e:
        print(f"Error in getBtnAttack: {e}")
        return None

def getBtnFindMatch() :
    try:
        frame = _screenshot_bgr()
        template = _load_template(TEMPLATE_BTN_FIND_A_MATCH_PATH)
        pt = _match_template(frame, template, threshold=0.3)
        if pt is None:
            print("Btn Find A Match not found.")
            return None
        pyautogui.moveTo(pt[0], pt[1], duration=0.25)
        time.sleep(1)
        print(f"Moved mouse to Btn Find A Match at {pt}")
        return pt
    except Exception as e:
        print(f"Error in getBtnFindMatch: {e}")
        return None

def getTroopBalloon() :
    try:
        frame = _screenshot_bgr()
        template = _load_template(TEMPLATE_TROOP_BALLOON_PATH)
        pt = _match_template(frame, template, threshold=0.6)
        if pt is None:
            print("Troop Balloon not found.")
            return None
        pyautogui.moveTo(pt[0], pt[1], duration=0.25)
        time.sleep(1)
        pyautogui.click()
        print(f"Moved mouse to Troop Balloon at {pt}")
        return pt
    except Exception as e:
        print(f"Error in getTroopBalloon: {e}")
        return None

def getTroopDragon() :
    try:
        frame = _screenshot_bgr()
        template = _load_template(TEMPLATE_TROOP_DRAGON_PATH)
        pt = _match_template(frame, template, threshold=0.6)
        if pt is None:
            print("Troop Dragon not found.")
            return None
        pyautogui.moveTo(pt[0], pt[1], duration=0.25)
        time.sleep(1)
        pyautogui.click()
        print(f"Moved mouse to Troop Dragon at {pt}")
        return pt
    except Exception as e:
        print(f"Error in getTroopDragon: {e}")
        return None

def getHeroWarden() :
    try:
        global warden_loc
        frame = _screenshot_bgr()
        template = _load_template(TEMPLATE_TROOP_WARDEN_PATH)
        pt = _match_template(frame, template, threshold=0.6)
        if pt is None:
            if warden_loc is None:
                print("Hero Warden not found.")
                return None
        warden_loc = pt
        pyautogui.moveTo(pt[0], pt[1], duration=0.25)
        time.sleep(1)
        pyautogui.doubleClick()
        print(f"Moved mouse to Hero Warden at {pt}")
        return warden_loc
    except Exception as e:
        print(f"Error in getHeroWarden: {e}")
        return None

def getHeroMinion() :
    try:
        global minion_loc
        frame = _screenshot_bgr()
        template = _load_template(TEMPLATE_TROOP_MINION_PATH)
        pt = _match_template(frame, template, threshold=0.6)
        if pt is None:
            if minion_loc is None:
                print("Hero Minion not found.")
                return None
        minion_loc = pt
        pyautogui.moveTo(pt[0], pt[1], duration=0.25)
        time.sleep(1)
        pyautogui.doubleClick()
        print(f"Moved mouse to Hero Minion at {pt}")
        return minion_loc
    except Exception as e:
        print(f"Error in getHeroMinion: {e}")
        return None

def getHeroQueen() :
    try:
        global queen_loc
        frame = _screenshot_bgr()
        template = _load_template(TEMPLATE_TROOP_QUEEN_PATH)
        pt = _match_template(frame, template, threshold=0.6)
        if pt is None:
            if queen_loc is None:
                print("Hero Queen not found.")
                return None
        
        queen_loc = pt
        pyautogui.moveTo(pt[0], pt[1], duration=0.25)
        time.sleep(1)
        pyautogui.doubleClick()
        print(f"Moved mouse to Hero Queen at {pt}")
        return queen_loc
    except Exception as e:
        print(f"Error in getHeroQueen: {e}")
        return None

def getHeroRoyal() :
    try:
        global royal_loc
        frame = _screenshot_bgr()
        template = _load_template(TEMPLATE_TROOP_ROYAL_PATH)
        pt = _match_template(frame, template, threshold=0.6)
        if pt is None:
            if royal_loc is None:
                print("Hero Royal not found.")
                return None
        royal_loc = pt
        pyautogui.moveTo(pt[0], pt[1], duration=0.25)
        time.sleep(1)
        pyautogui.doubleClick()
        print(f"Moved mouse to Hero Royal at {pt}")
        return royal_loc
    except Exception as e:
        print(f"Error in getHeroRoyal: {e}")
        return None

def getSpellBat() :
    try:
        frame = _screenshot_bgr()
        template = _load_template(TEMPLATE_TROOP_BAT_PATH)
        pt = _match_template(frame, template, threshold=0.6)
        if pt is None:
            print("Spell Bat not found.")
            return None
        pyautogui.moveTo(pt[0], pt[1], duration=0.25)
        time.sleep(1)
        pyautogui.click()
        print(f"Moved mouse to Spell Bat at {pt}")
        return pt
    except Exception as e:
        print(f"Error in getSpellBat: {e}")
        return None

def getMachineBalloon() :
    try:
        frame = _screenshot_bgr()
        template = _load_template(TEMPLATE_TROOP_MACHINE_BALLON_PATH)
        pt = _match_template(frame, template, threshold=0.6)
        if pt is None:
            print("Machine Balloon not found.")
            return None
        pyautogui.moveTo(pt[0], pt[1], duration=0.25)
        time.sleep(1)
        pyautogui.click()
        print(f"Moved mouse to Machine Balloon at {pt}")
        return pt
    except Exception as e:
        print(f"Error in getMachineBalloon: {e}")
        return None

def getBtnFindNextMatch() :
    print("getBtnFindNextMatch")

def moveMouseToCenterOfScreen() :
    screen_width, screen_height = pyautogui.size()
    center_x, center_y = screen_width // 2, screen_height // 2
    pyautogui.moveTo(center_x, center_y, duration=0.25)

def getBtnReturnHome() :
    time.sleep(5)
    isLoading = True
   
    
    while isLoading:
        frame = _screenshot_bgr()
        template = _load_template(TEMPLATE_BTN_RETURN_HOME_PATH)
        pt = _match_template(frame, template, threshold=0.7)
        if pt is None:
            print("Btn Return Home not found.")
            isLoading = False
        else :
            pyautogui.moveTo(pt[0], pt[1], duration=0.25)
            print(f"Moved mouse to Btn Return Home at {pt}")
            print(str(isLoading))
            isLoading = True
        
        time.sleep(1)

def getBtnFinishMatch() :
    time.sleep(5)
    isLoading = True

    while isLoading:
        frame = _screenshot_bgr()
        template = _load_template(TEMPLATE_BTN_FINISH_MATCH_PATH)
        pt = _match_template(frame, template, threshold=0.7)

        if pt is None:
            print("Btn Finish Match not found.")
            isLoading = True
        else :
            pyautogui.moveTo(pt[0], pt[1], duration=0.25)
            print(f"Moved mouse to Btn Finish Match at {pt}")
            print(str(isLoading))
            isLoading = False
        
        time.sleep(1)
    
    pyautogui.moveTo(pt[0], pt[1], duration=0.25)
    

def click():
    time.sleep(0.1)
    pyautogui.click()

def getLocation() :
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr)
        time.sleep(2)

def deployTroop(num) :
    for i in range(num):
        time.sleep(0.1)
        click()
        

def moveToLoc(loc) :
    time.sleep(1)
    pyautogui.moveTo(loc[0], loc[1], duration=0.25)

def DragDown(start: Optional[Tuple[int, int]] = None, distance: int = 500, duration: float = 0.4):
    """Click left and drag the mouse downward.
    - start: (x, y) to begin drag; if None, use current cursor
    - distance: pixels to drag down (positive = down)
    - duration: seconds for the drag movement
    """
    try:
        if start is not None:
            pyautogui.moveTo(start[0], start[1], duration=0.2)
        pyautogui.mouseDown(button='left')
        pyautogui.moveRel(max(1, distance), max(1, distance), duration=duration)
        pyautogui.mouseUp(button='left')
        print(f"Dragged down from {start if start else 'current'} by {distance} px")
    except Exception as e:
        print(f"Error in leftClickAndDragDown: {e}")

def run():
    
    moveMouseToCenterOfScreen()
    
    # getLocation()

    # new match
    getBtnAttack()
    time.sleep(3)
    click()
    time.sleep(3)
    getBtnFindMatch()
    time.sleep(1)
    click()

    # finding match
    getBtnReturnHome()
    time.sleep(2)
    DragDown()
    time.sleep(2)
    # play match
    # getTroopBalloon()
    # time.sleep(1)
    # moveToLoc(loc1)
    # deployTroop(40)
    # time.sleep(1)

    # deploy Dragon
    getTroopDragon()
    time.sleep(0.5)
    moveToLoc(loc1)
    deployTroop(20)

    # deploy Machine Balloon
    getMachineBalloon()
    time.sleep(0.5)
    moveToLoc(loc1)
    deployTroop(3)


    # deploy Hero Warden
    getHeroWarden()
    time.sleep(0.5)
    moveToLoc(loc1)
    deployTroop(3)

    # deploy Hero Royal
    getHeroRoyal()
    time.sleep(0.5)
    moveToLoc(loc1)
    deployTroop(3)
    time.sleep(1)
    getHeroRoyal()


    # deploy Spell Bat
    getSpellBat()
    time.sleep(1)
    moveToLoc(loc1)
    time.sleep(0.5)
    deployTroop(15)
    time.sleep(1)

    # deploy Hero Minion
    getHeroMinion()
    time.sleep(0.5)
    moveToLoc(loc1)
    deployTroop(3)
    time.sleep(1)
    getHeroMinion()

    # deploy Hero Queen
    getHeroQueen()
    time.sleep(0.5)
    moveToLoc(loc1)
    deployTroop(3)
    time.sleep(1)
    getHeroQueen()


    print("warden spelling")
    getHeroWarden()

    getBtnFinishMatch()
    
    time.sleep(5)
    click()
    print("done")

if __name__ == "__main__":
    while True:
        run()
