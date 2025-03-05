import cv2
import utils.screenshot as screenshot
import numpy as np

def read_image(file_path):
    return cv2.imread(file_path)

def get_messageArea():
    image=read_image(screenshot.get_screenshot())
    cropped = image[220:2016, 200:880]  # 裁剪坐标为[y0:y1, x0:x1]
    return cropped

def get_dialogueArea():
    image=read_image(screenshot.get_screenshot())
    cropped = image[420:2025, 0:1080]  # 裁剪坐标为[y0:y1, x0:x1]
    return cropped



def find_split_rows(img):
    """找出所有行全为 f0f0f0 (RGB) 的行索引"""
    height, width, _ = img.shape
    split_rows = []
    
    for y in range(height):
        if np.all(img[y, :] == [241, 241, 241]):  # OpenCV 采用 BGR 排序
            split_rows.append(y)
    
    return split_rows

def group_continuous_rows(split_rows):
    """将连续的行分组为区域"""
    if not split_rows:
        return []
    
    groups = []
    current_group = [split_rows[0]]
    
    for y in split_rows[1:]:
        if y == current_group[-1] + 1:
            current_group.append(y)
        else:
            groups.append(current_group)
            current_group = [y]
    
    groups.append(current_group)
    return [(group[0], group[-1]) for group in groups]

def get_valid_split_regions(split_regions, total_height):
    """根据分割区域生成有效的拆分区域"""
    split_points = []
    prev_end = -1
    
    for start, end in split_regions:
        split_points.append((prev_end + 1, start - 1))
        prev_end = end
    
    split_points.append((prev_end + 1, total_height - 1))
    
    return [(s, e) for s, e in split_points if s <= e]

def split_image(img):
    """处理图像并拆分保存各部分"""
    height, width, _ = img.shape
    
    split_rows = find_split_rows(img)
    split_regions = group_continuous_rows(split_rows)
    valid_regions = get_valid_split_regions(split_regions, height)
    
    
    return valid_regions

def isFullDialogue(image):
    height, width, _ = image.shape
    # print(height,width)
    b,g,r=get_pixel_color(image,180,height-1)
    # print(b,g,r)
    if (b, g, r) == (255, 255, 255):
        b,g,r = get_pixel_color(image,160,1)
        if (b, g, r) == (255, 255, 255):
            return False
        else:
            return True
    else:
        return False
    
def get_DialogueContent(image):
    height,width,_=image.shape
    cropped = image[88:height-1, 168:1080]  # 裁剪坐标为[y0:y1, x0:x1]
    return cropped

def get_IDContent(image):
    cropped = image[1:45, 145:1080]  # 裁剪坐标为[y0:y1, x0:x1]
    return cropped


def get_pixel_color(image,x,y):
    b, g, r = image[y, x]

    return b,g,r

    