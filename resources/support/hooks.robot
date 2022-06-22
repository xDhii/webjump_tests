*** Keywords ***
Before
    import all resources
    start automation

After
    after suite

Before Each
# if needed

After Each
# if needed (e.g. taking screenshots)

Open Session
    Set Appium Timeout     20
    Open Real Device Application
    # Open Test Application

Close Session
    Capture Page Screenshot
    Close Application

Launch Test Application
    Launch Application
    Log in with existing user
    Wait until Home is visible

Open Test Application
    Open Application    http://localhost:4723/wd/hub
    ...                 automationName=${ANDROID_AUTOMATION_NAME}
    ...                 platformName=${ANDROID_PLATFORM_NAME}
    ...                 deviceName=${ANDROID_DEVICE_NAME}
    ...                 app=${ANDROID_APP}
    ...                 uiid=${ANDROID_UIID}
    ...                 avd=${ANDROID_AVD}

Open Real Device Application
    Open Application    http://localhost:4723/wd/hub
    ...                 automationName=${ANDROID_AUTOMATION_NAME}
    ...                 platformName=${ANDROID_PLATFORM_NAME}
    ...                 deviceName=${ANDROID_DEVICE_NAME}
    ...                 app=${ANDROID_APP}
    ...                 uiid=RQCR9005QEW
