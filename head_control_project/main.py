import cv2
import mediapipe as mp
import numpy as np
from collections import deque

# -----------------------------
# MediaPipe Setup
# -----------------------------

mp_face = mp.solutions.face_mesh

face_mesh = mp_face.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.85,
    min_tracking_confidence=0.85
)

# -----------------------------
# Webcam
# -----------------------------

cap = cv2.VideoCapture(0)

# -----------------------------
# Smoothing Buffers
# -----------------------------

x_buffer = deque(maxlen=7)
y_buffer = deque(maxlen=7)

current_action = "NONE"

# -----------------------------
# Main Loop
# -----------------------------

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

            # -----------------------------------
            # IMPORTANT LANDMARKS
            # -----------------------------------

            nose = landmarks.landmark[1]

            left_face = landmarks.landmark[234]
            right_face = landmarks.landmark[454]

            top_face = landmarks.landmark[10]
            bottom_face = landmarks.landmark[152]

            # Convert to pixels
            nose_x = int(nose.x * w)
            nose_y = int(nose.y * h)

            left_x = int(left_face.x * w)
            right_x = int(right_face.x * w)

            top_y = int(top_face.y * h)
            bottom_y = int(bottom_face.y * h)

            # -----------------------------------
            # FACE CENTER
            # -----------------------------------

            center_x = (left_x + right_x) // 2
            center_y = (top_y + bottom_y) // 2

            # Difference from center
            dx = nose_x - center_x
            dy = nose_y - center_y

            # -----------------------------------
            # SMOOTHING
            # -----------------------------------

            x_buffer.append(dx)
            y_buffer.append(dy)

            avg_dx = int(np.mean(x_buffer))
            avg_dy = int(np.mean(y_buffer))

            # -----------------------------------
            # DRAWING
            # -----------------------------------

            cv2.circle(frame, (nose_x, nose_y), 8, (0, 0, 255), -1)

            cv2.circle(frame, (center_x, center_y),
                       6, (255, 255, 255), -1)

            cv2.line(frame,
                     (center_x, center_y),
                     (nose_x, nose_y),
                     (0, 255, 255), 2)

            # -----------------------------------
            # DETECTION LOGIC
            # -----------------------------------

            action = "NONE"

            # Horizontal movement priority
            if avg_dx < -35:
                action = "FOOD REQUEST 🍽"

            elif avg_dx > 35:
                action = "ELECTRICAL HELP 🔌"

            # Vertical movement
            elif avg_dy < -25:
                action = "🚨 EMERGENCY"

            elif avg_dy > 30:
                action = "RESTROOM NEEDED 🚻"

            else:
                action = "NONE"

            current_action = action

            # -----------------------------------
            # DISPLAY
            # -----------------------------------

            cv2.putText(
                frame,
                current_action,
                (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                3
            )

            # Debug values
            cv2.putText(
                frame,
                f"DX:{avg_dx} DY:{avg_dy}",
                (30, 90),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255, 255, 255),
                2
            )

    else:

        current_action = "NO FACE DETECTED"

        cv2.putText(
            frame,
            current_action,
            (30, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            3
        )

    # -----------------------------------
    # GUIDE TEXT
    # -----------------------------------

    cv2.putText(
        frame,
        "LEFT=FOOD | RIGHT=ELECTRICAL",
        (20, h - 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        "UP=EMERGENCY | DOWN=RESTROOM",
        (20, h - 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )

    # -----------------------------------
    # SHOW OUTPUT
    # -----------------------------------

    cv2.imshow("Healthcare Head Control", frame)

    # ESC key
    if cv2.waitKey(1) & 0xFF == 27:
        break

# -----------------------------
# Cleanup
# -----------------------------

cap.release()
cv2.destroyAllWindows()