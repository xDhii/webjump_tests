import os
import os.path
import JSONLibrary
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger
from robot.libraries.OperatingSystem import OperatingSystem
from PageObjectLibrary import PageObject


class InvoiceManipulation(PageObject):

    def __init__(self):
        self.builtin = BuiltIn()

    @property
    def transmissions(self):
        BuiltIn().import_library("../pages/italy/TransmissionPage.py")
        return BuiltIn().get_library_instance("TransmissionPage")

    @property
    def automationsetup(self):
        return BuiltIn().get_library_instance("automationsetup")

    @property
    def utils(self):
        return BuiltIn().get_library_instance("Utils")

    @property
    def mass(self):
        return BuiltIn().get_variable_value("${MASS}")

    @property
    def json(self):
        return BuiltIn().get_library_instance("JSONLibrary")

    @property
    def opsys(self):
        return OperatingSystem()

    @property
    def curdir(self):
        return os.getcwd()

    def manipulate_italy_invoice(self, operation_type, transmission_type, expected_scenario):
        """ Manipulates batch with the selected scenario """
        italy_mass = self.mass["TRANSMISSIONS"]["ITALY"][operation_type]
        locator = self.mass["TRANSMISSIONS"]["FOLDERS"]["italy_folder"] + \
            '\\transmission\\'
        mass_1 = self.mass["TRANSMISSIONS"]["ITALY"]

        if (self.mass["TRANSMISSIONS"]["italy_country"]) == "Italy":
            if (italy_mass[transmission_type]["transmission_type"]) == "B2B" and (italy_mass["transmission"]) == "BATCH":

                if (italy_mass[transmission_type][expected_scenario]["expected_scenario"]) == "Approved":
                    self.automationsetup.open_excel_document(
                        str(locator), mass_1["template_batch"])
                    self.transmissions.change_invoice_number_and_date("Italy")
                    self.transmissions.change_italy_id_number(
                        "BATCH", "B2B", "APPROVED")
                    self.transmissions.change_italy_communication_type(
                        "BATCH", "B2B")
                    self.transmissions.read_invoice_number_excel(
                        "INVNUM_B2BAPPROVED")
                    self.automationsetup.save_excel_changes(
                        str(locator), "BATCH_B2B_Approved.xlsx")

                elif (italy_mass[transmission_type][expected_scenario]["expected_scenario"]) == "Rejected":

                    self.automationsetup.open_excel_document(
                        str(locator), mass_1["template_batch"])
                    self.transmissions.change_invoice_number_and_date("Italy")
                    self.transmissions.change_italy_id_number(
                        "BATCH", "B2B", "REJECTED")
                    self.transmissions.change_italy_communication_type(
                        "BATCH", "B2B")
                    self.transmissions.read_invoice_number_excel(
                        "INVNUM_B2BREJECTED")
                    self.automationsetup.save_excel_changes(
                        str(locator), "BATCH_B2B_Rejected.xlsx")

                elif (italy_mass[transmission_type][expected_scenario]["expected_scenario"]) == "ApprovedWithErrors":

                    self.automationsetup.open_excel_document(
                        str(locator), mass_1["template_batch"])
                    self.transmissions.change_invoice_number_and_date("Italy")
                    self.transmissions.change_italy_id_number(
                        "BATCH", "B2B", "APPROVEDWERRORS")
                    self.transmissions.change_italy_communication_type(
                        "BATCH", "B2B")
                    self.transmissions.read_invoice_number_excel(
                        "INVNUM_B2BAPPROVEDWERRORS")
                    self.automationsetup.save_excel_changes(
                        str(locator), "BATCH_B2B_ApprovedWErrors.xlsx")

                elif (italy_mass[transmission_type][expected_scenario]["expected_scenario"]) == "NegativeQuantity":

                    self.automationsetup.open_excel_document(
                        str(locator), mass_1["template_batch"])
                    self.transmissions.change_invoice_number_and_date("Italy")
                    self.transmissions.change_italy_id_number(
                        "BATCH", "B2B", "NEGATIVEQUANTITY")
                    self.transmissions.change_italy_quantity(
                        "BATCH", "NEGATIVEQUANTITY", "wrong_quantity_value")
                    self.transmissions.change_italy_communication_type(
                        "BATCH", "B2B")
                    self.transmissions.read_invoice_number_excel(
                        "INVNUM_B2BNQUANTITY")
                    invoice_number = self.automationsetup.read_cell_on_excel(
                        'Sheet1', 2, 3)
                    invoice_date = self.automationsetup.read_cell_on_excel(
                        'Sheet1', 2, 4)
                    report_date = self.automationsetup.read_cell_on_excel(
                        'Sheet1', 2, 4)
                    self.builtin.set_global_variable(
                        "${invoice_num}", invoice_number)
                    self.builtin.set_global_variable(
                        "${invoice_date}", invoice_date)
                    self.builtin.set_global_variable(
                        "${report_date}", report_date)
                    self.automationsetup.save_excel_changes(
                        str(locator), "BATCH_B2B_NegativeQuantity.xlsx")

                elif (italy_mass[transmission_type][expected_scenario]["expected_scenario"]) == "Corrected_Quantity":

                    self.automationsetup.open_excel_document(
                        str(locator), mass_1["template_batch"])
                    invoice_num = self.builtin.get_variable_value(
                        "${invoice_num}")
                    invoice_date = self.builtin.get_variable_value(
                        "${invoice_date}")
                    report_date = self.builtin.get_variable_value(
                        "${report_date}")
                    self.transmissions.change_italy_id_number(
                        "BATCH", "B2B", "APPROVED")
                    self.transmissions.change_italy_quantity(
                        "BATCH", "CORRECTED_QUANTITY", "correct_quantity_value")
                    self.transmissions.change_italy_communication_type(
                        "BATCH", "B2B")
                    self.automationsetup.change_cell_on_excel(
                        'Sheet1', 2, 4, invoice_date)
                    self.automationsetup.change_cell_on_excel(
                        'Sheet1', 2, 3, invoice_num)
                    self.automationsetup.change_cell_on_excel(
                        'Sheet1', 2, 2, report_date)
                    self.transmissions.read_invoice_number_excel(
                        "INVNUM_CORRECTED_QUANTITY")
                    self.automationsetup.save_excel_changes(
                        str(locator), "BATCH_B2B_CorrectedNegativeQuantity.xlsx")

            if (italy_mass[transmission_type]["transmission_type"]) == "B2G" and (italy_mass["transmission"]) == "BATCH":

                if (italy_mass[transmission_type][expected_scenario]["expected_scenario"]) == "Accept":

                    self.automationsetup.open_excel_document(
                        str(locator), mass_1["template_batch"])
                    self.transmissions.change_invoice_number_and_date("Italy")
                    self.transmissions.change_italy_id_number(
                        "BATCH", "B2G", "ACCEPT")
                    self.transmissions.change_italy_communication_type(
                        "BATCH", "B2G")
                    self.transmissions.read_invoice_number_excel(
                        "INVNUM_B2GACCEPT")
                    self.automationsetup.save_excel_changes(
                        str(locator), "BATCH_B2G_Accept.xlsx")

                elif (italy_mass[transmission_type][expected_scenario]["expected_scenario"]) == "Reject":

                    self.automationsetup.open_excel_document(
                        str(locator), mass_1["template_batch"])
                    self.transmissions.change_invoice_number_and_date("Italy")
                    self.transmissions.change_italy_id_number(
                        "BATCH", "B2G", "REJECT")
                    self.transmissions.change_italy_communication_type(
                        "BATCH", "B2G")
                    self.transmissions.read_invoice_number_excel(
                        "INVNUM_B2GREJECT")
                    self.automationsetup.save_excel_changes(
                        str(locator), "BATCH_B2G_Reject.xlsx")

                elif (italy_mass[transmission_type][expected_scenario]["expected_scenario"]) == "Deadli":

                    self.automationsetup.open_excel_document(
                        str(locator), mass_1["template_batch"])
                    self.transmissions.change_invoice_number_and_date("Italy")
                    self.transmissions.change_italy_id_number(
                        "BATCH", "B2G", "DEADLI")
                    self.transmissions.change_italy_communication_type(
                        "BATCH", "B2G")
                    self.transmissions.read_invoice_number_excel(
                        "INVNUM_B2GDEADLI")
                    self.automationsetup.save_excel_changes(
                        str(locator), "BATCH_B2G_Deadli.xlsx")

                elif (italy_mass[transmission_type][expected_scenario]["expected_scenario"]) == "Undeli":

                    self.automationsetup.open_excel_document(
                        str(locator), mass_1["template_batch"])
                    self.transmissions.change_invoice_number_and_date("Italy")
                    self.transmissions.change_italy_id_number(
                        "BATCH", "B2G", "UNDELI")
                    self.transmissions.change_italy_communication_type(
                        "BATCH", "B2G")
                    self.transmissions.read_invoice_number_excel(
                        "INVNUM_B2GUNDELI")
                    self.automationsetup.save_excel_changes(
                        str(locator), "BATCH_B2G_Undeli.xlsx")

            if (italy_mass[transmission_type]["transmission_type"]) == "B2B" and (italy_mass["transmission"]) == "XML":

                if (italy_mass[transmission_type][expected_scenario]["expected_scenario"]) == "Approved":

                    self.utils.open_xml_file("italy", "TemplateXML.xml")
                    self.transmissions.change_italy_xml_invoice_number(
                        "INVXML_B2BAPPROVED")
                    self.transmissions.change_italy_xml_invoice_date()
                    self.transmissions.change_italy_xml_id_number(
                        "XML", "B2B", "APPROVED")
                    self.transmissions.change_italy_xml_communication_type(
                        "XML", "B2B")
                    self.utils.save_xml_changes("italy", "XML_B2B_Approved")

                elif (italy_mass[transmission_type][expected_scenario]["expected_scenario"]) == "Rejected":

                    self.utils.open_xml_file("italy", "TemplateXML.xml")
                    self.transmissions.change_italy_xml_invoice_number(
                        "INVXML_B2BREJECTED")
                    self.transmissions.change_italy_xml_invoice_date()
                    self.transmissions.change_italy_xml_id_number(
                        "XML", "B2B", "REJECTED")
                    self.transmissions.change_italy_xml_communication_type(
                        "XML", "B2B")
                    self.utils.save_xml_changes("italy", "XML_B2B_Rejected")

            if (italy_mass[transmission_type]["transmission_type"]) == "B2G" and (italy_mass["transmission"]) == "XML":

                if (italy_mass[transmission_type][expected_scenario]["expected_scenario"]) == "Accept":

                    self.utils.open_xml_file("italy", "TemplateXML.xml")
                    self.transmissions.change_italy_xml_invoice_number(
                        "INVXML_B2GACCEPT")
                    self.transmissions.change_italy_xml_invoice_date()
                    self.transmissions.change_italy_xml_id_number(
                        "XML", "B2G", "ACCEPT")
                    self.transmissions.change_italy_xml_communication_type(
                        "XML", "B2G")
                    self.utils.save_xml_changes("italy", "XML_B2G_Accept")

                elif (italy_mass[transmission_type][expected_scenario]["expected_scenario"]) == "Reject":

                    self.utils.open_xml_file("italy", "TemplateXML.xml")
                    self.transmissions.change_italy_xml_invoice_number(
                        "INVXML_B2GREJECT")
                    self.transmissions.change_italy_xml_invoice_date()
                    self.transmissions.change_italy_xml_id_number(
                        "XML", "B2G", "REJECT")
                    self.transmissions.change_italy_xml_communication_type(
                        "XML", "B2G")
                    self.utils.save_xml_changes("italy", "XML_B2G_Reject")

            if (italy_mass[transmission_type]["transmission_type"]) == "B2B" and (italy_mass["transmission"]) == "FATTURAPA":

                if (italy_mass[transmission_type][expected_scenario]["expected_scenario"]) == "Approved":

                    self.utils.open_xml_file("italy", "TemplateFatturaPA.xml")
                    self.transmissions.change_italy_xml_invoice_number(
                        "INV_FATTURAPA_B2BAPPROVED", "Numero")
                    self.transmissions.change_italy_xml_invoice_date(
                        "Data", "%Y-%m-%d")
                    self.utils.save_xml_changes(
                        "italy", "FatturaPA_B2B_Approved")

                elif (italy_mass[transmission_type][expected_scenario]["expected_scenario"]) == "Wrong_quantity":
                    self.utils.open_xml_file("italy", "TemplateFatturaPA.xml")
                    self.transmissions.change_italy_xml_invoice_number(
                        "INV_FATTURAPA_B2B_WRONG_QUANTITY", "Numero")
                    self.transmissions.change_italy_xml_invoice_date(
                        "Data", "%Y-%m-%d")
                    self.transmissions.change_italy_xml_quantity(
                        "FATTURAPA", "B2B", "WRONG_QUANTITY", "wrong_quantity_value")
                    invoice_date = self.utils.read_value_xml('Data')
                    invoice_number = self.utils.read_value_xml('Numero')
                    self.builtin.set_global_variable(
                        "${invoice_num}", invoice_number)
                    self.builtin.set_global_variable(
                        "${invoice_date}", invoice_date)
                    self.utils.save_xml_changes(
                        "italy", "FatturaPA_B2B_WRONG_QUANTITY")

                elif (italy_mass[transmission_type][expected_scenario]["expected_scenario"]) == "Corrected_Quantity":
                    self.utils.open_xml_file("italy", "TemplateFatturaPA.xml")
                    invoice_num = self.builtin.get_variable_value(
                        "${invoice_num}")
                    invoice_date = self.builtin.get_variable_value(
                        "${invoice_date}")
                    self.transmissions.change_italy_xml_id_number(
                        "FATTURAPA", "B2B", "CORRECTED_QUANTITY", "CodiceDestinatario")
                    self.transmissions.change_italy_xml_quantity(
                        "FATTURAPA", "B2B", "CORRECTED_QUANTITY", "correct_quantity_value")
                    self.utils.change_value_xml('Data', invoice_date)
                    self.utils.change_value_xml('Numero', invoice_num)
                    invoice_number = self.utils.read_value_xml('Numero')
                    self.builtin.set_global_variable(
                        "${INV_FATTURAPA_CORRECTED_QUANTITY}", invoice_number)
                    self.utils.save_xml_changes(
                        "italy", "FatturaPA_B2B_CORRECTED_QUANTITY")

    def open_json_file(self, country, file_name):
        """ Open a JSON file """
        path_locator = self.curdir + '\\resources\\fixtures\\'
        data = self.json.load_json_from_file(
            str(path_locator) + country + '\\transmission\\' + file_name + '.json')
        BuiltIn().set_suite_variable('${JSON}', data)

    def edit_json_file(self, element_path, value):
        """ Edit a JSON file """
        data = BuiltIn().get_variable_value('${JSON}')
        self.json.update_value_to_json(data, element_path, value)

    def convert_json_to_string(self):
        """ Convert JSON file to a string """
        data = BuiltIn().get_variable_value("${JSON}")
        json_string = self.json.convert_json_to_string(data)
        BuiltIn().set_suite_variable("${JSON_STRING}", json_string)

    def get_invoice_number_field_value_json(self, country, variable_name):
        """ Get Invoice Number field from a JSON """
        data = BuiltIn().get_variable_value("${JSON}")
        invoice_number_path = self.get_json_invoice_number_path_by_country(
            '%s' % country)
        value = str(self.json.get_value_from_json(data, invoice_number_path)).replace(
            "'", '').replace("[", '').replace("]", '')
        BuiltIn().set_suite_variable('${%s}' % variable_name, value)
        return value

    def save_json_file(self, country, file_name):
        """ Save a JSON file """
        path_locator = self.curdir + '\\resources\\fixtures\\'
        json_string = BuiltIn().get_variable_value("${JSON_STRING}")
        self.opsys.create_file(str(path_locator) + country +
                               '\\transmission\\' + file_name + '.json', json_string)

    def get_json_invoice_number_path_by_country(self, country):
        """ Get JSON Invoice Number Path by Country """
        if country == 'Italy':
            invoice_number_path = '$..Entities[?(@.Name=="DATIGENERALIDOCUMENTO")].Fields[?(@.Name=="NUMERO")].Value'
        elif country == 'Hungary':
            invoice_number_path = '$..Entities[?(@.Name=="INVOICEDATA")].Fields[?(@.Name=="INVOICENUMBER")].Value'
        return invoice_number_path

    def get_json_date_path_by_country(self, country):
        """ Get JSON Date Path by Country """
        if country == 'Italy':
            date_path = '$..Entities[?(@.Name=="DATIGENERALIDOCUMENTO")].Fields[?(@.Name=="DATA")].Value'
        elif country == 'Hungary':
            date_path = '$..Entities[?(@.Name=="INVOICEDATA")].Fields[?(@.Name=="INVOICEISSUEDATE")].Value'
        elif country == 'HungaryReference':
            date_path == '$..Entities[?(@.Name=="INVOICEANNULMENT")].Fields[?(@.Name=="ANNULMENTREFERENCE")].Value'
        return date_path

    def manipulate_json(self, operation_type, transmission_type, expected_scenario):
        """ Manipulate a JSON file """
        italy_mass = self.mass["TRANSMISSIONS"]["ITALY"][operation_type]

        if (self.mass["TRANSMISSIONS"]["italy_country"]) == "Italy":
            if (italy_mass[transmission_type]["transmission_type"]) == "B2B" and (italy_mass["transmission"]) == "JSON":

                if (italy_mass[transmission_type][expected_scenario]["expected_scenario"]) == "ValidAllegati":

                    self.send_valid_allegati()

                if (italy_mass[transmission_type][expected_scenario]["expected_scenario"]) == "AllegatiWithoutExtension":

                    self.send_allegati_without_extension()

    def send_valid_allegati(self):
        """ Send a Valid Allegati Invoice """
        # Open File
        self.open_json_file("italy", "JSONTemplate")

        # Invoice Number
        invoice_number_path = self.get_json_invoice_number_path_by_country(
            "Italy")
        string = self.automationsetup.generate_random_string(7)
        invoice_number = self.automationsetup.generate_string_with_random_number(
            string, 0, 99999999)
        self.edit_json_file(invoice_number_path, invoice_number)

        # Date Value
        date_path = self.get_json_date_path_by_country("Italy")
        date = self.automationsetup.generate_current_date()
        self.edit_json_file(date_path, date)

        # Convert to String
        self.convert_json_to_string()

        # Save Value
        self.get_invoice_number_field_value_json(
            "Italy", "INVNUM_VALIDALLEGATI")
        self.save_json_file("italy", "JSON_ValidAllegati")

    def send_allegati_without_extension(self):
        """ Send a Allegati Without Extension Invoice """
        # Open File
        self.open_json_file("italy", "JSONTemplate")

        # Invoice Number
        invoice_number_path = self.get_json_invoice_number_path_by_country(
            "Italy")
        string = self.automationsetup.generate_random_string(7)
        invoice_number = self.automationsetup.generate_string_with_random_number(
            string, 0, 99999999)
        self.edit_json_file(invoice_number_path, invoice_number)

        # Date Value
        date_path = self.get_json_date_path_by_country("Italy")
        date = self.automationsetup.generate_current_date()
        self.edit_json_file(date_path, date)

        # Change Allegati Extension
        extension_path = '$..Entities[?(@.Name=="ALLEGATI")].Fields[?(@.Name=="FORMATOATTACHMENT")].Value'
        self.edit_json_file(extension_path, '')

        # Convert to String
        self.convert_json_to_string()

        # Save Value
        self.get_invoice_number_field_value_json(
            "Italy", "INVNUM_ALLEGATIWEXTENSION")
        self.save_json_file("italy", "JSON_AllegatiWExtension")
