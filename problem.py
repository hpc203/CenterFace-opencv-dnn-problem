import cv2
from centerface import CenterFace

if __name__ == '__main__':
    frame = cv2.imread('1.jpg')
    h, w = frame.shape[:2]
    landmarks = True
    centerface = CenterFace(landmarks=landmarks)
    if landmarks:
        dets, lms = centerface(frame, h, w, threshold=0.35)
    else:
        dets = centerface(frame, threshold=0.35)

    for det in dets:
        boxes, score = det[:4], det[4]
        cv2.rectangle(frame, (int(boxes[0]), int(boxes[1])), (int(boxes[2]), int(boxes[3])), (2, 255, 0), 1)
    if landmarks:
        for lm in lms:
            for i in range(0, 5):
                cv2.circle(frame, (int(lm[i * 2]), int(lm[i * 2 + 1])), 2, (0, 0, 255), -1)
    cv2.namedWindow('out', cv2.WINDOW_NORMAL)
    cv2.imshow('out', frame)
    # cv2.waitKey(0)

    landmarks = True
    centerface = CenterFace(landmarks=landmarks)
    for i in range(2):
        frame = cv2.imread(str(i)+'.jpg')
        h, w = frame.shape[:2]
        # landmarks = True
        # centerface = CenterFace(landmarks=landmarks)
        if landmarks:
            dets, lms = centerface(frame, h, w, threshold=0.35)
        else:
            dets = centerface(frame, threshold=0.35)

        for det in dets:
            boxes, score = det[:4], det[4]
            cv2.rectangle(frame, (int(boxes[0]), int(boxes[1])), (int(boxes[2]), int(boxes[3])), (2, 255, 0), 1)
        if landmarks:
            for lm in lms:
                for i in range(0, 5):
                    cv2.circle(frame, (int(lm[i * 2]), int(lm[i * 2 + 1])), 2, (0, 0, 255), -1)
        # cv2.namedWindow('problem', cv2.WINDOW_NORMAL)
        # cv2.imshow('problem', frame)
        # cv2.waitKey(0)
    cv2.namedWindow('problem', cv2.WINDOW_NORMAL)
    cv2.imshow('problem', frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()