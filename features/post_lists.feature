Feature: POST /lists

  Scenario: Create new list
     Given a list name
      When we POST /lists
      Then receive HTTP 200 OK
      And receive a new list with the name