# 这是一个示例 Python 脚本。
import glob
import os
import shutil


# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def split(file_path):
    img_dir = glob.glob(os.path.join(file_path, '*'))
    img_dir = [d for d in img_dir if os.path.isdir(d)]

    # 2.进行每一个切分
    for file in img_dir:
        file1 = file
        # 获取下标名称
        file = file.split('\\')[-1]
        nir_path = os.path.join(file_path, 'NIR', file)
        vis_path = os.path.join(file_path, 'VIS', file)
        os.makedirs(nir_path, exist_ok=True)
        os.makedirs(vis_path, exist_ok=True)

        img_files = glob.glob(os.path.join(file_path, file, '*.bmp'))

        for i, img in enumerate(img_files):
            index = img[:-4]
            index = index.split('\\')[-1]
            index = int(index)

            if index > 28:
                continue
            elif index % 2 == 0:
                img_index = index // 2
                shutil.copy(img, os.path.join(vis_path, f'{img_index}.bmp'))
            elif index % 2 == 1:
                img_index = index // 2 + 1
                shutil.copy(img, os.path.join(nir_path, f'{img_index}.bmp'))

        print(f"{file} process over")

    print("finish processing")


def sort_img(file_path):
    img_dir = glob.glob(os.path.join(file_path, '*'))
    img_dir = [d for d in img_dir if os.path.isdir(d)]

    # 2.进行每一个切分,第一组
    for file in img_dir:
        img_files = glob.glob(os.path.join(file, '*.bmp'))
        n = len(img_files)
        resize = 100
        err_list = []
        hint = -1
        for i, img in enumerate(img_files):
            index = img[:-4]
            index = index.split('/')[-1]
            index = int(index)
            hint = index
            if index >= n:
                resize = min(resize, index)
                err_list.append(index)
        dis = n - len(err_list)
        err_list.sort()

        for index, i in enumerate(err_list):
            os.renames(os.path.join(file, f'{i}.bmp'), os.path.join(file, f'{dis + index}.bmp'))

        print(f'{hint} sorted')

def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # print_hi('PyCharm')
    # path = 'D:\datasets\BUAAVISNIR'
    path = '/home/tonnn/.nas/weijia/work/heterogeneous/VD-GAN/dataset/BUAAVISNIR'
    # split(path)
    target = [os.path.join(path, 'NIR'), os.path.join(path, 'VIS')]
    for pth in target:
        sort_img(pth)
        print("ok---------")
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
