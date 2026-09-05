# Test before accepting a change

Optional agent lab · 20 to 30 minutes

## Try

Use the broken subtotal in exercises/2.3. Ask for test inputs before an implementation, or use [] and [3, 4] as the stored fallback.

## Build

Record the failed assertion, repair the function, and rerun pytest. Inspect the diff to ensure the tests were not weakened to match the bug.

## Verify

At least one test distinguishes the old and new behavior. A test that passes before the fix does not demonstrate this defect.

Save your observations in an evidence note. If you revealed an answer, repeat with a new input before marking the practice complete. No live provider is required.
