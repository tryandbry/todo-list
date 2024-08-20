Feature: GET /items

    Scenario: Get items
        Given one or more lists
        And one or more items in each list
        When we GET /items/
        Then receive HTTP 200 OK
        And get the items