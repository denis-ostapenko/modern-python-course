export type Saved = {
  version: 2;
  code: string;
  quoteError: boolean;
  completed: string[];
  notes: Record<string, string>;
  reviewed: Record<string, string>;
};
let db: IDBDatabase | null = null;
export async function connect(): Promise<boolean> {
  try {
    db = await new Promise<IDBDatabase>((resolve, reject) => {
      const r = indexedDB.open("modern-python-course-v2", 1);
      const timer = setTimeout(
        () => reject(new Error("Storage timeout")),
        1500,
      );
      r.onupgradeneeded = () => r.result.createObjectStore("state");
      r.onsuccess = () => {
        clearTimeout(timer);
        resolve(r.result);
      };
      r.onerror = () => {
        clearTimeout(timer);
        reject(r.error);
      };
    });
    return true;
  } catch {
    return false;
  }
}
export async function read(): Promise<Saved | null> {
  if (!db) return null;
  return new Promise((resolve) => {
    const r = db!.transaction("state").objectStore("state").get("course");
    r.onsuccess = () => resolve(valid(r.result) ? r.result : null);
    r.onerror = () => resolve(null);
  });
}
export function valid(value: unknown): value is Saved {
  if (!value || typeof value !== "object") return false;
  const s = value as Saved;
  return (
    s.version === 2 &&
    typeof s.code === "string" &&
    s.code.length <= 100000 &&
    typeof s.quoteError === "boolean" &&
    Array.isArray(s.completed) &&
    s.completed.every((x) => typeof x === "string") &&
    [s.notes, s.reviewed].every(
      (x) =>
        x &&
        typeof x === "object" &&
        !Array.isArray(x) &&
        Object.values(x).every((y) => typeof y === "string"),
    )
  );
}
export async function save(state: Saved): Promise<boolean> {
  if (!db) return false;
  return new Promise((resolve) => {
    try {
      const t = db!.transaction("state", "readwrite");
      t.objectStore("state").put(structuredClone(state), "course");
      t.oncomplete = () => resolve(true);
      t.onerror = t.onabort = () => resolve(false);
    } catch {
      resolve(false);
    }
  });
}
