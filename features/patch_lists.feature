Feature: PATCH /lists/listId

Scenario: Update list name
    Given a list
    And a new list name
    When we PATCH /lists/listId
    Then receive HTTP 200 OK
    And receive the list with the new name