import os
import requests

def download_images(url_list, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for index, url in enumerate(url_list):
        try:
            response = requests.get(url)
            response.raise_for_status()  

            image_name = os.path.basename(url)

            image_path = os.path.join(output_folder, f"{index}_{image_name}")

            with open(image_path, 'wb') as file:
                file.write(response.content)

            print(f"Downloaded {image_name} to {image_path}")

        except requests.exceptions.RequestException as e:
            print(f"Failed to download {url}: {e}")

url_list = [
    'https://www.example.com/image1.jpg',
    'https://www.example.com/image2.png',
    'https://www.example.com/image3.gif'
]
output_folder = os.path.join(os.path.join(os.environ['USERPROFILE'], 'Desktop'), 'Downloaded Images')

download_images(url_list, output_folder)
