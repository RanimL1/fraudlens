import importlib

import pytest


@pytest.mark.parametrize(
    "module",
    ["fraudlens", "pandas", "numpy", "pyarrow", "sklearn", "lightgbm", "mlflow", "yaml"],
)
def test_import(module):
    assert importlib.import_module(module) is not None