# Document

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**list[Link]**](Link.md) | A list of links that originate from this document. | [optional] 
**file_name** | **str** | Gets the name of the file. | [optional] 
**source_format** | **str** | Gets the original format of the document. | 
**is_encrypted** | **bool** | Returns true if the document is encrypted and requires a password to open.  | 
**is_signed** | **bool** | Returns true if the document contains a digital signature. This property merely informs that a  digital signature is present on a document, but it does not specify whether the signature is valid or not.  | 
**document_properties** | [**DocumentProperties**](DocumentProperties.md) | Returns document properties. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


