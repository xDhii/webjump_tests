from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger
from DebugLibrary import DebugLibrary

class WebJumpPage(PageObject):
    PAGE_URL = "/qa-test/"

    _locators = {
        # buttons
        "button_one": "xpath=//div[@id='panel_body_one']//button[@id='btn_one']",
        "button_two": "xpath=//div[@id='panel_body_one']//button[@id='btn_two']",
        "button_three": "xpath=//div[@id='panel_body_one']//button[@id='btn_three']",
        "button_four": "xpath=//div[@id='panel_body_one']//button[@id='btn_link']",

        # iframe buttons
        "button_one_iframe": "xpath=//div[@class='col-sm-12']//button[@id='btn_one']",
        "button_two_iframe": "xpath=//div[@class='col-sm-12']//button[@id='btn_two']",
        "button_three_iframe": "xpath=//div[@class='col-sm-12']//button[@id='btn_three']",
        "button_four_iframe": "xpath=//div[@class='col-sm-12']//button[@id='btn_link']",

        # input
        "input_first_name": "xpath=//div[@class='form-group']//input[@id='first_name']",

        # checkbox
        "checkbox_option_three": "xpath=//div[@class='col-sm-4']//input[@id='opt_three']",

        # selectbox
        "selectbox_main": "xpath=//div[@class='col-sm-4']//select[@id='select_box']",
        "selectbox_option_two": "xpath=//option[contains(text(), 'ExampleTwo')]",

        # image
        "image_selenium": "xpath=//img[@alt='selenium']",

        # iframe
        "iframe_buttons": "xpath=//iframe[@src='buttons.html']"
    }

    def _is_current_page(self):
        location = self.selib.get_location()
        if not location.endswith(self.PAGE_URL):
            message = "Expected location to end with " + \
                self.PAGE_URL + " but it did not"
            raise Exception(message)
        return True

    @property
    def mass(self):
        return BuiltIn().get_variable_value("${MASS}")

    @property
    def utils(self):
        return self.builtin.get_library_instance("Utils")

    @property
    def automationsetup(self):
        return BuiltIn().get_library_instance("automationsetup")

    def click_on_webjump_buttons(self):
        self.automationsetup.wait_for_click(self.locator.button_one)
        self.automationsetup.wait_for_click(self.locator.button_two)
        self.automationsetup.wait_for_click(self.locator.button_three)
        self.automationsetup.wait_for_click(self.locator.button_four)

    def click_on_webjump_iframe_buttons(self):
        self.automationsetup.wait_for_keyword("select frame", self.locator.iframe_buttons)
        self.automationsetup.wait_for_click(self.locator.button_one_iframe)
        self.automationsetup.wait_for_click(self.locator.button_two_iframe)
        self.automationsetup.wait_for_click(self.locator.button_three_iframe)
        self.automationsetup.wait_for_click(self.locator.button_four_iframe)

    def check_for_hidden_buttons(self):
        self.automationsetup.wait_for_keyword("element should not be visible", self.locator.button_one)
        self.automationsetup.wait_for_keyword("element should not be visible", self.locator.button_two)
        self.automationsetup.wait_for_keyword("element should not be visible", self.locator.button_three)
        self.automationsetup.wait_for_keyword("element should not be visible", self.locator.button_four)

    def check_for_hidden_iframe_buttons(self):
        self.automationsetup.wait_for_keyword("element should not be visible", self.locator.button_one_iframe)
        self.automationsetup.wait_for_keyword("element should not be visible", self.locator.button_two_iframe)
        self.automationsetup.wait_for_keyword("element should not be visible", self.locator.button_three_iframe)
        self.automationsetup.wait_for_keyword("element should not be visible", self.locator.button_four_iframe)

    def fill_the_YourFisrtName_field(self):
        self.automationsetup.wait_input_text(self.locator.input_first_name, "Adriano")

    def click_on_button_one(self):
        self.automationsetup.wait_for_click(self.locator.button_one)

    def check_optionthree_checkbox(self):
        self.selib.select_checkbox(self.locator.checkbox_option_three)

    def select_exampletwo_on_the_select_box(self):
        self.automationsetup.wait_for_click(self.locator.selectbox_main)
        self.automationsetup.wait_for_click(self.locator.selectbox_option_two)

    def validate_selenium_webdriver_image(self):
        self.selib.page_should_contain_element(self.locator.image_selenium)
