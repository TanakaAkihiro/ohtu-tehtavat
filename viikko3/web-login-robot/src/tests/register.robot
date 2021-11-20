*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Registeration Page


*** Test Cases ***
Register With Valid Username And Password
    Set Username  konsta
    Set Password  konsta123
    Set Password Confirmation  konsta123
    Submit Registeration Credentials
    Registeration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  mi
    Set Password  mikko123
    Set Password Confirmation  mikko123
    Submit Registeration Credentials
    Registeration Should Fail With Message  Username should contain only lowercase letters (a to z) and be at least 3 letters long

Register With Valid Username And Too Short Password
    Set Username  mikko
    Set Password  m
    Set Password Confirmation  m
    Submit Registeration Credentials
    Registeration Should Fail With Message  Password should not contain only letters and it should be at least 8 letters long

Register With Nonmatching Password And Password Confirmation
    Set Username  mikko
    Set Password  mikko123
    Set Password Confirmation  mikko456
    Submit Registeration Credentials
    Registeration Should Fail With Message  Password and password confirmation didn't match

*** Keywords ***
Registeration Should Succeed
    Welcome Page Should Be Open

Registeration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Registeration Credentials
    Click Button  Register
