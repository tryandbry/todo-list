Feature: GET /health

  Scenario: Health check
      When we GET /health
      Then receive HTTP 200 OK