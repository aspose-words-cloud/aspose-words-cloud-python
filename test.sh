!#bin/bash
pip install -r requirements.txt && pip install --index-url https://testpypi.python.org/pypi asposestoragecloud==1.0.8 && python -m unittest discover -v -s .