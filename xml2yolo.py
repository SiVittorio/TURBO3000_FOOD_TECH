import os 
import shutil
import xml.etree.ElementTree as ET

# Метки данных
class_name_to_id = { "seed": 0 }


# Функция конвертирует .xml файл в словарь Python
def extract_info_from_xml(xml_file):
    root = ET.parse(xml_file).getroot()
     
    info_dict = {}
    info_dict['bboxes'] = []

    for elem in root:
        # Сохраняем имя файла 
        if elem.tag == "filename":
            info_dict['filename'] = elem.text
            
        # Получаем его размер
        elif elem.tag == "size":
            image_size = []
            for subelem in elem:
                image_size.append(int(subelem.text))
            
            info_dict['image_size'] = tuple(image_size)
        
        # Сохраняем координаты
        elif elem.tag == "object":
            points = {}
            for subelem in elem:
                if subelem.tag == "name":
                    points["class"] = subelem.text
                    
                elif subelem.tag == "points":
                    for subsubelem in subelem:
                        points[subsubelem.tag] = int(subsubelem.text)            
            info_dict['points'].append(points)
    
    return info_dict


# Конверирование словаря Python в YOLO-формат
def convert_to_yolov5(info_dict):
    print_buffer = []
    
    for p in info_dict["points"]:
        try:
            class_id = class_name_to_id[p["class"]]
        except KeyError:
            print("Неправильный класс. Ожидались:", class_name_to_id.keys())
        
        b_center_x = (b["xmin"] + b["xmax"]) / 2 
        b_center_y = (b["ymin"] + b["ymax"]) / 2
        b_width    = (b["xmax"] - b["xmin"])
        b_height   = (b["ymax"] - b["ymin"])
        
        # Нормализация координат (см. требования к .txt файлам YOLO)
        image_w, image_h, image_c = info_dict["image_size"]  
        b_center_x /= image_w 
        b_center_y /= image_h 
        b_width    /= image_w 
        b_height   /= image_h 
        
        # Запись в .txt YOLO файл
        print_buffer.append("{} {:.3f} {:.3f} {:.3f} {:.3f}".format(class_id, b_center_x, b_center_y, b_width, b_height))
        
    save_file_name = os.path.join("annotations", info_dict["filename"].replace("png", "txt"))
    
    # Сохранить аннотацию
    print("\n".join(print_buffer), file=open(save_file_name, "w"))


for f in os.listdir('xml'):
    convert_to_yolov5( extract_info_from_xml(f) )
