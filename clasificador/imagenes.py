import os
from PIL import Image
import numpy as np

# Directorios base
base_dir = 'data'
train_dir = os.path.join(base_dir, 'train')
val_dir = os.path.join(base_dir, 'val')

# Crear directorios base
os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)

# Directorios para cada clase
train_teamA_dir = os.path.join(train_dir, 'TeamA')
train_teamB_dir = os.path.join(train_dir, 'TeamB')
val_teamA_dir = os.path.join(val_dir, 'TeamA')
val_teamB_dir = os.path.join(val_dir, 'TeamB')

# Crear directorios de entrenamiento y validación para cada clase
os.makedirs(train_teamA_dir, exist_ok=True)
os.makedirs(train_teamB_dir, exist_ok=True)
os.makedirs(val_teamA_dir, exist_ok=True)
os.makedirs(val_teamB_dir, exist_ok=True)

print("Estructura de directorios creada:")
print(f"- {train_teamA_dir}")
print(f"- {train_teamB_dir}")
print(f"- {val_teamA_dir}")
print(f"- {val_teamB_dir}")

# Función para crear imágenes de ejemplo
def create_sample_image(directory, image_name):
    image_path = os.path.join(directory, image_name)
    image = Image.fromarray(np.random.randint(0, 255, (150, 150, 3), dtype=np.uint8))
    image.save(image_path)

# Generar imágenes de ejemplo
num_samples = 20  # Número de imágenes de ejemplo por clase por conjunto (entrenamiento/validación)

for i in range(num_samples):
    create_sample_image(train_teamA_dir, f'teamA_train_{i}.jpg')
    create_sample_image(train_teamB_dir, f'teamB_train_{i}.jpg')
    create_sample_image(val_teamA_dir, f'teamA_val_{i}.jpg')
    create_sample_image(val_teamB_dir, f'teamB_val_{i}.jpg')

print("Imágenes de ejemplo creadas.")
