git reset --hard
git checkout
pip install --upgrade pip
python -m pip install --upgrade setuptools wheel
python setup.py sdist bdist_wheel
python -m pip install --upgrade twine python-dateutil
touch ~/.pypirc
printf "[distutils] \\nindex-servers= \\n\\tpypi \\n\\tpypitest\\n[pypi] \\nusername: $1 \\npassword: $2 \\n[pypitest]\\nrepository: https://test.pypi.org/legacy/ \\nusername: $1 \\npassword: $2" > ~/.pypirc
python setup.py sdist
twine upload dist/* -r pypitest
chmod 777 -R .
