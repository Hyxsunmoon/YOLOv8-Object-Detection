from ultralytics import YOLO

# 加载预训练模型
model = YOLO('yolov8n.pt') 

# 训练模型
results = model.train(
    data='yolo/data/data.yaml', # 数据集配置文件
    epochs=100, # 训练轮数
    imgsz=640, # 输入图像尺寸
    batch=16, # 批量大小
    name='my_custom_detector', # 结果保存目录名称
    device=0, # 指定GPU设备，例如0, 1, 2, 3或'cpu'
    workers=8 # 数据加载工作者数量
)

# 评估模型 (可选，训练结束后会自动评估)
metrics = model.val()
print(metrics.box.map)    # mAP50-95
print(metrics.box.map50)  # mAP50
print(metrics.box.map75)  # mAP75


