# Balanced Parentheses
This is a Python program that implements stacks, queues, and linked lists to recognize a balanced parentheses.

## Project Specification 

This program reads random strings from a user, consisting of any number of “(“ and “)” in any combination, and determine whether they contain balanced parentheses until the user wishes to end the program. A string with balanced parentheses is one where each “(“ is paired with a “)”. For instance, the string “()((()()))” has balanced parentheses, but the strings “(“, “)”, “(()”, “))((” and “()(()))()()” do not have balanced parentheses. 

- Both stack and queue data structures are used, where two queues can be used to simulate a stack's behavior. 
- Instead of using arrays for the underlying structures of stacks and queues, doubly linked lists are implemented, where a node contains a pointer to the previous as well as the next node in the sequence.
- A few classes are involved in this program, which are `Queue`, `Stack`, `Node`, `LinkedList`, `StackParenthesesChecker`, and `QueueParenthesesChecker`.
- The program exits when the user enters some input rather than 'y'.

## Example Output 

<img width="700" alt="Screen Shot 2022-05-16 at 12 43 04 PM" src="https://user-images.githubusercontent.com/105037989/168652679-0b66c1b7-40d8-46ee-afb5-46ff793b236b.png">
