import json
import os
from PIL import Image

# Global Variables
server_url = "https://webdokumente.c3sl.ufpr.br:8182/iiif/2"
files_dir = "/home/olimpiada/cantaloupe/imgs/"
output_dir = "./manifests/"

def get_image_size(image_path):
    """
    Get the dimensions (width and height) of an image file.
    
    Args:
        image_path (str): The path to the image file.
    
    Returns:
        tuple: Width and height of the image.
    """
    with Image.open(image_path) as img:
        width, height = img.size
    return width, height

def generate_iiif_manifest(image_id, width, height):
    """
    Generate a IIIF manifest for a given image, including its dynamic size.
    
    Args:
        image_id (str): The identifier of the image on the Cantaloupe server.
        width (int): The width of the image.
        height (int): The height of the image.
    
    Returns:
        dict: A IIIF manifest as a Python dictionary.
    """
    
    # Define the structure of a IIIF Manifest
    manifest = {
        "@context": "http://iiif.io/api/presentation/2/context.json",
        "@id": f"{server_url}/{image_id}/manifest.json",
        "@type": "sc:Manifest",
        "label": image_id,
        "sequences": [
            {
                "@type": "sc:Sequence",
                "canvases": [
                    {
                        "@id": f"{server_url}/{image_id}/canvas",
                        "@type": "sc:Canvas",
                        "label": image_id,
                        "height": height,
                        "width": width,
                        "images": [
                            {
                                "@type": "oa:Annotation",
                                "motivation": "sc:painting",
                                "resource": {
                                    "@id": f"{server_url}/{image_id}/full/full/0/default.jpg",
                                    "@type": "dctypes:Image",
                                    "format": "image/jpeg",
                                    "service": {
                                        "@context": "http://iiif.io/api/image/2/context.json",
                                        "@id": f"{server_url}/{image_id}",
                                        "profile": "http://iiif.io/api/image/2/level2.json"
                                    }
                                },
                                "on": f"{server_url}/{image_id}/canvas"
                            }
                        ]
                    }
                ]
            }
        ]
    }

    return manifest

def save_manifest_to_file(manifest, output_path):
    """
    Save a IIIF manifest to a JSON file.
    
    Args:
        manifest (dict): The IIIF manifest to save.
        output_path (str): The path where the manifest file will be saved.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)  # Ensure the directory exists
    with open(output_path, 'w') as f:
        json.dump(manifest, f, indent=4)

if __name__ == "__main__":
    # Iterate through files in the specified directory
    for filename in os.listdir(files_dir):
        file_path = os.path.join(files_dir, filename)
        if os.path.isfile(file_path):
            print(f"Processing file: {filename}")

            # Get the dimensions of the image
            width, height = get_image_size(file_path)

            # Generate the manifest with dynamic image size
            manifest = generate_iiif_manifest(filename, width, height)
            
            # Save the manifest to a file
            output_path = f"{output_dir}/{filename}_manifest.json"
            save_manifest_to_file(manifest, output_path)

            print(f"Manifest saved to {output_path}")

