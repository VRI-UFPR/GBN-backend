import json
import os

server_url = "http://127.0.0.1:8182/iiif/2"
files_dir = "/media/thomas/c7f0a812-bbd2-4bf9-a7af-ead8d9a44d45/GBN-imgs/teste/"
output_dir = "./manifests"


def generate_iiif_manifest(image_id, image_label, server_url):
    """
    Generate a IIIF manifest for a given image.
    
    Args:
        image_id (str): The identifier of the image on the Cantaloupe server.
        image_label (str): A human-readable label for the image.
        server_url (str): The base URL of the Cantaloupe server.
        
    Returns:
        dict: A IIIF manifest as a Python dictionary.
    """
    
    # Define the structure of a IIIF Manifest
    manifest = {
        "@context": "http://iiif.io/api/presentation/2/context.json",
        "@id": f"{server_url}/{image_id}/manifest.json",
        "@type": "sc:Manifest",
        "label": image_label,
        "sequences": [
            {
                "@type": "sc:Sequence",
                "canvases": [
                    {
                        "@id": f"{server_url}/{image_id}/canvas",
                        "@type": "sc:Canvas",
                        "label": image_label,
                        "height": 1000,  # Example height, adjust as needed
                        "width": 1000,   # Example width, adjust as needed
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
    with open(output_path, 'w') as f:
        json.dump(manifest, f, indent=4)

if __name__ == "__main__":
    # Example usage
    # image_id = "DerGemeindebote-p01.png"  # Replace with your image ID
    # image_label = "DerGemeindebote-p01.png"  # Replace with your image label
    server_url = "http://127.0.0.1:8182/iiif/2"

    files_dir = "/media/thomas/c7f0a812-bbd2-4bf9-a7af-ead8d9a44d45/GBN-imgs/teste/"

    for filename in os.listdir(files_dir):
        file_path = os.path.join(files_dir, filename)
        if os.path.isfile(file_path):
            print(filename)  # or perform other operations with the file

            # Generate the manifest
            manifest = generate_iiif_manifest(filename, filename, server_url)
            
            # Save the manifest to a file
            output_path = f"{output_dir}/{filename}_manifest.json"
            save_manifest_to_file(manifest, output_path)

            print(f"Manifest saved to {output_path}")