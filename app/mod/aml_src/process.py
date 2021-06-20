import os
from posix import listdir
import shutil


class Process:
    def __init__(self):
        self.process_infolder = os.path.join(os.getcwd(), "shared", "input")
        self.process_outfolder = os.path.join(os.getcwd(), "shared", "output")

    def create_folders(self, unique_id):
        if ~os.path.isdir(os.path.join(self.process_outfolder, unique_id)):
            os.mkdir(os.path.join(self.process_outfolder, unique_id))
            os.mkdir(os.path.join(self.process_outfolder, unique_id, "process_images"))
            os.mkdir(os.path.join(self.process_outfolder, unique_id, "process_texts"))
            os.mkdir(os.path.join(self.process_outfolder, unique_id, "process_selected_images"))
            os.mkdir(os.path.join(self.process_outfolder, unique_id, "process_selected_images", "invoice"))
            return True
        else:
            return False

    def ocr_operation(self, unique_id, file_name):
        file_path = os.path.join(self.process_outfolder, unique_id, file_name)

    def page_classification(self, page):
        pass

    def data_extraction(self, page):
        pass

    def job(self, unique_id, file_name):
        process_status = False

        if self.create_folders(unique_id):
            shutil.move(os.path.join(self.process_infolder, file_name), os.path.join(self.process_outfolder, unique_id))

            if self.ocr_operation(unique_id, file_name):
                pass
                # files = os.listdir(os.path.join(self.process_outfolder, ))


        return process_status
