import cv2
from ultralytics import YOLO

# 1. load train model
model = YOLO('best.pt')

# 2. Input video 
video_path = 'input.mp4'  
cap = cv2.VideoCapture(video_path)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

output_path = 'output_result.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

print("Smart Video processing start ho chuki hai... Live window check karein.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # 3. Get prediction from model
    results = model(frame, conf=0.1, imgsz=640, verbose=True)

    # boxes draw with YOlO 
    annotated_frame = results[0].plot()


    defect_count = len(results[0].boxes)

    # if any disterbance status BAD
    if defect_count > 0:
        status_text = f"Status: BAD ROAD ({defect_count} Defects Found!)"
        text_color = (0, 0, 255)  # Red color (BGR format)
    else:
        status_text = "Status: GOOD ROAD (Clear)"
        text_color = (0, 255, 0)  # Green color

    # 5. show video on screen
    cv2.putText(annotated_frame, status_text, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, text_color, 3, cv2.LINE_AA)

    # save output video and show
    out.write(annotated_frame)
    cv2.imshow("Smart Infrastructure Inspection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print("Processing complete! Now your video in 'output_result.mp4' saved.")