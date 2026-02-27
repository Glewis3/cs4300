Feature: Movie API Behavior
  Scenario: Retrieve the list of movies
    Given a movie named "Avatar" exists in the database
    When I request the movie list from the API
    Then I should receive a 200 status code