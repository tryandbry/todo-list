Feature: GET /lists/listId/items

    Scenario: Get items
        Given a list
        And one or more items in that list
        When we GET /lists/listId/items
        Then receive HTTP 200 OK
        And get the items