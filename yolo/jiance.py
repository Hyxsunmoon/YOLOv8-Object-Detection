from ultralytics import YOLO

# 加载预训练模型
model = YOLO('runs/detect/my_custom_detector/weights/best.pt') 

model('yolo/data/images/test/IMG_2289_jpeg_jpg.rf.fe2a7a149e7b11f2313f5a7b30386e85.jpg', save=True)