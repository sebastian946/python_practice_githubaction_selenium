Feature: The user enter the soucedemo web page

    @login
    Scenario: Validate the user can login
        Given user enter the source demo web page
        When user enter the user 1 and password click login
        Then show the login in the web page
    
    Scenario: Validate the message validation
        Given user enter the source demo web page
        When user enter the user 7 and login invalid
        Then show message is incorrect the user and password