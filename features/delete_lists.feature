Feature: DELETE /lists/listId

    Scenario: Delete list
        Given a list
        When we DELETE /lists/listId
        Then receive HTTP 204 No Content