About my project:


About the grammar:
The following is the inital grammar that I made using the Lark online IDE.
It worked with all my test cases and was very helpful in the creation of my project.

?start: expr
expr: term | factor
term: LP expr+ RP | expr+
?factor: var | NUMBER
var: /["+"-"-"-"*"-"%"]/
LP: /["("]/
RP: /[")"]/
%import common.NUMBER
%import common.WS
%ignore WS

The following is what symbols to use, when entering an input in my program:
0,1,2,3,4,5,6,7,8,9 
+ = plus
- = minus
* = multiplication
% = division 
( = left parentheses
) = right parentheses
***The "/" symbol did not want to work in my program so I just changed it for my purposes***

About testing:
For testing my inital plan was to have an external file that was able to be preloaded with possible test case and then return if it was true or false.
Instead I create a a function within my program that will do this testing.
It will allows run each time my program is first launched.
This feature an be deactivated by commentting out line #######################################
