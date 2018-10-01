# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="words_api.py">
#   Copyright (c) 2018 Aspose.Words for Cloud
# </copyright>
# <summary>
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# </summary>
# -----------------------------------------------------------------------------------


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six
from asposewordscloud.rest import ApiException
from asposewordscloud.api_client import ApiClient


class WordsApi(object):
    """
    Aspose.Words for Cloud API

    :param api_client: an api client to perfom http requests
    """
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.__request_token()

    def accept_all_revisions(self, request, **kwargs):  # noqa: E501
        """Accept all revisions in document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :return: RevisionsModificationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.accept_all_revisions_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.accept_all_revisions_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.accept_all_revisions_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.accept_all_revisions_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def accept_all_revisions_with_http_info(self, request, **kwargs):  # noqa: E501
        """Accept all revisions in document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request AcceptAllRevisionsRequest object with parameters
        :return: RevisionsModificationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method accept_all_revisions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `accept_all_revisions`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/revisions/acceptAll'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RevisionsModificationResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def classify(self, request, **kwargs):  # noqa: E501
        """Classify raw text.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param text str : Text to classify. (required)
        :param best_classes_count str : Count of the best classes to return.
        :return: ClassificationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.classify_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.classify_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.classify_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.classify_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def classify_with_http_info(self, request, **kwargs):  # noqa: E501
        """Classify raw text.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request ClassifyRequest object with parameters
        :return: ClassificationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method classify" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'text' is set
        if request.text is None:
            raise ValueError("Missing the required parameter `text` when calling `classify`")  # noqa: E501

        collection_formats = {}
        path = '/words/classify'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('BestClassesCount') in path:
            path = path.replace('{' + self.__downcase_first_letter('BestClassesCount' + '}'), request.best_classes_count if request.best_classes_count is not None else '')
        else:
            if request.best_classes_count is not None:
                query_params.append((self.__downcase_first_letter('BestClassesCount'), request.best_classes_count))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.text is not None:
            body_params = request.text
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ClassificationResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def classify_document(self, request, **kwargs):  # noqa: E501
        """Classify document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param document_name str : The document name. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param best_classes_count str : Count of the best classes to return.
        :param taxonomy str : Taxonomy to use for classification return.
        :return: ClassificationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.classify_document_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.classify_document_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.classify_document_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.classify_document_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def classify_document_with_http_info(self, request, **kwargs):  # noqa: E501
        """Classify document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request ClassifyDocumentRequest object with parameters
        :return: ClassificationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method classify_document" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'document_name' is set
        if request.document_name is None:
            raise ValueError("Missing the required parameter `document_name` when calling `classify_document`")  # noqa: E501

        collection_formats = {}
        path = '/words/{documentName}/classify'
        path_params = {}
        if request.document_name is not None:
            path_params[self.__downcase_first_letter('DocumentName')] = request.document_name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('BestClassesCount') in path:
            path = path.replace('{' + self.__downcase_first_letter('BestClassesCount' + '}'), request.best_classes_count if request.best_classes_count is not None else '')
        else:
            if request.best_classes_count is not None:
                query_params.append((self.__downcase_first_letter('BestClassesCount'), request.best_classes_count))  # noqa: E501
        if self.__downcase_first_letter('Taxonomy') in path:
            path = path.replace('{' + self.__downcase_first_letter('Taxonomy' + '}'), request.taxonomy if request.taxonomy is not None else '')
        else:
            if request.taxonomy is not None:
                query_params.append((self.__downcase_first_letter('Taxonomy'), request.taxonomy))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ClassificationResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_or_update_document_property(self, request, **kwargs):  # noqa: E501
        """Add new or update existing document property.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param property_name str : The property name. (required)
        :param _property DocumentProperty : The property with new value. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: DocumentPropertyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.create_or_update_document_property_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.create_or_update_document_property_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.create_or_update_document_property_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.create_or_update_document_property_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def create_or_update_document_property_with_http_info(self, request, **kwargs):  # noqa: E501
        """Add new or update existing document property.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request CreateOrUpdateDocumentPropertyRequest object with parameters
        :return: DocumentPropertyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_or_update_document_property" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `create_or_update_document_property`")  # noqa: E501
        # verify the required parameter 'property_name' is set
        if request.property_name is None:
            raise ValueError("Missing the required parameter `property_name` when calling `create_or_update_document_property`")  # noqa: E501
        # verify the required parameter '_property' is set
        if request._property is None:
            raise ValueError("Missing the required parameter `_property` when calling `create_or_update_document_property`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/documentProperties/{propertyName}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.property_name is not None:
            path_params[self.__downcase_first_letter('PropertyName')] = request.property_name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request._property is not None:
            body_params = request._property
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DocumentPropertyResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_border(self, request, **kwargs):  # noqa: E501
        """Resets border properties to default values.               # noqa: E501

        'nodePath' should refer to node with cell or row  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param node_path str : Path to node with border(node should be cell or row). (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: BorderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_border_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_border_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.delete_border_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_border_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_border_with_http_info(self, request, **kwargs):  # noqa: E501
        """Resets border properties to default values.               # noqa: E501

        'nodePath' should refer to node with cell or row  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request DeleteBorderRequest object with parameters
        :return: BorderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_border" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `delete_border`")  # noqa: E501
        # verify the required parameter 'node_path' is set
        if request.node_path is None:
            raise ValueError("Missing the required parameter `node_path` when calling `delete_border`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `delete_border`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/borders/{index}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.node_path is not None:
            path_params[self.__downcase_first_letter('NodePath')] = request.node_path  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BorderResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_borders(self, request, **kwargs):  # noqa: E501
        """Resets borders properties to default values.               # noqa: E501

        'nodePath' should refer to node with cell or row  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param node_path str : Path to node with borders(node should be cell or row). (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: BordersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_borders_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_borders_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.delete_borders_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_borders_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_borders_with_http_info(self, request, **kwargs):  # noqa: E501
        """Resets borders properties to default values.               # noqa: E501

        'nodePath' should refer to node with cell or row  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request DeleteBordersRequest object with parameters
        :return: BordersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_borders" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `delete_borders`")  # noqa: E501
        # verify the required parameter 'node_path' is set
        if request.node_path is None:
            raise ValueError("Missing the required parameter `node_path` when calling `delete_borders`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/borders'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.node_path is not None:
            path_params[self.__downcase_first_letter('NodePath')] = request.node_path  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BordersResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_comment(self, request, **kwargs):  # noqa: E501
        """Remove comment from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The file name. (required)
        :param comment_index int : Comment index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_comment_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_comment_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.delete_comment_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_comment_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_comment_with_http_info(self, request, **kwargs):  # noqa: E501
        """Remove comment from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request DeleteCommentRequest object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_comment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `delete_comment`")  # noqa: E501
        # verify the required parameter 'comment_index' is set
        if request.comment_index is None:
            raise ValueError("Missing the required parameter `comment_index` when calling `delete_comment`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/comments/{commentIndex}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.comment_index is not None:
            path_params[self.__downcase_first_letter('CommentIndex')] = request.comment_index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_document_macros(self, request, **kwargs):  # noqa: E501
        """Remove macros from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The file name. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_document_macros_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_document_macros_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.delete_document_macros_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_document_macros_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_document_macros_with_http_info(self, request, **kwargs):  # noqa: E501
        """Remove macros from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request DeleteDocumentMacrosRequest object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_document_macros" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `delete_document_macros`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/macros'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_document_property(self, request, **kwargs):  # noqa: E501
        """Delete document property.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param property_name str : The property name. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_document_property_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_document_property_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.delete_document_property_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_document_property_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_document_property_with_http_info(self, request, **kwargs):  # noqa: E501
        """Delete document property.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request DeleteDocumentPropertyRequest object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_document_property" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `delete_document_property`")  # noqa: E501
        # verify the required parameter 'property_name' is set
        if request.property_name is None:
            raise ValueError("Missing the required parameter `property_name` when calling `delete_document_property`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/documentProperties/{propertyName}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.property_name is not None:
            path_params[self.__downcase_first_letter('PropertyName')] = request.property_name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_document_watermark(self, request, **kwargs):  # noqa: E501
        """Delete watermark (for deleting last watermark from the document).  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_document_watermark_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_document_watermark_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.delete_document_watermark_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_document_watermark_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_document_watermark_with_http_info(self, request, **kwargs):  # noqa: E501
        """Delete watermark (for deleting last watermark from the document).  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request DeleteDocumentWatermarkRequest object with parameters
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_document_watermark" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `delete_document_watermark`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/watermark'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DocumentResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_drawing_object(self, request, **kwargs):  # noqa: E501
        """Removes drawing object from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The file name. (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :param node_path str : Path to node, which contains collection of drawing objects.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_drawing_object_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_drawing_object_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.delete_drawing_object_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_drawing_object_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_drawing_object_with_http_info(self, request, **kwargs):  # noqa: E501
        """Removes drawing object from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request DeleteDrawingObjectRequest object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_drawing_object" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `delete_drawing_object`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `delete_drawing_object`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/drawingObjects/{index}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if self.__downcase_first_letter('NodePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('NodePath' + '}'), request.node_path if request.node_path is not None else '')
        else:
            if request.node_path is not None:
                query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_field(self, request, **kwargs):  # noqa: E501
        """Delete field from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The file name. (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :param node_path str : Path to node, which contains collection of fields.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_field_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_field_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.delete_field_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_field_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_field_with_http_info(self, request, **kwargs):  # noqa: E501
        """Delete field from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request DeleteFieldRequest object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_field" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `delete_field`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `delete_field`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/fields/{index}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if self.__downcase_first_letter('NodePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('NodePath' + '}'), request.node_path if request.node_path is not None else '')
        else:
            if request.node_path is not None:
                query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_fields(self, request, **kwargs):  # noqa: E501
        """Remove fields from section paragraph.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The file name. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :param node_path str : Path to node, which contains collection of fields.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_fields_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_fields_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.delete_fields_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_fields_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_fields_with_http_info(self, request, **kwargs):  # noqa: E501
        """Remove fields from section paragraph.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request DeleteFieldsRequest object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_fields" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `delete_fields`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/fields'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if self.__downcase_first_letter('NodePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('NodePath' + '}'), request.node_path if request.node_path is not None else '')
        else:
            if request.node_path is not None:
                query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_footnote(self, request, **kwargs):  # noqa: E501
        """Removes footnote from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The file name. (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :param node_path str : Path to node, which contains collection of footnotes.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_footnote_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_footnote_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.delete_footnote_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_footnote_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_footnote_with_http_info(self, request, **kwargs):  # noqa: E501
        """Removes footnote from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request DeleteFootnoteRequest object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_footnote" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `delete_footnote`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `delete_footnote`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/footnotes/{index}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if self.__downcase_first_letter('NodePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('NodePath' + '}'), request.node_path if request.node_path is not None else '')
        else:
            if request.node_path is not None:
                query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_form_field(self, request, **kwargs):  # noqa: E501
        """Removes form field from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :param node_path str : Path to node that contains collection of formfields.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_form_field_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_form_field_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.delete_form_field_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_form_field_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_form_field_with_http_info(self, request, **kwargs):  # noqa: E501
        """Removes form field from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request DeleteFormFieldRequest object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_form_field" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `delete_form_field`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `delete_form_field`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/formfields/{index}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if self.__downcase_first_letter('NodePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('NodePath' + '}'), request.node_path if request.node_path is not None else '')
        else:
            if request.node_path is not None:
                query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_header_footer(self, request, **kwargs):  # noqa: E501
        """Delete header/footer from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :param section_path str : Path to parent section.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_header_footer_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_header_footer_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.delete_header_footer_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_header_footer_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_header_footer_with_http_info(self, request, **kwargs):  # noqa: E501
        """Delete header/footer from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request DeleteHeaderFooterRequest object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_header_footer" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `delete_header_footer`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `delete_header_footer`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{sectionPath}/headersfooters/{index}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if self.__downcase_first_letter('SectionPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('SectionPath' + '}'), request.section_path if request.section_path is not None else '')
        else:
            if request.section_path is not None:
                query_params.append((self.__downcase_first_letter('SectionPath'), request.section_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_headers_footers(self, request, **kwargs):  # noqa: E501
        """Delete document headers and footers.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :param section_path str : Path to parent section.
        :param headers_footers_types str : List of types of headers and footers.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_headers_footers_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_headers_footers_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.delete_headers_footers_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_headers_footers_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_headers_footers_with_http_info(self, request, **kwargs):  # noqa: E501
        """Delete document headers and footers.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request DeleteHeadersFootersRequest object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_headers_footers" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `delete_headers_footers`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{sectionPath}/headersfooters'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if self.__downcase_first_letter('SectionPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('SectionPath' + '}'), request.section_path if request.section_path is not None else '')
        else:
            if request.section_path is not None:
                query_params.append((self.__downcase_first_letter('SectionPath'), request.section_path))  # noqa: E501
        if self.__downcase_first_letter('HeadersFootersTypes') in path:
            path = path.replace('{' + self.__downcase_first_letter('HeadersFootersTypes' + '}'), request.headers_footers_types if request.headers_footers_types is not None else '')
        else:
            if request.headers_footers_types is not None:
                query_params.append((self.__downcase_first_letter('HeadersFootersTypes'), request.headers_footers_types))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_office_math_object(self, request, **kwargs):  # noqa: E501
        """Removes OfficeMath object from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The file name. (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :param node_path str : Path to node, which contains collection of OfficeMath objects.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_office_math_object_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_office_math_object_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.delete_office_math_object_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_office_math_object_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_office_math_object_with_http_info(self, request, **kwargs):  # noqa: E501
        """Removes OfficeMath object from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request DeleteOfficeMathObjectRequest object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_office_math_object" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `delete_office_math_object`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `delete_office_math_object`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/OfficeMathObjects/{index}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if self.__downcase_first_letter('NodePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('NodePath' + '}'), request.node_path if request.node_path is not None else '')
        else:
            if request.node_path is not None:
                query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_paragraph(self, request, **kwargs):  # noqa: E501
        """Remove paragraph from section.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The file name. (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :param node_path str : Path to node which contains paragraphs.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_paragraph_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_paragraph_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.delete_paragraph_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_paragraph_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_paragraph_with_http_info(self, request, **kwargs):  # noqa: E501
        """Remove paragraph from section.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request DeleteParagraphRequest object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_paragraph" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `delete_paragraph`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `delete_paragraph`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/paragraphs/{index}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if self.__downcase_first_letter('NodePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('NodePath' + '}'), request.node_path if request.node_path is not None else '')
        else:
            if request.node_path is not None:
                query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_run(self, request, **kwargs):  # noqa: E501
        """Removes run from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The file name. (required)
        :param paragraph_path str : Path to parent paragraph. (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_run_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_run_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.delete_run_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_run_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_run_with_http_info(self, request, **kwargs):  # noqa: E501
        """Removes run from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request DeleteRunRequest object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_run" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `delete_run`")  # noqa: E501
        # verify the required parameter 'paragraph_path' is set
        if request.paragraph_path is None:
            raise ValueError("Missing the required parameter `paragraph_path` when calling `delete_run`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `delete_run`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{paragraphPath}/runs/{index}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.paragraph_path is not None:
            path_params[self.__downcase_first_letter('ParagraphPath')] = request.paragraph_path  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_table(self, request, **kwargs):  # noqa: E501
        """Delete a table.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :param node_path str : Path to node, which contains tables.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_table_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_table_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.delete_table_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_table_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_table_with_http_info(self, request, **kwargs):  # noqa: E501
        """Delete a table.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request DeleteTableRequest object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_table" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `delete_table`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `delete_table`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/tables/{index}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if self.__downcase_first_letter('NodePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('NodePath' + '}'), request.node_path if request.node_path is not None else '')
        else:
            if request.node_path is not None:
                query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_table_cell(self, request, **kwargs):  # noqa: E501
        """Delete a table cell.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param table_row_path str : Path to table row. (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_table_cell_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_table_cell_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.delete_table_cell_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_table_cell_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_table_cell_with_http_info(self, request, **kwargs):  # noqa: E501
        """Delete a table cell.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request DeleteTableCellRequest object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_table_cell" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `delete_table_cell`")  # noqa: E501
        # verify the required parameter 'table_row_path' is set
        if request.table_row_path is None:
            raise ValueError("Missing the required parameter `table_row_path` when calling `delete_table_cell`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `delete_table_cell`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{tableRowPath}/cells/{index}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.table_row_path is not None:
            path_params[self.__downcase_first_letter('TableRowPath')] = request.table_row_path  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_table_row(self, request, **kwargs):  # noqa: E501
        """Delete a table row.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param table_path str : Path to table. (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_table_row_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_table_row_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.delete_table_row_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_table_row_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_table_row_with_http_info(self, request, **kwargs):  # noqa: E501
        """Delete a table row.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request DeleteTableRowRequest object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_table_row" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `delete_table_row`")  # noqa: E501
        # verify the required parameter 'table_path' is set
        if request.table_path is None:
            raise ValueError("Missing the required parameter `table_path` when calling `delete_table_row`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `delete_table_row`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{tablePath}/rows/{index}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.table_path is not None:
            path_params[self.__downcase_first_letter('TablePath')] = request.table_path  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_unprotect_document(self, request, **kwargs):  # noqa: E501
        """Unprotect document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param protection_request ProtectionRequest : with protection settings.             (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :return: ProtectionDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_unprotect_document_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_unprotect_document_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.delete_unprotect_document_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_unprotect_document_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_unprotect_document_with_http_info(self, request, **kwargs):  # noqa: E501
        """Unprotect document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request DeleteUnprotectDocumentRequest object with parameters
        :return: ProtectionDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_unprotect_document" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `delete_unprotect_document`")  # noqa: E501
        # verify the required parameter 'protection_request' is set
        if request.protection_request is None:
            raise ValueError("Missing the required parameter `protection_request` when calling `delete_unprotect_document`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/protection'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.protection_request is not None:
            body_params = request.protection_request
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProtectionDataResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_available_fonts(self, request, **kwargs):  # noqa: E501
        """Gets the list of fonts, available for document processing  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param fonts_location str : Folder in filestorage with custom fonts.
        :return: AvailableFontsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_available_fonts_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_available_fonts_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_available_fonts_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_available_fonts_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_available_fonts_with_http_info(self, request, **kwargs):  # noqa: E501
        """Gets the list of fonts, available for document processing  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetAvailableFontsRequest object with parameters
        :return: AvailableFontsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_available_fonts" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}
        path = '/words/fonts/available'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('FontsLocation') in path:
            path = path.replace('{' + self.__downcase_first_letter('FontsLocation' + '}'), request.fonts_location if request.fonts_location is not None else '')
        else:
            if request.fonts_location is not None:
                query_params.append((self.__downcase_first_letter('FontsLocation'), request.fonts_location))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AvailableFontsResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_border(self, request, **kwargs):  # noqa: E501
        """Return a border.  # noqa: E501

        'nodePath' should refer to node with cell or row  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param node_path str : Path to node with border(node should be cell or row). (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :return: BorderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_border_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_border_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_border_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_border_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_border_with_http_info(self, request, **kwargs):  # noqa: E501
        """Return a border.  # noqa: E501

        'nodePath' should refer to node with cell or row  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetBorderRequest object with parameters
        :return: BorderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_border" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_border`")  # noqa: E501
        # verify the required parameter 'node_path' is set
        if request.node_path is None:
            raise ValueError("Missing the required parameter `node_path` when calling `get_border`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `get_border`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/borders/{index}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.node_path is not None:
            path_params[self.__downcase_first_letter('NodePath')] = request.node_path  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BorderResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_borders(self, request, **kwargs):  # noqa: E501
        """Return a collection of borders.  # noqa: E501

        'nodePath' should refer to node with cell or row  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param node_path str : Path to node with borders(node should be cell or row). (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :return: BordersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_borders_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_borders_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_borders_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_borders_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_borders_with_http_info(self, request, **kwargs):  # noqa: E501
        """Return a collection of borders.  # noqa: E501

        'nodePath' should refer to node with cell or row  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetBordersRequest object with parameters
        :return: BordersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_borders" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_borders`")  # noqa: E501
        # verify the required parameter 'node_path' is set
        if request.node_path is None:
            raise ValueError("Missing the required parameter `node_path` when calling `get_borders`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/borders'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.node_path is not None:
            path_params[self.__downcase_first_letter('NodePath')] = request.node_path  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BordersResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_comment(self, request, **kwargs):  # noqa: E501
        """Get comment from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The file name. (required)
        :param comment_index int : Comment index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :return: CommentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_comment_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_comment_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_comment_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_comment_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_comment_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get comment from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetCommentRequest object with parameters
        :return: CommentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_comment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_comment`")  # noqa: E501
        # verify the required parameter 'comment_index' is set
        if request.comment_index is None:
            raise ValueError("Missing the required parameter `comment_index` when calling `get_comment`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/comments/{commentIndex}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.comment_index is not None:
            path_params[self.__downcase_first_letter('CommentIndex')] = request.comment_index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CommentResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_comments(self, request, **kwargs):  # noqa: E501
        """Get comments from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The file name. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :return: CommentsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_comments_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_comments_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_comments_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_comments_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_comments_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get comments from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetCommentsRequest object with parameters
        :return: CommentsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_comments" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_comments`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/comments'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CommentsResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document(self, request, **kwargs):  # noqa: E501
        """Read document common info.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param document_name str : The file name. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_document_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_document_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_document_with_http_info(self, request, **kwargs):  # noqa: E501
        """Read document common info.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetDocumentRequest object with parameters
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'document_name' is set
        if request.document_name is None:
            raise ValueError("Missing the required parameter `document_name` when calling `get_document`")  # noqa: E501

        collection_formats = {}
        path = '/words/{documentName}'
        path_params = {}
        if request.document_name is not None:
            path_params[self.__downcase_first_letter('DocumentName')] = request.document_name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DocumentResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_bookmark_by_name(self, request, **kwargs):  # noqa: E501
        """Read document bookmark data by its name.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param bookmark_name str : The bookmark name. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :return: BookmarkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_document_bookmark_by_name_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_bookmark_by_name_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_document_bookmark_by_name_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_bookmark_by_name_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_document_bookmark_by_name_with_http_info(self, request, **kwargs):  # noqa: E501
        """Read document bookmark data by its name.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetDocumentBookmarkByNameRequest object with parameters
        :return: BookmarkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document_bookmark_by_name" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_document_bookmark_by_name`")  # noqa: E501
        # verify the required parameter 'bookmark_name' is set
        if request.bookmark_name is None:
            raise ValueError("Missing the required parameter `bookmark_name` when calling `get_document_bookmark_by_name`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/bookmarks/{bookmarkName}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.bookmark_name is not None:
            path_params[self.__downcase_first_letter('BookmarkName')] = request.bookmark_name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BookmarkResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_bookmarks(self, request, **kwargs):  # noqa: E501
        """Read document bookmarks common info.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :return: BookmarksResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_document_bookmarks_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_bookmarks_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_document_bookmarks_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_bookmarks_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_document_bookmarks_with_http_info(self, request, **kwargs):  # noqa: E501
        """Read document bookmarks common info.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetDocumentBookmarksRequest object with parameters
        :return: BookmarksResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document_bookmarks" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_document_bookmarks`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/bookmarks'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BookmarksResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_drawing_object_by_index(self, request, **kwargs):  # noqa: E501
        """Read document drawing object common info by its index or convert to format specified.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param node_path str : Path to node, which contains collection of drawing objects.
        :return: DrawingObjectResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_document_drawing_object_by_index_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_drawing_object_by_index_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_document_drawing_object_by_index_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_drawing_object_by_index_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_document_drawing_object_by_index_with_http_info(self, request, **kwargs):  # noqa: E501
        """Read document drawing object common info by its index or convert to format specified.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetDocumentDrawingObjectByIndexRequest object with parameters
        :return: DrawingObjectResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document_drawing_object_by_index" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_document_drawing_object_by_index`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `get_document_drawing_object_by_index`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/drawingObjects/{index}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('NodePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('NodePath' + '}'), request.node_path if request.node_path is not None else '')
        else:
            if request.node_path is not None:
                query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DrawingObjectResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_drawing_object_image_data(self, request, **kwargs):  # noqa: E501
        """Read drawing object image data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param node_path str : Path to node, which contains collection of drawing objects.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_document_drawing_object_image_data_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_drawing_object_image_data_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_document_drawing_object_image_data_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_drawing_object_image_data_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_document_drawing_object_image_data_with_http_info(self, request, **kwargs):  # noqa: E501
        """Read drawing object image data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetDocumentDrawingObjectImageDataRequest object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document_drawing_object_image_data" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_document_drawing_object_image_data`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `get_document_drawing_object_image_data`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/drawingObjects/{index}/imageData'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('NodePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('NodePath' + '}'), request.node_path if request.node_path is not None else '')
        else:
            if request.node_path is not None:
                query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_drawing_object_ole_data(self, request, **kwargs):  # noqa: E501
        """Get drawing object OLE data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param node_path str : Path to node, which contains collection of drawing objects.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_document_drawing_object_ole_data_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_drawing_object_ole_data_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_document_drawing_object_ole_data_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_drawing_object_ole_data_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_document_drawing_object_ole_data_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get drawing object OLE data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetDocumentDrawingObjectOleDataRequest object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document_drawing_object_ole_data" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_document_drawing_object_ole_data`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `get_document_drawing_object_ole_data`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/drawingObjects/{index}/oleData'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('NodePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('NodePath' + '}'), request.node_path if request.node_path is not None else '')
        else:
            if request.node_path is not None:
                query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_drawing_objects(self, request, **kwargs):  # noqa: E501
        """Read document drawing objects common info.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param node_path str : Path to node, which contains collection of drawing objects.
        :return: DrawingObjectsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_document_drawing_objects_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_drawing_objects_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_document_drawing_objects_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_drawing_objects_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_document_drawing_objects_with_http_info(self, request, **kwargs):  # noqa: E501
        """Read document drawing objects common info.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetDocumentDrawingObjectsRequest object with parameters
        :return: DrawingObjectsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document_drawing_objects" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_document_drawing_objects`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/drawingObjects'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('NodePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('NodePath' + '}'), request.node_path if request.node_path is not None else '')
        else:
            if request.node_path is not None:
                query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DrawingObjectsResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_field_names(self, request, **kwargs):  # noqa: E501
        """Read document field names.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param use_non_merge_fields bool : If true, result includes \"mustache\" field names.
        :return: FieldNamesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_document_field_names_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_field_names_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_document_field_names_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_field_names_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_document_field_names_with_http_info(self, request, **kwargs):  # noqa: E501
        """Read document field names.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetDocumentFieldNamesRequest object with parameters
        :return: FieldNamesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document_field_names" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_document_field_names`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/mailMergeFieldNames'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('UseNonMergeFields') in path:
            path = path.replace('{' + self.__downcase_first_letter('UseNonMergeFields' + '}'), request.use_non_merge_fields if request.use_non_merge_fields is not None else '')
        else:
            if request.use_non_merge_fields is not None:
                query_params.append((self.__downcase_first_letter('UseNonMergeFields'), request.use_non_merge_fields))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FieldNamesResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_hyperlink_by_index(self, request, **kwargs):  # noqa: E501
        """Read document hyperlink by its index.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param hyperlink_index int : The hyperlink index. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :return: HyperlinkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_document_hyperlink_by_index_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_hyperlink_by_index_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_document_hyperlink_by_index_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_hyperlink_by_index_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_document_hyperlink_by_index_with_http_info(self, request, **kwargs):  # noqa: E501
        """Read document hyperlink by its index.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetDocumentHyperlinkByIndexRequest object with parameters
        :return: HyperlinkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document_hyperlink_by_index" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_document_hyperlink_by_index`")  # noqa: E501
        # verify the required parameter 'hyperlink_index' is set
        if request.hyperlink_index is None:
            raise ValueError("Missing the required parameter `hyperlink_index` when calling `get_document_hyperlink_by_index`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/hyperlinks/{hyperlinkIndex}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.hyperlink_index is not None:
            path_params[self.__downcase_first_letter('HyperlinkIndex')] = request.hyperlink_index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HyperlinkResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_hyperlinks(self, request, **kwargs):  # noqa: E501
        """Read document hyperlinks common info.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :return: HyperlinksResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_document_hyperlinks_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_hyperlinks_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_document_hyperlinks_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_hyperlinks_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_document_hyperlinks_with_http_info(self, request, **kwargs):  # noqa: E501
        """Read document hyperlinks common info.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetDocumentHyperlinksRequest object with parameters
        :return: HyperlinksResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document_hyperlinks" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_document_hyperlinks`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/hyperlinks'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HyperlinksResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_paragraph(self, request, **kwargs):  # noqa: E501
        """This resource represents one of the paragraphs contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param node_path str : Path to node which contains paragraphs.
        :return: ParagraphResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_document_paragraph_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_paragraph_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_document_paragraph_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_paragraph_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_document_paragraph_with_http_info(self, request, **kwargs):  # noqa: E501
        """This resource represents one of the paragraphs contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetDocumentParagraphRequest object with parameters
        :return: ParagraphResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document_paragraph" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_document_paragraph`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `get_document_paragraph`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/paragraphs/{index}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('NodePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('NodePath' + '}'), request.node_path if request.node_path is not None else '')
        else:
            if request.node_path is not None:
                query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ParagraphResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_paragraph_format(self, request, **kwargs):  # noqa: E501
        """Represents all the formatting for a paragraph.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param node_path str : Path to node which contains paragraphs.
        :return: ParagraphFormatResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_document_paragraph_format_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_paragraph_format_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_document_paragraph_format_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_paragraph_format_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_document_paragraph_format_with_http_info(self, request, **kwargs):  # noqa: E501
        """Represents all the formatting for a paragraph.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetDocumentParagraphFormatRequest object with parameters
        :return: ParagraphFormatResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document_paragraph_format" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_document_paragraph_format`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `get_document_paragraph_format`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/paragraphs/{index}/format'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('NodePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('NodePath' + '}'), request.node_path if request.node_path is not None else '')
        else:
            if request.node_path is not None:
                query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ParagraphFormatResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_paragraph_run(self, request, **kwargs):  # noqa: E501
        """This resource represents run of text contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param paragraph_path str : Path to parent paragraph. (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :return: RunResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_document_paragraph_run_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_paragraph_run_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_document_paragraph_run_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_paragraph_run_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_document_paragraph_run_with_http_info(self, request, **kwargs):  # noqa: E501
        """This resource represents run of text contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetDocumentParagraphRunRequest object with parameters
        :return: RunResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document_paragraph_run" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_document_paragraph_run`")  # noqa: E501
        # verify the required parameter 'paragraph_path' is set
        if request.paragraph_path is None:
            raise ValueError("Missing the required parameter `paragraph_path` when calling `get_document_paragraph_run`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `get_document_paragraph_run`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{paragraphPath}/runs/{index}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.paragraph_path is not None:
            path_params[self.__downcase_first_letter('ParagraphPath')] = request.paragraph_path  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RunResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_paragraph_run_font(self, request, **kwargs):  # noqa: E501
        """This resource represents font of run.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param paragraph_path str : Path to parent paragraph. (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :return: FontResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_document_paragraph_run_font_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_paragraph_run_font_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_document_paragraph_run_font_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_paragraph_run_font_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_document_paragraph_run_font_with_http_info(self, request, **kwargs):  # noqa: E501
        """This resource represents font of run.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetDocumentParagraphRunFontRequest object with parameters
        :return: FontResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document_paragraph_run_font" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_document_paragraph_run_font`")  # noqa: E501
        # verify the required parameter 'paragraph_path' is set
        if request.paragraph_path is None:
            raise ValueError("Missing the required parameter `paragraph_path` when calling `get_document_paragraph_run_font`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `get_document_paragraph_run_font`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{paragraphPath}/runs/{index}/font'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.paragraph_path is not None:
            path_params[self.__downcase_first_letter('ParagraphPath')] = request.paragraph_path  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FontResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_paragraph_runs(self, request, **kwargs):  # noqa: E501
        """This resource represents collection of runs in the paragraph.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param paragraph_path str : Path to parent paragraph. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :return: RunsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_document_paragraph_runs_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_paragraph_runs_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_document_paragraph_runs_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_paragraph_runs_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_document_paragraph_runs_with_http_info(self, request, **kwargs):  # noqa: E501
        """This resource represents collection of runs in the paragraph.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetDocumentParagraphRunsRequest object with parameters
        :return: RunsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document_paragraph_runs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_document_paragraph_runs`")  # noqa: E501
        # verify the required parameter 'paragraph_path' is set
        if request.paragraph_path is None:
            raise ValueError("Missing the required parameter `paragraph_path` when calling `get_document_paragraph_runs`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{paragraphPath}/runs'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.paragraph_path is not None:
            path_params[self.__downcase_first_letter('ParagraphPath')] = request.paragraph_path  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RunsResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_paragraphs(self, request, **kwargs):  # noqa: E501
        """Return a list of paragraphs that are contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param node_path str : Path to node which contains paragraphs.
        :return: ParagraphLinkCollectionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_document_paragraphs_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_paragraphs_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_document_paragraphs_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_paragraphs_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_document_paragraphs_with_http_info(self, request, **kwargs):  # noqa: E501
        """Return a list of paragraphs that are contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetDocumentParagraphsRequest object with parameters
        :return: ParagraphLinkCollectionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document_paragraphs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_document_paragraphs`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/paragraphs'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('NodePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('NodePath' + '}'), request.node_path if request.node_path is not None else '')
        else:
            if request.node_path is not None:
                query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ParagraphLinkCollectionResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_properties(self, request, **kwargs):  # noqa: E501
        """Read document properties info.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document's name. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :return: DocumentPropertiesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_document_properties_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_properties_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_document_properties_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_properties_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_document_properties_with_http_info(self, request, **kwargs):  # noqa: E501
        """Read document properties info.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetDocumentPropertiesRequest object with parameters
        :return: DocumentPropertiesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document_properties" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_document_properties`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/documentProperties'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DocumentPropertiesResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_property(self, request, **kwargs):  # noqa: E501
        """Read document property info by the property name.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param property_name str : The property name. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :return: DocumentPropertyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_document_property_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_property_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_document_property_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_property_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_document_property_with_http_info(self, request, **kwargs):  # noqa: E501
        """Read document property info by the property name.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetDocumentPropertyRequest object with parameters
        :return: DocumentPropertyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document_property" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_document_property`")  # noqa: E501
        # verify the required parameter 'property_name' is set
        if request.property_name is None:
            raise ValueError("Missing the required parameter `property_name` when calling `get_document_property`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/documentProperties/{propertyName}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.property_name is not None:
            path_params[self.__downcase_first_letter('PropertyName')] = request.property_name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DocumentPropertyResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_protection(self, request, **kwargs):  # noqa: E501
        """Read document protection common info.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :return: ProtectionDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_document_protection_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_protection_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_document_protection_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_protection_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_document_protection_with_http_info(self, request, **kwargs):  # noqa: E501
        """Read document protection common info.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetDocumentProtectionRequest object with parameters
        :return: ProtectionDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document_protection" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_document_protection`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/protection'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProtectionDataResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_statistics(self, request, **kwargs):  # noqa: E501
        """Read document statistics.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param include_comments bool : Support including/excluding comments from the WordCount. Default value is \"true\".
        :param include_footnotes bool : Support including/excluding footnotes from the WordCount. Default value is \"false\".
        :param include_text_in_shapes bool : Support including/excluding shape's text from the WordCount. Default value is \"false\"
        :return: StatDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_document_statistics_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_statistics_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_document_statistics_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_statistics_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_document_statistics_with_http_info(self, request, **kwargs):  # noqa: E501
        """Read document statistics.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetDocumentStatisticsRequest object with parameters
        :return: StatDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document_statistics" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_document_statistics`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/statistics'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('IncludeComments') in path:
            path = path.replace('{' + self.__downcase_first_letter('IncludeComments' + '}'), request.include_comments if request.include_comments is not None else '')
        else:
            if request.include_comments is not None:
                query_params.append((self.__downcase_first_letter('IncludeComments'), request.include_comments))  # noqa: E501
        if self.__downcase_first_letter('IncludeFootnotes') in path:
            path = path.replace('{' + self.__downcase_first_letter('IncludeFootnotes' + '}'), request.include_footnotes if request.include_footnotes is not None else '')
        else:
            if request.include_footnotes is not None:
                query_params.append((self.__downcase_first_letter('IncludeFootnotes'), request.include_footnotes))  # noqa: E501
        if self.__downcase_first_letter('IncludeTextInShapes') in path:
            path = path.replace('{' + self.__downcase_first_letter('IncludeTextInShapes' + '}'), request.include_text_in_shapes if request.include_text_in_shapes is not None else '')
        else:
            if request.include_text_in_shapes is not None:
                query_params.append((self.__downcase_first_letter('IncludeTextInShapes'), request.include_text_in_shapes))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StatDataResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_text_items(self, request, **kwargs):  # noqa: E501
        """Read document text items.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :return: TextItemsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_document_text_items_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_text_items_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_document_text_items_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_text_items_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_document_text_items_with_http_info(self, request, **kwargs):  # noqa: E501
        """Read document text items.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetDocumentTextItemsRequest object with parameters
        :return: TextItemsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document_text_items" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_document_text_items`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/textItems'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TextItemsResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_with_format(self, request, **kwargs):  # noqa: E501
        """Export the document into the specified format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The file name. (required)
        :param format str : The destination format. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param out_path str : Path to save result
        :param fonts_location str : Folder in filestorage with custom fonts.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_document_with_format_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_with_format_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_document_with_format_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_with_format_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_document_with_format_with_http_info(self, request, **kwargs):  # noqa: E501
        """Export the document into the specified format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetDocumentWithFormatRequest object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document_with_format" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_document_with_format`")  # noqa: E501
        # verify the required parameter 'format' is set
        if request.format is None:
            raise ValueError("Missing the required parameter `format` when calling `get_document_with_format`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Format') in path:
            path = path.replace('{' + self.__downcase_first_letter('Format' + '}'), request.format if request.format is not None else '')
        else:
            if request.format is not None:
                query_params.append((self.__downcase_first_letter('Format'), request.format))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('OutPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('OutPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('OutPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('FontsLocation') in path:
            path = path.replace('{' + self.__downcase_first_letter('FontsLocation' + '}'), request.fonts_location if request.fonts_location is not None else '')
        else:
            if request.fonts_location is not None:
                query_params.append((self.__downcase_first_letter('FontsLocation'), request.fonts_location))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_field(self, request, **kwargs):  # noqa: E501
        """Get field from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The file name. (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param node_path str : Path to node, which contains collection of fields.
        :return: FieldResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_field_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_field_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_field_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_field_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_field_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get field from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetFieldRequest object with parameters
        :return: FieldResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_field" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_field`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `get_field`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/fields/{index}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('NodePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('NodePath' + '}'), request.node_path if request.node_path is not None else '')
        else:
            if request.node_path is not None:
                query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FieldResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_fields(self, request, **kwargs):  # noqa: E501
        """Get fields from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The file name. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param node_path str : Path to node, which contains collection of fields.
        :return: FieldsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_fields_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_fields_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_fields_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_fields_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_fields_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get fields from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetFieldsRequest object with parameters
        :return: FieldsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_fields" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_fields`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/fields'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('NodePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('NodePath' + '}'), request.node_path if request.node_path is not None else '')
        else:
            if request.node_path is not None:
                query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FieldsResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_footnote(self, request, **kwargs):  # noqa: E501
        """Read footnote by index.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param node_path str : Path to node, which contains collection of footnotes.
        :return: FootnoteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_footnote_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_footnote_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_footnote_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_footnote_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_footnote_with_http_info(self, request, **kwargs):  # noqa: E501
        """Read footnote by index.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetFootnoteRequest object with parameters
        :return: FootnoteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_footnote" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_footnote`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `get_footnote`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/footnotes/{index}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('NodePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('NodePath' + '}'), request.node_path if request.node_path is not None else '')
        else:
            if request.node_path is not None:
                query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FootnoteResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_footnotes(self, request, **kwargs):  # noqa: E501
        """Get footnotes from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The file name. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param node_path str : Path to node, which contains collection of footnotes.
        :return: FootnotesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_footnotes_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_footnotes_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_footnotes_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_footnotes_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_footnotes_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get footnotes from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetFootnotesRequest object with parameters
        :return: FootnotesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_footnotes" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_footnotes`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/footnotes'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('NodePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('NodePath' + '}'), request.node_path if request.node_path is not None else '')
        else:
            if request.node_path is not None:
                query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FootnotesResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_form_field(self, request, **kwargs):  # noqa: E501
        """Returns representation of an one of the form field.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param node_path str : Path to node that contains collection of formfields.
        :return: FormFieldResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_form_field_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_form_field_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_form_field_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_form_field_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_form_field_with_http_info(self, request, **kwargs):  # noqa: E501
        """Returns representation of an one of the form field.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetFormFieldRequest object with parameters
        :return: FormFieldResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_form_field" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_form_field`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `get_form_field`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/formfields/{index}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('NodePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('NodePath' + '}'), request.node_path if request.node_path is not None else '')
        else:
            if request.node_path is not None:
                query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FormFieldResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_form_fields(self, request, **kwargs):  # noqa: E501
        """Get form fields from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The file name. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param node_path str : Path to node containing collection of form fields.
        :return: FormFieldsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_form_fields_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_form_fields_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_form_fields_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_form_fields_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_form_fields_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get form fields from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetFormFieldsRequest object with parameters
        :return: FormFieldsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_form_fields" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_form_fields`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/formfields'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('NodePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('NodePath' + '}'), request.node_path if request.node_path is not None else '')
        else:
            if request.node_path is not None:
                query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FormFieldsResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_header_footer(self, request, **kwargs):  # noqa: E501
        """Return a header/footer that is contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param header_footer_index int : Header/footer index. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param filter_by_type str : List of types of headers and footers.
        :return: HeaderFooterResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_header_footer_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_header_footer_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_header_footer_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_header_footer_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_header_footer_with_http_info(self, request, **kwargs):  # noqa: E501
        """Return a header/footer that is contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetHeaderFooterRequest object with parameters
        :return: HeaderFooterResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_header_footer" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_header_footer`")  # noqa: E501
        # verify the required parameter 'header_footer_index' is set
        if request.header_footer_index is None:
            raise ValueError("Missing the required parameter `header_footer_index` when calling `get_header_footer`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/headersfooters/{headerFooterIndex}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.header_footer_index is not None:
            path_params[self.__downcase_first_letter('HeaderFooterIndex')] = request.header_footer_index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('FilterByType') in path:
            path = path.replace('{' + self.__downcase_first_letter('FilterByType' + '}'), request.filter_by_type if request.filter_by_type is not None else '')
        else:
            if request.filter_by_type is not None:
                query_params.append((self.__downcase_first_letter('FilterByType'), request.filter_by_type))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HeaderFooterResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_header_footer_of_section(self, request, **kwargs):  # noqa: E501
        """Return a header/footer that is contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param header_footer_index int : Header/footer index. (required)
        :param section_index int : Section index. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param filter_by_type str : List of types of headers and footers.
        :return: HeaderFooterResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_header_footer_of_section_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_header_footer_of_section_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_header_footer_of_section_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_header_footer_of_section_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_header_footer_of_section_with_http_info(self, request, **kwargs):  # noqa: E501
        """Return a header/footer that is contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetHeaderFooterOfSectionRequest object with parameters
        :return: HeaderFooterResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_header_footer_of_section" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_header_footer_of_section`")  # noqa: E501
        # verify the required parameter 'header_footer_index' is set
        if request.header_footer_index is None:
            raise ValueError("Missing the required parameter `header_footer_index` when calling `get_header_footer_of_section`")  # noqa: E501
        # verify the required parameter 'section_index' is set
        if request.section_index is None:
            raise ValueError("Missing the required parameter `section_index` when calling `get_header_footer_of_section`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/sections/{sectionIndex}/headersfooters/{headerFooterIndex}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.header_footer_index is not None:
            path_params[self.__downcase_first_letter('HeaderFooterIndex')] = request.header_footer_index  # noqa: E501
        if request.section_index is not None:
            path_params[self.__downcase_first_letter('SectionIndex')] = request.section_index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('FilterByType') in path:
            path = path.replace('{' + self.__downcase_first_letter('FilterByType' + '}'), request.filter_by_type if request.filter_by_type is not None else '')
        else:
            if request.filter_by_type is not None:
                query_params.append((self.__downcase_first_letter('FilterByType'), request.filter_by_type))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HeaderFooterResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_header_footers(self, request, **kwargs):  # noqa: E501
        """Return a list of header/footers that are contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param section_path str : Path to parent section.
        :param filter_by_type str : List of types of headers and footers.
        :return: HeaderFootersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_header_footers_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_header_footers_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_header_footers_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_header_footers_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_header_footers_with_http_info(self, request, **kwargs):  # noqa: E501
        """Return a list of header/footers that are contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetHeaderFootersRequest object with parameters
        :return: HeaderFootersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_header_footers" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_header_footers`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{sectionPath}/headersfooters'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('SectionPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('SectionPath' + '}'), request.section_path if request.section_path is not None else '')
        else:
            if request.section_path is not None:
                query_params.append((self.__downcase_first_letter('SectionPath'), request.section_path))  # noqa: E501
        if self.__downcase_first_letter('FilterByType') in path:
            path = path.replace('{' + self.__downcase_first_letter('FilterByType' + '}'), request.filter_by_type if request.filter_by_type is not None else '')
        else:
            if request.filter_by_type is not None:
                query_params.append((self.__downcase_first_letter('FilterByType'), request.filter_by_type))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HeaderFootersResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_office_math_object(self, request, **kwargs):  # noqa: E501
        """Read OfficeMath object by index.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param node_path str : Path to node, which contains collection of OfficeMath objects.
        :return: OfficeMathObjectResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_office_math_object_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_office_math_object_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_office_math_object_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_office_math_object_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_office_math_object_with_http_info(self, request, **kwargs):  # noqa: E501
        """Read OfficeMath object by index.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetOfficeMathObjectRequest object with parameters
        :return: OfficeMathObjectResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_office_math_object" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_office_math_object`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `get_office_math_object`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/OfficeMathObjects/{index}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('NodePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('NodePath' + '}'), request.node_path if request.node_path is not None else '')
        else:
            if request.node_path is not None:
                query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OfficeMathObjectResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_office_math_objects(self, request, **kwargs):  # noqa: E501
        """Get OfficeMath objects from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The file name. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param node_path str : Path to node, which contains collection of OfficeMath objects.
        :return: OfficeMathObjectsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_office_math_objects_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_office_math_objects_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_office_math_objects_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_office_math_objects_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_office_math_objects_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get OfficeMath objects from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetOfficeMathObjectsRequest object with parameters
        :return: OfficeMathObjectsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_office_math_objects" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_office_math_objects`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/OfficeMathObjects'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('NodePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('NodePath' + '}'), request.node_path if request.node_path is not None else '')
        else:
            if request.node_path is not None:
                query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OfficeMathObjectsResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_section(self, request, **kwargs):  # noqa: E501
        """Get document section by index.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param section_index int : Section index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :return: SectionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_section_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_section_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_section_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_section_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_section_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get document section by index.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetSectionRequest object with parameters
        :return: SectionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_section" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_section`")  # noqa: E501
        # verify the required parameter 'section_index' is set
        if request.section_index is None:
            raise ValueError("Missing the required parameter `section_index` when calling `get_section`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/sections/{sectionIndex}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.section_index is not None:
            path_params[self.__downcase_first_letter('SectionIndex')] = request.section_index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SectionResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_section_page_setup(self, request, **kwargs):  # noqa: E501
        """Get page setup of section.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param section_index int : Section index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :return: SectionPageSetupResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_section_page_setup_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_section_page_setup_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_section_page_setup_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_section_page_setup_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_section_page_setup_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get page setup of section.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetSectionPageSetupRequest object with parameters
        :return: SectionPageSetupResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_section_page_setup" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_section_page_setup`")  # noqa: E501
        # verify the required parameter 'section_index' is set
        if request.section_index is None:
            raise ValueError("Missing the required parameter `section_index` when calling `get_section_page_setup`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/sections/{sectionIndex}/pageSetup'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.section_index is not None:
            path_params[self.__downcase_first_letter('SectionIndex')] = request.section_index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SectionPageSetupResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_sections(self, request, **kwargs):  # noqa: E501
        """Return a list of sections that are contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :return: SectionLinkCollectionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_sections_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_sections_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_sections_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_sections_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_sections_with_http_info(self, request, **kwargs):  # noqa: E501
        """Return a list of sections that are contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetSectionsRequest object with parameters
        :return: SectionLinkCollectionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sections" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_sections`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/sections'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SectionLinkCollectionResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_table(self, request, **kwargs):  # noqa: E501
        """Return a table.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param node_path str : Path to node, which contains tables.
        :return: TableResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_table_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_table_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_table_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_table_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_table_with_http_info(self, request, **kwargs):  # noqa: E501
        """Return a table.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetTableRequest object with parameters
        :return: TableResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_table" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_table`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `get_table`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/tables/{index}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('NodePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('NodePath' + '}'), request.node_path if request.node_path is not None else '')
        else:
            if request.node_path is not None:
                query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TableResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_table_cell(self, request, **kwargs):  # noqa: E501
        """Return a table cell.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param table_row_path str : Path to table row. (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :return: TableCellResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_table_cell_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_table_cell_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_table_cell_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_table_cell_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_table_cell_with_http_info(self, request, **kwargs):  # noqa: E501
        """Return a table cell.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetTableCellRequest object with parameters
        :return: TableCellResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_table_cell" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_table_cell`")  # noqa: E501
        # verify the required parameter 'table_row_path' is set
        if request.table_row_path is None:
            raise ValueError("Missing the required parameter `table_row_path` when calling `get_table_cell`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `get_table_cell`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{tableRowPath}/cells/{index}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.table_row_path is not None:
            path_params[self.__downcase_first_letter('TableRowPath')] = request.table_row_path  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TableCellResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_table_cell_format(self, request, **kwargs):  # noqa: E501
        """Return a table cell format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param table_row_path str : Path to table row. (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :return: TableCellFormatResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_table_cell_format_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_table_cell_format_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_table_cell_format_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_table_cell_format_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_table_cell_format_with_http_info(self, request, **kwargs):  # noqa: E501
        """Return a table cell format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetTableCellFormatRequest object with parameters
        :return: TableCellFormatResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_table_cell_format" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_table_cell_format`")  # noqa: E501
        # verify the required parameter 'table_row_path' is set
        if request.table_row_path is None:
            raise ValueError("Missing the required parameter `table_row_path` when calling `get_table_cell_format`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `get_table_cell_format`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{tableRowPath}/cells/{index}/cellformat'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.table_row_path is not None:
            path_params[self.__downcase_first_letter('TableRowPath')] = request.table_row_path  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TableCellFormatResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_table_properties(self, request, **kwargs):  # noqa: E501
        """Return a table properties.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param node_path str : Path to node, which contains tables.
        :return: TablePropertiesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_table_properties_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_table_properties_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_table_properties_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_table_properties_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_table_properties_with_http_info(self, request, **kwargs):  # noqa: E501
        """Return a table properties.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetTablePropertiesRequest object with parameters
        :return: TablePropertiesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_table_properties" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_table_properties`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `get_table_properties`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/tables/{index}/properties'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('NodePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('NodePath' + '}'), request.node_path if request.node_path is not None else '')
        else:
            if request.node_path is not None:
                query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TablePropertiesResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_table_row(self, request, **kwargs):  # noqa: E501
        """Return a table row.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param table_path str : Path to table. (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :return: TableRowResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_table_row_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_table_row_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_table_row_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_table_row_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_table_row_with_http_info(self, request, **kwargs):  # noqa: E501
        """Return a table row.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetTableRowRequest object with parameters
        :return: TableRowResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_table_row" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_table_row`")  # noqa: E501
        # verify the required parameter 'table_path' is set
        if request.table_path is None:
            raise ValueError("Missing the required parameter `table_path` when calling `get_table_row`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `get_table_row`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{tablePath}/rows/{index}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.table_path is not None:
            path_params[self.__downcase_first_letter('TablePath')] = request.table_path  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TableRowResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_table_row_format(self, request, **kwargs):  # noqa: E501
        """Return a table row format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param table_path str : Path to table. (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :return: TableRowFormatResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_table_row_format_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_table_row_format_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_table_row_format_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_table_row_format_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_table_row_format_with_http_info(self, request, **kwargs):  # noqa: E501
        """Return a table row format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetTableRowFormatRequest object with parameters
        :return: TableRowFormatResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_table_row_format" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_table_row_format`")  # noqa: E501
        # verify the required parameter 'table_path' is set
        if request.table_path is None:
            raise ValueError("Missing the required parameter `table_path` when calling `get_table_row_format`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `get_table_row_format`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{tablePath}/rows/{index}/rowformat'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.table_path is not None:
            path_params[self.__downcase_first_letter('TablePath')] = request.table_path  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TableRowFormatResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_tables(self, request, **kwargs):  # noqa: E501
        """Return a list of tables that are contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param node_path str : Path to node, which contains tables.
        :return: TableLinkCollectionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_tables_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_tables_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_tables_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_tables_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_tables_with_http_info(self, request, **kwargs):  # noqa: E501
        """Return a list of tables that are contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetTablesRequest object with parameters
        :return: TableLinkCollectionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_tables" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_tables`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/tables'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('NodePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('NodePath' + '}'), request.node_path if request.node_path is not None else '')
        else:
            if request.node_path is not None:
                query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TableLinkCollectionResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def insert_table(self, request, **kwargs):  # noqa: E501
        """Adds table to document, returns added table&#39;s data.               # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :param table TableInsert : Table parameters/
        :param node_path str : Path to node, which contains tables.
        :return: TableResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.insert_table_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.insert_table_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.insert_table_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.insert_table_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def insert_table_with_http_info(self, request, **kwargs):  # noqa: E501
        """Adds table to document, returns added table&#39;s data.               # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request InsertTableRequest object with parameters
        :return: TableResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method insert_table" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `insert_table`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/tables'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if self.__downcase_first_letter('NodePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('NodePath' + '}'), request.node_path if request.node_path is not None else '')
        else:
            if request.node_path is not None:
                query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.table is not None:
            body_params = request.table
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TableResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def insert_table_cell(self, request, **kwargs):  # noqa: E501
        """Adds table cell to table, returns added cell&#39;s data.               # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param table_row_path str : Path to table row. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :param cell TableCellInsert : Table cell parameters/
        :return: TableCellResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.insert_table_cell_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.insert_table_cell_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.insert_table_cell_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.insert_table_cell_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def insert_table_cell_with_http_info(self, request, **kwargs):  # noqa: E501
        """Adds table cell to table, returns added cell&#39;s data.               # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request InsertTableCellRequest object with parameters
        :return: TableCellResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method insert_table_cell" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `insert_table_cell`")  # noqa: E501
        # verify the required parameter 'table_row_path' is set
        if request.table_row_path is None:
            raise ValueError("Missing the required parameter `table_row_path` when calling `insert_table_cell`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{tableRowPath}/cells'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.table_row_path is not None:
            path_params[self.__downcase_first_letter('TableRowPath')] = request.table_row_path  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.cell is not None:
            body_params = request.cell
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TableCellResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def insert_table_row(self, request, **kwargs):  # noqa: E501
        """Adds table row to table, returns added row&#39;s data.               # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param table_path str : Path to table. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :param row TableRowInsert : Table row parameters/
        :return: TableRowResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.insert_table_row_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.insert_table_row_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.insert_table_row_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.insert_table_row_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def insert_table_row_with_http_info(self, request, **kwargs):  # noqa: E501
        """Adds table row to table, returns added row&#39;s data.               # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request InsertTableRowRequest object with parameters
        :return: TableRowResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method insert_table_row" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `insert_table_row`")  # noqa: E501
        # verify the required parameter 'table_path' is set
        if request.table_path is None:
            raise ValueError("Missing the required parameter `table_path` when calling `insert_table_row`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{tablePath}/rows'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.table_path is not None:
            path_params[self.__downcase_first_letter('TablePath')] = request.table_path  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.row is not None:
            body_params = request.row
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TableRowResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_append_document(self, request, **kwargs):  # noqa: E501
        """Append documents to original document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : Original document name. (required)
        :param document_list DocumentEntryList : with a list of documents to append.             (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_append_document_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_append_document_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_append_document_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_append_document_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_append_document_with_http_info(self, request, **kwargs):  # noqa: E501
        """Append documents to original document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PostAppendDocumentRequest object with parameters
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_append_document" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_append_document`")  # noqa: E501
        # verify the required parameter 'document_list' is set
        if request.document_list is None:
            raise ValueError("Missing the required parameter `document_list` when calling `post_append_document`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/appendDocument'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.document_list is not None:
            body_params = request.document_list
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DocumentResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_change_document_protection(self, request, **kwargs):  # noqa: E501
        """Change document protection.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param protection_request ProtectionRequest : with protection settings.             (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :return: ProtectionDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_change_document_protection_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_change_document_protection_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_change_document_protection_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_change_document_protection_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_change_document_protection_with_http_info(self, request, **kwargs):  # noqa: E501
        """Change document protection.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PostChangeDocumentProtectionRequest object with parameters
        :return: ProtectionDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_change_document_protection" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_change_document_protection`")  # noqa: E501
        # verify the required parameter 'protection_request' is set
        if request.protection_request is None:
            raise ValueError("Missing the required parameter `protection_request` when calling `post_change_document_protection`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/protection'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.protection_request is not None:
            body_params = request.protection_request
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProtectionDataResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_comment(self, request, **kwargs):  # noqa: E501
        """Updates the comment, returns updated comment&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param comment_index int : Comment index (required)
        :param comment Comment : Comment data. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: CommentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_comment_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_comment_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_comment_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_comment_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_comment_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates the comment, returns updated comment&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PostCommentRequest object with parameters
        :return: CommentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_comment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_comment`")  # noqa: E501
        # verify the required parameter 'comment_index' is set
        if request.comment_index is None:
            raise ValueError("Missing the required parameter `comment_index` when calling `post_comment`")  # noqa: E501
        # verify the required parameter 'comment' is set
        if request.comment is None:
            raise ValueError("Missing the required parameter `comment` when calling `post_comment`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/comments/{commentIndex}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.comment_index is not None:
            path_params[self.__downcase_first_letter('CommentIndex')] = request.comment_index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.comment is not None:
            body_params = request.comment
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CommentResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_compare_document(self, request, **kwargs):  # noqa: E501
        """Compare document with original document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : Original document name. (required)
        :param compare_data CompareData : with a document to compare.             (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_compare_document_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_compare_document_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_compare_document_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_compare_document_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_compare_document_with_http_info(self, request, **kwargs):  # noqa: E501
        """Compare document with original document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PostCompareDocumentRequest object with parameters
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_compare_document" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_compare_document`")  # noqa: E501
        # verify the required parameter 'compare_data' is set
        if request.compare_data is None:
            raise ValueError("Missing the required parameter `compare_data` when calling `post_compare_document`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/compareDocument'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.compare_data is not None:
            body_params = request.compare_data
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DocumentResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_document_execute_mail_merge(self, request, **kwargs):  # noqa: E501
        """Execute document mail merge operation.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param data str : Mail merge data
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param with_regions bool : With regions flag.
        :param mail_merge_data_file str : Mail merge data.
        :param cleanup str : Clean up options.
        :param use_whole_paragraph_as_region bool : Gets or sets a value indicating whether paragraph with TableStart or              TableEnd field should be fully included into mail merge region or particular range between TableStart and TableEnd fields.              The default value is true.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved with autogenerated name.
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_document_execute_mail_merge_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_document_execute_mail_merge_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_document_execute_mail_merge_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_document_execute_mail_merge_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_document_execute_mail_merge_with_http_info(self, request, **kwargs):  # noqa: E501
        """Execute document mail merge operation.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PostDocumentExecuteMailMergeRequest object with parameters
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_document_execute_mail_merge" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_document_execute_mail_merge`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/executeMailMerge'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('WithRegions') in path:
            path = path.replace('{' + self.__downcase_first_letter('WithRegions' + '}'), request.with_regions if request.with_regions is not None else '')
        else:
            if request.with_regions is not None:
                query_params.append((self.__downcase_first_letter('WithRegions'), request.with_regions))  # noqa: E501
        if self.__downcase_first_letter('MailMergeDataFile') in path:
            path = path.replace('{' + self.__downcase_first_letter('MailMergeDataFile' + '}'), request.mail_merge_data_file if request.mail_merge_data_file is not None else '')
        else:
            if request.mail_merge_data_file is not None:
                query_params.append((self.__downcase_first_letter('MailMergeDataFile'), request.mail_merge_data_file))  # noqa: E501
        if self.__downcase_first_letter('Cleanup') in path:
            path = path.replace('{' + self.__downcase_first_letter('Cleanup' + '}'), request.cleanup if request.cleanup is not None else '')
        else:
            if request.cleanup is not None:
                query_params.append((self.__downcase_first_letter('Cleanup'), request.cleanup))  # noqa: E501
        if self.__downcase_first_letter('UseWholeParagraphAsRegion') in path:
            path = path.replace('{' + self.__downcase_first_letter('UseWholeParagraphAsRegion' + '}'), request.use_whole_paragraph_as_region if request.use_whole_paragraph_as_region is not None else '')
        else:
            if request.use_whole_paragraph_as_region is not None:
                query_params.append((self.__downcase_first_letter('UseWholeParagraphAsRegion'), request.use_whole_paragraph_as_region))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.data is not None:
            form_params.append((self.__downcase_first_letter('Data'), request.data))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DocumentResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_document_paragraph_format(self, request, **kwargs):  # noqa: E501
        """Updates paragrpaph format properties, returns updated format properties.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param dto ParagraphFormat : Paragraph format object (required)
        :param node_path str : Path to node which contains paragraphs. (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: ParagraphFormatResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_document_paragraph_format_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_document_paragraph_format_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_document_paragraph_format_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_document_paragraph_format_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_document_paragraph_format_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates paragrpaph format properties, returns updated format properties.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PostDocumentParagraphFormatRequest object with parameters
        :return: ParagraphFormatResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_document_paragraph_format" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_document_paragraph_format`")  # noqa: E501
        # verify the required parameter 'dto' is set
        if request.dto is None:
            raise ValueError("Missing the required parameter `dto` when calling `post_document_paragraph_format`")  # noqa: E501
        # verify the required parameter 'node_path' is set
        if request.node_path is None:
            raise ValueError("Missing the required parameter `node_path` when calling `post_document_paragraph_format`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `post_document_paragraph_format`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/paragraphs/{index}/format'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.node_path is not None:
            path_params[self.__downcase_first_letter('NodePath')] = request.node_path  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.dto is not None:
            body_params = request.dto
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ParagraphFormatResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_document_paragraph_run_font(self, request, **kwargs):  # noqa: E501
        """Updates font properties, returns updated font data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param font_dto Font : Font dto object (required)
        :param paragraph_path str : Path to parent paragraph. (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: FontResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_document_paragraph_run_font_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_document_paragraph_run_font_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_document_paragraph_run_font_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_document_paragraph_run_font_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_document_paragraph_run_font_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates font properties, returns updated font data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PostDocumentParagraphRunFontRequest object with parameters
        :return: FontResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_document_paragraph_run_font" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_document_paragraph_run_font`")  # noqa: E501
        # verify the required parameter 'font_dto' is set
        if request.font_dto is None:
            raise ValueError("Missing the required parameter `font_dto` when calling `post_document_paragraph_run_font`")  # noqa: E501
        # verify the required parameter 'paragraph_path' is set
        if request.paragraph_path is None:
            raise ValueError("Missing the required parameter `paragraph_path` when calling `post_document_paragraph_run_font`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `post_document_paragraph_run_font`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{paragraphPath}/runs/{index}/font'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.paragraph_path is not None:
            path_params[self.__downcase_first_letter('ParagraphPath')] = request.paragraph_path  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.font_dto is not None:
            body_params = request.font_dto
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FontResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_document_save_as(self, request, **kwargs):  # noqa: E501
        """Convert document to destination format with detailed settings and save result to storage.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param save_options_data SaveOptionsData : Save options. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param fonts_location str : Folder in filestorage with custom fonts.
        :return: SaveResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_document_save_as_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_document_save_as_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_document_save_as_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_document_save_as_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_document_save_as_with_http_info(self, request, **kwargs):  # noqa: E501
        """Convert document to destination format with detailed settings and save result to storage.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PostDocumentSaveAsRequest object with parameters
        :return: SaveResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_document_save_as" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_document_save_as`")  # noqa: E501
        # verify the required parameter 'save_options_data' is set
        if request.save_options_data is None:
            raise ValueError("Missing the required parameter `save_options_data` when calling `post_document_save_as`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/saveAs'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('FontsLocation') in path:
            path = path.replace('{' + self.__downcase_first_letter('FontsLocation' + '}'), request.fonts_location if request.fonts_location is not None else '')
        else:
            if request.fonts_location is not None:
                query_params.append((self.__downcase_first_letter('FontsLocation'), request.fonts_location))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.save_options_data is not None:
            body_params = request.save_options_data
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SaveResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_drawing_object(self, request, **kwargs):  # noqa: E501
        """Updates drawing object, returns updated  drawing object&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param drawing_object str : Drawing object parameters (required)
        :param image_file file : File with image (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :param node_path str : Path to node, which contains collection of drawing objects.
        :return: DrawingObjectResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_drawing_object_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_drawing_object_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_drawing_object_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_drawing_object_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_drawing_object_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates drawing object, returns updated  drawing object&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PostDrawingObjectRequest object with parameters
        :return: DrawingObjectResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_drawing_object" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_drawing_object`")  # noqa: E501
        # verify the required parameter 'drawing_object' is set
        if request.drawing_object is None:
            raise ValueError("Missing the required parameter `drawing_object` when calling `post_drawing_object`")  # noqa: E501
        # verify the required parameter 'image_file' is set
        if request.image_file is None:
            raise ValueError("Missing the required parameter `image_file` when calling `post_drawing_object`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `post_drawing_object`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/drawingObjects/{index}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if self.__downcase_first_letter('NodePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('NodePath' + '}'), request.node_path if request.node_path is not None else '')
        else:
            if request.node_path is not None:
                query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.drawing_object is not None:
            form_params.append((self.__downcase_first_letter('DrawingObject'), request.drawing_object))  # noqa: E501
        if request.image_file is not None:
            local_var_files.append((self.__downcase_first_letter('ImageFile'), request.image_file))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DrawingObjectResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_execute_template(self, request, **kwargs):  # noqa: E501
        """Populate document template with data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The template document name. (required)
        :param data str : Mail merge data (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param cleanup str : Clean up options.
        :param use_whole_paragraph_as_region bool : Gets or sets a value indicating whether paragraph with TableStart or  TableEnd field should be fully included into mail merge region or particular range between TableStart and TableEnd fields.   The default value is true.
        :param with_regions bool : Merge with regions or not. True by default
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved with autogenerated name.
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_execute_template_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_execute_template_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_execute_template_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_execute_template_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_execute_template_with_http_info(self, request, **kwargs):  # noqa: E501
        """Populate document template with data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PostExecuteTemplateRequest object with parameters
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_execute_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_execute_template`")  # noqa: E501
        # verify the required parameter 'data' is set
        if request.data is None:
            raise ValueError("Missing the required parameter `data` when calling `post_execute_template`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/executeTemplate'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('Cleanup') in path:
            path = path.replace('{' + self.__downcase_first_letter('Cleanup' + '}'), request.cleanup if request.cleanup is not None else '')
        else:
            if request.cleanup is not None:
                query_params.append((self.__downcase_first_letter('Cleanup'), request.cleanup))  # noqa: E501
        if self.__downcase_first_letter('UseWholeParagraphAsRegion') in path:
            path = path.replace('{' + self.__downcase_first_letter('UseWholeParagraphAsRegion' + '}'), request.use_whole_paragraph_as_region if request.use_whole_paragraph_as_region is not None else '')
        else:
            if request.use_whole_paragraph_as_region is not None:
                query_params.append((self.__downcase_first_letter('UseWholeParagraphAsRegion'), request.use_whole_paragraph_as_region))  # noqa: E501
        if self.__downcase_first_letter('WithRegions') in path:
            path = path.replace('{' + self.__downcase_first_letter('WithRegions' + '}'), request.with_regions if request.with_regions is not None else '')
        else:
            if request.with_regions is not None:
                query_params.append((self.__downcase_first_letter('WithRegions'), request.with_regions))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.data is not None:
            form_params.append((self.__downcase_first_letter('Data'), request.data))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DocumentResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_field(self, request, **kwargs):  # noqa: E501
        """Updates field&#39;s properties, returns updated field&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param field Field : Field data. (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :param node_path str : Path to node, which contains collection of fields.
        :return: FieldResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_field_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_field_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_field_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_field_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_field_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates field&#39;s properties, returns updated field&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PostFieldRequest object with parameters
        :return: FieldResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_field" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_field`")  # noqa: E501
        # verify the required parameter 'field' is set
        if request.field is None:
            raise ValueError("Missing the required parameter `field` when calling `post_field`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `post_field`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/fields/{index}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if self.__downcase_first_letter('NodePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('NodePath' + '}'), request.node_path if request.node_path is not None else '')
        else:
            if request.node_path is not None:
                query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.field is not None:
            body_params = request.field
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FieldResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_footnote(self, request, **kwargs):  # noqa: E501
        """Updates footnote&#39;s properties, returns updated run&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param footnote_dto Footnote : Footnote data. (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :param node_path str : Path to node, which contains collection of footnotes.
        :return: FootnoteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_footnote_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_footnote_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_footnote_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_footnote_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_footnote_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates footnote&#39;s properties, returns updated run&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PostFootnoteRequest object with parameters
        :return: FootnoteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_footnote" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_footnote`")  # noqa: E501
        # verify the required parameter 'footnote_dto' is set
        if request.footnote_dto is None:
            raise ValueError("Missing the required parameter `footnote_dto` when calling `post_footnote`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `post_footnote`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/footnotes/{index}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if self.__downcase_first_letter('NodePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('NodePath' + '}'), request.node_path if request.node_path is not None else '')
        else:
            if request.node_path is not None:
                query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.footnote_dto is not None:
            body_params = request.footnote_dto
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FootnoteResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_form_field(self, request, **kwargs):  # noqa: E501
        """Updates properties of form field, returns updated form field.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param form_field FormField : From field data. (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :param node_path str : Path to node that contains collection of formfields.
        :return: FormFieldResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_form_field_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_form_field_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_form_field_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_form_field_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_form_field_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates properties of form field, returns updated form field.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PostFormFieldRequest object with parameters
        :return: FormFieldResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_form_field" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_form_field`")  # noqa: E501
        # verify the required parameter 'form_field' is set
        if request.form_field is None:
            raise ValueError("Missing the required parameter `form_field` when calling `post_form_field`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `post_form_field`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/formfields/{index}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if self.__downcase_first_letter('NodePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('NodePath' + '}'), request.node_path if request.node_path is not None else '')
        else:
            if request.node_path is not None:
                query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.form_field is not None:
            body_params = request.form_field
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FormFieldResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_insert_document_watermark_image(self, request, **kwargs):  # noqa: E501
        """Insert document watermark image.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param image_file file : File with image
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :param rotation_angle float : The watermark rotation angle.
        :param image str : The image file server full name. If the name is empty the image is expected in request content.
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_insert_document_watermark_image_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_insert_document_watermark_image_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_insert_document_watermark_image_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_insert_document_watermark_image_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_insert_document_watermark_image_with_http_info(self, request, **kwargs):  # noqa: E501
        """Insert document watermark image.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PostInsertDocumentWatermarkImageRequest object with parameters
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_insert_document_watermark_image" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_insert_document_watermark_image`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/watermark/insertImage'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if self.__downcase_first_letter('RotationAngle') in path:
            path = path.replace('{' + self.__downcase_first_letter('RotationAngle' + '}'), request.rotation_angle if request.rotation_angle is not None else '')
        else:
            if request.rotation_angle is not None:
                query_params.append((self.__downcase_first_letter('RotationAngle'), request.rotation_angle))  # noqa: E501
        if self.__downcase_first_letter('Image') in path:
            path = path.replace('{' + self.__downcase_first_letter('Image' + '}'), request.image if request.image is not None else '')
        else:
            if request.image is not None:
                query_params.append((self.__downcase_first_letter('Image'), request.image))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.image_file is not None:
            local_var_files.append((self.__downcase_first_letter('ImageFile'), request.image_file))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DocumentResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_insert_document_watermark_text(self, request, **kwargs):  # noqa: E501
        """Insert document watermark text.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param watermark_text WatermarkText : with the watermark data.             (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_insert_document_watermark_text_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_insert_document_watermark_text_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_insert_document_watermark_text_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_insert_document_watermark_text_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_insert_document_watermark_text_with_http_info(self, request, **kwargs):  # noqa: E501
        """Insert document watermark text.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PostInsertDocumentWatermarkTextRequest object with parameters
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_insert_document_watermark_text" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_insert_document_watermark_text`")  # noqa: E501
        # verify the required parameter 'watermark_text' is set
        if request.watermark_text is None:
            raise ValueError("Missing the required parameter `watermark_text` when calling `post_insert_document_watermark_text`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/watermark/insertText'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.watermark_text is not None:
            body_params = request.watermark_text
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DocumentResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_insert_page_numbers(self, request, **kwargs):  # noqa: E501
        """Insert document page numbers.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : A document name. (required)
        :param page_number PageNumber : with the page numbers settings. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_insert_page_numbers_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_insert_page_numbers_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_insert_page_numbers_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_insert_page_numbers_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_insert_page_numbers_with_http_info(self, request, **kwargs):  # noqa: E501
        """Insert document page numbers.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PostInsertPageNumbersRequest object with parameters
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_insert_page_numbers" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_insert_page_numbers`")  # noqa: E501
        # verify the required parameter 'page_number' is set
        if request.page_number is None:
            raise ValueError("Missing the required parameter `page_number` when calling `post_insert_page_numbers`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/insertPageNumbers'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.page_number is not None:
            body_params = request.page_number
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DocumentResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_load_web_document(self, request, **kwargs):  # noqa: E501
        """Loads new document from web into the file with any supported format of data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param data LoadWebDocumentData : Parameters of loading. (required)
        :param storage str : File storage, which have to be used.
        :return: SaveResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_load_web_document_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_load_web_document_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_load_web_document_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_load_web_document_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_load_web_document_with_http_info(self, request, **kwargs):  # noqa: E501
        """Loads new document from web into the file with any supported format of data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PostLoadWebDocumentRequest object with parameters
        :return: SaveResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_load_web_document" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data' is set
        if request.data is None:
            raise ValueError("Missing the required parameter `data` when calling `post_load_web_document`")  # noqa: E501

        collection_formats = {}
        path = '/words/loadWebDocument'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.data is not None:
            body_params = request.data
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SaveResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_replace_text(self, request, **kwargs):  # noqa: E501
        """Replace document text.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param replace_text ReplaceTextRequest : with the replace operation settings.             (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: ReplaceTextResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_replace_text_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_replace_text_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_replace_text_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_replace_text_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_replace_text_with_http_info(self, request, **kwargs):  # noqa: E501
        """Replace document text.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PostReplaceTextRequest object with parameters
        :return: ReplaceTextResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_replace_text" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_replace_text`")  # noqa: E501
        # verify the required parameter 'replace_text' is set
        if request.replace_text is None:
            raise ValueError("Missing the required parameter `replace_text` when calling `post_replace_text`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/replaceText'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.replace_text is not None:
            body_params = request.replace_text
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReplaceTextResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_run(self, request, **kwargs):  # noqa: E501
        """Updates run&#39;s properties, returns updated run&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param run Run : Run data. (required)
        :param paragraph_path str : Path to parent paragraph. (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: RunResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_run_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_run_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_run_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_run_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_run_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates run&#39;s properties, returns updated run&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PostRunRequest object with parameters
        :return: RunResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_run" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_run`")  # noqa: E501
        # verify the required parameter 'run' is set
        if request.run is None:
            raise ValueError("Missing the required parameter `run` when calling `post_run`")  # noqa: E501
        # verify the required parameter 'paragraph_path' is set
        if request.paragraph_path is None:
            raise ValueError("Missing the required parameter `paragraph_path` when calling `post_run`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `post_run`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{paragraphPath}/runs/{index}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.paragraph_path is not None:
            path_params[self.__downcase_first_letter('ParagraphPath')] = request.paragraph_path  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.run is not None:
            body_params = request.run
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RunResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_split_document(self, request, **kwargs):  # noqa: E501
        """Split document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : Original document name. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param format str : Format to split.
        :param _from int : Start page.
        :param to int : End page.
        :param zip_output bool : ZipOutput or not.
        :param fonts_location str : Folder in filestorage with custom fonts.
        :return: SplitDocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_split_document_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_split_document_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_split_document_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_split_document_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_split_document_with_http_info(self, request, **kwargs):  # noqa: E501
        """Split document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PostSplitDocumentRequest object with parameters
        :return: SplitDocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_split_document" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_split_document`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/split'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('Format') in path:
            path = path.replace('{' + self.__downcase_first_letter('Format' + '}'), request.format if request.format is not None else '')
        else:
            if request.format is not None:
                query_params.append((self.__downcase_first_letter('Format'), request.format))  # noqa: E501
        if self.__downcase_first_letter('From') in path:
            path = path.replace('{' + self.__downcase_first_letter('From' + '}'), request._from if request._from is not None else '')
        else:
            if request._from is not None:
                query_params.append((self.__downcase_first_letter('From'), request._from))  # noqa: E501
        if self.__downcase_first_letter('To') in path:
            path = path.replace('{' + self.__downcase_first_letter('To' + '}'), request.to if request.to is not None else '')
        else:
            if request.to is not None:
                query_params.append((self.__downcase_first_letter('To'), request.to))  # noqa: E501
        if self.__downcase_first_letter('ZipOutput') in path:
            path = path.replace('{' + self.__downcase_first_letter('ZipOutput' + '}'), request.zip_output if request.zip_output is not None else '')
        else:
            if request.zip_output is not None:
                query_params.append((self.__downcase_first_letter('ZipOutput'), request.zip_output))  # noqa: E501
        if self.__downcase_first_letter('FontsLocation') in path:
            path = path.replace('{' + self.__downcase_first_letter('FontsLocation' + '}'), request.fonts_location if request.fonts_location is not None else '')
        else:
            if request.fonts_location is not None:
                query_params.append((self.__downcase_first_letter('FontsLocation'), request.fonts_location))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SplitDocumentResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_update_document_bookmark(self, request, **kwargs):  # noqa: E501
        """Update document bookmark.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param bookmark_data BookmarkData : with new bookmark data.             (required)
        :param bookmark_name str : The bookmark name. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: BookmarkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_update_document_bookmark_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_update_document_bookmark_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_update_document_bookmark_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_update_document_bookmark_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_update_document_bookmark_with_http_info(self, request, **kwargs):  # noqa: E501
        """Update document bookmark.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PostUpdateDocumentBookmarkRequest object with parameters
        :return: BookmarkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_update_document_bookmark" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_update_document_bookmark`")  # noqa: E501
        # verify the required parameter 'bookmark_data' is set
        if request.bookmark_data is None:
            raise ValueError("Missing the required parameter `bookmark_data` when calling `post_update_document_bookmark`")  # noqa: E501
        # verify the required parameter 'bookmark_name' is set
        if request.bookmark_name is None:
            raise ValueError("Missing the required parameter `bookmark_name` when calling `post_update_document_bookmark`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/bookmarks/{bookmarkName}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.bookmark_name is not None:
            path_params[self.__downcase_first_letter('BookmarkName')] = request.bookmark_name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.bookmark_data is not None:
            body_params = request.bookmark_data
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BookmarkResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_update_document_fields(self, request, **kwargs):  # noqa: E501
        """Update (reevaluate) fields in document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_update_document_fields_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_update_document_fields_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_update_document_fields_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_update_document_fields_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_update_document_fields_with_http_info(self, request, **kwargs):  # noqa: E501
        """Update (reevaluate) fields in document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PostUpdateDocumentFieldsRequest object with parameters
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_update_document_fields" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_update_document_fields`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/updateFields'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DocumentResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_comment(self, request, **kwargs):  # noqa: E501
        """Adds comment to document, returns inserted comment&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param comment Comment : Comment data. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: CommentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_comment_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_comment_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_comment_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_comment_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_comment_with_http_info(self, request, **kwargs):  # noqa: E501
        """Adds comment to document, returns inserted comment&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PutCommentRequest object with parameters
        :return: CommentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_comment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `put_comment`")  # noqa: E501
        # verify the required parameter 'comment' is set
        if request.comment is None:
            raise ValueError("Missing the required parameter `comment` when calling `put_comment`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/comments'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.comment is not None:
            body_params = request.comment
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CommentResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_convert_document(self, request, **kwargs):  # noqa: E501
        """Convert document from request content to format specified.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param document file : Converting document (required)
        :param format str : Format to convert. (required)
        :param storage str : File storage, which have to be used.
        :param out_path str : Path for saving operation result to the local storage.
        :param document_file_name str : This file name will be used when resulting document has dynamic field for document file name {filename}. If it is not setted, \"sourceFilename\" will be used instead. 
        :param fonts_location str : Folder in filestorage with custom fonts.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_convert_document_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_convert_document_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_convert_document_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_convert_document_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_convert_document_with_http_info(self, request, **kwargs):  # noqa: E501
        """Convert document from request content to format specified.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PutConvertDocumentRequest object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_convert_document" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'document' is set
        if request.document is None:
            raise ValueError("Missing the required parameter `document` when calling `put_convert_document`")  # noqa: E501
        # verify the required parameter 'format' is set
        if request.format is None:
            raise ValueError("Missing the required parameter `format` when calling `put_convert_document`")  # noqa: E501

        collection_formats = {}
        path = '/words/convert'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('Format') in path:
            path = path.replace('{' + self.__downcase_first_letter('Format' + '}'), request.format if request.format is not None else '')
        else:
            if request.format is not None:
                query_params.append((self.__downcase_first_letter('Format'), request.format))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('OutPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('OutPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('OutPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('DocumentFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DocumentFileName' + '}'), request.document_file_name if request.document_file_name is not None else '')
        else:
            if request.document_file_name is not None:
                query_params.append((self.__downcase_first_letter('DocumentFileName'), request.document_file_name))  # noqa: E501
        if self.__downcase_first_letter('FontsLocation') in path:
            path = path.replace('{' + self.__downcase_first_letter('FontsLocation' + '}'), request.fonts_location if request.fonts_location is not None else '')
        else:
            if request.fonts_location is not None:
                query_params.append((self.__downcase_first_letter('FontsLocation'), request.fonts_location))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.document is not None:
            local_var_files.append((self.__downcase_first_letter('Document'), request.document))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_create_document(self, request, **kwargs):  # noqa: E501
        """Creates new document. Document is created with format which is recognized from file extensions.  Supported extentions: \&quot;.doc\&quot;, \&quot;.docx\&quot;, \&quot;.docm\&quot;, \&quot;.dot\&quot;, \&quot;.dotm\&quot;, \&quot;.dotx\&quot;, \&quot;.flatopc\&quot;, \&quot;.fopc\&quot;, \&quot;.flatopc_macro\&quot;, \&quot;.fopc_macro\&quot;, \&quot;.flatopc_template\&quot;, \&quot;.fopc_template\&quot;, \&quot;.flatopc_template_macro\&quot;, \&quot;.fopc_template_macro\&quot;, \&quot;.wordml\&quot;, \&quot;.wml\&quot;, \&quot;.rtf\&quot;  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param storage str : File storage, which have to be used.
        :param file_name str : The file name.
        :param folder str : The document folder.
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_create_document_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_create_document_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_create_document_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_create_document_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_create_document_with_http_info(self, request, **kwargs):  # noqa: E501
        """Creates new document. Document is created with format which is recognized from file extensions.  Supported extentions: \&quot;.doc\&quot;, \&quot;.docx\&quot;, \&quot;.docm\&quot;, \&quot;.dot\&quot;, \&quot;.dotm\&quot;, \&quot;.dotx\&quot;, \&quot;.flatopc\&quot;, \&quot;.fopc\&quot;, \&quot;.flatopc_macro\&quot;, \&quot;.fopc_macro\&quot;, \&quot;.flatopc_template\&quot;, \&quot;.fopc_template\&quot;, \&quot;.flatopc_template_macro\&quot;, \&quot;.fopc_template_macro\&quot;, \&quot;.wordml\&quot;, \&quot;.wml\&quot;, \&quot;.rtf\&quot;  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PutCreateDocumentRequest object with parameters
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_create_document" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}
        path = '/words/create'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('FileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('FileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('FileName'), request.file_name))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DocumentResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_document_field_names(self, request, **kwargs):  # noqa: E501
        """Read document field names.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param template file : File with template (required)
        :param use_non_merge_fields bool : Use non merge fields or not.
        :return: FieldNamesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_document_field_names_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_document_field_names_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_document_field_names_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_document_field_names_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_document_field_names_with_http_info(self, request, **kwargs):  # noqa: E501
        """Read document field names.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PutDocumentFieldNamesRequest object with parameters
        :return: FieldNamesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_document_field_names" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'template' is set
        if request.template is None:
            raise ValueError("Missing the required parameter `template` when calling `put_document_field_names`")  # noqa: E501

        collection_formats = {}
        path = '/words/mailMergeFieldNames'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('UseNonMergeFields') in path:
            path = path.replace('{' + self.__downcase_first_letter('UseNonMergeFields' + '}'), request.use_non_merge_fields if request.use_non_merge_fields is not None else '')
        else:
            if request.use_non_merge_fields is not None:
                query_params.append((self.__downcase_first_letter('UseNonMergeFields'), request.use_non_merge_fields))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.template is not None:
            local_var_files.append((self.__downcase_first_letter('Template'), request.template))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FieldNamesResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_document_save_as_tiff(self, request, **kwargs):  # noqa: E501
        """Convert document to tiff with detailed settings and save result to storage.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param save_options TiffSaveOptionsData : Tiff save options. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param result_file str : The resulting file name.
        :param use_anti_aliasing bool : Use antialiasing flag.
        :param use_high_quality_rendering bool : Use high quality flag.
        :param image_brightness float : Brightness for the generated images.
        :param image_color_mode str : Color mode for the generated images.
        :param image_contrast float : The contrast for the generated images.
        :param numeral_format str : The images numeral format.
        :param page_count int : Number of pages to render.
        :param page_index int : Page index to start rendering.
        :param paper_color str : Background image color.
        :param pixel_format str : The pixel format of generated images.
        :param resolution float : The resolution of generated images.
        :param scale float : Zoom factor for generated images.
        :param tiff_compression str : The compression tipe.
        :param dml_rendering_mode str : Optional, default is Fallback.
        :param dml_effects_rendering_mode str : Optional, default is Simplified.
        :param tiff_binarization_method str : Optional, Tiff binarization method, possible values are: FloydSteinbergDithering, Threshold.
        :param zip_output bool : Optional. A value determining zip output or not.
        :param fonts_location str : Folder in filestorage with custom fonts.
        :return: SaveResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_document_save_as_tiff_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_document_save_as_tiff_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_document_save_as_tiff_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_document_save_as_tiff_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_document_save_as_tiff_with_http_info(self, request, **kwargs):  # noqa: E501
        """Convert document to tiff with detailed settings and save result to storage.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PutDocumentSaveAsTiffRequest object with parameters
        :return: SaveResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_document_save_as_tiff" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `put_document_save_as_tiff`")  # noqa: E501
        # verify the required parameter 'save_options' is set
        if request.save_options is None:
            raise ValueError("Missing the required parameter `save_options` when calling `put_document_save_as_tiff`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/saveAs/tiff'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('ResultFile') in path:
            path = path.replace('{' + self.__downcase_first_letter('ResultFile' + '}'), request.result_file if request.result_file is not None else '')
        else:
            if request.result_file is not None:
                query_params.append((self.__downcase_first_letter('ResultFile'), request.result_file))  # noqa: E501
        if self.__downcase_first_letter('UseAntiAliasing') in path:
            path = path.replace('{' + self.__downcase_first_letter('UseAntiAliasing' + '}'), request.use_anti_aliasing if request.use_anti_aliasing is not None else '')
        else:
            if request.use_anti_aliasing is not None:
                query_params.append((self.__downcase_first_letter('UseAntiAliasing'), request.use_anti_aliasing))  # noqa: E501
        if self.__downcase_first_letter('UseHighQualityRendering') in path:
            path = path.replace('{' + self.__downcase_first_letter('UseHighQualityRendering' + '}'), request.use_high_quality_rendering if request.use_high_quality_rendering is not None else '')
        else:
            if request.use_high_quality_rendering is not None:
                query_params.append((self.__downcase_first_letter('UseHighQualityRendering'), request.use_high_quality_rendering))  # noqa: E501
        if self.__downcase_first_letter('ImageBrightness') in path:
            path = path.replace('{' + self.__downcase_first_letter('ImageBrightness' + '}'), request.image_brightness if request.image_brightness is not None else '')
        else:
            if request.image_brightness is not None:
                query_params.append((self.__downcase_first_letter('ImageBrightness'), request.image_brightness))  # noqa: E501
        if self.__downcase_first_letter('ImageColorMode') in path:
            path = path.replace('{' + self.__downcase_first_letter('ImageColorMode' + '}'), request.image_color_mode if request.image_color_mode is not None else '')
        else:
            if request.image_color_mode is not None:
                query_params.append((self.__downcase_first_letter('ImageColorMode'), request.image_color_mode))  # noqa: E501
        if self.__downcase_first_letter('ImageContrast') in path:
            path = path.replace('{' + self.__downcase_first_letter('ImageContrast' + '}'), request.image_contrast if request.image_contrast is not None else '')
        else:
            if request.image_contrast is not None:
                query_params.append((self.__downcase_first_letter('ImageContrast'), request.image_contrast))  # noqa: E501
        if self.__downcase_first_letter('NumeralFormat') in path:
            path = path.replace('{' + self.__downcase_first_letter('NumeralFormat' + '}'), request.numeral_format if request.numeral_format is not None else '')
        else:
            if request.numeral_format is not None:
                query_params.append((self.__downcase_first_letter('NumeralFormat'), request.numeral_format))  # noqa: E501
        if self.__downcase_first_letter('PageCount') in path:
            path = path.replace('{' + self.__downcase_first_letter('PageCount' + '}'), request.page_count if request.page_count is not None else '')
        else:
            if request.page_count is not None:
                query_params.append((self.__downcase_first_letter('PageCount'), request.page_count))  # noqa: E501
        if self.__downcase_first_letter('PageIndex') in path:
            path = path.replace('{' + self.__downcase_first_letter('PageIndex' + '}'), request.page_index if request.page_index is not None else '')
        else:
            if request.page_index is not None:
                query_params.append((self.__downcase_first_letter('PageIndex'), request.page_index))  # noqa: E501
        if self.__downcase_first_letter('PaperColor') in path:
            path = path.replace('{' + self.__downcase_first_letter('PaperColor' + '}'), request.paper_color if request.paper_color is not None else '')
        else:
            if request.paper_color is not None:
                query_params.append((self.__downcase_first_letter('PaperColor'), request.paper_color))  # noqa: E501
        if self.__downcase_first_letter('PixelFormat') in path:
            path = path.replace('{' + self.__downcase_first_letter('PixelFormat' + '}'), request.pixel_format if request.pixel_format is not None else '')
        else:
            if request.pixel_format is not None:
                query_params.append((self.__downcase_first_letter('PixelFormat'), request.pixel_format))  # noqa: E501
        if self.__downcase_first_letter('Resolution') in path:
            path = path.replace('{' + self.__downcase_first_letter('Resolution' + '}'), request.resolution if request.resolution is not None else '')
        else:
            if request.resolution is not None:
                query_params.append((self.__downcase_first_letter('Resolution'), request.resolution))  # noqa: E501
        if self.__downcase_first_letter('Scale') in path:
            path = path.replace('{' + self.__downcase_first_letter('Scale' + '}'), request.scale if request.scale is not None else '')
        else:
            if request.scale is not None:
                query_params.append((self.__downcase_first_letter('Scale'), request.scale))  # noqa: E501
        if self.__downcase_first_letter('TiffCompression') in path:
            path = path.replace('{' + self.__downcase_first_letter('TiffCompression' + '}'), request.tiff_compression if request.tiff_compression is not None else '')
        else:
            if request.tiff_compression is not None:
                query_params.append((self.__downcase_first_letter('TiffCompression'), request.tiff_compression))  # noqa: E501
        if self.__downcase_first_letter('DmlRenderingMode') in path:
            path = path.replace('{' + self.__downcase_first_letter('DmlRenderingMode' + '}'), request.dml_rendering_mode if request.dml_rendering_mode is not None else '')
        else:
            if request.dml_rendering_mode is not None:
                query_params.append((self.__downcase_first_letter('DmlRenderingMode'), request.dml_rendering_mode))  # noqa: E501
        if self.__downcase_first_letter('DmlEffectsRenderingMode') in path:
            path = path.replace('{' + self.__downcase_first_letter('DmlEffectsRenderingMode' + '}'), request.dml_effects_rendering_mode if request.dml_effects_rendering_mode is not None else '')
        else:
            if request.dml_effects_rendering_mode is not None:
                query_params.append((self.__downcase_first_letter('DmlEffectsRenderingMode'), request.dml_effects_rendering_mode))  # noqa: E501
        if self.__downcase_first_letter('TiffBinarizationMethod') in path:
            path = path.replace('{' + self.__downcase_first_letter('TiffBinarizationMethod' + '}'), request.tiff_binarization_method if request.tiff_binarization_method is not None else '')
        else:
            if request.tiff_binarization_method is not None:
                query_params.append((self.__downcase_first_letter('TiffBinarizationMethod'), request.tiff_binarization_method))  # noqa: E501
        if self.__downcase_first_letter('ZipOutput') in path:
            path = path.replace('{' + self.__downcase_first_letter('ZipOutput' + '}'), request.zip_output if request.zip_output is not None else '')
        else:
            if request.zip_output is not None:
                query_params.append((self.__downcase_first_letter('ZipOutput'), request.zip_output))  # noqa: E501
        if self.__downcase_first_letter('FontsLocation') in path:
            path = path.replace('{' + self.__downcase_first_letter('FontsLocation' + '}'), request.fonts_location if request.fonts_location is not None else '')
        else:
            if request.fonts_location is not None:
                query_params.append((self.__downcase_first_letter('FontsLocation'), request.fonts_location))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.save_options is not None:
            body_params = request.save_options
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SaveResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_drawing_object(self, request, **kwargs):  # noqa: E501
        """Adds  drawing object to document, returns added  drawing object&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param drawing_object str : Drawing object parameters (required)
        :param image_file file : File with image (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :param node_path str : Path to node, which contains collection of drawing objects.
        :return: DrawingObjectResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_drawing_object_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_drawing_object_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_drawing_object_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_drawing_object_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_drawing_object_with_http_info(self, request, **kwargs):  # noqa: E501
        """Adds  drawing object to document, returns added  drawing object&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PutDrawingObjectRequest object with parameters
        :return: DrawingObjectResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_drawing_object" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `put_drawing_object`")  # noqa: E501
        # verify the required parameter 'drawing_object' is set
        if request.drawing_object is None:
            raise ValueError("Missing the required parameter `drawing_object` when calling `put_drawing_object`")  # noqa: E501
        # verify the required parameter 'image_file' is set
        if request.image_file is None:
            raise ValueError("Missing the required parameter `image_file` when calling `put_drawing_object`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/drawingObjects'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if self.__downcase_first_letter('NodePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('NodePath' + '}'), request.node_path if request.node_path is not None else '')
        else:
            if request.node_path is not None:
                query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.drawing_object is not None:
            form_params.append((self.__downcase_first_letter('DrawingObject'), request.drawing_object))  # noqa: E501
        if request.image_file is not None:
            local_var_files.append((self.__downcase_first_letter('ImageFile'), request.image_file))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DrawingObjectResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_execute_mail_merge_online(self, request, **kwargs):  # noqa: E501
        """Execute document mail merge online.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param template file : File with template (required)
        :param data file : File with mailmerge data (required)
        :param with_regions bool : With regions flag.
        :param cleanup str : Clean up options.
        :param document_file_name str : This file name will be used when resulting document has dynamic field for document file name {filename}. If it is not setted, \"template\" will be used instead. 
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_execute_mail_merge_online_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_execute_mail_merge_online_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_execute_mail_merge_online_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_execute_mail_merge_online_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_execute_mail_merge_online_with_http_info(self, request, **kwargs):  # noqa: E501
        """Execute document mail merge online.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PutExecuteMailMergeOnlineRequest object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_execute_mail_merge_online" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'template' is set
        if request.template is None:
            raise ValueError("Missing the required parameter `template` when calling `put_execute_mail_merge_online`")  # noqa: E501
        # verify the required parameter 'data' is set
        if request.data is None:
            raise ValueError("Missing the required parameter `data` when calling `put_execute_mail_merge_online`")  # noqa: E501

        collection_formats = {}
        path = '/words/executeMailMerge'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('WithRegions') in path:
            path = path.replace('{' + self.__downcase_first_letter('WithRegions' + '}'), request.with_regions if request.with_regions is not None else '')
        else:
            if request.with_regions is not None:
                query_params.append((self.__downcase_first_letter('WithRegions'), request.with_regions))  # noqa: E501
        if self.__downcase_first_letter('Cleanup') in path:
            path = path.replace('{' + self.__downcase_first_letter('Cleanup' + '}'), request.cleanup if request.cleanup is not None else '')
        else:
            if request.cleanup is not None:
                query_params.append((self.__downcase_first_letter('Cleanup'), request.cleanup))  # noqa: E501
        if self.__downcase_first_letter('DocumentFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DocumentFileName' + '}'), request.document_file_name if request.document_file_name is not None else '')
        else:
            if request.document_file_name is not None:
                query_params.append((self.__downcase_first_letter('DocumentFileName'), request.document_file_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.template is not None:
            local_var_files.append((self.__downcase_first_letter('Template'), request.template))  # noqa: E501
        if request.data is not None:
            local_var_files.append((self.__downcase_first_letter('Data'), request.data))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_execute_template_online(self, request, **kwargs):  # noqa: E501
        """Populate document template with data online.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param template file : File with template (required)
        :param data file : File with mailmerge data (required)
        :param cleanup str : Clean up options.
        :param use_whole_paragraph_as_region bool : Gets or sets a value indicating whether paragraph with TableStart or              TableEnd field should be fully included into mail merge region or particular range between TableStart and TableEnd fields.              The default value is true.
        :param with_regions bool : Merge with regions or not. True by default
        :param document_file_name str : This file name will be used when resulting document has dynamic field for document file name {filename}.  If it is not setted, \"template\" will be used instead.  Note: if withRegions == true executeTemplate updates fields only inside regions
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_execute_template_online_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_execute_template_online_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_execute_template_online_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_execute_template_online_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_execute_template_online_with_http_info(self, request, **kwargs):  # noqa: E501
        """Populate document template with data online.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PutExecuteTemplateOnlineRequest object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_execute_template_online" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'template' is set
        if request.template is None:
            raise ValueError("Missing the required parameter `template` when calling `put_execute_template_online`")  # noqa: E501
        # verify the required parameter 'data' is set
        if request.data is None:
            raise ValueError("Missing the required parameter `data` when calling `put_execute_template_online`")  # noqa: E501

        collection_formats = {}
        path = '/words/executeTemplate'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('Cleanup') in path:
            path = path.replace('{' + self.__downcase_first_letter('Cleanup' + '}'), request.cleanup if request.cleanup is not None else '')
        else:
            if request.cleanup is not None:
                query_params.append((self.__downcase_first_letter('Cleanup'), request.cleanup))  # noqa: E501
        if self.__downcase_first_letter('UseWholeParagraphAsRegion') in path:
            path = path.replace('{' + self.__downcase_first_letter('UseWholeParagraphAsRegion' + '}'), request.use_whole_paragraph_as_region if request.use_whole_paragraph_as_region is not None else '')
        else:
            if request.use_whole_paragraph_as_region is not None:
                query_params.append((self.__downcase_first_letter('UseWholeParagraphAsRegion'), request.use_whole_paragraph_as_region))  # noqa: E501
        if self.__downcase_first_letter('WithRegions') in path:
            path = path.replace('{' + self.__downcase_first_letter('WithRegions' + '}'), request.with_regions if request.with_regions is not None else '')
        else:
            if request.with_regions is not None:
                query_params.append((self.__downcase_first_letter('WithRegions'), request.with_regions))  # noqa: E501
        if self.__downcase_first_letter('DocumentFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DocumentFileName' + '}'), request.document_file_name if request.document_file_name is not None else '')
        else:
            if request.document_file_name is not None:
                query_params.append((self.__downcase_first_letter('DocumentFileName'), request.document_file_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.template is not None:
            local_var_files.append((self.__downcase_first_letter('Template'), request.template))  # noqa: E501
        if request.data is not None:
            local_var_files.append((self.__downcase_first_letter('Data'), request.data))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_field(self, request, **kwargs):  # noqa: E501
        """Adds field to document, returns inserted field&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param field Field : Field data. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :param node_path str : Path to node, which contains collection of fields.
        :param insert_before_node str : Field will be inserted before node with id=\"nodeId\".
        :return: FieldResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_field_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_field_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_field_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_field_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_field_with_http_info(self, request, **kwargs):  # noqa: E501
        """Adds field to document, returns inserted field&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PutFieldRequest object with parameters
        :return: FieldResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_field" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `put_field`")  # noqa: E501
        # verify the required parameter 'field' is set
        if request.field is None:
            raise ValueError("Missing the required parameter `field` when calling `put_field`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/fields'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if self.__downcase_first_letter('NodePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('NodePath' + '}'), request.node_path if request.node_path is not None else '')
        else:
            if request.node_path is not None:
                query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501
        if self.__downcase_first_letter('InsertBeforeNode') in path:
            path = path.replace('{' + self.__downcase_first_letter('InsertBeforeNode' + '}'), request.insert_before_node if request.insert_before_node is not None else '')
        else:
            if request.insert_before_node is not None:
                query_params.append((self.__downcase_first_letter('InsertBeforeNode'), request.insert_before_node))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.field is not None:
            body_params = request.field
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FieldResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_footnote(self, request, **kwargs):  # noqa: E501
        """Adds footnote to document, returns added footnote&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param footnote_dto Footnote : Footnote data. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :param node_path str : Path to node, which contains collection of footnotes.
        :return: FootnoteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_footnote_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_footnote_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_footnote_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_footnote_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_footnote_with_http_info(self, request, **kwargs):  # noqa: E501
        """Adds footnote to document, returns added footnote&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PutFootnoteRequest object with parameters
        :return: FootnoteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_footnote" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `put_footnote`")  # noqa: E501
        # verify the required parameter 'footnote_dto' is set
        if request.footnote_dto is None:
            raise ValueError("Missing the required parameter `footnote_dto` when calling `put_footnote`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/footnotes'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if self.__downcase_first_letter('NodePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('NodePath' + '}'), request.node_path if request.node_path is not None else '')
        else:
            if request.node_path is not None:
                query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.footnote_dto is not None:
            body_params = request.footnote_dto
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FootnoteResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_form_field(self, request, **kwargs):  # noqa: E501
        """Adds form field to paragraph, returns added form field&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param form_field FormField : From field data. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :param node_path str : Path to node that contains collection of formfields.
        :param insert_before_node str : Form field will be inserted before node with index.
        :return: FormFieldResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_form_field_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_form_field_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_form_field_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_form_field_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_form_field_with_http_info(self, request, **kwargs):  # noqa: E501
        """Adds form field to paragraph, returns added form field&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PutFormFieldRequest object with parameters
        :return: FormFieldResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_form_field" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `put_form_field`")  # noqa: E501
        # verify the required parameter 'form_field' is set
        if request.form_field is None:
            raise ValueError("Missing the required parameter `form_field` when calling `put_form_field`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/formfields'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if self.__downcase_first_letter('NodePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('NodePath' + '}'), request.node_path if request.node_path is not None else '')
        else:
            if request.node_path is not None:
                query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501
        if self.__downcase_first_letter('InsertBeforeNode') in path:
            path = path.replace('{' + self.__downcase_first_letter('InsertBeforeNode' + '}'), request.insert_before_node if request.insert_before_node is not None else '')
        else:
            if request.insert_before_node is not None:
                query_params.append((self.__downcase_first_letter('InsertBeforeNode'), request.insert_before_node))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.form_field is not None:
            body_params = request.form_field
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FormFieldResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_header_footer(self, request, **kwargs):  # noqa: E501
        """Insert to document header or footer.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param header_footer_type str : Type of header/footer. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :param section_path str : Path to parent section.
        :return: HeaderFooterResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_header_footer_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_header_footer_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_header_footer_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_header_footer_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_header_footer_with_http_info(self, request, **kwargs):  # noqa: E501
        """Insert to document header or footer.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PutHeaderFooterRequest object with parameters
        :return: HeaderFooterResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_header_footer" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `put_header_footer`")  # noqa: E501
        # verify the required parameter 'header_footer_type' is set
        if request.header_footer_type is None:
            raise ValueError("Missing the required parameter `header_footer_type` when calling `put_header_footer`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{sectionPath}/headersfooters'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if self.__downcase_first_letter('SectionPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('SectionPath' + '}'), request.section_path if request.section_path is not None else '')
        else:
            if request.section_path is not None:
                query_params.append((self.__downcase_first_letter('SectionPath'), request.section_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.header_footer_type is not None:
            body_params = request.header_footer_type
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HeaderFooterResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_paragraph(self, request, **kwargs):  # noqa: E501
        """Adds paragraph to document, returns added paragraph&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param paragraph ParagraphInsert : Paragraph data. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :param node_path str : Path to node which contains paragraphs.
        :param insert_before_node str : Paragraph will be inserted before node with index.
        :return: ParagraphResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_paragraph_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_paragraph_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_paragraph_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_paragraph_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_paragraph_with_http_info(self, request, **kwargs):  # noqa: E501
        """Adds paragraph to document, returns added paragraph&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PutParagraphRequest object with parameters
        :return: ParagraphResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_paragraph" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `put_paragraph`")  # noqa: E501
        # verify the required parameter 'paragraph' is set
        if request.paragraph is None:
            raise ValueError("Missing the required parameter `paragraph` when calling `put_paragraph`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/paragraphs'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if self.__downcase_first_letter('NodePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('NodePath' + '}'), request.node_path if request.node_path is not None else '')
        else:
            if request.node_path is not None:
                query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501
        if self.__downcase_first_letter('InsertBeforeNode') in path:
            path = path.replace('{' + self.__downcase_first_letter('InsertBeforeNode' + '}'), request.insert_before_node if request.insert_before_node is not None else '')
        else:
            if request.insert_before_node is not None:
                query_params.append((self.__downcase_first_letter('InsertBeforeNode'), request.insert_before_node))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.paragraph is not None:
            body_params = request.paragraph
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ParagraphResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_protect_document(self, request, **kwargs):  # noqa: E501
        """Protect document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param protection_request ProtectionRequest : with protection settings.             (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :return: ProtectionDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_protect_document_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_protect_document_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_protect_document_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_protect_document_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_protect_document_with_http_info(self, request, **kwargs):  # noqa: E501
        """Protect document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PutProtectDocumentRequest object with parameters
        :return: ProtectionDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_protect_document" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `put_protect_document`")  # noqa: E501
        # verify the required parameter 'protection_request' is set
        if request.protection_request is None:
            raise ValueError("Missing the required parameter `protection_request` when calling `put_protect_document`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/protection'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.protection_request is not None:
            body_params = request.protection_request
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProtectionDataResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_run(self, request, **kwargs):  # noqa: E501
        """Adds run to document, returns added paragraph&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param paragraph_path str : Path to parent paragraph. (required)
        :param run Run : Run data. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :param insert_before_node str : Paragraph will be inserted before node with index.
        :return: RunResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_run_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_run_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_run_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_run_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_run_with_http_info(self, request, **kwargs):  # noqa: E501
        """Adds run to document, returns added paragraph&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PutRunRequest object with parameters
        :return: RunResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_run" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `put_run`")  # noqa: E501
        # verify the required parameter 'paragraph_path' is set
        if request.paragraph_path is None:
            raise ValueError("Missing the required parameter `paragraph_path` when calling `put_run`")  # noqa: E501
        # verify the required parameter 'run' is set
        if request.run is None:
            raise ValueError("Missing the required parameter `run` when calling `put_run`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{paragraphPath}/runs'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.paragraph_path is not None:
            path_params[self.__downcase_first_letter('ParagraphPath')] = request.paragraph_path  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if self.__downcase_first_letter('InsertBeforeNode') in path:
            path = path.replace('{' + self.__downcase_first_letter('InsertBeforeNode' + '}'), request.insert_before_node if request.insert_before_node is not None else '')
        else:
            if request.insert_before_node is not None:
                query_params.append((self.__downcase_first_letter('InsertBeforeNode'), request.insert_before_node))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.run is not None:
            body_params = request.run
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RunResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def reject_all_revisions(self, request, **kwargs):  # noqa: E501
        """Reject all revisions in document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :return: RevisionsModificationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.reject_all_revisions_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.reject_all_revisions_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.reject_all_revisions_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.reject_all_revisions_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def reject_all_revisions_with_http_info(self, request, **kwargs):  # noqa: E501
        """Reject all revisions in document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request RejectAllRevisionsRequest object with parameters
        :return: RevisionsModificationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reject_all_revisions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `reject_all_revisions`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/revisions/rejectAll'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RevisionsModificationResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def render_drawing_object(self, request, **kwargs):  # noqa: E501
        """Renders drawing object to specified format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The file name. (required)
        :param format str : The destination format. (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param node_path str : Path to node, which contains drawing objects.
        :param fonts_location str : Folder in filestorage with custom fonts.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.render_drawing_object_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.render_drawing_object_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.render_drawing_object_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.render_drawing_object_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def render_drawing_object_with_http_info(self, request, **kwargs):  # noqa: E501
        """Renders drawing object to specified format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request RenderDrawingObjectRequest object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method render_drawing_object" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `render_drawing_object`")  # noqa: E501
        # verify the required parameter 'format' is set
        if request.format is None:
            raise ValueError("Missing the required parameter `format` when calling `render_drawing_object`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `render_drawing_object`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/drawingObjects/{index}/render'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Format') in path:
            path = path.replace('{' + self.__downcase_first_letter('Format' + '}'), request.format if request.format is not None else '')
        else:
            if request.format is not None:
                query_params.append((self.__downcase_first_letter('Format'), request.format))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('NodePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('NodePath' + '}'), request.node_path if request.node_path is not None else '')
        else:
            if request.node_path is not None:
                query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501
        if self.__downcase_first_letter('FontsLocation') in path:
            path = path.replace('{' + self.__downcase_first_letter('FontsLocation' + '}'), request.fonts_location if request.fonts_location is not None else '')
        else:
            if request.fonts_location is not None:
                query_params.append((self.__downcase_first_letter('FontsLocation'), request.fonts_location))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def render_math_object(self, request, **kwargs):  # noqa: E501
        """Renders math object to specified format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The file name. (required)
        :param format str : The destination format. (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param node_path str : Path to node, which contains office math objects.
        :param fonts_location str : Folder in filestorage with custom fonts.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.render_math_object_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.render_math_object_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.render_math_object_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.render_math_object_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def render_math_object_with_http_info(self, request, **kwargs):  # noqa: E501
        """Renders math object to specified format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request RenderMathObjectRequest object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method render_math_object" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `render_math_object`")  # noqa: E501
        # verify the required parameter 'format' is set
        if request.format is None:
            raise ValueError("Missing the required parameter `format` when calling `render_math_object`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `render_math_object`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/OfficeMathObjects/{index}/render'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Format') in path:
            path = path.replace('{' + self.__downcase_first_letter('Format' + '}'), request.format if request.format is not None else '')
        else:
            if request.format is not None:
                query_params.append((self.__downcase_first_letter('Format'), request.format))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('NodePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('NodePath' + '}'), request.node_path if request.node_path is not None else '')
        else:
            if request.node_path is not None:
                query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501
        if self.__downcase_first_letter('FontsLocation') in path:
            path = path.replace('{' + self.__downcase_first_letter('FontsLocation' + '}'), request.fonts_location if request.fonts_location is not None else '')
        else:
            if request.fonts_location is not None:
                query_params.append((self.__downcase_first_letter('FontsLocation'), request.fonts_location))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def render_page(self, request, **kwargs):  # noqa: E501
        """Renders page to specified format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The file name. (required)
        :param page_index int : Comment index (required)
        :param format str : The destination format. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param fonts_location str : Folder in filestorage with custom fonts.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.render_page_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.render_page_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.render_page_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.render_page_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def render_page_with_http_info(self, request, **kwargs):  # noqa: E501
        """Renders page to specified format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request RenderPageRequest object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method render_page" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `render_page`")  # noqa: E501
        # verify the required parameter 'page_index' is set
        if request.page_index is None:
            raise ValueError("Missing the required parameter `page_index` when calling `render_page`")  # noqa: E501
        # verify the required parameter 'format' is set
        if request.format is None:
            raise ValueError("Missing the required parameter `format` when calling `render_page`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/pages/{pageIndex}/render'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.page_index is not None:
            path_params[self.__downcase_first_letter('PageIndex')] = request.page_index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Format') in path:
            path = path.replace('{' + self.__downcase_first_letter('Format' + '}'), request.format if request.format is not None else '')
        else:
            if request.format is not None:
                query_params.append((self.__downcase_first_letter('Format'), request.format))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('FontsLocation') in path:
            path = path.replace('{' + self.__downcase_first_letter('FontsLocation' + '}'), request.fonts_location if request.fonts_location is not None else '')
        else:
            if request.fonts_location is not None:
                query_params.append((self.__downcase_first_letter('FontsLocation'), request.fonts_location))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def render_paragraph(self, request, **kwargs):  # noqa: E501
        """Renders paragraph to specified format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The file name. (required)
        :param format str : The destination format. (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param node_path str : Path to node, which contains paragraphs.
        :param fonts_location str : Folder in filestorage with custom fonts.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.render_paragraph_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.render_paragraph_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.render_paragraph_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.render_paragraph_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def render_paragraph_with_http_info(self, request, **kwargs):  # noqa: E501
        """Renders paragraph to specified format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request RenderParagraphRequest object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method render_paragraph" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `render_paragraph`")  # noqa: E501
        # verify the required parameter 'format' is set
        if request.format is None:
            raise ValueError("Missing the required parameter `format` when calling `render_paragraph`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `render_paragraph`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/paragraphs/{index}/render'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Format') in path:
            path = path.replace('{' + self.__downcase_first_letter('Format' + '}'), request.format if request.format is not None else '')
        else:
            if request.format is not None:
                query_params.append((self.__downcase_first_letter('Format'), request.format))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('NodePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('NodePath' + '}'), request.node_path if request.node_path is not None else '')
        else:
            if request.node_path is not None:
                query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501
        if self.__downcase_first_letter('FontsLocation') in path:
            path = path.replace('{' + self.__downcase_first_letter('FontsLocation' + '}'), request.fonts_location if request.fonts_location is not None else '')
        else:
            if request.fonts_location is not None:
                query_params.append((self.__downcase_first_letter('FontsLocation'), request.fonts_location))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def render_table(self, request, **kwargs):  # noqa: E501
        """Renders table to specified format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The file name. (required)
        :param format str : The destination format. (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param node_path str : Path to node, which contains tables.
        :param fonts_location str : Folder in filestorage with custom fonts.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.render_table_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.render_table_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.render_table_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.render_table_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def render_table_with_http_info(self, request, **kwargs):  # noqa: E501
        """Renders table to specified format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request RenderTableRequest object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method render_table" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `render_table`")  # noqa: E501
        # verify the required parameter 'format' is set
        if request.format is None:
            raise ValueError("Missing the required parameter `format` when calling `render_table`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `render_table`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/tables/{index}/render'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Format') in path:
            path = path.replace('{' + self.__downcase_first_letter('Format' + '}'), request.format if request.format is not None else '')
        else:
            if request.format is not None:
                query_params.append((self.__downcase_first_letter('Format'), request.format))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('NodePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('NodePath' + '}'), request.node_path if request.node_path is not None else '')
        else:
            if request.node_path is not None:
                query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501
        if self.__downcase_first_letter('FontsLocation') in path:
            path = path.replace('{' + self.__downcase_first_letter('FontsLocation' + '}'), request.fonts_location if request.fonts_location is not None else '')
        else:
            if request.fonts_location is not None:
                query_params.append((self.__downcase_first_letter('FontsLocation'), request.fonts_location))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def reset_cache(self, request, **kwargs):  # noqa: E501
        """Resets font&#39;s cache.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.reset_cache_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.reset_cache_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.reset_cache_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.reset_cache_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def reset_cache_with_http_info(self, request, **kwargs):  # noqa: E501
        """Resets font&#39;s cache.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request ResetCacheRequest object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reset_cache" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}
        path = '/words/fonts/cache'
        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search(self, request, **kwargs):  # noqa: E501
        """Search text in document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param pattern str : The regular expression used to find matches. (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :return: SearchResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.search_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.search_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.search_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.search_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def search_with_http_info(self, request, **kwargs):  # noqa: E501
        """Search text in document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request SearchRequest object with parameters
        :return: SearchResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `search`")  # noqa: E501
        # verify the required parameter 'pattern' is set
        if request.pattern is None:
            raise ValueError("Missing the required parameter `pattern` when calling `search`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/search'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Pattern') in path:
            path = path.replace('{' + self.__downcase_first_letter('Pattern' + '}'), request.pattern if request.pattern is not None else '')
        else:
            if request.pattern is not None:
                query_params.append((self.__downcase_first_letter('Pattern'), request.pattern))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SearchResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_border(self, request, **kwargs):  # noqa: E501
        """Updates border properties.               # noqa: E501

        'nodePath' should refer to node with cell or row  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param border_properties Border : Border properties (required)
        :param node_path str : Path to node with border(node should be cell or row). (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: BorderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.update_border_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_border_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.update_border_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_border_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def update_border_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates border properties.               # noqa: E501

        'nodePath' should refer to node with cell or row  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request UpdateBorderRequest object with parameters
        :return: BorderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_border" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `update_border`")  # noqa: E501
        # verify the required parameter 'border_properties' is set
        if request.border_properties is None:
            raise ValueError("Missing the required parameter `border_properties` when calling `update_border`")  # noqa: E501
        # verify the required parameter 'node_path' is set
        if request.node_path is None:
            raise ValueError("Missing the required parameter `node_path` when calling `update_border`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `update_border`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/borders/{index}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.node_path is not None:
            path_params[self.__downcase_first_letter('NodePath')] = request.node_path  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.border_properties is not None:
            body_params = request.border_properties
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BorderResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_section_page_setup(self, request, **kwargs):  # noqa: E501
        """Update page setup of section.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param section_index int : Section index (required)
        :param page_setup PageSetup : Page setup properties dto (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: SectionPageSetupResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.update_section_page_setup_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_section_page_setup_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.update_section_page_setup_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_section_page_setup_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def update_section_page_setup_with_http_info(self, request, **kwargs):  # noqa: E501
        """Update page setup of section.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request UpdateSectionPageSetupRequest object with parameters
        :return: SectionPageSetupResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_section_page_setup" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `update_section_page_setup`")  # noqa: E501
        # verify the required parameter 'section_index' is set
        if request.section_index is None:
            raise ValueError("Missing the required parameter `section_index` when calling `update_section_page_setup`")  # noqa: E501
        # verify the required parameter 'page_setup' is set
        if request.page_setup is None:
            raise ValueError("Missing the required parameter `page_setup` when calling `update_section_page_setup`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/sections/{sectionIndex}/pageSetup'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.section_index is not None:
            path_params[self.__downcase_first_letter('SectionIndex')] = request.section_index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.page_setup is not None:
            body_params = request.page_setup
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SectionPageSetupResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_table_cell_format(self, request, **kwargs):  # noqa: E501
        """Updates a table cell format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param table_row_path str : Path to table row. (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :param format TableCellFormat : The properties.
        :return: TableCellFormatResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.update_table_cell_format_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_table_cell_format_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.update_table_cell_format_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_table_cell_format_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def update_table_cell_format_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates a table cell format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request UpdateTableCellFormatRequest object with parameters
        :return: TableCellFormatResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_table_cell_format" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `update_table_cell_format`")  # noqa: E501
        # verify the required parameter 'table_row_path' is set
        if request.table_row_path is None:
            raise ValueError("Missing the required parameter `table_row_path` when calling `update_table_cell_format`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `update_table_cell_format`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{tableRowPath}/cells/{index}/cellformat'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.table_row_path is not None:
            path_params[self.__downcase_first_letter('TableRowPath')] = request.table_row_path  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.format is not None:
            body_params = request.format
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TableCellFormatResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_table_properties(self, request, **kwargs):  # noqa: E501
        """Updates a table properties.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :param properties TableProperties : The properties.
        :param node_path str : Path to node, which contains tables.
        :return: TablePropertiesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.update_table_properties_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_table_properties_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.update_table_properties_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_table_properties_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def update_table_properties_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates a table properties.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request UpdateTablePropertiesRequest object with parameters
        :return: TablePropertiesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_table_properties" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `update_table_properties`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `update_table_properties`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{nodePath}/tables/{index}/properties'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if self.__downcase_first_letter('NodePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('NodePath' + '}'), request.node_path if request.node_path is not None else '')
        else:
            if request.node_path is not None:
                query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.properties is not None:
            body_params = request.properties
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TablePropertiesResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_table_row_format(self, request, **kwargs):  # noqa: E501
        """Updates a table row format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param table_path str : Path to table. (required)
        :param index int : Object's index (required)
        :param folder str : Original document folder.
        :param storage str : File storage, which have to be used.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :param format TableRowFormat : Table row format.
        :return: TableRowFormatResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.update_table_row_format_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_table_row_format_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.update_table_row_format_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_table_row_format_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def update_table_row_format_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates a table row format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request UpdateTableRowFormatRequest object with parameters
        :return: TableRowFormatResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_table_row_format" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `update_table_row_format`")  # noqa: E501
        # verify the required parameter 'table_path' is set
        if request.table_path is None:
            raise ValueError("Missing the required parameter `table_path` when calling `update_table_row_format`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `update_table_row_format`")  # noqa: E501

        collection_formats = {}
        path = '/words/{name}/{tablePath}/rows/{index}/rowformat'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.table_path is not None:
            path_params[self.__downcase_first_letter('TablePath')] = request.table_path  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('LoadEncoding') in path:
            path = path.replace('{' + self.__downcase_first_letter('LoadEncoding' + '}'), request.load_encoding if request.load_encoding is not None else '')
        else:
            if request.load_encoding is not None:
                query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DestFileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DestFileName' + '}'), request.dest_file_name if request.dest_file_name is not None else '')
        else:
            if request.dest_file_name is not None:
                query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if self.__downcase_first_letter('RevisionAuthor') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionAuthor' + '}'), request.revision_author if request.revision_author is not None else '')
        else:
            if request.revision_author is not None:
                query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if self.__downcase_first_letter('RevisionDateTime') in path:
            path = path.replace('{' + self.__downcase_first_letter('RevisionDateTime' + '}'), request.revision_date_time if request.revision_date_time is not None else '')
        else:
            if request.revision_date_time is not None:
                query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.format is not None:
            body_params = request.format
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TableRowFormatResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    # Helper method to convert first letter to downcase
    def __downcase_first_letter(self, s):
        if len(s) == 0:
            return s
        else:
            return s[0].lower() + s[1:]

    def __request_token(self):
        config = self.api_client.configuration
        api_version = config.api_version
        config.api_version = ''
        request_url = "oauth2/token"
        form_params = [('grant_type', 'client_credentials'), ('client_id', config.api_key['app_sid']),
                       ('client_secret', config.api_key['api_key'])]

        header_params = {'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}

        data = self.api_client.call_api(request_url, 'POST',
                                        {},
                                        [],
                                        header_params,
                                        post_params=form_params,
                                        response_type='object',
                                        files={}, _return_http_data_only=True)
        access_token = data['access_token'] if six.PY3 else data['access_token'].encode('utf8')
        refresh_token = data['refresh_token'] if six.PY3 else data['refresh_token'].encode('utf8')
        self.api_client.configuration.access_token = access_token
        self.api_client.configuration.api_version = api_version
        self.api_client.configuration.refresh_token = refresh_token

    
    # Refresh token method is going to be removed soon. Obsolete, do not use
    def __refresh_token(self):
        config = self.api_client.configuration
        api_version = config.api_version
        config.api_version = ''
        request_url = "oauth2/token"
        form_params = [('grant_type', 'refresh_token'), ('refresh_token', config.refresh_token)]

        header_params = {'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}

        data = self.api_client.call_api(request_url, 'POST',
                                        {},
                                        [],
                                        header_params,
                                        post_params=form_params,
                                        response_type='object',
                                        files={}, _return_http_data_only=True)
        access_token = data['access_token'] if six.PY3 else data['access_token'].encode('utf8')
        refresh_token = data['refresh_token'] if six.PY3 else data['refresh_token'].encode('utf8')
        self.api_client.configuration.access_token = access_token
        self.api_client.configuration.api_version = api_version
        self.api_client.configuration.refresh_token = refresh_token

