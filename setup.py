from sklearn.model_selection import train_test_split


# Вспомогательная функция перемещения файлов
def move_files_to_folder(list_of_files, destination_folder):
    for f in list_of_files:
        try:
            shutil.move(f, destination_folder)
        except:
            print(f)
            assert False


# Считать картинки и аннотации
images      = [os.path.join('images', x) for x in os.listdir('images')]
annotations = [os.path.join('annotations', x) for x in os.listdir('annotations') if x[-3:] == "txt"]

images.sort()
annotations.sort()

# Распределить датасет в test и train наборы
train_images, val_images, train_annotations, val_annotations = train_test_split(images, annotations, test_size = 0.2, random_state = 42)
val_images, test_images, val_annotations, test_annotations = train_test_split(val_images, val_annotations, test_size = 0.5, random_state = 42)

# Переместить данные по их папкам
move_files_to_folder(train_images,      'images/train'      )
move_files_to_folder(val_images,        'images/val/'       )
move_files_to_folder(test_images,       'images/test/'      )
move_files_to_folder(train_annotations, 'annotations/train/')
move_files_to_folder(val_annotations,   'annotations/val/'  )
move_files_to_folder(test_annotations,  'annotations/test/' )
