from PageObjectLibrary import PageObject
from robot.libraries.OperatingSystem import OperatingSystem
from robot.libraries.BuiltIn import BuiltIn
import xml.etree.ElementTree as ET
from robot.api import logger
from datetime import datetime
from datetime import date
import random
import os
import openpyxl
import string


class Generator(PageObject):

    @property
    def utils(self):
        return self.builtin.get_library_instance("Utils")

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
    def home(self):
        return self.builtin.get_variable_value('${USER_HOME_PATH}')

    @property
    def env_name(self):
        return self.builtin.get_variable_value('${CONFIG["run_env"]}')

    @property
    def env(self):
        return BuiltIn().get_variable_value("${ENV}")

    @property
    def opsys(self):
        return OperatingSystem()

    def generate_nrProc_1(self):
        block_1 = random.randint(10000, 99999)
        block_2 = random.randint(100000, 999999)
        block_3 = random.randint(2013, 2018)
        a = str(block_1) + "." + str(block_2) + "/" + str(block_3)

        # Criando DV1
        n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15 = a[0], a[1], a[
            2], a[3], a[4], a[6], a[7], a[8], a[9], a[10], a[11], a[13], a[14], a[15], a[16]
        prd_1_1 = int(16) * int(n1)
        prd_1_2 = int(15) * int(n2)
        prd_1_3 = int(14) * int(n3)
        prd_1_4 = int(13) * int(n4)
        prd_1_5 = int(12) * int(n5)
        prd_1_6 = int(11) * int(n6)
        prd_1_7 = int(10) * int(n7)
        prd_1_8 = int(9) * int(n8)
        prd_1_9 = int(8) * int(n9)
        prd_1_10 = 7 * int(n10)
        prd_1_11 = 6 * int(n11)
        prd_1_12 = 5 * int(n12)
        prd_1_13 = 4 * int(n13)
        prd_1_14 = 3 * int(n14)
        prd_1_15 = 1 * int(n15)

        total_1 = int(prd_1_1) + int(prd_1_2) + int(prd_1_3) + int(prd_1_4) + int(prd_1_5) + int(prd_1_6) + int(prd_1_7) + int(
            prd_1_8) + int(prd_1_9) + int(prd_1_10) + int(prd_1_11) + int(prd_1_12) + int(prd_1_13) + int(prd_1_14) + int(prd_1_15)
        resto_1 = int(total_1) % 11
        subtrai_1 = int(11) - int(resto_1)
        subtrai_a = str(subtrai_1)
        dv1 = subtrai_a[-1]

        # Criando DV2
        m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, m15, m16 = a[0], a[1], a[
            2], a[3], a[4], a[6], a[7], a[8], a[9], a[10], a[11], a[13], a[14], a[15], a[16], dv1
        prd_2_1 = int(17) * int(m1)
        prd_2_2 = int(16) * int(m2)
        prd_2_3 = int(15) * int(m3)
        prd_2_4 = int(14) * int(m4)
        prd_2_5 = int(13) * int(m5)
        prd_2_6 = int(12) * int(m6)
        prd_2_7 = int(11) * int(m7)
        prd_2_8 = int(10) * int(m8)
        prd_2_9 = int(9) * int(m9)
        prd_2_10 = 8 * int(m10)
        prd_2_11 = 7 * int(m11)
        prd_2_12 = 6 * int(m12)
        prd_2_13 = 5 * int(m13)
        prd_2_14 = 4 * int(m14)
        prd_2_15 = 3 * int(m15)
        prd_2_16 = 1 * int(m16)
        total_2 = int(prd_2_1) + int(prd_2_2) + int(prd_2_3) + int(prd_2_4) + int(prd_2_5) + int(prd_2_6) + int(prd_2_7) + int(prd_2_8) + \
            int(prd_2_9) + int(prd_2_10) + int(prd_2_11) + int(prd_2_12) + \
            int(prd_2_13) + int(prd_2_14) + int(prd_2_15) + int(prd_2_16)
        resto_2 = int(total_2) % 11
        subtrai_2 = int(11) - int(resto_2)
        subtrai_b = str(subtrai_2)
        dv2 = subtrai_b[-1]

        # Final
        cnpj = a + "-" + dv1 + dv2
        return cnpj

    def generate_nrProc_2(self):
        block_1 = random.randint(1000000, 9999999)
        block_2 = random.randint(2014, 2017)
        block_3 = 3
        block_4 = random.randint(10, 99)
        block_5 = random.randint(1000, 9999)

        processnumbernodv = str(
            str(block_1) + "-DD" + str(block_2) + str(block_3) + str(block_4) + str(block_5))

        n6 = str(processnumbernodv[0])
        n5 = str(processnumbernodv[1])
        n4 = str(processnumbernodv[2])
        n3 = str(processnumbernodv[3])
        n2 = str(processnumbernodv[4])
        n1 = str(processnumbernodv[5])
        n0 = str(processnumbernodv[6])
        a3 = str(processnumbernodv[10])
        a2 = str(processnumbernodv[11])
        a1 = str(processnumbernodv[12])
        a0 = str(processnumbernodv[13])
        j2 = str(processnumbernodv[14])
        t1 = str(processnumbernodv[15])
        r0 = str(processnumbernodv[16])
        o3 = str(processnumbernodv[17])
        o2 = str(processnumbernodv[18])
        o1 = str(processnumbernodv[19])
        o0 = str(processnumbernodv[20])
        d1 = 0

        r1_2 = str(n6) + str(n5) + str(n4) + \
            str(n3) + str(n2) + str(n1) + str(n0)
        r1 = int(r1_2) % int(97)
        r2_2 = str(r1) + str(a3) + str(a2) + str(a1) + \
            str(a0) + str(j2) + str(t1) + str(r0)
        r2 = int(r2_2) % int(97)

        r3_2 = str(r2) + str(o3) + str(o2) + str(o1) + str(o0) + str(d1)
        r3 = int(r3_2) % int(97)

        dv = int(98) - int(r3)
        dv = str(dv)

        d1_2 = dv[-1]
        d2_2 = dv[-2]
        processnumberdv = str(block_1) + str(d1_2) + str(d2_2) + \
            str(block_2) + str(block_3) + str(block_4) + str(block_5)
        return str(processnumberdv)

    def edit_excel_batch(self, product, event_type, yaml_mass):
        """Generate an excel batch with given YAML mass.
        "K" is for the item, "V" is for the value given on this item,
        We need only the value from the YAML mass to create the Excel File"""
        file_path_create_event = product + '\\batchImport\\'
        event_template = event_type + ".xlsx"
        locator = self.mass[yaml_mass]
        starting_row = 1
        column = 1       # Excel cells
        self.automationsetup.open_excel_document(
            file_path_create_event, event_template)
        for j, linha in locator.items():
            for k, v in linha.items():
                if "nrProcesso2_1070" in v:
                    v = self.generate_nrProc_2()
                    while v[0] == "0":
                        v = self.generate_nrProc_2()
                if "random_cnpj" in v:
                    v = self.automationsetup.generate_cnpj()
                if "random_valor" in v:
                    v = self.automationsetup.generate_random_number(
                        end=99999)
                if "previous_month" in v:
                    date = self.automationsetup.get_date_from_previous_month()
                    if date[1] == 1:
                        date[1] = int(12)
                        date[0] -= 1
                    else:
                        date[1] -= 1
                    v = str(date[1])
                if "actual_year" in v:
                    date = self.automationsetup.get_date_from_previous_month()
                    v = str(date[0])
                if "actual_date_dot" in v:
                    date = self.automationsetup.get_date_from_previous_month()
                    if date[1] == 1:
                        date[1] = int(12)
                        date[0] -= 1
                    else:
                        date[1] -= 1
                    if len(str(date[2])) == 1:
                        date[2] = str(0) + str(date[2])
                    if len(str(date[1])) == 1:
                        date[1] = str(0) + str(date[2])
                    v = str(date[2]) + "." + str(date[1]) + "." + str(date[0])
                if "ano-mes" in v:
                    date = self.automationsetup.get_date_from_previous_month()
                    if date[1] == 1:
                        date[1] = int(12)
                        date[0] -= 1
                    else:
                        date[1] -= 1
                    if len(str(date[2])) == 1:
                        date[2] = str(0) + str(date[2])
                    if len(str(date[1])) == 1:
                        date[1] = str(0) + str(date[2])
                    v = str(date[0]) + "-" + str(date[1])
                self.automationsetup.change_cell_on_excel(
                    'Sheet1', starting_row, column, str(v))
                column += 1
            column = 1               # Go back to the first column after jump to the next row
            starting_row += 1   # Jump to the next row on excel if needed
        self.builtin.set_global_variable("${PRODUCT}", product)
        self.builtin.set_global_variable(
            "${EVENT_TEMPLATE}", str(event_template))
        self.builtin.set_global_variable("${EXCEL_ROWS}", int(starting_row))
        self.automationsetup.save_excel_changes(
            file_path_create_event, event_template)
