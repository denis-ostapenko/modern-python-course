# Your first Python run

0.1 · 10 to 15 minutes · Browser

Run three lines, change their result, and repair one small error.

## Try

Read the three lines in the editor. Choose an expected output, then select Run code. A prediction is an experiment, not a score. If Python is still loading, you can read and edit immediately.



## Understand

A program is a set of instructions. The editor holds the source, the instructions you can change. Python executes those instructions from top to bottom. The Output panel shows what this particular run printed.

In the first line, `category` is a name referring to the text `"reading"`. Quotes mark the boundaries of that text. In the second, `minutes` refers to the whole number `25`. The third calls `print`: the parentheses contain what to display. The `f` before the quoted text makes it a formatted string. A name inside braces contributes its current value.

| Source part | Meaning in this run |
| --- | --- |
| `category = "reading"` | Bind a name to text |
| `minutes = 25` | Bind a name to a number |
| `{category}` | Insert the current category value |
| `print(...)` | Send the constructed text to output |

Each Run starts a fresh set of Python names. Removing the assignments will not leave their old values available.

```python
category = "reading"
minutes = 25
print(f"{category}: {minutes} minutes")
```

Expected output:

```text
reading: 25 minutes
```

## Build

Change `reading` to `walking` and `25` to `40`, leaving quotes and punctuation in place. Predict, then run.

Now deliberately remove the closing quote after walking. Run again. Python reports a `SyntaxError`: it cannot find the end of the text. Read the marked source line, restore the quote, and run once more. A failed run does not damage your computer or lose your draft.

Describe the quote repair in the explanation box. Select Check this change. It checks the current source revision, target output, deliberate quote-error activity, and the presence of your explanation. It does not automatically grade the meaning of your explanation.



## Verify and explain

Final output: `walking: 40 minutes`. Explain which text was source and which was output. Point to the quote you restored. After another edit, the old output becomes stale until you run again.

## Bring it back later

In the next lesson, run the same three lines from a file. Which application displays the output there?

## Save and continue

Download main.py to keep the source. Export course progress to keep your draft and notes, and import that JSON later to restore them. Browser storage is best effort; a visible message tells you if saving is unavailable. Python needs a first network load. If it cannot load, download the learner workspace and follow [Your real workspace](../00-start-here/02-real-workspace.md).
