*** Keywords ***
the user is on WebJump page
    Go to page    WebJumpPage
    The Current Page Should Be  WebJumpPage

the user clicks on the buttons
    click on webjump buttons

the buttons are not visible anymore
    check for hidden buttons

the user clicks on the iframe buttons
    click on webjump iframe buttons

the iframe buttons are not visible anymore
    check for hidden iframe buttons

the user does all the input steps on the third scenario
    fill the YourFisrtName field
    click on button one
    check OptionThree checkbox
    select ExampleTwo on the select box

the user validates that the page contains Selenium WebDriver image
    validate selenium webdriver image
