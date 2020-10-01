python -m pip install --upgrade setuptools wheel
pip install urllib3
pip install requests-toolbelt
pip install --index-url https://test.pypi.org/simple/ aspose-words-cloud
python -m pip install -r requirements.txt && python -m pip install -r test-requirements.txt
echo "{\"AppSid\":\"$1\",\"AppKey\":\"$2\",\"BaseUrl\":\"$3\" }" > Settings/servercreds.json
python -m unittest discover -v -s .
