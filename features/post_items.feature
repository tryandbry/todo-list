Feature: Items

  Scenario: POST /items
     Given a list
     And an item name
      When we POST /lists/listId/items with the name
      Then receive HTTP 200 OK
      And receive a new item with the name
      And associated with the list