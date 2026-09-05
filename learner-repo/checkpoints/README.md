# Recovery checkpoints

Each lesson has a start and complete folder. A complete folder is a worked reference, not proof that you independently solved the exercise.

Copy into a new work folder:

```text
uv run python tools/checkpoint.py lesson-1.4-start iteration-attempt
uv run python work/iteration-attempt/main.py
```

The copy command refuses to overwrite an existing folder. To retry, choose another folder name. For input examples, type the requested values. The files and JSON lesson writes only beside its copied script. Later CLI lessons accept an explicit --data path.

Unit 2.3 isolates reporting for focused tests. Unit 2.4 reunites reporting and storage as separate modules. This is a deliberate practice branch of Daybook, not lost learner work.
