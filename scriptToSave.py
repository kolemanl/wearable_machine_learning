import subprocess

def pull_xml_file(device_path, local_path):
    """Pull an XML file from the Wear OS device."""
    pull_command = ["adb", "pull", device_path, local_path]
    subprocess.run(pull_command, check=True)

def delete_xml_file(device_path):
    """Delete an XML file from the Wear OS device."""
    delete_command = ["adb", "shell", "rm", device_path]
    subprocess.run(delete_command, check=True)

# Path to the XML file on the Wear OS device
localPath = "C:/Users/kolem/Documents/Accelerometer/Data/"
device_xml_path = "/sdcard/Android/data/com.example.appforaccelerometer/files/accelerometer_data.xml"

# Pull the XML file from the Wear OS device to the local directory
pull_xml_file(device_xml_path, localPath)

# Delete the XML file from the Wear OS device
delete_xml_file(device_xml_path)

