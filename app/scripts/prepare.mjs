import { execFileSync } from "node:child_process";
execFileSync(
  process.platform === "win32" ? "python" : "python3",
  ["../scripts/build_course.py"],
  { stdio: "inherit" },
);
