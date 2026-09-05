# Notebooks and hidden state

Optional · After functions and tests · 30 to 45 minutes

A notebook combines executable cells and explanation. Its kernel holds state between cell runs. That can support exploration, but execution order may differ from the page order.

## Try

In a Jupyter environment you already have, create one cell assigning total = 10 and a second printing total + 5. Run both. Delete the assignment cell and run the print cell again: the old value may still exist. Restart the kernel and Run All; the missing assignment now becomes visible.

For a local optional notebook environment, create a separate folder and use `uv init`, then `uv add --dev jupyterlab`. Launch with `uv run jupyter lab`. This is an optional dependency, not required by the core learner repository.

## Build

Use three cells: data definition, summary function, and explanation with its displayed result. Change the data and rerun in order. Move the stable summary function into a .py module and test it with pytest outside the notebook.

## Verify

Restart and Run All from a clean kernel. Every result must be reproducible in page order. Record any difference caused by out-of-order execution. Keep credentials and private outputs out of a shared notebook.

If installation is unavailable, reproduce the same state experiment with the Python interactive prompt, then compare it with two fresh script runs. The conceptual objective is understanding persistent execution state, not installing a particular notebook product.

See [JupyterLab documentation](https://jupyterlab.readthedocs.io/en/stable/) for the current interface.
