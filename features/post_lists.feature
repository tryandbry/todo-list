Feature: Lists

  Scenario: POST /lists
     Given a list name
      When we POST /lists with the name
      Then receive HTTP 200 OK
      And receive a new list with the name