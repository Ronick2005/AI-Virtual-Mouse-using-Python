from cvzone.HandTrackingModule import HandDetector
import cv2
import pyautogui

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.5, maxHands=1)

while True:
    # Get image frame
    success, img = cap.read()

    # Find the hand and its landmarks
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    
    # Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)

if lmList:
        # Find how many fingers are up
        fingers = detector.fingersUp()
        totalFingers = fingers.count(1)
        cv2.putText(img, f'Fingers:{totalFingers}', (bbox[0] + 200, bbox[1] - 30),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        if fingers[1] == 1 and fingers[2] == 0:
            cv2.rectangle(img, (framer, framer), (wcam-framer, hcam-framer), (255, 0, 255), 2)
            x3 = np.interp(x1, (framer, wcam-framer), (0, wscr))
            y3 = np.interp(y1, (framer, hcam-framer), (0, hscr))
            clocx = plocx + (x3 - plocx) / smooth
            clocy = plocy + (x3 - plocy) / smooth
            pyautogui.FAILSAFE = False
            pyautogui.moveTo(wscr - clocx, clocy)
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            plocx, plocy = clocx, clocy
                 
if lmList:
    if fingers[1] == 1 and fingers[2] == 1:
            length, img, lineinfo = detector.findDistance(8, 12, img)
            #print(length)
            if length < 40:
                cv2.circle(img, (lineinfo[4], lineinfo[5]), 15, (0, 255, 0), cv2.FILLED)
                pyautogui.click()
        # Find Distance Between Two Fingers
        #distance, img, info = detector.findDistance(8, 12, img)
        #cv2.putText(img, f'Dist:{int(distance)}', (bbox[0] + 400, bbox[1] - 30),
                    #cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        #if distance < 40:
                #cv2.circle(img, (lineinfo[4], lineinfo[5]), 15, (0, 255, 0), cv2.FILLED)
                #pyautogui.click()
               