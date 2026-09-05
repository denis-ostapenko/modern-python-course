export type Evidence = { source: string; stdout: string; error: string | null };
export function canCheck(source: string, result: Evidence | null): boolean {
  return result !== null && result.source === source && result.error === null;
}
export function evaluateWarmup(
  source: string,
  result: Evidence | null,
  repaired: boolean,
  explanation: string,
): string | null {
  if (!canCheck(source, result))
    return "Run this version of your code before checking it.";
  if (result!.stdout.replace(/\n$/, "") !== "walking: 40 minutes")
    return `Expected walking: 40 minutes. Observed: ${result!.stdout || "no output"}`;
  if (!repaired)
    return "Try the missing-quote activity, run the error, then repair and run again.";
  if (explanation.trim().length < 15)
    return "Explain which quote was missing and why restoring it lets Python read the text.";
  return null;
}
