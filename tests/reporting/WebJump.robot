*** Settings ***
Documentation    This test suite aims to validate WebJump test scenarios
Resource         ../../resources/support/index.robot
Suite Setup      Run Keywords  Before   AND
...              Set Selenium Speed    0.1
Suite Teardown   After
Force Tags       webjump

*** Test Cases ***

Scenario 1
    [Documentation]    Crie um cenário onde clicamos nos botões "One", "Two, e "Four", depois verifique a ausência dos mesmos.
    Given the user is on WebJump page
    When the user clicks on the buttons
    Then the buttons are not visible anymore

Scenario 2
    [Documentation]    Dentro da mesma página, clique nos botões "One", "Two" e "Four" que encontram-se dentro do painel "IFRAME BUTTONS" e valide a não-presença dos mesmos.
    Given the user is on WebJump page
    When the user clicks on the iframe buttons
    Then the iframe buttons are not visible anymore

Scenario 3
    [Documentation]    No cenário final, iremos preencher o campo "YourFirstName" com um texto qualquer. Clique no botão "One", cheque a opção "OptionThree", selecione a opção "ExampleTwo" dentro da select box, e valide a presença da imagem do logo do "Selenium Webdriver".
    Given the user is on WebJump page
    When the user does all the input steps on the third scenario
    Then the user validates that the page contains Selenium WebDriver image
