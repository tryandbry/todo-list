Feature: GET /items/itemId

    Scenario: Get a specific item
        Given a list
        And an item
        When we GET /items/itemId
        Then receive HTTP 200 OK
        And get the item