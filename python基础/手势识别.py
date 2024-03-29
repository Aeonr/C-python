import cv2
import mediapipe as mp
import math

def findhands(img,hands,draw):
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    
    handlmsstyle = draw.DrawingSpec(color=(0,255,180),thickness=3)
    handconstyle = draw.DrawingSpec(color=(255,180,130),thickness=3)
    
    
    results = hands.process(imgRGB)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            draw.draw_landmarks(img,handLms,mp.solutions.hands.HAND_CONNECTIONS,handlmsstyle,handconstyle)


cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
hands = mp.solutions.hands.Hands()
draw = mp.solutions.drawing_utils


while True:
    ret,img=cap.read()
    
    if ret:
        hand_landmarks = findhands(img, hands, draw)
        cv2.imshow("test",img)
        
    if cv2.waitKey(1) == ord('q'):
        break
    

dist_thresh= 215 


def findhands(img,hands,draw):
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    
    
    handlmsstyle = draw.DrawingSpec(color=(0,0,255),thickness=5)
    handconstyle = draw.DrawingSpec(color=(0,255,0),thinkness=5)
    
    results = hands.process(imgRGB)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            draw.draw_landmarks(img,handLms,mp.solutions.hands.HAND_CONNECTIONS,handlmsstyle,handconstyle)
    
    return results.multi_hand_landmarks

def detectednumber(hand_landmarks,img):
    h,w,c=img.shape
    
    
    myHand = hand_landmarks[0]
    hand_landmarks = myHand.landmark
    
    print(myHand)
    
    thumb_tip_id = 4
    index_finger_tip_id = 8
    middle_finger_tip_id = 12
    ring_finger_tip_id = 16
    pinky_tip_id = 20
    pinky_mcp_id = 17
    
    
    
    
    thumb_tip_id = 4
    index_finger_tip_id = 8
    middle_finger_tip_id = 12
    ring_finger_tip_id = 16
    pinky_tip_id = 20
    pinky_mcp_id = 17
    
    thumb_tip_y = hand_landmarks[thumb_tip_id]. y * h
    index_finger_tip_y = hand_landmarks[index_finger_tip_id]. y * h
    middle_finger_tip_y = hand_landmarks[middle_finger_tip_id]. y * h
    ring_finger_tip_y = hand_landmarks[ring_finger_tip_id].y * h
    pinky_tip_y = hand_landmarks[pinky_tip_id].y * h
    pinky_mcp_y = hand_landmarks [pinky_mcp_id].y * h
    
    thumb_tip_x = hand_landmarks [thumb_tip_id].x*w
    index_finger_tip_x = hand_landmarks[index_finger_tip_id].x * w
    middle_finger_tip_x = hand_landmarks[middle_finger_tip_id].x * w
    ring_finger_tip_x = hand_landmarks[ring_finger_tip_id].x * w
    pinky_tip_x = hand_landmarks[pinky_tip_id].x * w
    pinky_mcp_x = hand_landmarks[pinky_mcp_id].x * w
    
    dist_thumb2index = math.sqrt((thumb_tip_x - index_finger_tip_x)**2 + (thumb_tip_y - index_finger_tip_y)**2)
    dist_thumb2middle = math.sqrt((thumb_tip_x - middle_finger_tip_x)**2 + (thumb_tip_y - middle_finger_tip_y)**2)
    dist_thumb2ring = math.sqrt((thumb_tip_x - ring_finger_tip_x)**2 + (thumb_tip_y - ring_finger_tip_y)**2)
    dist_thumb2pinky = math.sqrt((thumb_tip_x - pinky_tip_x)**2 + (thumb_tip_y - pinky_tip_y)**2)
    dist_thumb2mcp = math.sqrt((thumb_tip_x - pinky_mcp_x)**2 + (thumb_tip_y - pinky_mcp_y)**2)
    print(dist_thumb2index,dist_thumb2middle,dist_thumb2ring,dist_thumb2pinky, dist_thumb2mcp)
    
    if dist_thumb2index<dist_thresh and dist_thumb2middle <dist_thresh and dist_thumb2ring <dist_thresh and dist_thumb2pinky <dist_thresh:
    	res=0
    elif dist_thumb2index>dist_thresh and dist_thumb2middle >dist_thresh and dist_thumb2ring >dist_thresh and dist_thumb2pinky >dist_thresh and dist_thumb2mcp>dist_thresh:
    	res=5
    elif dist_thumb2index>dist_thresh and dist_thumb2middle < dist_thresh and dist_thumb2ring <dist_thresh and dist_thumb2pinky <dist_thresh:
    	res=1
    elif dist_thumb2index>dist_thresh and dist_thumb2middle > dist_thresh and dist_thumb2ring <dist_thresh and dist_thumb2pinky <dist_thresh:
    	res=2
    elif dist_thumb2index>dist_thresh and dist_thumb2middle > dist_thresh and dist_thumb2ring > dist_thresh and dist_thumb2pinky <dist_thresh:
    	res=3
    elif dist_thumb2index>dist_thresh and dist_thumb2middle > dist_thresh and dist_thumb2ring > dist_thresh and dist_thumb2pinky >dist_thresh and dist_thumb2mcp<dist_thresh:
    	res=4
    return res    
    
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
hands=mp.solutions.hands.Hands()
draw=mp.solutions.drawing_utils
img_shape=(1000,800)
while True:

	ret,img=cap.read()
	img=cv2.resize(img,img_shape)

	if ret:
		hand_landmarks=findhands(img,hands,draw)
		if hand_landmarks:
			detected_number=detectednumber(hand_landmarks,img)
			if detected_number>=0:
				cv2.putText(img,str(detected_number),(300,300),cv2.FONT_HERSHEY_TRIPLEX,10,(0,255,0))

		cv2.imshow("test",img)


	if cv2.waitKey(1)==ord('q'):
		break