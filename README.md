About my project:
For my project I create a interpreter for normal mathamatical expressions with parentheses. This project was actually something I had started on a very long time ago, when I first started with python. I ended up giving up very early on it because I just didn't know enough to finish it. Fast foward to present day, I was able to finish it due to what I learned in Programming Languages.

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
