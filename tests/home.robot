*** Settings ***
Documentation    This test suite aims to validate WebJump test scenarios
Resource         ../../resources/support/index.robot
Suite Setup      Run Keywords  Before   AND
...              Set Selenium Speed    0.1
Suite Teardown   After
Force Tags       webjump


Library      AppiumLibrary
# Resource    ../resources/base/base.resource
# Resource     ../resources/home/home.resource
# Resource     ../resources/goal/goal_kw.resource
# Resource     ../resources/goal/upd_kw.resource
# Resource    ../resources/ciglog/ciglog.resource
# Variables    ../resources/login.yaml

Suite Setup       Open Session
Test Setup        Launch Test Application
Test Teardown     Quit Application
Suite Teardown    Close Session

Force Tags        homescreen
Documentation     Pivot tests related to homescreen and its main widgets, as UPD, Log and Goal


*** Test Cases ***

1 - Must log a cig
    [Tags]              log     robot:skip-on-failure       skipping
    [Documentation]     Validates if logging a cig reflects on home screen widget
    ...                 This test also is skipped for demonstration
    Log                 This test is skipped
    Trigger usage log flow
    Select smoking reason       1
    Validate ashtray value

2 - Must log a cig of each reason
    [Tags]              cig_log     skipping
    [Documentation]     Validates if logging a cig of each reason still reflects on home screen widget
    ...                 Also, this test is skipped for demonstration
    Fail                This is intentionally failing       failing     -s*
    Select one of each kind


3 - Must update UPD
    [Tags]                  usage_per_day
    [Documentation]         Validates if updating UPD reflects on home screen widget
    Trigger UPD flow
    Set UPD                 40
    ${expected_upd} =       Set Variable          40
    Confirm UPD
    Validate UPD value      ${expected_upd}

4 - Must update UPD and cancel
    [Tags]              usage_per_day
    [Documentation]     Validates if not updating UPD reflects on home screen widget
    Trigger UPD flow
    Set UPD                 50
    ${expected_upd} =       Set Variable          ${current_upd}
    Cancel UPD
    Validate UPD value      ${expected_upd}

5 - Must update goal to Learn
    [Tags]              goal    usage_per_day
    [Documentation]     Validates if updating Goal reflects on home screen widget
    Set Goal to Learn        30
    Validate UPD value       30

6 - Must update goal and cancel
    [Tags]              goal    usage_per_day
    [Documentation]     Validates if not updating Goal reflects on home screen widget
    ...                 Co-dependant on previous test for simplicity reasons
    Set Goal to Learn and cancel    10
    Validate UPD value              ${current_upd}

7 - Must update goal to Reduce
    [Tags]              goal    usage_per_day
    [Documentation]     Validates if updating Goal reflects on home screen widget
    Set Goal to Reduce       20
    Validate UPD value       20

8 - Must update goal to Prepare
    [Tags]              goal    usage_per_day
    [Documentation]     Validates if updating Goal reflects on home screen widget
    Set Goal to Prepare    30
    Validate commit celebration
    Click on close
    Validate UPD value     30


9 - Must update goal to Stay Quit
    [Tags]              goal    usage_per_day
    [Documentation]     Validates if updating Goal reflects on home screen widget



