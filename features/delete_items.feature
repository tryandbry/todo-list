Feature: DELETE /items/itemId

    Scenario: Delete item
        Given a list
        And an item
        When we DELETE /items/itemId
        Then receive HTTP 204 No Content