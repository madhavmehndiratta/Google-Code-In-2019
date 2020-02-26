from PIL import Image
from os import path, remove, listdir, chdir, mkdir

def open_image():
    filename = input("[?] Enter image path: ")
    try:
        image = Image.open(filename)
    except FileNotFoundError:
        exit(f"[-] File {filename} not found.")
    else:
        return image

def get_aspect_ratio(image):
    width, height = image.size
    aspect_ratio = width / height
    print(f"[+] Old image resolution: {width}x{height}")
    print(f"[+] Image aspect ratio: {aspect_ratio}")
    return aspect_ratio


def resize_image(image, aspect_ratio):
    base_size = 400
    if aspect_ratio > 1:
        return image.resize((base_size, int(base_size / aspect_ratio)), Image.ANTIALIAS)
    elif aspect_ratio < 1:
        return image.resize((int(base_size * aspect_ratio), base_size), Image.ANTIALIAS)
    else:
        return image.resize((base_size, base_size), Image.ANTIALIAS)

def save_image(image, output_file):
    quality = 95
    max_size = 65536
    image.save(output_file, quality=100)
    output_size = path.getsize(output_file)
    while output_size > max_size:
        try:
            remove(output_file)
            image.save(output_file, quality=quality, format="JPEG")
        except FileNotFoundError:
            pass
        output_size = path.getsize(output_file)
        quality -= 5
    print(f"[+] File {output_file} saved successfully. (JPEG Quality: {quality})\n")

def single_image():
    image = open_image()
    aspect_ratio = get_aspect_ratio(image)
    image = resize_image(image, aspect_ratio)
    output = input("[?] Where do you want to save the output image? ")
    
    if image.format != "JPEG":
        image = image.convert("RGB")
        filename, extension = path.splitext(output)
        output = filename + ".jpg"
    save_image(image, output)

def whole_directory():
    input_dir = input("[?] Enter the Images directory path: ")

    if not path.isdir(input_dir):
        exit(f"[!] {input_dir} is not a directory.")

    output_dir = input("[?] Enter the output directory path: ")
    mkdir(output_dir)

    if not path.isdir(output_dir):
        exit(f"[!] {output_dir} is not a directory.")

    output_dir = path.abspath(output_dir)
    chdir(input_dir)

    for img in listdir():
        image = Image.open(img)
        print(f"[+] Opened {img}")
        aspect_ratio = get_aspect_ratio(image)
        image = resize_image(image, aspect_ratio)
        if image.format != "JPEG":
            image = image.convert("RGB")
            filename, extension = path.splitext(img)
            output = filename + ".jpg"
        save_image(image, path.join(output_dir, output))
        
def main():
    print("\nWelcome to The Image Manipulation!\n")
    print("1. Resize Single Image\n2. Resize all the Images in a directory\n")
    choice = input("[?] What would you like to do? ")
    
    if choice == "1":
        single_image()
    
    elif choice == "2":
        whole_directory()

    else:
        print("Invalid Choice Entered! Exiting the Program....")
        exit()

main()
