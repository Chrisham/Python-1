# manuell ausführen mit
# python3.9 /volume1/Christof/Daten/Organisation/030_Infrastruktur/020_Devices/Smart-Home/IOBroker/Blockly/Backup-Automation/iobroker-script-backup.py


import subprocess
import shutil
import os
from datetime import datetime

# test
# Define function for copy command for single with in linux filesystem
def copy_file(source_folder, destination_folder, filename):
    # Check if the source folder exists
    if not os.path.exists(source_folder):
        print(f"Source folder '{source_folder}' does not exist.")
        return
    
    # Check if the destination folder exists, create it if not
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    # Check if the specified file exists in the source folder
    source_path = os.path.join(source_folder, filename)
    if not os.path.exists(source_path):
        print(f"File '{filename}' not found in '{source_folder}'.")
        return
    
    # Copy the file to the destination folder
    destination_path = os.path.join(destination_folder, filename)
    shutil.copy2(source_path, destination_path)
    print(f"File '{filename}' copied to '{destination_folder}'.")




# Define function for copy command from Docker Container
def copy_file_from_container(container_id, source_path, destination_path):
    try:
        subprocess.run(["docker", "cp", f"{container_id}:{source_path}", destination_path], check=True)
        print("File copied successfully!")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while copying the file: {e}")


# Get the current date and time
current_date = datetime.now()
# Format the date as a string
date_string = current_date.strftime("%Y-%m-%d-%H-%M-%S")
        
# IOBroker Blockly Backup
container_id = "1bcd9b0d4644"
source_path = "opt/iobroker/iobroker-data/objects.jsonl"
destination_path = "/volume1/Christof/Daten/Organisation/030_Infrastruktur/030_Backup/Smart-Home/IOBroker/Blockly/" + "blockly-bak_" + date_string + ".jsonl"


copy_file_from_container(container_id, source_path, destination_path)


# Grafana DB Backup
source_folder = "/volume1/docker/grafana2"
destination_folder= "/volume1/Christof/Daten/Organisation/030_Infrastruktur/030_Backup/Smart-Home/Visualisation/Grafana/" + "backup_" + date_string
filename = "grafana.db"

copy_file(source_folder, destination_folder, filename)

