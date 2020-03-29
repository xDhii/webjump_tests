# Tutorial

Use this section as a helper to write your test cases.
For project installation and usage, please, go to README.md

## Test data files

### Structure

You can put your test data files on the ./resources/fixtures path. To organizations means it's preferable that you create a subfolder for your suit file.
In order to do that it means every suit file should have the correspondent folder to its product. Like the following:
\
..\
**fixtures**\
└── **reinf**\
└──└── **R-2010**\
├──└──└── r-2010.yaml\
├──└──└── r-2010.xlsx\
└──└── **R-2020**\
├──└──└── r-2020.yaml\
├──└──└── r-2020.xlsx\

It also can have another organization approach inside fixtures path, but, is recommended avoid breaking this standard.

### Files

You can use json files or either yaml/yml files. It will be the model classes who needs to know what extension you're using and the path to the correct files for each mass.

Each mass should have a unique accessor name inside the file, so, we can call the unique name inside our tests to get the wanted mass value.
Examples:

Yaml example:

```yaml
create_valid_company_1: # <= first key as unique accessor name
  DocumentTypesByCompanyCode:
    - CompanyCode: "890900535"
      DocumentTypes:
        - "COL_FAC"
  Name: "Automation Company Name"
  Email: "automation.company@test.com"
  SearchCode: "KFQ"

create_invalid_company_1: # <= first key as unique accessor
  DocumentTypesByCompanyCode:
    - CompanyCode: ""
      DocumentTypes:
        - ""
  Name: ""
  Email: ""
  SearchCode: ""
```

Json example:

```json
// first key as unique accessor name
{
  "invalid_invoice_6": {
    // <= unique accessor: invalid_invoice_6
    "Entities": [
      {
        "Name": "Product",
        "Fields": [
          {
            "Name": "Country",
            "Value": "HU"
          },
          {
            "Name": "DocType",
            "Value": "HUN_SALES"
          },
          {
            "Name": "ProcessType",
            "Value": "Outbound"
          }
        ]
      }
    ]
  }
}
```

**Avoid using json files to small data mass.**

## Pages

The pages classes should has the following attributes:

- PAGE_URL: relative url to the current page.
- \_locators: locatos map that should be define with the same usage as default robotframework seleniumlibrary locators.
- \_is_current_page: Function that will be executed when the page is loaded to see if the current page was correct loaded. You can put whatever you need inside its function as soon as it executes its responsibility.

Example:

```python
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn

class LoginPage(PageObject):
    PAGE_URL = "/Account/Login"

    _locators = {
        "username": "id=Email",
        "password": "id=Password",
        "submit_button":  "xpath=//button[@type='submit']"
    }

    def _is_current_page(self):
        location = self.selib.get_location()
        if not location.endswith(self.PAGE_URL):
            message = "Expected location to end with " + \
                      self.PAGE_URL + " but it did not"
            raise Exception(message)
        return True

    def do_login(self, user):
        self.enter_username(user['user'])
        self.enter_password(user['password'])
        with self._wait_for_page_refresh():
            self.click_the_login_button()

    def enter_username(self, username):
        """Type the given text into the username field """
        self.automationsetup.wait_input_text(self.locator.username, username)

    def enter_password(self, password):
        """Type the given text into the password field"""
        self.automationsetup.wait_input_text(self.locator.password, password)

    def click_the_login_button(self):
        """Clicks the submit button on the form"""
        with self._wait_for_page_refresh():
            self.automationsetup.wait_for_keyword('click button', self.locator.submit_button)
```

Obs.: The .py file name has to be the same as the class name. On the example below, both are named
as "LoginPage".

Path Example:
\
..\
**resources**\
└── **pages**\
└──└── **common**\
├──└──└── LoginPage.py

Class Example:

```python
class LoginPage(PageObject):
    PAGE_URL = "/Account/Login"
```

The locators defined in each page should be used only inside it. Then you will be able to define methods that has interaction with this elements, also, you can create methods that has logic using python and also import whatever library this page needs.

**In order to this class be a Page Object we use the PageObjectLibrary and inherit it to our class**

### Using a page

To use the selenium webelements:

```python
    self.locator.your_locator
```

To use methods of SeleniumLibrary:

```python
    # the same method of robotframework
    self.selib.selenium_library_method()

    # e.g.
    self.automationsetup.wait_input_text(self.locator.your_input_text_locator)
```

To use BuiltIn methods:

```python
    self.builtIn.some_method()
```

To use methods you written inside the page class:

```python
    self.your_method()
```

In order to go to a given page you can use the following keyword inside your tests or keywords files:

```python
    Wait Until Keyword Succeeds    20s    1s    Go to page    YourPage
```

If you went to that page using other method you will need to use the following keyword due to the page needs to be imported inside robotframework as a library:

```python
    Wait Until Keyword Succeeds    15s    1s    The Current Page Should Be    YourPage
```

## automationsetup

This library should provide all we need to test our application without too much effort to do it.

## Project Keywords

You can define your keywords inside the keywords folder. It's a good practice keep just one keyword file to each test suit file and inside its correspondent folder structure.

### Importing keywords files

You don't need to import keywords files if they are inside keywords and support folders. Inside the class ./resources/lib/BeforeConfiguration.py we have the method that dynamically imports all keywords files from the project.

```python
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
```

You don't need to import your keywords resources, but you need to import index.robot inside your suit file:

```python
*** Settings ***
Resource         ../../resources/support/index.robot
Suite Setup      Before
Suite Teardown   After
```

Note that to the project work properly you will need to use the keyword "Before" and "After", you can see it on the code above. This keyword has the implementation inside the hooks file, you can also add other keywords you define inside your suit or in other files in addition to its setup, but, you will also need the Before and After too:

```python
*** Keywords ***
Before
    import all resources
    start automation

After
    after suite
```

