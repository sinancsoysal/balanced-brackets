# Balanced Brackets
# A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].
# Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {)
# occurs to the left of a closing bracket (i.e., ), ], or }) of the exact same type.
#
# we say a sequence of brackets is balanced if the following conditions are met:
# - it contains no unmatched brackets
# - subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets
#
# Solution by: Sinan Can Soysal 11/06/2022


# defining constraints
opening_brackets = ["(", "{", "["]
closing_brackets = [")", "}", "]"]
matched_brackets = dict(zip(opening_brackets, closing_brackets))


def is_balanced(s):
    stack = []
    balanced = "NO"

    for char in s:
        if char in opening_brackets:
            # char is an opening bracket
            # add opening bracket to the stack
            stack.append(char)
        elif char in closing_brackets:
            # char is a closing bracket
            # check if we encountered a closing bracket
            # when there is no opening bracket in the stack
            # continue if stack has elements
            # terminate otherwise
            if len(stack) != 0:
                # get the bracket from the top to see if it matches
                popped = stack.pop()
                # print(popped, char)
                if not matched_brackets.get(popped) == char:
                    return balanced
            else:
                return balanced
    # check if there is any brackets left in the stack
    # if yes:
    # this means there were one or more unmatched brackets
    if len(stack) == 0:
        # we finished matching brackets
        # and there are no leftover brackets
        # so the string is balanced
        balanced = "YES"
        return balanced
