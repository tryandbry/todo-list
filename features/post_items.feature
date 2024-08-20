Feature: POST /items

  Scenario: Create new item
     Given a list
     And an item name
      When we POST /lists/listId/items
      Then receive HTTP 200 OK
      And receive a new item with the name
      And associated with the list