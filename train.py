from ultralytics import YOLO 
 

if __name__ == "__main__":
    
    model = YOLO("runs/detect/train13/weights/best.pt")

    model.train(data="./datasets/data.yaml", epochs=20, imgsz=(472, 303), batch=4, optimizer="Adam")

