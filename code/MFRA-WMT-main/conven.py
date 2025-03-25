import os
from PIL import Image

# 定义输入和输出文件夹路径
input_folder = ''
output_folder = ''


# 确保输出文件夹存在
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 获取输入文件夹中的所有文件
for filename in os.listdir(input_folder):
    # 生成完整的文件路径
    input_path = os.path.join(input_folder, filename)

    # 检查文件是否为图像文件（可根据需要扩展文件类型）
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        # 打开图像
        image = Image.open(input_path)

        # 缩放图像
        resized_image = image.resize((128, 128), Image.LANCZOS)

        # 生成输出路径
        output_path = os.path.join(output_folder, filename)

        # 保存缩放后的图像
        resized_image.save(output_path)

        print(f"Processed {filename}")

print("All images have been resized.")
