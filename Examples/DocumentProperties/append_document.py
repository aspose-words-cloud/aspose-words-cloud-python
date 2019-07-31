import os
import asposestoragecloud
import asposewordscloud
import asposewordscloud.models.requests

class Document(object):

	def __init__(self):
		api_client = asposewordscloud.ApiClient()
		api_client.configuration.host = 'https://api.aspose.cloud'
		api_client.configuration.api_key['api_key'] = 'xxxx' # Put your appkey here
		api_client.configuration.api_key['app_sid'] = 'xxxx-xxxx-xxxx-xxxx-xxxx' # Put your appSid here

		# Same credentials for storage
		self.storage_api = asposestoragecloud.StorageApi(asposestoragecloud.ApiClient(apiKey='xxxx', appSid='xxxx-xxxx-xxxx-xxxx-xxxx')) # Same credentials for storage
		self.storage_api.api_client.configuration.base_url = 'https://api.aspose.cloud' + '/v1.1'
		self.words_api = asposewordscloud.WordsApi(api_client)

		ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../..")
		self.dataFolder = os.path.join(ABSPATH, "TestData/Common")

	def appendDocument(self):
		main_document = 'test_multi_pages.docx'
		append_document_1 = 'test_doc.docx'
		append_document_2 = 'TableDocument.doc'
		dest_name = 'FinalDocument.docx'
		
		# Upload Main Document and "Documents to append" to Cloud Storage
		for filename in [main_document, append_document_1, append_document_2]:
			filePath = os.path.join(self.dataFolder, filename)
			with open(filePath, 'rb') as f:
				fileData = f.read()
			file_upload_response = self.storage_api.put_create(filename, fileData)
		
		# importFormatMode defines which formatting will be used: appended or destination document. 
		# Can be KeepSourceFormatting or UseDestinationStyles. 
		doc_entry_1 = asposewordscloud.DocumentEntry(append_document_1,
                                             'KeepSourceFormatting')
		doc_entry_2 = asposewordscloud.DocumentEntry(append_document_2,
                                             'UseDestinationStyles')
		document_list = asposewordscloud.DocumentEntryList([doc_entry_1, doc_entry_2])
		request = asposewordscloud.models.requests.PostAppendDocumentRequest(main_document, 
																			document_list,
                                                                       dest_file_name=dest_name)
		result = self.words_api.post_append_document(request)
		print("Result {}".format(result))

document = Document()
document.appendDocument()