import glob
import json
import logging
import subprocess
import os

def print_image(img_file, conf: dict):
    """Given a image file print the label"""

    model = conf['model']
    printer = conf['printer']
    brother_ql_cmd= conf['brother_ql_cmd']
    abs_img_path = os.path.abspath(img_file)
    # working command:
    # brother_ql -m QL-500 -p usb://0x04f9:0x2015 print -l 29 C:\Users\the_b\labdoo_print\brother_ql_labdoo_tags_printer\img\device_tag.png -r 90

    bash_command = brother_ql_cmd + " -m " + model + " -p " + printer + " print -l 29 " + abs_img_path
    #+ " -r 90"
    logging.info(bash_command)

    subprocess.run(bash_command,  shell=True)

    print("")
    input("Press Enter key to continue next image")


if __name__ == '__main__':
    logging.basicConfig(
        format="%(asctime)s: %(message)s",
        # filemode='a',
        # filename='HA-Watch.log',
        level=logging.INFO,
        datefmt="%H:%M:%S")

    # Read Printer Configuration File
    with open('config.json', 'r') as f:
        conf = json.load(f)
    for conf_elem in conf:
        logging.info(str(conf_elem) + ": " + str(conf[conf_elem]))
    logging.info("current OS: " + os.name)


    try:
        # PNGs in root folder
        img_files = glob.glob("./*.png")

        # Print the Labels
        for img in img_files:
            print_image(img, conf)
    except Exception as exc:
        logging.error("image " + img + " could not be printed:")
        logging.error(exc)
    logging.info("print job finished")
