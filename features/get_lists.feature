Feature: GET /lists

    Scenario: Get lists
        Given one or more lists
        When we GET /lists/
        Then receive HTTP 200 OK
        And get the lists