from PageObjectLibrary import PageObject
from robot.libraries.OperatingSystem import OperatingSystem
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger
from datetime import datetime
from datetime import date

import xml.etree.ElementTree as ET
import random
import string
import shutil
import fnmatch
import time
import os


class Utils(PageObject):

    _locators = {
        # button
        "label_rule_name": "xpath=//*[@id='root']//div[2]/div/div/div/div[2]/div/div/div/div/div",
        "label_rule_checkbox": "xpath=//*[@id='root']//div[2]//input"
    }

    @property
    def automationsetup(self):
        return BuiltIn().get_library_instance("automationsetup")

    @property
    def home(self):
        return self.builtin.get_variable_value('${USER_HOME_PATH}')

    @property
    def env_name(self):
        return self.builtin.get_variable_value('${CONFIG["run_env"]}')

    @property
    def env(self):
        return BuiltIn().get_variable_value("${ENV}")

    @property
    def automationsetup(self):
        return BuiltIn().get_library_instance("automationsetup")

    @property
    def mass(self):
        return BuiltIn().get_variable_value("${MASS}")

    @property
    def curdir(self):
        return os.getcwd()

    @property
    def opsys(self):
        return OperatingSystem()

    def go_back(self):
        """ Simulates the user clicking the back button on the browser """
        self.selib.go_back()

    def select_rule_checkbox(self, name):
        """ This method select the checkbox on the Rules page """
        self.selib.wait_until_page_contains_element(
            self.locator.label_rule_name)
        x = self.selib.get_webelements(self.locator.label_rule_name)
        y = self.selib.get_webelements(self.locator.label_rule_checkbox)
        i = 0
        for item in x:
            if name in self.selib.get_text(item):
                self.automationsetup.wait_for_click(y[i])
            i += 1

    def get_folder_path(self, folder):
        """ Get a folder path """
        dirPath = self.home
        folderDir = self.opsys.join_path(
            dirPath + "\\" + folder)
        return folderDir

    def check_if_was_downloaded_successfuly(self, file, download_dir="SVR"):
        """ Check if the file was downloaded successfully """
        path = self.get_folder_path("Downloads\\" + download_dir)
        locator = path + "\\" + file
        logger.info("LOCATOR:  " + locator)
        self.opsys.wait_until_created(locator)
        self.opsys.file_should_exist(locator)

    def remove_downloaded_file(self, file, download_dir="SVR"):
        """ Remove downloaded file from a directory """
        path = self.get_folder_path("Downloads\\" + download_dir)
        locator = path + "\\" + file
        self.opsys.file_should_exist(locator)
        self.opsys.remove_files(path + "\\" + file)

    def generate_current_data_time(self, value):
        """ Get the current date and time """
        today = date.today()
        x = today.strftime(value)
        return x

    def go_to_url(self, url):
        """ Go to a desired url """
        url = self.selib.go_to(self.env[self.env_name][url])
        return url

    def open_xml_file(self, path, file):
        path_locator = self.curdir + "\\resources\\fixtures\\" + path
        tree = ET.parse(str(path_locator) + file)
        self.builtin.set_suite_variable("${XMLFILE}", tree)
        return tree

    def change_value_xml(self, field, value):
        tree = self.builtin.get_variable_value("${XMLFILE}")
        root = tree.getroot()
        for field in root.iter(str(field)):
            field.text = value

    def read_value_xml(self, field):
        """ Read a field value on a given xml.

        Arguments:
        - field: Field to be read.


        Examples:
        |Read Value Xml | Numero |

        =>
        | (string) Invoice_01 | """
        tree = self.builtin.get_variable_value("${XMLFILE}")
        root = tree.getroot()
        for field in root.iter(str(field)):
            value = field.text
        return value

    def save_xml_changes(self, path, file_name):
        """ Saves XML on a given path.

        Arguments:
        - path: Path to define where your xml will be saved.
        - file_name: The name of the file to be saved.

        Examples:
        |Save XML Changes | "Italy" | FatturaPA_Approved |

        =>
        | (file) italy\FatturaPA_Approved.xml | """
        path_locator = self.curdir + "\\resources\\fixtures\\" + path
        tree = self.builtin.get_variable_value("${XMLFILE}")
        tree.write(str(path_locator) + file_name + ".xml")
        value = (str(path_locator) + file_name + ".xml")
        tree.write(value, xml_declaration=True, encoding='utf-8')

    def remove_files_from_fixtures(self, country, file):
        path = self.curdir + '\\resources\\fixtures\\' + \
            country + '\\transmission\\' + file
        self.opsys.file_should_exist(path)
        self.opsys.remove_files(path)

    def clean_download_folder(self):
        download_path = str(
            self.automationsetup.user_home_path) + '\\Downloads\\SVR\\'
        for filename in os.listdir(download_path):
            file_path = os.path.join(download_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))

    def find_files(self, pattern, path):
        result = []
        retry = int(10)
        while not result:
            if retry == 0:
                raise Exception("Timeout error: File not found")
            else:
                for root, dirs, files in os.walk(path):
                    for name in files:
                        if fnmatch.fnmatch(name, pattern):
                            result.append(os.path.join(root, name))
                time.sleep(3)
                retry -= 1
        return result

    def wait_loading(self, locator):
        """ Wait until loading process is complete"""
        self.automationsetup.wait_for_keyword(
            "wait_until_page_contains_element", locator)
        x = self.selib.get_element_count(locator)
        delta = 0
        while x > 0 and delta < 5:
            self.selib.wait_until_page_does_not_contain_element(
                locator, timeout="300s")
            x = self.selib.get_element_count(locator)
            delta += 1

    def validate_results_on_table(self, yaml_mass, locator, starting_row="2"):
        """This test is to validate the results inside a table cell by cell
        Arguments:
        - path: Relative path of the yml file.
        - Locator (xpath) from the grid (Line as row_xxx column as column_xxx and value as value_xxx)
            Example:
                "xpath=//*[@id='grdTransactionsMaster']/div[row_xxx]/table/tbody/tr/td[column_xxx][contains(text(),'value_xxx')]"

        Examples:
        def validate_result_grid_vies_check(self):
        self.utils.validate_results_on_table('VIES_CHECK', self.locator.table_vies_check)
        In this case , VIES_CHECK is a locator that comes from yaml file with the values to consult on the table and the self locator is the table locator
        =>
        | Python dictionary object. |
        """
        mass = self.mass[yaml_mass]
        starting_row = int(starting_row)
        column = 1
        for root, child in mass.items():
            for k, v in child.items():
                find_locator = locator
                find_locator = str(find_locator).replace(
                    'row_xxx', str(starting_row)).replace(
                        'column_xxx', str(column)).replace(
                            'value_xxx', str(v))
                self.automationsetup.wait_for_keyword(
                    'page should contain element', find_locator)
                column += 1
            column = 1
            starting_row += 1
