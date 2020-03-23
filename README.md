Python Cloud SDK wraps Aspose.Words Cloud API so you could seamlessly integrate Microsoft Word® file generation, manipulation, conversion & inspection features into your own python applications.

[Aspose.Words Cloud SDK for Python](https://products.aspose.cloud/slides/python) allows to work with Word document headers, footers, page numbering, tables, sections, document comments, drawing objects, FormFields, fonts, hyperlinks, ranges, paragraphs, math objects, watermarks, revisions and document protection. It also assists in appending documents, splitting documents as well as converting document to other supported file formats. Please feel free to explore the [Developer's Guide](https://docs.aspose.cloud/display/wordscloud/Developer+Guide) for all possible usage scenarios. 

## Document Processing Features

- Programmatically create new documents of various file formats.
- Availability of Mail Merge and report generation features.
- Split or merge documents on demand.
- Manage watermarks and protection.
- Full read & write access to Document Object Model.
- Fetch web pages via URL and save in Microsoft Word file formats.
- Get document information in JSON or XML representation.
- [Fetch statistical data](https://docs.aspose.cloud/display/wordscloud/Get+Document+Statistics) of a document.
- [Remove all macros](https://docs.aspose.cloud/display/wordscloud/Remove+all+Macros+from+Document) contained in a specific document.
- [Convert a document to desired file format](https://docs.aspose.cloud/display/wordscloud/Convert+Document+to+Destination+Format+with+Detailed+Settings+and+Save+Result+to+Storage) along with detailed settings.
- Convert an encrypted PDF document into Word document format.

## Enhancements in Version 20.3.1
- Added RtfSaveOptionsData.SaveImagesAsWmf property
- WordsApi class now has credentials parameters
- All methods which are used files, now operate with bytes array

## Enhancements in Version 20.1.0

- Moved property `ColorMode` from `SaveOptionsData` to `FixedPageSaveOptionsData`.
- Replaced `MemoryStream` and `byte[]` with `SixLabors.ImageSharp.IImage` in image processing.
- Included support of `ICC` profiles and implement `ICCBased` color space.

For the detailed notes, please visit [Aspose.Words Cloud 20.1 Release Notes](https://docs.aspose.cloud/display/wordscloud/Aspose.Words+Cloud+20.1+Release+Notes).

## Read & Write Document Formats

**Microsoft Word:** DOC, DOCX, RTF, DOT, DOTX, DOTM, FlatOPC (XML)
**OpenOffice:** ODT, OTT
**WordprocessingML:** XML
**Web:** HTML, MHTML, HtmlFixed
**Text:** TXT
**Fixed Layout:** PDF

## Save Document As

**Fixed Layout:** PDF/A, XPS, OpenXPS, PS
**Images:** JPEG, PNG, BMP, SVG, TIFF, EMF
**Others:** PCL

## Platform Independence

Aspose.Words Cloud’s platform independent document manipulation API is a true REST API that can be used from any platform. You can use it with any language or platform that supports REST, be it the web, desktop, mobile, or the cloud. The API integrates with other cloud services to provide you the flexibility you require for processing documents. It is suitable for the most types of businesses, documents, or content.

## Getting Started with Aspose.Words Cloud SDK for Python

Firstly, create an account at [Aspose for Cloud](https://dashboard.aspose.cloud/#/apps) to get your application information and free quota to use the API. Now execute `pip install aspose-words-cloud` from the command line to fetch the SDK. Then import the package via `import asposewordscloud`. 

### Install via Setuptools

Execute `python setup.py install --user` and import the package as `import asposewordscloud`.

The complete source code is available at [GitHub Repository](https://github.com/aspose-words-cloud/aspose-words-cloud-python).

## Delete Watermarks from Word Document via Python

```python
import asposewordscloud
import asposewordscloud.models.requests

words_api = asposewordscloud.WordsApi('appSid', 'appKey', 'https://api.aspose.cloud')
filename = 'test_doc.docx'
remote_name = 'TestDeleteDocumentWatermark.docx'
remote_folder = 'FolderWhereFileLocates'

with open(os.path.join(self.local_common_folder, filename), 'rb') as f:
    file = f.read()

upload_request = asposewordscloud.models.requests.UploadFileRequest(file, os.path.join(remote_folder, remote_name))
request = asposewordscloud.models.requests.DeleteDocumentWatermarkRequest(remote_name, remote_folder)
result = words_api.delete_document_watermark(request)
self.assertTrue(result.code == 200, 'Error has occurred while delete document watermark')
```

[Product Page](https://products.aspose.cloud/words/python) | [Documentation](https://docs.aspose.cloud/display/wordscloud/Home) | [API Reference](https://apireference.aspose.cloud/words/) | [Code Samples](https://github.com/aspose-words-cloud/aspose-words-cloud-python) | [Blog](https://blog.aspose.cloud/category/words/) | [Free Support](https://forum.aspose.cloud/c/words) | [Free Trial](https://dashboard.aspose.cloud/#/apps)