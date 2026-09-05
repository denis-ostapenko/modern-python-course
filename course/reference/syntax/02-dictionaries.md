# Dictionaries

Status: reference outline

## Shape

    entry = {
        "category": "reading",
        "minutes": 25,
    }

A dictionary maps hashable keys to values. Each item is written as `key: value`, and commas separate items.

## Read and update

    category = entry["category"]
    entry["minutes"] = 30

Indexing with a missing key raises `KeyError`. Use `get()` only when a missing key has a meaningful alternative rather than to hide an unexpected data problem.

## First rules

- Keys are unique within one dictionary.
- Values do not need to have the same type.
- Dictionaries are mutable.
- Iteration follows insertion order in modern Python.
- Membership with `in` checks keys by default.

Primary reference: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
