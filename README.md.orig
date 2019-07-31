# asposewordscloud
This repository contains Aspose.Words Cloud SDK for Ruby source code. This SDK allows you to work with Aspose.Words Cloud REST APIs in your Ruby applications quickly and easily, with zero initial cost.

## Key Features
* Conversion between various document-related formats (20+ formats supported), including PDF<->Word conversion
* Mail merge and reports generation 
* Splitting Word documents
* Accessing Word document metadata and statistics
* Find and replace
* Watermarks and protection
* Full read & write access to Document Object Model, including sections, paragraphs, text, images, tables, headers/footers and many others

See [API Reference](https://apireference.aspose.cloud/words/) for full API specification.

## How to use the SDK?
The complete source code is available in this repository folder. You can either directly use it in your project via source code or get [PyPi](https://pypi.org/project/asposewordscloud) (recommended). For more details, please visit our [documentation website](https://docs.aspose.cloud/display/wordscloud/Available+SDKs).

### Prerequisites

To use Aspose Words for Cloud Ruby SDK you need to register an account with [Aspose Cloud](https://www.aspose.cloud/) and lookup/create App Key and SID at [Cloud Dashboard](https://dashboard.aspose.cloud/#/apps). There is free quota available. For more details, see [Aspose Cloud Pricing](https://purchase.aspose.cloud/pricing).

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install asposewordscloud
```
(you may need to run `pip` with root permission: `sudo pip install asposewordscloud`)

Then import the package:
```python
import asposewordscloud
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import asposewordscloud
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import asposewordscloud
import asposewordscloud.models.requests
api_client = asposewordscloud.ApiClient()
api_client.configuration.host = 'https://api.aspose.cloud'
api_client.configuration.api_key['api_key'] = '' # Put your appKey here
api_client.configuration.api_key['app_sid'] = '' # Put your appSid here
storage_api = asposestoragecloud.StorageApi(asposestoragecloud.ApiClient('', '')) # Same credentials for storage
storage_api.api_client.configuration.base_url = 'https://api.aspose.cloud/v1.1'
words_api = asposewordscloud.WordsApi(api_client)
filename = 'test_doc.docx'
remote_name = 'TestDeleteDocumentWatermark.docx'

with open(os.path.join(self.local_common_folder, filename), 'rb') as f:
    file = f.read()
self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
request = asposewordscloud.models.requests.DeleteDocumentWatermarkRequest(remote_name,
                                                                           os.path.join(
                                                                                 self.remote_test_folder,
                                                                                 self.test_folder))
result = words_api.delete_document_watermark(request)
self.assertTrue(result.code == 200, 'Error has occurred while delete document watermark')

```

[Test](test/) contain various examples of using the SDK.
Please put your credentials into [Configuration](asposewordscloud/configuration.py).

## Dependencies
- Python 2.7 and 3.4+
- referenced packages (see [here](setup.py) for more details)

## Comparison with Old generation SDK
New SDK has the following advantages over the [previous version](https://github.com/aspose-words/Aspose.Words-for-Cloud):
+ SDK is fully in sync with the API, all missing methods are added
+ Classes, methods and properties have comments and are IDE-friendly
+ Better security
+ Usage of Request/Response classes to represent long lists of parameters. This allows for cleaner code and easier backwards-compatibility going forward

New SDK is not backwards compatible with previous generation because of the last item. It should be straightforward to convert your code to using Request/Response objects, if you need any help on migration please ask at [Free Support Forums](https://forum.aspose.cloud/c/words).

## Contact Us
Your feedback is very important to us. Please feel free to contact us using our [Support Forums](https://forum.aspose.cloud/c/words).
