# Program Shape

Status: initial syntax reference

## Simple statement

    activity = "reading"

A name appears on the left of `=` and an expression appears on the right.

## Function call

    print(activity)

The function expression comes first. Parentheses contain arguments separated by commas.

## Indented block

    if activity:
        print(activity)

The colon ends the block header. The indented statement belongs to that block.

## Comment

    # Show the selected activity.
    print(activity)

Comments describe useful context for humans. They do not replace clear names or lesson explanation.

## First rules

- Names are case-sensitive.
- Statements normally end at a newline.
- Consistent indentation defines block structure.
- Quotes delimit text.
- Parentheses group expressions and function-call arguments.
- A syntax error prevents the program from being executed normally.

Primary reference: https://docs.python.org/3/reference/lexical_analysis.html
