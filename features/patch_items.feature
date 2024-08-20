Feature: PATCH /items/itemId

    Scenario: Update item name
        Given a list
        And an item
        And a new item name
        When we PATCH /items/itemId
        Then receive HTTP 200 OK
        And receive the item with the new name

    Scenario: Update item completed status
        Given a list
        And an item
        And a new item completed status
        When we PATCH /items/itemId
        Then receive HTTP 200 OK
        And receive the item with the new completed status