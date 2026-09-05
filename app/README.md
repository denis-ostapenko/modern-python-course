# Course application

Static TypeScript and Vite application for Modern Python by Denis Ostapenko.

Run npm ci, npm run build, then npm run preview. Prebuild generates the content catalog, learner and reading ZIPs, and pinned local Pyodide assets.

The first lesson uses CodeMirror and a module Worker. Every run uses a fresh namespace; evidence belongs to a source revision. Storage failure leaves an editable in-memory session with export. Other lessons render sanitized Markdown and retain explicitly self-recorded evidence. Browser progress is not a remote certification system.

npm test covers source/result association, completion criteria and import validation. Browser journeys verify the actual Worker, layout, navigation, saving and recovery. No live model integration is included.
