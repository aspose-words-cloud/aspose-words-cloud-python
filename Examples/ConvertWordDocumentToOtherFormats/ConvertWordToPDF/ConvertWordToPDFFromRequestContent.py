import os
import asposestoragecloud
import asposewordscloud
import asposewordscloud.models.requests

class Document(object):

	def __init__(self):
		api_client = asposewordscloud.ApiClient()
		api_client.configuration.host = 'https://api.aspose.cloud'
		api_client.configuration.api_key['api_key'] = 'xxxx' # Put your App Key here
		api_client.configuration.api_key['app_sid'] = 'xxxx-xxxx-xxxx-xxxx-xxxx' # Put your App SID here

		# Same credentials for storage
		self.storage_api = asposestoragecloud.StorageApi(asposestoragecloud.ApiClient(apiKey='xxxx', appSid='xxxx-xxxx-xxxx-xxxx-xxxx'))
		self.storage_api.api_client.configuration.base_url = 'https://api.aspose.cloud' + '/v1.1'
		self.words_api = asposewordscloud.WordsApi(api_client)

		ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../..")
		self.dataFolder = os.path.join(ABSPATH, "Data")
		self.outputFolder = os.path.join(ABSPATH, "Ouput")

	def convertWordToPDF(self):
		filename = 'test_multi_pages.docx'
		filePath = os.path.join(self.dataFolder, filename)
		
		# Send the Word document in the API request
		request = asposewordscloud.models.requests.PutConvertDocumentRequest(document=filePath, format='pdf')
		# The API returns PDF document and save in the local temporary folder
		pdfFilePath = self.words_api.put_convert_document(request)

		# Move the PDF document from the temporary folder to the Output folder
		os.rename(pdfFilePath, os.path.join(self.outputFolder, os.path.basename(pdfFilePath)))
		print("Successfully converted Word Document to PDF and saved the PDF documment in the Output Folder")

document = Document()
document.convertWordToPDF()
