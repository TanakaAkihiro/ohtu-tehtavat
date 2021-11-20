*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command
    Input Credentials  kalle  toinen123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input New Command
    Input Credentials  ka  kalle123
    Output Should Contain  Username should contain only lowercase letters (a to z) and be at least 3 letters long

Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  konsta  mo
    Output Should Contain  Password should not contain only letters and it should be at least 8 letters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials  konsta  moimoimoi
    Output Should Contain  Password should not contain only letters and it should be at least 8 letters long

*** Keywords ***
Input New Command And Create User
    Input New Command
    Input Credentials  kalle  kalle123