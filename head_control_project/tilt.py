import cv2
import mediapipe as mp
import math
import numpy as np
from collections import deque

# MediaPipe
mp_face = mp.solutions.face_mesh

face_mesh = mp_face.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.85,
    min_tracking_confidence=0.85
)

# Webcam
cap = cv2.VideoCapture(0)

# Smoothing
angle_buffer = deque(maxlen=7)

current_action = "NONE"

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Mirror view
    frame = cv2.flip(frame, 1)

    h, w, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = face_mesh.process(rgb)

    if result.multi_face_landmarks:

        for landmarks in result.multi_face_landmarks:

            # Left eye
            left_eye = landmarks.landmark[33]

            # Right eye
            right_eye = landmarks.landmark[263]

            x1 = int(left_eye.x * w)
            y1 = int(left_eye.y * h)

            x2 = int(right_eye.x * w)
            y2 = int(right_eye.y * h)

            # Draw eyes
            cv2.circle(frame, (x1, y1), 5, (255, 0, 0), -1)
            cv2.circle(frame, (x2, y2), 5, (0, 255, 0), -1)

            # Eye line
            cv2.line(frame, (x1, y1), (x2, y2),
                     (0, 255, 255), 2)

            # Calculate angle
            angle = math.degrees(
                math.atan2(y2 - y1, x2 - x1)
            )

            # Smooth angle
            angle_buffer.append(angle)

            avg_angle = np.mean(angle_buffer)

            # --------------------------------
            # TILT DETECTION
            # --------------------------------

            action = "NONE"

            # LEFT TILT
            if avg_angle < -12:
                action = "FOOD REQUEST 🍽"

            # RIGHT TILT
            elif avg_angle > 12:
                action = "ELECTRICAL HELP 🔌"

            # LOOK UP
            elif y1 < h * 0.30 and y2 < h * 0.30:
                action = "🚨 EMERGENCY"

            # LOOK DOWN
            elif y1 > h * 0.45 and y2 > h * 0.45:
                action = "RESTROOM NEEDED 🚻"

            else:
                action = "NONE"

            current_action = action

            # --------------------------------
            # DISPLAY
            # --------------------------------

            cv2.putText(
                frame,
                current_action,
                (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                3
            )

            cv2.putText(
                frame,
                f"ANGLE: {int(avg_angle)}",
                (30, 90),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 255),
                2
            )

    else:

        current_action = "NO FACE"

    # Instructions
    cv2.putText(
        frame,
        "TILT LEFT = FOOD",
        (20, h - 90),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        "TILT RIGHT = ELECTRICAL",
        (20, h - 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        "UP = EMERGENCY | DOWN = RESTROOM",
        (20, h - 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    cv2.imshow("Healthcare Tilt Detection", frame)

    # ESC to Exit
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()