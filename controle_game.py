import cv2
import mediapipe as mp
import numpy as np
import pyautogui
import time

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

last_action = ""
last_action_time = 0
debounce_delay = 0.3

def get_gesture(hand_landmarks):
    index_tip = hand_landmarks.landmark[8]
    index_mid = hand_landmarks.landmark[6]
    thumb_tip = hand_landmarks.landmark[4]
    thumb_mid = hand_landmarks.landmark[2]
    
    if thumb_tip.x < thumb_mid.x:
        if index_tip.y < index_mid.y:
            return "Jump"   
        else:
            return "Down"
    else:
        if index_tip.y < index_mid.y:
            return "Left"
        else:
            return "Right"

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break
    
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    
    current_gesture = "None"
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(
                frame, 
                hand_landmarks, 
                mp_hands.HAND_CONNECTIONS
            )
            
            current_gesture = get_gesture(hand_landmarks)
            current_time = time.time()
            if current_gesture != last_action and (current_time - last_action_time) > debounce_delay:
                print(f"Action: {current_gesture}")
                last_action = current_gesture
                last_action_time = current_time
                

                if current_gesture == "Jump":
                    pyautogui.press('up')
                elif current_gesture == "Left":
                    pyautogui.press('left')
                elif current_gesture == "Right":
                    pyautogui.press('right')
                elif current_gesture == "Down":
                    pyautogui.press('down')


    cv2.putText(frame, f"Gesture: {current_gesture}", (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    cv2.imshow("Hand Gesture Control", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
hands.close()