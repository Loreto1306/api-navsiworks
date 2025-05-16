import os
import json
import clr
import sys
import traceback
import time

# Adding the reference.DLL to the sys.path
sys.path.append(r"C:\Program Files\Autodesk\Navisworks Manage 2025")

# Setting up the references
clr.AddReference(r"C:\Program Files\Autodesk\Navisworks Manage 2025\Autodesk.Navisworks.Automation.dll")
from Autodesk.Navisworks.Api.Automation import NavisworksApplication, AutomationException

class Api:
    def __init__(self, json_data: str = ''):
        """ This function cacth the path and the folders """
        self.path = ''
        self.folder = {}
        self.os = ''
        self.contract = ''

        if not json_data:
            return
        try:
            json_answer = json.loads(json_data)
            # You can add here a root path with subfolder and files inside, you can send the path with json.
            self.path = r"/your_directory_root/"
            self.contract = json_answer['id']
            self.folder = json_answer['folder']
            self.os = json_answer['os']
            return
        except Exception as e:
            print(f"Unexpected in the Api class: {e}")

# Starting App, verify if the path exists
def start_app(folder_path : str):
    """ Initializer Function, reads and confirm the path existence and files with *.dwg """
    try:
        if os.path.exists(folder_path):
            # Starting the application in background, Visible = True (Visual mode)
            nw_app = NavisworksApplication()
            nw_app.Visible = True

            # Recursively traverse a folder and all subfolders
            # Each iteration, returns a tuple
            for root, _, files in os.walk(folder_path):
                for file_name in files:
                    if file_name.endswith(".dwg"):
                        end = os.path.join(root, file_name)
                        print(f"Attaching: {end}")
                        try:
                            nw_app.AppendFile(end)
                        except Exception as e:
                            print(f"Error in attaching {end}: {e}")
                            traceback.print_exc()
                    else:
                        print(f"Invalid file {file_name}")
                        traceback.print_exc()
            OUTPUT = os.path.join(
                r"C:\\output_path", "model_fedaration.nwd")
            nw_app.SaveFile(OUTPUT)
            time.sleep(20)
        else:
            print('Invalid Path')
    except TypeError:
        print("The argument isn't a str.")
        traceback.print_exc()
    except Exception as e:
        print(f"Unexpected error: {e}")
        traceback.print_exc()

def Main():
    "Principle function of script, when running the file this is the first function."
    dados = sys.argv[1]
    response = Api(dados)
    if response.path:
        print("Starting the path processing.")
        start_app(response.path)
    else:
        print("Invalid path or JSON malformed.")

if __name__ == "__main__":
    Main()