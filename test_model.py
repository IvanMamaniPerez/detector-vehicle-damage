import numpy as np
import cv2
from ultralytics import YOLO

# analyzer = LicensePlateDetector()
# path_image = 'moto.png'



modelOCR = YOLO("runs/detect/train13/weights/best.pt")
modelOCR.fuse()
name_image = "vehicle_damage.png"
path_image = 'storage/'+ name_image
nparr = np.fromfile(path_image, np.uint8)
img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

list_pred = modelOCR.predict(img)
# print(list_pred)

contador = 0

""" pred = list_pred[0] """
""" detections = [(box, pred.boxes.conf[i].item(), int(pred.boxes.cls[i].item()))
                for i, box in enumerate(pred.boxes.xyxy.tolist())]

detections.sort(key=lambda x: (x[0][2] - x[0][0]) * (x[0][3] - x[0][1]), reverse=True) """

for pred in list_pred:
    print('boxeesss')
    print(pred.boxes.xyxy.tolist())
    print('boxeesss')

    # pintar todos los resultados 
    for box in pred.boxes.xyxy.tolist():

        x1, y1, x2, y2 = map(int, box)
        print(x1, y1, x2, y2)
        class_name = pred.names[pred.boxes.cls.tolist().index(int(pred.boxes.cls[0].item()))]
        if(pred.boxes.conf[0].item() >= 0.1):
            print('Class Name:', class_name)
            print('Class Confidence:', pred.boxes.conf[0].item())
            print('Box Coordinates:', x1, y1, x2, y2)
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(img, f"{class_name}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            cv2.imwrite(str(contador)+ '_resultado_'+ name_image+'.png', img)
            contador += 1


""" if detections:
    # Solo usar el primer resultado, que es el más grande
    box, confidence, class_id = detections[0]

    x1, y1, x2, y2 = map(int, box)
    class_name = pred.names[class_id]
    if(confidence >= 0.5):
        print('Class Name:', class_name)
        print('Class Confidence:', confidence)
        print('Box Coordinates:', x1, y1, x2, y2)
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(img, f"{class_name}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imwrite(str(contador)+ '_resultado_'+ name_image+'.png', img) """
