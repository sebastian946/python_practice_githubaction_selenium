Feature: Validate all products in the sauce demo

    @validate
    Scenario: Get Information about the product
        Given user enter the source demo web page
        When user enter the user 1 and password click login
        When get all products
