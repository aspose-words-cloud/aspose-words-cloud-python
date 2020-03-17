# Aspose.Words Cloud SDK for Python
This repository contains Aspose.Words Cloud SDK for Python source code. This SDK allows you to work with Aspose.Words Cloud REST APIs in your Python applications quickly and easily, with zero initial cost.

[Aspose.Words Cloud](https://products.aspose.cloud/words/family "Aspose.Words Cloud")  
[API Reference](https://apireference.aspose.cloud/words/)  

## Key Features
* Conversion between various document-related formats (20+ formats supported), including PDF<->Word conversion
* Mail merge and reports generation 
* Splitting Word documents
* Accessing Word document metadata and statistics
* Find and replace
* Watermarks and protection
* Full read & write access to Document Object Model, including sections, paragraphs, text, images, tables, headers/footers and many others

## How to use the SDK?
The complete source code is available in this repository folder. You can either directly use it in your project via source code or get [PyPi](https://pypi.org/project/asposewordscloud) (recommended). For more details, please visit our [documentation website](https://docs.aspose.cloud/display/wordscloud/Available+SDKs).

### Prerequisites

To use Aspose Words for Cloud Python SDK you need to register an account with [Aspose Cloud](https://www.aspose.cloud/) and lookup/create App Key and SID at [Cloud Dashboard](https://dashboard.aspose.cloud/#/apps). There is free quota available. For more details, see [Aspose Cloud Pricing](https://purchase.aspose.cloud/pricing).

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install aspose-words-cloud
```
(you may need to run `pip` with root permission: `sudo pip install aspose-words-cloud`)

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
words_api = asposewordscloud.WordsApi(AppSid, AppKey, Host)
remote_name = 'TestDeleteWatermark.docx'

upload_request = asposewordscloud.models.requests.UploadFileRequest(file, remote_name)
upload_result = self.words_api.upload_file(request)
self.assertTrue(upload_result.code == 200, 'Error has occurred while uploading document')

request = asposewordscloud.models.requests.DeleteWatermarkRequest(remote_name)
result = words_api.delete_watermark(request)
self.assertTrue(result.code == 200, 'Error has occurred while deleting document watermark')

```

[Test](test/) contain various examples of using the SDK.
Please put your credentials into [Configuration](asposewordscloud/configuration.py).

## Dependencies
- Python 3.7
- referenced packages (see [here](setup.py) for more details)

## Licensing
 
All Aspose.Words Cloud SDKs, helper scripts and templates are licensed under [MIT License](https://github.com/aspose-words-cloud/aspose-words-cloud-python/blob/master/LICENSE). 

## Contact Us
Your feedback is very important to us. Please feel free to contact us using our [Support Forums](https://forum.aspose.cloud/c/words).

## Resources
 
[Website](https://www.aspose.cloud/)  
[Product Home](https://products.aspose.cloud/words/family)  
[API Reference](https://apireference.aspose.cloud/words/)  
[Documentation](https://docs.aspose.cloud/display/wordscloud/Home)  
[Blog](https://blog.aspose.cloud/category/words/) 
 
## Other languages
We generate our SDKs in different languages so you may check if yours is available in our [list](https://github.com/aspose-words-cloud).
 
If you don't find your language in the list, feel free to request it from us, or use raw REST API requests as you can find it [here](https://products.aspose.cloud/words/curl).
