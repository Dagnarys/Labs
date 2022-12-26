# Created by Dagnarys at 20.12.2022
Feature: Get only unique elements of list

  Scenario Outline: Getting list of unique elements
    Given some data <list>
    When data is getting unique and there is case <case>
    Then data is unique <result>
    Examples:
      | list                           |result     | case |
      | [1, 1, 1, 1, 1, 2, 2, 2, 2, 2] |[1,2]      | False|


  Scenario Outline: Getting list of unique letters
    Given some data <list>
    When data is getting unique and there is case <case>
    Then data is unique <result>
    Examples:
      | list                                     | result                | case  |
      | ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B'] | ['a', 'A', 'b', 'B']  | False |

  Scenario Outline: Getting list of unique letters with lower case
    Given some data <list>
    When data is getting unique and there is case <case>
    Then data is unique <result>
    Examples:
      | list                                     | result               | case |
      | ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B'] | ['a','b'] | True |