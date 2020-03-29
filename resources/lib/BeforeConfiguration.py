import os
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger

class BeforeConfiguration:

    def import_all_resources(self):
        self.import_resources_from_folder("./resources/keywords")
        self.import_resources_from_folder("./resources/support")

    def import_resources_from_folder(self, os_path):
        for path in os.walk(os_path):
            for f in path[2]:
                if  "robot" in f:
                    source_path = (path[0] + "/" + f).replace("\\", "/").replace("./resources", "..")
                    BuiltIn().import_resource(source_path)