Feature: GET /lists/listId

Scenario: Get a specific list
    Given a list
    When we GET /lists/listId
    Then receive HTTP 200 OK
    And get the list