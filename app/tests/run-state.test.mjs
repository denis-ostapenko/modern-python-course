import test from "node:test";
import assert from "node:assert/strict";
import { canCheck, evaluateWarmup } from "../src/run-state.ts";
import { valid } from "../src/storage.ts";
const source =
  'category = "walking"\nminutes = 40\nprint(f"{category}: {minutes} minutes")';
const result = { source, stdout: "walking: 40 minutes", error: null };
test("changed source rejects old successful output", () => {
  assert.equal(canCheck('print("wrong")', result), false);
  assert.match(
    evaluateWarmup(
      'print("wrong")',
      result,
      true,
      "I restored the closing quote.",
    ),
    /Run this version/,
  );
});
test("an edit during a run cannot receive the old evidence", () => {
  assert.equal(canCheck(source + '\nprint("extra")', result), false);
});
test("completion requires current output, quote activity and explanation", () => {
  assert.equal(
    evaluateWarmup(source, result, true, "I restored the closing quote."),
    null,
  );
  assert.match(
    evaluateWarmup(source, result, false, "I restored the closing quote."),
    /missing-quote/,
  );
  assert.match(evaluateWarmup(source, result, true, ""), /Explain/);
});
test("extra whitespace and output do not satisfy exact target", () => {
  for (const stdout of [" walking: 40 minutes", "walking: 40 minutes\nextra"])
    assert.match(
      evaluateWarmup(
        source,
        { ...result, stdout },
        true,
        "I restored the closing quote.",
      ),
      /Expected/,
    );
});
test("failed and absent results are not checkable", () => {
  assert.equal(canCheck(source, null), false);
  assert.equal(canCheck(source, { ...result, error: "SyntaxError" }), false);
});
test("import validates its shape", () => {
  assert.equal(valid({}), false);
  assert.equal(
    valid({
      version: 2,
      code: source,
      quoteError: false,
      completed: [],
      notes: {},
      reviewed: {},
    }),
    true,
  );
  assert.equal(
    valid({
      version: 2,
      code: source,
      quoteError: false,
      completed: [4],
      notes: {},
      reviewed: {},
    }),
    false,
  );
});
