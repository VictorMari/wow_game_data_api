python -m pip install --upgrade pip build twine
python -m build
python -m twine upload --repository testpypi dist/*
