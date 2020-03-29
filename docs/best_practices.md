# Best practices guide
This section was prepared to act as a guide for writing good and clean test cases following our standards and rules for this project.

**Any suggestion or doubt that you have with the information below we can discuss and work to solve it, the idea is to make this project as collaborative as possible.**

## Pages

### Default page structure

Define your pages using the default page structure, every method that you need to implement you add it to the end of your class like the following:

```python
from PageObjectLibrary import PageObject

class YourPage(PageObject):
    PAGE_URL = "/RelativePathToYourPage"

    _locators = {
        # input
        "input_your_element": "id=Email",

        # button
        "button_your_element":  "xpath=//button[@type='submit']"
    }

    def _is_current_page(self):
      # code - Validate that you are in the correct page
      # you can implement with whatever you need as soon as you satisfy its responsability

    def your_method(self, your_argument="your_default_value"):
      # code here
```

### Locator strategy

To make easier and more visible to others developers we decided to follow some standards to how define our locators based on the pattern bellow:

The locator name should be defined using snack case and having first its type name so that we can group our elements together by type, this has intention of making easier to visualize and maintain:
- button_<localor_name>
- input_<locator_name>
- label_<locator_name>
- select_<locator_name>
- option_<locator_name>
- link_<locator_name>
- checkbox_<locator_name>
- radio_<locator_name>
- table_<locator_name>
- image_<locator_name>
- ...

Every locator that is a group of webelements should has its type used in the plural form like the following:
- buttons_<localor_name>
- inputs_<locator_name>
- ...

Follow the example to how to group the elements:
```python
class LoginPage(PageObject):
    PAGE_URL = "/Account/Login"

    _locators = {
        # input
        "input_username": "id=Email",
        "input_password": "id=Password",

        # button
        "button_submit":  "xpath=//button[@type='submit']"
    }
```

## Folder conventions
This project will be used to automate the SVR platform, so, we need to use a folder structure that fits our needs as products inside the platform. Use the following as example:

- common -> should has only keywords, fixtures or pages that can be used independent of product.
- reinf -> example of structure that should contain only keywords, fixtures or pages that is related with reinf product.
- reporting -> example of structure that should contain only keywords, fixtures or pages that is related with reporting product.
- ...

## Tags and Force Tags conventions
Because this project has different products and types of tests like regression, smoke and features tests we need to reinforce the standard for creating tags. Please follow the tips bellow:

### Force Tags

**Every tag defined in force tags will go to every test in its suite, so, be careful with the scope you add in your force tags to not add regression tests in your smoke tests scope for example**

Use the tags bellow to define your force tags:
```python
 # regression
 # smoke
 # product (e.g. italy, reinf, reporting)
 # feature (e.g. R-2010, company, filing_calendar)
```

### Tags on scenarios:
Use the tags bellow in your scenarios:
```python
 # positive
 # negative
 # smoke
 # regression
```

**This tags will be used to execute the tests cases on CI tools and will also be used to define profiles on the profiles.yaml file.**


## Documentation

### Suite documentation
Make sure you add documentation to your suites describing its functionality and other needed informations.

```python
*** Settings ***
Resource   ../../resources/support/index.robot
Documentation   This test suite aims to validade the Rules
...             on the distribution page.
...             For more information check the check the Italy Auomation scope page.
```

To ensure we are keeping the work flow we need document our test cases with the link of the related test case that was created on JIRA (that also has the automation fields filled like is test automated with "yes"). Follow the example:

```python
*** Test Cases ***
Testcase 1 - Create Distribution Rule
    [Documentation]   Jira Test Case: PGS-540
    Given the User Access the Distribution Rules Page
    ...
```
