python -m pip install --upgrade pip build twine
rm dist/*
python -m build
python -m twine upload  dist/*
