import os
from pdf2image import convert_from_path

folder_path = os.getcwd()
files = os.listdir(folder_path)

for file_name in files:
    if file_name.lower().endswith('.pdf'):
        pdf_path = os.path.join(folder_path, file_name)
        pdf_name = os.path.splitext(file_name)[0]
        pdf_output_dir = os.path.join(folder_path, pdf_name)

        os.makedirs(pdf_output_dir, exist_ok=True)
        images = convert_from_path(pdf_path)

        for i, image in enumerate(images):
            jpg_file_name = f"{pdf_name}_page_{i + 1}.jpg"
            jpg_path = os.path.join(pdf_output_dir, jpg_file_name)
            image.save(jpg_path, 'JPEG')

        print(f"Converted {file_name} to {len(images)} JPG file(s) and saved in folder '{pdf_name}'.")
