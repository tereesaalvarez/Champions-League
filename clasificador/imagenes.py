import os
from PIL import Image
import numpy as np

# Directorios base
base_dir = 'clasificador/data'
train_dir = os.path.join(base_dir, 'train')
val_dir = os.path.join(base_dir, 'val')

# Crear directorios base
os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)

# Directorios para cada equipo
train_dortmund_dir = os.path.join(train_dir, 'Dortmund')
train_madrid_dir = os.path.join(train_dir, 'RealMadrid')
val_dortmund_dir = os.path.join(val_dir, 'Dortmund')
val_madrid_dir = os.path.join(val_dir, 'RealMadrid')

# Crear directorios de entrenamiento y validación para cada equipo
os.makedirs(train_dortmund_dir, exist_ok=True)
os.makedirs(train_madrid_dir, exist_ok=True)
os.makedirs(val_dortmund_dir, exist_ok=True)
os.makedirs(val_madrid_dir, exist_ok=True)

print("Estructura de directorios creada:")
print(f"- {train_dortmund_dir}")
print(f"- {train_madrid_dir}")
print(f"- {val_dortmund_dir}")
print(f"- {val_madrid_dir}")

# Función para crear imágenes de ejemplo
def create_sample_image(directory, image_name):
    image_path = os.path.join(directory, image_name)
    image = Image.fromarray(np.random.randint(0, 255, (150, 150, 3), dtype=np.uint8))
    image.save(image_path)

# Generar imágenes de ejemplo
num_samples = 20  # Número de imágenes de ejemplo por equipo por conjunto (entrenamiento/validación)

for i in range(num_samples):
    create_sample_image(train_dortmund_dir, f'dortmund_train_{i}.jpg')
    create_sample_image(train_madrid_dir, f'madrid_train_{i}.jpg')
    create_sample_image(val_dortmund_dir, f'dortmund_val_{i}.jpg')
    create_sample_image(val_madrid_dir, f'madrid_val_{i}.jpg')

print("Imágenes de ejemplo creadas.")
