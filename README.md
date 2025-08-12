# YOLOv8 自定义目标检测项目

本项目基于 [YOLOv8](https://github.com/ultralytics/ultralytics) 实现，支持自定义数据集的训练、验证和推理。`runs` 文件夹保存了训练过程的可视化结果和模型权重，`yolo` 文件夹包含训练与推理脚本及数据集。

---

## 目录结构

```
yolo/
├── jiance.py           # 推理脚本
├── main.py             # 训练/主控脚本
├── yolov8n.pt          # 预训练权重
├── data/
│   ├── data.yaml       # 数据集配置文件
│   ├── images/         # 原始图片（train/val/test）
│   └── labels/         # 标签文件（train/val/test）
runs/
└── detect/
    └── my_custom_detector/   # 训练结果、可视化、权重等
```

---

## 环境依赖

- Python 3.8+
- torch
- opencv-python
- matplotlib
- ultralytics (推荐直接安装官方 YOLOv8)
- 其它依赖见 `requirements.txt`

安装依赖：
```bash
pip install -r requirements.txt
# 或直接安装ultralytics
pip install ultralytics
```

---

## 数据集准备

- 图片放在 `yolo/data/images/{train,val,test}/`
- 标签放在 `yolo/data/labels/{train,val,test}/`
- 数据集配置文件为 `yolo/data/data.yaml`，格式如下：

```yaml
train: data/images/train
val: data/images/val
test: data/images/test

nc: 7  # 类别数
names: ['fish', 'jellyfish', 'penguin', 'puffin', 'shark', 'starfish', 'stingray'] #类别名称
```

---

## 训练模型

在 `yolo/` 目录下运行：

```bash
python main.py
```
或直接用 ultralytics 命令行（如适用）：

```bash
yolo detect train data=data/data.yaml model=yolov8n.pt epochs=100 imgsz=640
```

训练过程中的权重、loss曲线、混淆矩阵等会保存在 `runs/detect/my_custom_detector/` 下。

---

## 推理/测试

```bash
python jiance.py --weights runs/detect/my_custom_detector/weights/best.pt --source data/images/test/
```
推理结果图片会保存在 `runs/detect/predict/` 目录下。

---

## 结果可视化

- 训练过程的 loss 曲线、混淆矩阵、PR 曲线等可在 `runs/detect/my_custom_detector/` 查看。
- 推理结果图片在 `runs/detect/predict/`。

---

## 致谢

- [Ultralytics YOLO](https://github.com/ultralytics/ultralytics)

---
