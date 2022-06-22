*** Settings ***

Library     AppiumLibrary

Resource    ../resources/base/base.resource
Resource    ../resources/onboarding/onboarding.resource

Suite Setup       Open application for the first time
Test Setup        Launch Application
Test Teardown     Quit Application
Suite Teardown    Close Session

Force Tags        onboarding
Documentation     Pivot tests related to onboarding, welcome and login screens


*** Test Cases ***

Must display splash screen
    [Tags]              welcome_screen
    [Documentation]     Validates if splash screen is displayed after launching the app
    Wait Until Page Contains Element    ${img_splash}

Must display welcome carousel
    [Tags]              welcome_screen
    [Documentation]     Validates if welcome carousel is displayed after splash screen
    Wait Until Page Contains Element    ${img_splash}
    Wait Until Page Contains Element    ${img_wave}
    Wait Until Page Contains Element    ${img_logo}
    Element Text Should Be              ${txt_welcome_id}    ${txt_welcome_text}


Must scroll through onboarding welcome
    [Tags]              welcome_screen
    [Documentation]     Validates if welcome carousel is scrollable and if text and images change
    Wait Until Element Is Visible       ${img_logo}
    Element Text Should Be              ${txt_welcome_id}    ${txt_welcome_text}

    Swipe By Percent                    90    50    10    50
    Wait Until Element Is Visible       ${img_intro_plan}
    Element Text Should Be              ${txt_intro_title_id}       ${txt_intro_title_plan}
    Element Text Should Be              ${txt_intro_paragraph_id}   ${txt_intro_plan}

    Swipe By Percent                    90    50    10    50
    Wait Until Element Is Visible       ${img_intro_practice}
    Element Text Should Be              ${txt_intro_title_id}       ${txt_intro_title_practice}
    Element Text Should Be              ${txt_intro_paragraph_id}   ${txt_intro_practice}

    Swipe By Percent                    90    50    10    50
    Wait Until Element Is Visible       ${img_intro_support}
    Element Text Should Be              ${txt_intro_title_id}       ${txt_intro_title_support}
    Element Text Should Be              ${txt_intro_paragraph_id}   ${txt_intro_support}

Must login sucessfully
    [Tags]              login
    [Documentation]     Validates if user can log in in a existing account
    Log in with existing user
