# Balanced Brackets
Python implementation of balanced brackets challenge. 

## Challenge Description
There are 3 kinds of **Brackets**: **[] {} ()**. Given a string of characters, check if all the brackets in the string are balanced. 
A string is **balanced** if all the _start_ and _end_ brackets are **in** a **correct order** so they match each other. 

Here are some balanced strings:
```
- {}
- (hello)[world]
- [({}{}{})([])]
- { ( [ ] ) } ( )
```

Here are some unbalanced strings:
```
- [}
- { [ ( ] ) }
- {((})]]
- { this is unbalanced )]
```
<p align="right">(<a href="#top">back to top</a>)</p>

### Given
> Strings of brackets, determine whether each sequence of brackets is balanced. If a string is balanced, return YES. Otherwise, return NO.
<p align="right">(<a href="#top">back to top</a>)</p>

### Function Description
> It must return a string: YES if the sequence is balanced or NO if it is not.
<p align="right">(<a href="#top">back to top</a>)</p>

## My Approach
I decided to go with stacks to solve this problem.

### Algorithm
- Declare a stack
- Traverse the string
  - if the character is an opening bracket then push it to stack
  - if the character is a closing bracket then pop the stack and check if the popped and the character are matching brackets
  - if they match continue else string is not balanced
  - after traversal, check if stack is empty
  - if stack is empty; String is balanced else not balanced

### Pseudo Code
```
    func is_balanced(string):
        var stack
        var balanced = "NO"

        for char in string:
            if char is an opening bracket:
                add char to stack
            else if char is a closing bracket:
                if stack is not empty:
                    popped = stack.pop
                    if popped is not a match for char:
                        return balanced
                else:
                    return balanced
        
        if stack is empty:
            balanced = "YES"
            return balanced
```

### Explanation
Assume, string is "{()}":

Step 1: 
```
Stack : Empty
String : {()}
Index:   ^
Conc.: Index is at an opening bracket; Push it to stack
```
Step 2:
```
Stack : {
String : {()}
Index:    ^
Conc.: Index is at an opening bracket; Push it to stack
```
Step 3:
```
Stack : {(
String : {()}
Index:     ^
Conc.: Index is at a closing bracket; check top of the stack if they match
```
Step 4:
```
Stack : {
String : {()}
Index:      ^
Conc.: Index is at a closing bracket; check top of the stack if they match
```
Step 4:
```
Stack : Empty
String : {()}
Index:      ^
Conc.: Traversal completed and stack is empty; Given string is **balanced**
```


<p align="right">(<a href="#top">back to top</a>)</p>

## How to Use
```
    from balanced_brackets import is_balanced

    print(is_balanced("{}")
```
<p align="right">(<a href="#top">back to top</a>)</p>

## Tests
Run unit tests by typing in the _tests_ folder
```
python -m unittest tests.test
```
Code Coverage is **66.6%** for this solution.
<p align="right">(<a href="#top">back to top</a>)</p>

## Contact

Sinan Can Soysal - [@sinancansoysal](https://linkedin.com/in/sinancsoysal) - sinancsoysal@gmail.com

<p align="right">(<a href="#top">back to top</a>)</p>
