# Style

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**font** | [**Font**](Font.md) |  | [optional] 
**built_in** | **bool** | Gets or sets a value indicating whether true if this style is one of the built-in styles in MS Word. | [optional] 
**next_paragraph_style_name** | **str** | Gets or sets /sets the name of the style to be applied automatically to a new paragraph inserted after a paragraph formatted with the specified style. | [optional] 
**base_style_name** | **str** | Gets or sets /sets the name of the style this style is based on. | [optional] 
**is_quick_style** | **bool** | Gets or sets a value indicating whether specifies whether this style is shown in the Quick Style gallery inside MS Word UI. | [optional] 
**linked_style_name** | **str** | Gets or sets the name of the Style linked to this one. Returns Empty string if no styles are linked. | [optional] 
**type** | **str** | Gets or sets the style type (paragraph or character). | [optional] 
**is_heading** | **bool** | Gets or sets a value indicating whether true when the style is one of the built-in Heading styles. | [optional] 
**aliases** | **list[str]** | Gets or sets all aliases of this style. If style has no aliases then empty array of string is returned. | [optional] 
**style_identifier** | **str** | Gets or sets the locale independent style identifier for a built-in style. | [optional] 
**name** | **str** | Gets or sets the name of the style. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

