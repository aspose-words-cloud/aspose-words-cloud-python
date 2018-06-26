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

from wordspythonsdk.api_client import ApiClient


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
        asynchronous HTTP request, please pass async=True
        >>> thread = api.accept_all_revisions(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :return: RevisionsModificationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.accept_all_revisions_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.accept_all_revisions_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def accept_all_revisions_with_http_info(self, request, **kwargs):  # noqa: E501
        """Accept all revisions in document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.accept_all_revisions_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param accept_all_revisions_request request object with parameters
        :return: RevisionsModificationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/revisions/acceptAll', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RevisionsModificationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def classify(self, request, **kwargs):  # noqa: E501
        """Classify raw text.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.classify(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str text: Text to classify. (required)
        :param str best_classes_count: Count of the best classes to return.
        :return: ClassificationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.classify_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.classify_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def classify_with_http_info(self, request, **kwargs):  # noqa: E501
        """Classify raw text.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.classify_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param classify_request request object with parameters
        :return: ClassificationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}

        query_params = []
        if request.best_classes_count is not None:
            query_params.append((self.__downcase_first_letter('BestClassesCount'), request.best_classes_count))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/classify', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ClassificationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def classify_document(self, request, **kwargs):  # noqa: E501
        """Classify document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.classify_document(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str document_name: The document name. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str best_classes_count: Count of the best classes to return.
        :return: ClassificationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.classify_document_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.classify_document_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def classify_document_with_http_info(self, request, **kwargs):  # noqa: E501
        """Classify document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.classify_document_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param classify_document_request request object with parameters
        :return: ClassificationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.document_name is not None:
            path_params[self.__downcase_first_letter('DocumentName')] = request.document_name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.best_classes_count is not None:
            query_params.append((self.__downcase_first_letter('BestClassesCount'), request.best_classes_count))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{documentName}/classify', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ClassificationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_or_update_document_property(self, request, **kwargs):  # noqa: E501
        """Add new or update existing document property.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_or_update_document_property(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str property_name: The property name. (required)
        :param DocumentProperty _property: The property with new value. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :return: DocumentPropertyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_or_update_document_property_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.create_or_update_document_property_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def create_or_update_document_property_with_http_info(self, request, **kwargs):  # noqa: E501
        """Add new or update existing document property.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_or_update_document_property_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param create_or_update_document_property_request request object with parameters
        :return: DocumentPropertyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.property_name is not None:
            path_params[self.__downcase_first_letter('PropertyName')] = request.property_name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/documentProperties/{propertyName}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DocumentPropertyResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_border(self, request, **kwargs):  # noqa: E501
        """Resets border properties to default values.               # noqa: E501

        'nodePath' should refer to node with cell or row  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_border(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str node_path: Path to node with border(node should be cell or row). (required)
        :param int index: Object's index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :return: BorderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_border_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.delete_border_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def delete_border_with_http_info(self, request, **kwargs):  # noqa: E501
        """Resets border properties to default values.               # noqa: E501

        'nodePath' should refer to node with cell or row  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_border_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param delete_border_request request object with parameters
        :return: BorderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.node_path is not None:
            path_params[self.__downcase_first_letter('NodePath')] = request.node_path  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/borders/{index}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BorderResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_borders(self, request, **kwargs):  # noqa: E501
        """Resets borders properties to default values.               # noqa: E501

        'nodePath' should refer to node with cell or row  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_borders(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str node_path: Path to node with borders(node should be cell or row). (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :return: BordersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_borders_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.delete_borders_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def delete_borders_with_http_info(self, request, **kwargs):  # noqa: E501
        """Resets borders properties to default values.               # noqa: E501

        'nodePath' should refer to node with cell or row  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_borders_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param delete_borders_request request object with parameters
        :return: BordersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.node_path is not None:
            path_params[self.__downcase_first_letter('NodePath')] = request.node_path  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/borders', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BordersResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_comment(self, request, **kwargs):  # noqa: E501
        """Remove comment from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_comment(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The file name. (required)
        :param int comment_index: Comment index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_comment_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.delete_comment_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def delete_comment_with_http_info(self, request, **kwargs):  # noqa: E501
        """Remove comment from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_comment_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param delete_comment_request request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.comment_index is not None:
            path_params[self.__downcase_first_letter('CommentIndex')] = request.comment_index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/comments/{commentIndex}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_document_macros(self, request, **kwargs):  # noqa: E501
        """Remove macros from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_document_macros(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The file name. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_document_macros_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.delete_document_macros_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def delete_document_macros_with_http_info(self, request, **kwargs):  # noqa: E501
        """Remove macros from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_document_macros_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param delete_document_macros_request request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/macros', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_document_property(self, request, **kwargs):  # noqa: E501
        """Delete document property.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_document_property(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str property_name: The property name. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_document_property_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.delete_document_property_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def delete_document_property_with_http_info(self, request, **kwargs):  # noqa: E501
        """Delete document property.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_document_property_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param delete_document_property_request request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.property_name is not None:
            path_params[self.__downcase_first_letter('PropertyName')] = request.property_name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/documentProperties/{propertyName}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_document_watermark(self, request, **kwargs):  # noqa: E501
        """Delete watermark (for deleting last watermark from the document).  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_document_watermark(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_document_watermark_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.delete_document_watermark_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def delete_document_watermark_with_http_info(self, request, **kwargs):  # noqa: E501
        """Delete watermark (for deleting last watermark from the document).  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_document_watermark_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param delete_document_watermark_request request object with parameters
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/watermark', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DocumentResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_drawing_object(self, request, **kwargs):  # noqa: E501
        """Removes drawing object from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_drawing_object(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The file name. (required)
        :param int index: Object's index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :param str node_path: Path to node, which contains collection of drawing objects.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_drawing_object_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.delete_drawing_object_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def delete_drawing_object_with_http_info(self, request, **kwargs):  # noqa: E501
        """Removes drawing object from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_drawing_object_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param delete_drawing_object_request request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if request.node_path is not None:
            query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/drawingObjects/{index}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_field(self, request, **kwargs):  # noqa: E501
        """Delete field from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_field(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The file name. (required)
        :param int index: Object's index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :param str node_path: Path to node, which contains collection of fields.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_field_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.delete_field_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def delete_field_with_http_info(self, request, **kwargs):  # noqa: E501
        """Delete field from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_field_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param delete_field_request request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if request.node_path is not None:
            query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/fields/{index}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_fields(self, request, **kwargs):  # noqa: E501
        """Remove fields from section paragraph.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_fields(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The file name. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :param str node_path: Path to node, which contains collection of fields.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_fields_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.delete_fields_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def delete_fields_with_http_info(self, request, **kwargs):  # noqa: E501
        """Remove fields from section paragraph.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_fields_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param delete_fields_request request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if request.node_path is not None:
            query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/fields', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_footnote(self, request, **kwargs):  # noqa: E501
        """Removes footnote from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_footnote(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The file name. (required)
        :param int index: Object's index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :param str node_path: Path to node, which contains collection of footnotes.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_footnote_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.delete_footnote_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def delete_footnote_with_http_info(self, request, **kwargs):  # noqa: E501
        """Removes footnote from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_footnote_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param delete_footnote_request request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if request.node_path is not None:
            query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/footnotes/{index}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_form_field(self, request, **kwargs):  # noqa: E501
        """Removes form field from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_form_field(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param int index: Object's index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :param str node_path: Path to node that contains collection of formfields.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_form_field_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.delete_form_field_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def delete_form_field_with_http_info(self, request, **kwargs):  # noqa: E501
        """Removes form field from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_form_field_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param delete_form_field_request request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if request.node_path is not None:
            query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/formfields/{index}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_header_footer(self, request, **kwargs):  # noqa: E501
        """Delete header/footer from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_header_footer(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param int index: Object's index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :param str section_path: Path to parent section.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_header_footer_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.delete_header_footer_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def delete_header_footer_with_http_info(self, request, **kwargs):  # noqa: E501
        """Delete header/footer from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_header_footer_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param delete_header_footer_request request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if request.section_path is not None:
            query_params.append((self.__downcase_first_letter('SectionPath'), request.section_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{sectionPath}/headersfooters/{index}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_headers_footers(self, request, **kwargs):  # noqa: E501
        """Delete document headers and footers.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_headers_footers(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :param str section_path: Path to parent section.
        :param str headers_footers_types: List of types of headers and footers.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_headers_footers_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.delete_headers_footers_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def delete_headers_footers_with_http_info(self, request, **kwargs):  # noqa: E501
        """Delete document headers and footers.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_headers_footers_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param delete_headers_footers_request request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if request.section_path is not None:
            query_params.append((self.__downcase_first_letter('SectionPath'), request.section_path))  # noqa: E501
        if request.headers_footers_types is not None:
            query_params.append((self.__downcase_first_letter('HeadersFootersTypes'), request.headers_footers_types))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{sectionPath}/headersfooters', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_office_math_object(self, request, **kwargs):  # noqa: E501
        """Removes OfficeMath object from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_office_math_object(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The file name. (required)
        :param int index: Object's index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :param str node_path: Path to node, which contains collection of OfficeMath objects.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_office_math_object_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.delete_office_math_object_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def delete_office_math_object_with_http_info(self, request, **kwargs):  # noqa: E501
        """Removes OfficeMath object from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_office_math_object_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param delete_office_math_object_request request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if request.node_path is not None:
            query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/OfficeMathObjects/{index}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_paragraph(self, request, **kwargs):  # noqa: E501
        """Remove paragraph from section.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_paragraph(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The file name. (required)
        :param int index: Object's index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :param str node_path: Path to node which contains paragraphs.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_paragraph_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.delete_paragraph_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def delete_paragraph_with_http_info(self, request, **kwargs):  # noqa: E501
        """Remove paragraph from section.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_paragraph_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param delete_paragraph_request request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if request.node_path is not None:
            query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/paragraphs/{index}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_run(self, request, **kwargs):  # noqa: E501
        """Removes run from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_run(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The file name. (required)
        :param str paragraph_path: Path to parent paragraph. (required)
        :param int index: Object's index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_run_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.delete_run_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def delete_run_with_http_info(self, request, **kwargs):  # noqa: E501
        """Removes run from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_run_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param delete_run_request request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.paragraph_path is not None:
            path_params[self.__downcase_first_letter('ParagraphPath')] = request.paragraph_path  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{paragraphPath}/runs/{index}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_table(self, request, **kwargs):  # noqa: E501
        """Delete a table.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_table(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param int index: Object's index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :param str node_path: Path to node, which contains tables.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_table_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.delete_table_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def delete_table_with_http_info(self, request, **kwargs):  # noqa: E501
        """Delete a table.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_table_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param delete_table_request request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if request.node_path is not None:
            query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/tables/{index}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_table_cell(self, request, **kwargs):  # noqa: E501
        """Delete a table cell.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_table_cell(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str table_row_path: Path to table row. (required)
        :param int index: Object's index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_table_cell_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.delete_table_cell_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def delete_table_cell_with_http_info(self, request, **kwargs):  # noqa: E501
        """Delete a table cell.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_table_cell_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param delete_table_cell_request request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.table_row_path is not None:
            path_params[self.__downcase_first_letter('TableRowPath')] = request.table_row_path  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{tableRowPath}/cells/{index}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_table_row(self, request, **kwargs):  # noqa: E501
        """Delete a table row.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_table_row(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str table_path: Path to table. (required)
        :param int index: Object's index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_table_row_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.delete_table_row_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def delete_table_row_with_http_info(self, request, **kwargs):  # noqa: E501
        """Delete a table row.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_table_row_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param delete_table_row_request request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.table_path is not None:
            path_params[self.__downcase_first_letter('TablePath')] = request.table_path  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{tablePath}/rows/{index}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_unprotect_document(self, request, **kwargs):  # noqa: E501
        """Unprotect document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_unprotect_document(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param ProtectionRequest protection_request: with protection settings.             (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :return: ProtectionDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_unprotect_document_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.delete_unprotect_document_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def delete_unprotect_document_with_http_info(self, request, **kwargs):  # noqa: E501
        """Unprotect document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_unprotect_document_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param delete_unprotect_document_request request object with parameters
        :return: ProtectionDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/protection', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProtectionDataResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_border(self, request, **kwargs):  # noqa: E501
        """Return a border.  # noqa: E501

        'nodePath' should refer to node with cell or row  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_border(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str node_path: Path to node with border(node should be cell or row). (required)
        :param int index: Object's index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :return: BorderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_border_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_border_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_border_with_http_info(self, request, **kwargs):  # noqa: E501
        """Return a border.  # noqa: E501

        'nodePath' should refer to node with cell or row  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_border_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_border_request request object with parameters
        :return: BorderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.node_path is not None:
            path_params[self.__downcase_first_letter('NodePath')] = request.node_path  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/borders/{index}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BorderResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_borders(self, request, **kwargs):  # noqa: E501
        """Return a collection of borders.  # noqa: E501

        'nodePath' should refer to node with cell or row  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_borders(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str node_path: Path to node with borders(node should be cell or row). (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :return: BordersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_borders_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_borders_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_borders_with_http_info(self, request, **kwargs):  # noqa: E501
        """Return a collection of borders.  # noqa: E501

        'nodePath' should refer to node with cell or row  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_borders_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_borders_request request object with parameters
        :return: BordersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.node_path is not None:
            path_params[self.__downcase_first_letter('NodePath')] = request.node_path  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/borders', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BordersResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_comment(self, request, **kwargs):  # noqa: E501
        """Get comment from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_comment(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The file name. (required)
        :param int comment_index: Comment index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :return: CommentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_comment_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_comment_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_comment_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get comment from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_comment_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_comment_request request object with parameters
        :return: CommentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.comment_index is not None:
            path_params[self.__downcase_first_letter('CommentIndex')] = request.comment_index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/comments/{commentIndex}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CommentResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_comments(self, request, **kwargs):  # noqa: E501
        """Get comments from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_comments(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The file name. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :return: CommentsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_comments_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_comments_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_comments_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get comments from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_comments_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_comments_request request object with parameters
        :return: CommentsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/comments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CommentsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document(self, request, **kwargs):  # noqa: E501
        """Read document common info.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_document(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str document_name: The file name. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_document_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_document_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_document_with_http_info(self, request, **kwargs):  # noqa: E501
        """Read document common info.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_document_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_document_request request object with parameters
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.document_name is not None:
            path_params[self.__downcase_first_letter('DocumentName')] = request.document_name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{documentName}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DocumentResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_bookmark_by_name(self, request, **kwargs):  # noqa: E501
        """Read document bookmark data by its name.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_document_bookmark_by_name(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str bookmark_name: The bookmark name. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :return: BookmarkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_document_bookmark_by_name_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_document_bookmark_by_name_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_document_bookmark_by_name_with_http_info(self, request, **kwargs):  # noqa: E501
        """Read document bookmark data by its name.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_document_bookmark_by_name_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_document_bookmark_by_name_request request object with parameters
        :return: BookmarkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.bookmark_name is not None:
            path_params[self.__downcase_first_letter('BookmarkName')] = request.bookmark_name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/bookmarks/{bookmarkName}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BookmarkResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_bookmarks(self, request, **kwargs):  # noqa: E501
        """Read document bookmarks common info.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_document_bookmarks(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :return: BookmarksResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_document_bookmarks_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_document_bookmarks_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_document_bookmarks_with_http_info(self, request, **kwargs):  # noqa: E501
        """Read document bookmarks common info.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_document_bookmarks_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_document_bookmarks_request request object with parameters
        :return: BookmarksResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/bookmarks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BookmarksResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_drawing_object_by_index(self, request, **kwargs):  # noqa: E501
        """Read document drawing object common info by its index or convert to format specified.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_document_drawing_object_by_index(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param int index: Object's index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str node_path: Path to node, which contains collection of drawing objects.
        :return: DrawingObjectResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_document_drawing_object_by_index_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_document_drawing_object_by_index_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_document_drawing_object_by_index_with_http_info(self, request, **kwargs):  # noqa: E501
        """Read document drawing object common info by its index or convert to format specified.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_document_drawing_object_by_index_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_document_drawing_object_by_index_request request object with parameters
        :return: DrawingObjectResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.node_path is not None:
            query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/drawingObjects/{index}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DrawingObjectResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_drawing_object_image_data(self, request, **kwargs):  # noqa: E501
        """Read drawing object image data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_document_drawing_object_image_data(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param int index: Object's index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str node_path: Path to node, which contains collection of drawing objects.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_document_drawing_object_image_data_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_document_drawing_object_image_data_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_document_drawing_object_image_data_with_http_info(self, request, **kwargs):  # noqa: E501
        """Read drawing object image data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_document_drawing_object_image_data_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_document_drawing_object_image_data_request request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.node_path is not None:
            query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/drawingObjects/{index}/imageData', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_drawing_object_ole_data(self, request, **kwargs):  # noqa: E501
        """Get drawing object OLE data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_document_drawing_object_ole_data(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param int index: Object's index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str node_path: Path to node, which contains collection of drawing objects.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_document_drawing_object_ole_data_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_document_drawing_object_ole_data_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_document_drawing_object_ole_data_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get drawing object OLE data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_document_drawing_object_ole_data_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_document_drawing_object_ole_data_request request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.node_path is not None:
            query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/drawingObjects/{index}/oleData', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_drawing_objects(self, request, **kwargs):  # noqa: E501
        """Read document drawing objects common info.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_document_drawing_objects(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str node_path: Path to node, which contains collection of drawing objects.
        :return: DrawingObjectsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_document_drawing_objects_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_document_drawing_objects_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_document_drawing_objects_with_http_info(self, request, **kwargs):  # noqa: E501
        """Read document drawing objects common info.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_document_drawing_objects_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_document_drawing_objects_request request object with parameters
        :return: DrawingObjectsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.node_path is not None:
            query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/drawingObjects', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DrawingObjectsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_field_names(self, request, **kwargs):  # noqa: E501
        """Read document field names.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_document_field_names(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param bool use_non_merge_fields: If true, result includes \"mustache\" field names.
        :return: FieldNamesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_document_field_names_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_document_field_names_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_document_field_names_with_http_info(self, request, **kwargs):  # noqa: E501
        """Read document field names.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_document_field_names_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_document_field_names_request request object with parameters
        :return: FieldNamesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.use_non_merge_fields is not None:
            query_params.append((self.__downcase_first_letter('UseNonMergeFields'), request.use_non_merge_fields))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/mailMergeFieldNames', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FieldNamesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_hyperlink_by_index(self, request, **kwargs):  # noqa: E501
        """Read document hyperlink by its index.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_document_hyperlink_by_index(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param int hyperlink_index: The hyperlink index. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :return: HyperlinkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_document_hyperlink_by_index_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_document_hyperlink_by_index_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_document_hyperlink_by_index_with_http_info(self, request, **kwargs):  # noqa: E501
        """Read document hyperlink by its index.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_document_hyperlink_by_index_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_document_hyperlink_by_index_request request object with parameters
        :return: HyperlinkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.hyperlink_index is not None:
            path_params[self.__downcase_first_letter('HyperlinkIndex')] = request.hyperlink_index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/hyperlinks/{hyperlinkIndex}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HyperlinkResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_hyperlinks(self, request, **kwargs):  # noqa: E501
        """Read document hyperlinks common info.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_document_hyperlinks(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :return: HyperlinksResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_document_hyperlinks_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_document_hyperlinks_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_document_hyperlinks_with_http_info(self, request, **kwargs):  # noqa: E501
        """Read document hyperlinks common info.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_document_hyperlinks_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_document_hyperlinks_request request object with parameters
        :return: HyperlinksResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/hyperlinks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HyperlinksResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_paragraph(self, request, **kwargs):  # noqa: E501
        """This resource represents one of the paragraphs contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_document_paragraph(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param int index: Object's index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str node_path: Path to node which contains paragraphs.
        :return: ParagraphResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_document_paragraph_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_document_paragraph_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_document_paragraph_with_http_info(self, request, **kwargs):  # noqa: E501
        """This resource represents one of the paragraphs contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_document_paragraph_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_document_paragraph_request request object with parameters
        :return: ParagraphResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.node_path is not None:
            query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/paragraphs/{index}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ParagraphResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_paragraph_run(self, request, **kwargs):  # noqa: E501
        """This resource represents run of text contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_document_paragraph_run(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str paragraph_path: Path to parent paragraph. (required)
        :param int index: Object's index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :return: RunResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_document_paragraph_run_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_document_paragraph_run_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_document_paragraph_run_with_http_info(self, request, **kwargs):  # noqa: E501
        """This resource represents run of text contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_document_paragraph_run_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_document_paragraph_run_request request object with parameters
        :return: RunResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.paragraph_path is not None:
            path_params[self.__downcase_first_letter('ParagraphPath')] = request.paragraph_path  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{paragraphPath}/runs/{index}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RunResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_paragraph_run_font(self, request, **kwargs):  # noqa: E501
        """This resource represents font of run.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_document_paragraph_run_font(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str paragraph_path: Path to parent paragraph. (required)
        :param int index: Object's index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :return: FontResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_document_paragraph_run_font_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_document_paragraph_run_font_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_document_paragraph_run_font_with_http_info(self, request, **kwargs):  # noqa: E501
        """This resource represents font of run.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_document_paragraph_run_font_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_document_paragraph_run_font_request request object with parameters
        :return: FontResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.paragraph_path is not None:
            path_params[self.__downcase_first_letter('ParagraphPath')] = request.paragraph_path  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{paragraphPath}/runs/{index}/font', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FontResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_paragraph_runs(self, request, **kwargs):  # noqa: E501
        """This resource represents collection of runs in the paragraph.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_document_paragraph_runs(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str paragraph_path: Path to parent paragraph. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :return: RunsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_document_paragraph_runs_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_document_paragraph_runs_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_document_paragraph_runs_with_http_info(self, request, **kwargs):  # noqa: E501
        """This resource represents collection of runs in the paragraph.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_document_paragraph_runs_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_document_paragraph_runs_request request object with parameters
        :return: RunsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.paragraph_path is not None:
            path_params[self.__downcase_first_letter('ParagraphPath')] = request.paragraph_path  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{paragraphPath}/runs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RunsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_paragraphs(self, request, **kwargs):  # noqa: E501
        """Return a list of paragraphs that are contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_document_paragraphs(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str node_path: Path to node which contains paragraphs.
        :return: ParagraphLinkCollectionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_document_paragraphs_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_document_paragraphs_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_document_paragraphs_with_http_info(self, request, **kwargs):  # noqa: E501
        """Return a list of paragraphs that are contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_document_paragraphs_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_document_paragraphs_request request object with parameters
        :return: ParagraphLinkCollectionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.node_path is not None:
            query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/paragraphs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ParagraphLinkCollectionResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_properties(self, request, **kwargs):  # noqa: E501
        """Read document properties info.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_document_properties(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document's name. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :return: DocumentPropertiesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_document_properties_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_document_properties_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_document_properties_with_http_info(self, request, **kwargs):  # noqa: E501
        """Read document properties info.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_document_properties_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_document_properties_request request object with parameters
        :return: DocumentPropertiesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/documentProperties', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DocumentPropertiesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_property(self, request, **kwargs):  # noqa: E501
        """Read document property info by the property name.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_document_property(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str property_name: The property name. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :return: DocumentPropertyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_document_property_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_document_property_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_document_property_with_http_info(self, request, **kwargs):  # noqa: E501
        """Read document property info by the property name.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_document_property_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_document_property_request request object with parameters
        :return: DocumentPropertyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.property_name is not None:
            path_params[self.__downcase_first_letter('PropertyName')] = request.property_name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/documentProperties/{propertyName}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DocumentPropertyResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_protection(self, request, **kwargs):  # noqa: E501
        """Read document protection common info.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_document_protection(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :return: ProtectionDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_document_protection_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_document_protection_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_document_protection_with_http_info(self, request, **kwargs):  # noqa: E501
        """Read document protection common info.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_document_protection_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_document_protection_request request object with parameters
        :return: ProtectionDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/protection', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProtectionDataResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_statistics(self, request, **kwargs):  # noqa: E501
        """Read document statistics.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_document_statistics(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param bool include_comments: Support including/excluding comments from the WordCount. Default value is \"true\".
        :param bool include_footnotes: Support including/excluding footnotes from the WordCount. Default value is \"false\".
        :param bool include_text_in_shapes: Support including/excluding shape's text from the WordCount. Default value is \"false\"
        :return: StatDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_document_statistics_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_document_statistics_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_document_statistics_with_http_info(self, request, **kwargs):  # noqa: E501
        """Read document statistics.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_document_statistics_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_document_statistics_request request object with parameters
        :return: StatDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.include_comments is not None:
            query_params.append((self.__downcase_first_letter('IncludeComments'), request.include_comments))  # noqa: E501
        if request.include_footnotes is not None:
            query_params.append((self.__downcase_first_letter('IncludeFootnotes'), request.include_footnotes))  # noqa: E501
        if request.include_text_in_shapes is not None:
            query_params.append((self.__downcase_first_letter('IncludeTextInShapes'), request.include_text_in_shapes))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/statistics', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StatDataResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_text_items(self, request, **kwargs):  # noqa: E501
        """Read document text items.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_document_text_items(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :return: TextItemsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_document_text_items_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_document_text_items_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_document_text_items_with_http_info(self, request, **kwargs):  # noqa: E501
        """Read document text items.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_document_text_items_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_document_text_items_request request object with parameters
        :return: TextItemsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/textItems', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TextItemsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_with_format(self, request, **kwargs):  # noqa: E501
        """Export the document into the specified format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_document_with_format(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The file name. (required)
        :param str format: The destination format. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str out_path: Path to save result
        :param str fonts_location: Folder in filestorage with custom fonts.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_document_with_format_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_document_with_format_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_document_with_format_with_http_info(self, request, **kwargs):  # noqa: E501
        """Export the document into the specified format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_document_with_format_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_document_with_format_request request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.format is not None:
            query_params.append((self.__downcase_first_letter('Format'), request.format))  # noqa: E501
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.out_path is not None:
            query_params.append((self.__downcase_first_letter('OutPath'), request.out_path))  # noqa: E501
        if request.fonts_location is not None:
            query_params.append((self.__downcase_first_letter('FontsLocation'), request.fonts_location))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_field(self, request, **kwargs):  # noqa: E501
        """Get field from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_field(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The file name. (required)
        :param int index: Object's index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str node_path: Path to node, which contains collection of fields.
        :return: FieldResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_field_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_field_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_field_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get field from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_field_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_field_request request object with parameters
        :return: FieldResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.node_path is not None:
            query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/fields/{index}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FieldResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_fields(self, request, **kwargs):  # noqa: E501
        """Get fields from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_fields(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The file name. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str node_path: Path to node, which contains collection of fields.
        :return: FieldsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_fields_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_fields_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_fields_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get fields from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_fields_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_fields_request request object with parameters
        :return: FieldsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.node_path is not None:
            query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/fields', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FieldsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_footnote(self, request, **kwargs):  # noqa: E501
        """Read footnote by index.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_footnote(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param int index: Object's index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str node_path: Path to node, which contains collection of footnotes.
        :return: FootnoteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_footnote_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_footnote_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_footnote_with_http_info(self, request, **kwargs):  # noqa: E501
        """Read footnote by index.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_footnote_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_footnote_request request object with parameters
        :return: FootnoteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.node_path is not None:
            query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/footnotes/{index}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FootnoteResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_footnotes(self, request, **kwargs):  # noqa: E501
        """Get footnotes from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_footnotes(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The file name. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str node_path: Path to node, which contains collection of footnotes.
        :return: FootnotesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_footnotes_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_footnotes_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_footnotes_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get footnotes from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_footnotes_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_footnotes_request request object with parameters
        :return: FootnotesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.node_path is not None:
            query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/footnotes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FootnotesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_form_field(self, request, **kwargs):  # noqa: E501
        """Returns representation of an one of the form field.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_form_field(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param int index: Object's index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str node_path: Path to node that contains collection of formfields.
        :return: FormFieldResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_form_field_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_form_field_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_form_field_with_http_info(self, request, **kwargs):  # noqa: E501
        """Returns representation of an one of the form field.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_form_field_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_form_field_request request object with parameters
        :return: FormFieldResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.node_path is not None:
            query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/formfields/{index}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FormFieldResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_form_fields(self, request, **kwargs):  # noqa: E501
        """Get form fields from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_form_fields(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The file name. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str node_path: Path to node containing collection of form fields.
        :return: FormFieldsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_form_fields_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_form_fields_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_form_fields_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get form fields from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_form_fields_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_form_fields_request request object with parameters
        :return: FormFieldsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.node_path is not None:
            query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/formfields', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FormFieldsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_header_footer(self, request, **kwargs):  # noqa: E501
        """Return a header/footer that is contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_header_footer(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param int header_footer_index: Header/footer index. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str filter_by_type: List of types of headers and footers.
        :return: HeaderFooterResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_header_footer_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_header_footer_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_header_footer_with_http_info(self, request, **kwargs):  # noqa: E501
        """Return a header/footer that is contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_header_footer_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_header_footer_request request object with parameters
        :return: HeaderFooterResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.header_footer_index is not None:
            path_params[self.__downcase_first_letter('HeaderFooterIndex')] = request.header_footer_index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.filter_by_type is not None:
            query_params.append((self.__downcase_first_letter('FilterByType'), request.filter_by_type))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/headersfooters/{headerFooterIndex}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HeaderFooterResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_header_footer_of_section(self, request, **kwargs):  # noqa: E501
        """Return a header/footer that is contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_header_footer_of_section(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param int header_footer_index: Header/footer index. (required)
        :param int section_index: Section index. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str filter_by_type: List of types of headers and footers.
        :return: HeaderFooterResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_header_footer_of_section_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_header_footer_of_section_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_header_footer_of_section_with_http_info(self, request, **kwargs):  # noqa: E501
        """Return a header/footer that is contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_header_footer_of_section_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_header_footer_of_section_request request object with parameters
        :return: HeaderFooterResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.header_footer_index is not None:
            path_params[self.__downcase_first_letter('HeaderFooterIndex')] = request.header_footer_index  # noqa: E501
        if request.section_index is not None:
            path_params[self.__downcase_first_letter('SectionIndex')] = request.section_index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.filter_by_type is not None:
            query_params.append((self.__downcase_first_letter('FilterByType'), request.filter_by_type))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/sections/{sectionIndex}/headersfooters/{headerFooterIndex}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HeaderFooterResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_header_footers(self, request, **kwargs):  # noqa: E501
        """Return a list of header/footers that are contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_header_footers(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str section_path: Path to parent section.
        :param str filter_by_type: List of types of headers and footers.
        :return: HeaderFootersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_header_footers_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_header_footers_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_header_footers_with_http_info(self, request, **kwargs):  # noqa: E501
        """Return a list of header/footers that are contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_header_footers_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_header_footers_request request object with parameters
        :return: HeaderFootersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.section_path is not None:
            query_params.append((self.__downcase_first_letter('SectionPath'), request.section_path))  # noqa: E501
        if request.filter_by_type is not None:
            query_params.append((self.__downcase_first_letter('FilterByType'), request.filter_by_type))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{sectionPath}/headersfooters', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HeaderFootersResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_office_math_object(self, request, **kwargs):  # noqa: E501
        """Read OfficeMath object by index.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_office_math_object(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param int index: Object's index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str node_path: Path to node, which contains collection of OfficeMath objects.
        :return: OfficeMathObjectResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_office_math_object_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_office_math_object_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_office_math_object_with_http_info(self, request, **kwargs):  # noqa: E501
        """Read OfficeMath object by index.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_office_math_object_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_office_math_object_request request object with parameters
        :return: OfficeMathObjectResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.node_path is not None:
            query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/OfficeMathObjects/{index}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OfficeMathObjectResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_office_math_objects(self, request, **kwargs):  # noqa: E501
        """Get OfficeMath objects from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_office_math_objects(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The file name. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str node_path: Path to node, which contains collection of OfficeMath objects.
        :return: OfficeMathObjectsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_office_math_objects_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_office_math_objects_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_office_math_objects_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get OfficeMath objects from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_office_math_objects_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_office_math_objects_request request object with parameters
        :return: OfficeMathObjectsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.node_path is not None:
            query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/OfficeMathObjects', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OfficeMathObjectsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_section(self, request, **kwargs):  # noqa: E501
        """Get document section by index.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_section(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param int section_index: Section index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :return: SectionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_section_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_section_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_section_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get document section by index.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_section_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_section_request request object with parameters
        :return: SectionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.section_index is not None:
            path_params[self.__downcase_first_letter('SectionIndex')] = request.section_index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/sections/{sectionIndex}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SectionResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_section_page_setup(self, request, **kwargs):  # noqa: E501
        """Get page setup of section.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_section_page_setup(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param int section_index: Section index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :return: SectionPageSetupResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_section_page_setup_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_section_page_setup_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_section_page_setup_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get page setup of section.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_section_page_setup_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_section_page_setup_request request object with parameters
        :return: SectionPageSetupResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.section_index is not None:
            path_params[self.__downcase_first_letter('SectionIndex')] = request.section_index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/sections/{sectionIndex}/pageSetup', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SectionPageSetupResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_sections(self, request, **kwargs):  # noqa: E501
        """Return a list of sections that are contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_sections(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :return: SectionLinkCollectionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_sections_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_sections_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_sections_with_http_info(self, request, **kwargs):  # noqa: E501
        """Return a list of sections that are contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_sections_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_sections_request request object with parameters
        :return: SectionLinkCollectionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/sections', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SectionLinkCollectionResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_table(self, request, **kwargs):  # noqa: E501
        """Return a table.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_table(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param int index: Object's index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str node_path: Path to node, which contains tables.
        :return: TableResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_table_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_table_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_table_with_http_info(self, request, **kwargs):  # noqa: E501
        """Return a table.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_table_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_table_request request object with parameters
        :return: TableResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.node_path is not None:
            query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/tables/{index}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TableResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_table_cell(self, request, **kwargs):  # noqa: E501
        """Return a table cell.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_table_cell(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str table_row_path: Path to table row. (required)
        :param int index: Object's index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :return: TableCellResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_table_cell_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_table_cell_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_table_cell_with_http_info(self, request, **kwargs):  # noqa: E501
        """Return a table cell.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_table_cell_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_table_cell_request request object with parameters
        :return: TableCellResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.table_row_path is not None:
            path_params[self.__downcase_first_letter('TableRowPath')] = request.table_row_path  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{tableRowPath}/cells/{index}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TableCellResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_table_cell_format(self, request, **kwargs):  # noqa: E501
        """Return a table cell format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_table_cell_format(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str table_row_path: Path to table row. (required)
        :param int index: Object's index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :return: TableCellFormatResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_table_cell_format_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_table_cell_format_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_table_cell_format_with_http_info(self, request, **kwargs):  # noqa: E501
        """Return a table cell format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_table_cell_format_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_table_cell_format_request request object with parameters
        :return: TableCellFormatResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.table_row_path is not None:
            path_params[self.__downcase_first_letter('TableRowPath')] = request.table_row_path  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{tableRowPath}/cells/{index}/cellformat', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TableCellFormatResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_table_properties(self, request, **kwargs):  # noqa: E501
        """Return a table properties.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_table_properties(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param int index: Object's index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str node_path: Path to node, which contains tables.
        :return: TablePropertiesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_table_properties_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_table_properties_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_table_properties_with_http_info(self, request, **kwargs):  # noqa: E501
        """Return a table properties.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_table_properties_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_table_properties_request request object with parameters
        :return: TablePropertiesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.node_path is not None:
            query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/tables/{index}/properties', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TablePropertiesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_table_row(self, request, **kwargs):  # noqa: E501
        """Return a table row.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_table_row(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str table_path: Path to table. (required)
        :param int index: Object's index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :return: TableRowResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_table_row_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_table_row_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_table_row_with_http_info(self, request, **kwargs):  # noqa: E501
        """Return a table row.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_table_row_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_table_row_request request object with parameters
        :return: TableRowResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.table_path is not None:
            path_params[self.__downcase_first_letter('TablePath')] = request.table_path  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{tablePath}/rows/{index}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TableRowResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_table_row_format(self, request, **kwargs):  # noqa: E501
        """Return a table row format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_table_row_format(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str table_path: Path to table. (required)
        :param int index: Object's index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :return: TableRowFormatResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_table_row_format_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_table_row_format_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_table_row_format_with_http_info(self, request, **kwargs):  # noqa: E501
        """Return a table row format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_table_row_format_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_table_row_format_request request object with parameters
        :return: TableRowFormatResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.table_path is not None:
            path_params[self.__downcase_first_letter('TablePath')] = request.table_path  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{tablePath}/rows/{index}/rowformat', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TableRowFormatResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_tables(self, request, **kwargs):  # noqa: E501
        """Return a list of tables that are contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_tables(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str node_path: Path to node, which contains tables.
        :return: TableLinkCollectionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_tables_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.get_tables_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def get_tables_with_http_info(self, request, **kwargs):  # noqa: E501
        """Return a list of tables that are contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_tables_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param get_tables_request request object with parameters
        :return: TableLinkCollectionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.node_path is not None:
            query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/tables', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TableLinkCollectionResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def insert_table(self, request, **kwargs):  # noqa: E501
        """Adds table to document, returns added table&#39;s data.               # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.insert_table(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :param TableInsert table: Table parameters/
        :param str node_path: Path to node, which contains tables.
        :return: TableResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.insert_table_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.insert_table_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def insert_table_with_http_info(self, request, **kwargs):  # noqa: E501
        """Adds table to document, returns added table&#39;s data.               # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.insert_table_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param insert_table_request request object with parameters
        :return: TableResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if request.node_path is not None:
            query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/tables', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TableResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def insert_table_cell(self, request, **kwargs):  # noqa: E501
        """Adds table cell to table, returns added cell&#39;s data.               # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.insert_table_cell(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str table_row_path: Path to table row. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :param TableCellInsert cell: Table cell parameters/
        :return: TableCellResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.insert_table_cell_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.insert_table_cell_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def insert_table_cell_with_http_info(self, request, **kwargs):  # noqa: E501
        """Adds table cell to table, returns added cell&#39;s data.               # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.insert_table_cell_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param insert_table_cell_request request object with parameters
        :return: TableCellResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.table_row_path is not None:
            path_params[self.__downcase_first_letter('TableRowPath')] = request.table_row_path  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{tableRowPath}/cells', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TableCellResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def insert_table_row(self, request, **kwargs):  # noqa: E501
        """Adds table row to table, returns added row&#39;s data.               # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.insert_table_row(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str table_path: Path to table. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :param TableRowInsert row: Table row parameters/
        :return: TableRowResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.insert_table_row_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.insert_table_row_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def insert_table_row_with_http_info(self, request, **kwargs):  # noqa: E501
        """Adds table row to table, returns added row&#39;s data.               # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.insert_table_row_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param insert_table_row_request request object with parameters
        :return: TableRowResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.table_path is not None:
            path_params[self.__downcase_first_letter('TablePath')] = request.table_path  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{tablePath}/rows', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TableRowResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_append_document(self, request, **kwargs):  # noqa: E501
        """Append documents to original document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_append_document(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: Original document name. (required)
        :param DocumentEntryList document_list: with a list of documents to append.             (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.post_append_document_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.post_append_document_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def post_append_document_with_http_info(self, request, **kwargs):  # noqa: E501
        """Append documents to original document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_append_document_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param post_append_document_request request object with parameters
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/appendDocument', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DocumentResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_change_document_protection(self, request, **kwargs):  # noqa: E501
        """Change document protection.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_change_document_protection(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param ProtectionRequest protection_request: with protection settings.             (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :return: ProtectionDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.post_change_document_protection_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.post_change_document_protection_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def post_change_document_protection_with_http_info(self, request, **kwargs):  # noqa: E501
        """Change document protection.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_change_document_protection_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param post_change_document_protection_request request object with parameters
        :return: ProtectionDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/protection', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProtectionDataResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_comment(self, request, **kwargs):  # noqa: E501
        """Updates the comment, returns updated comment&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_comment(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param int comment_index: Comment index (required)
        :param Comment comment: Comment data. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :return: CommentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.post_comment_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.post_comment_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def post_comment_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates the comment, returns updated comment&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_comment_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param post_comment_request request object with parameters
        :return: CommentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.comment_index is not None:
            path_params[self.__downcase_first_letter('CommentIndex')] = request.comment_index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/comments/{commentIndex}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CommentResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_compare_document(self, request, **kwargs):  # noqa: E501
        """Compare document with original document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_compare_document(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: Original document name. (required)
        :param CompareData compare_data: with a document to compare.             (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.post_compare_document_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.post_compare_document_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def post_compare_document_with_http_info(self, request, **kwargs):  # noqa: E501
        """Compare document with original document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_compare_document_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param post_compare_document_request request object with parameters
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/compareDocument', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DocumentResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_document_execute_mail_merge(self, request, **kwargs):  # noqa: E501
        """Execute document mail merge operation.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_document_execute_mail_merge(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str data: Mail merge data
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param bool with_regions: With regions flag.
        :param str mail_merge_data_file: Mail merge data.
        :param str cleanup: Clean up options.
        :param bool use_whole_paragraph_as_region: Gets or sets a value indicating whether paragraph with TableStart or              TableEnd field should be fully included into mail merge region or particular range between TableStart and TableEnd fields.              The default value is true.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved with autogenerated name.
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.post_document_execute_mail_merge_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.post_document_execute_mail_merge_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def post_document_execute_mail_merge_with_http_info(self, request, **kwargs):  # noqa: E501
        """Execute document mail merge operation.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_document_execute_mail_merge_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param post_document_execute_mail_merge_request request object with parameters
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.with_regions is not None:
            query_params.append((self.__downcase_first_letter('WithRegions'), request.with_regions))  # noqa: E501
        if request.mail_merge_data_file is not None:
            query_params.append((self.__downcase_first_letter('MailMergeDataFile'), request.mail_merge_data_file))  # noqa: E501
        if request.cleanup is not None:
            query_params.append((self.__downcase_first_letter('Cleanup'), request.cleanup))  # noqa: E501
        if request.use_whole_paragraph_as_region is not None:
            query_params.append((self.__downcase_first_letter('UseWholeParagraphAsRegion'), request.use_whole_paragraph_as_region))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}
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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/executeMailMerge', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DocumentResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_document_paragraph_run_font(self, request, **kwargs):  # noqa: E501
        """Updates font properties, returns updated font data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_document_paragraph_run_font(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param Font font_dto: Font dto object (required)
        :param str paragraph_path: Path to parent paragraph. (required)
        :param int index: Object's index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :return: FontResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.post_document_paragraph_run_font_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.post_document_paragraph_run_font_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def post_document_paragraph_run_font_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates font properties, returns updated font data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_document_paragraph_run_font_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param post_document_paragraph_run_font_request request object with parameters
        :return: FontResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.paragraph_path is not None:
            path_params[self.__downcase_first_letter('ParagraphPath')] = request.paragraph_path  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{paragraphPath}/runs/{index}/font', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FontResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_document_save_as(self, request, **kwargs):  # noqa: E501
        """Convert document to destination format with detailed settings and save result to storage.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_document_save_as(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param SaveOptionsData save_options_data: Save options. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str fonts_location: Folder in filestorage with custom fonts.
        :return: SaveResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.post_document_save_as_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.post_document_save_as_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def post_document_save_as_with_http_info(self, request, **kwargs):  # noqa: E501
        """Convert document to destination format with detailed settings and save result to storage.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_document_save_as_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param post_document_save_as_request request object with parameters
        :return: SaveResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.fonts_location is not None:
            query_params.append((self.__downcase_first_letter('FontsLocation'), request.fonts_location))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/saveAs', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SaveResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_drawing_object(self, request, **kwargs):  # noqa: E501
        """Updates drawing object, returns updated  drawing object&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_drawing_object(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str drawing_object: Drawing object parameters (required)
        :param file image_file: File with image (required)
        :param int index: Object's index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :param str node_path: Path to node, which contains collection of drawing objects.
        :return: DrawingObjectResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.post_drawing_object_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.post_drawing_object_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def post_drawing_object_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates drawing object, returns updated  drawing object&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_drawing_object_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param post_drawing_object_request request object with parameters
        :return: DrawingObjectResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if request.node_path is not None:
            query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}
        if request.drawing_object is not None:
            form_params.append((self.__downcase_first_letter('DrawingObject'), request.drawing_object))  # noqa: E501
        if request.image_file is not None:
            local_var_files[self.__downcase_first_letter('ImageFile')] = request.image_file  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/drawingObjects/{index}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DrawingObjectResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_execute_template(self, request, **kwargs):  # noqa: E501
        """Populate document template with data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_execute_template(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The template document name. (required)
        :param str data: Mail merge data (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str cleanup: Clean up options.
        :param bool use_whole_paragraph_as_region: Gets or sets a value indicating whether paragraph with TableStart or  TableEnd field should be fully included into mail merge region or particular range between TableStart and TableEnd fields.   The default value is true.
        :param bool with_regions: Merge with regions or not. True by default
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved with autogenerated name.
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.post_execute_template_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.post_execute_template_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def post_execute_template_with_http_info(self, request, **kwargs):  # noqa: E501
        """Populate document template with data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_execute_template_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param post_execute_template_request request object with parameters
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.cleanup is not None:
            query_params.append((self.__downcase_first_letter('Cleanup'), request.cleanup))  # noqa: E501
        if request.use_whole_paragraph_as_region is not None:
            query_params.append((self.__downcase_first_letter('UseWholeParagraphAsRegion'), request.use_whole_paragraph_as_region))  # noqa: E501
        if request.with_regions is not None:
            query_params.append((self.__downcase_first_letter('WithRegions'), request.with_regions))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}
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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/executeTemplate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DocumentResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_field(self, request, **kwargs):  # noqa: E501
        """Updates field&#39;s properties, returns updated field&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_field(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param Field field: Field data. (required)
        :param int index: Object's index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :param str node_path: Path to node, which contains collection of fields.
        :return: FieldResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.post_field_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.post_field_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def post_field_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates field&#39;s properties, returns updated field&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_field_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param post_field_request request object with parameters
        :return: FieldResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if request.node_path is not None:
            query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/fields/{index}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FieldResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_footnote(self, request, **kwargs):  # noqa: E501
        """Updates footnote&#39;s properties, returns updated run&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_footnote(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param Footnote footnote_dto: Footnote data. (required)
        :param int index: Object's index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :param str node_path: Path to node, which contains collection of footnotes.
        :return: FootnoteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.post_footnote_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.post_footnote_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def post_footnote_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates footnote&#39;s properties, returns updated run&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_footnote_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param post_footnote_request request object with parameters
        :return: FootnoteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if request.node_path is not None:
            query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/footnotes/{index}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FootnoteResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_form_field(self, request, **kwargs):  # noqa: E501
        """Updates properties of form field, returns updated form field.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_form_field(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param FormField form_field: From field data. (required)
        :param int index: Object's index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :param str node_path: Path to node that contains collection of formfields.
        :return: FormFieldResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.post_form_field_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.post_form_field_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def post_form_field_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates properties of form field, returns updated form field.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_form_field_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param post_form_field_request request object with parameters
        :return: FormFieldResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if request.node_path is not None:
            query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/formfields/{index}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FormFieldResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_insert_document_watermark_image(self, request, **kwargs):  # noqa: E501
        """Insert document watermark image.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_insert_document_watermark_image(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param file image_file: File with image
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :param float rotation_angle: The watermark rotation angle.
        :param str image: The image file server full name. If the name is empty the image is expected in request content.
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.post_insert_document_watermark_image_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.post_insert_document_watermark_image_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def post_insert_document_watermark_image_with_http_info(self, request, **kwargs):  # noqa: E501
        """Insert document watermark image.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_insert_document_watermark_image_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param post_insert_document_watermark_image_request request object with parameters
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if request.rotation_angle is not None:
            query_params.append((self.__downcase_first_letter('RotationAngle'), request.rotation_angle))  # noqa: E501
        if request.image is not None:
            query_params.append((self.__downcase_first_letter('Image'), request.image))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}
        if request.image_file is not None:
            local_var_files[self.__downcase_first_letter('ImageFile')] = request.image_file  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/watermark/insertImage', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DocumentResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_insert_document_watermark_text(self, request, **kwargs):  # noqa: E501
        """Insert document watermark text.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_insert_document_watermark_text(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param WatermarkText watermark_text: with the watermark data.             (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.post_insert_document_watermark_text_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.post_insert_document_watermark_text_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def post_insert_document_watermark_text_with_http_info(self, request, **kwargs):  # noqa: E501
        """Insert document watermark text.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_insert_document_watermark_text_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param post_insert_document_watermark_text_request request object with parameters
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/watermark/insertText', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DocumentResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_insert_page_numbers(self, request, **kwargs):  # noqa: E501
        """Insert document page numbers.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_insert_page_numbers(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: A document name. (required)
        :param PageNumber page_number: with the page numbers settings. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.post_insert_page_numbers_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.post_insert_page_numbers_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def post_insert_page_numbers_with_http_info(self, request, **kwargs):  # noqa: E501
        """Insert document page numbers.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_insert_page_numbers_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param post_insert_page_numbers_request request object with parameters
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/insertPageNumbers', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DocumentResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_load_web_document(self, request, **kwargs):  # noqa: E501
        """Loads new document from web into the file with any supported format of data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_load_web_document(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param LoadWebDocumentData data: Parameters of loading. (required)
        :param str storage: File storage, which have to be used.
        :return: SaveResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.post_load_web_document_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.post_load_web_document_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def post_load_web_document_with_http_info(self, request, **kwargs):  # noqa: E501
        """Loads new document from web into the file with any supported format of data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_load_web_document_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param post_load_web_document_request request object with parameters
        :return: SaveResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}

        query_params = []
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/loadWebDocument', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SaveResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_replace_text(self, request, **kwargs):  # noqa: E501
        """Replace document text.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_replace_text(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param ReplaceTextRequest replace_text: with the replace operation settings.             (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :return: ReplaceTextResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.post_replace_text_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.post_replace_text_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def post_replace_text_with_http_info(self, request, **kwargs):  # noqa: E501
        """Replace document text.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_replace_text_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param post_replace_text_request request object with parameters
        :return: ReplaceTextResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/replaceText', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReplaceTextResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_run(self, request, **kwargs):  # noqa: E501
        """Updates run&#39;s properties, returns updated run&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_run(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param Run run: Run data. (required)
        :param str paragraph_path: Path to parent paragraph. (required)
        :param int index: Object's index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :return: RunResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.post_run_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.post_run_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def post_run_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates run&#39;s properties, returns updated run&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_run_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param post_run_request request object with parameters
        :return: RunResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.paragraph_path is not None:
            path_params[self.__downcase_first_letter('ParagraphPath')] = request.paragraph_path  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{paragraphPath}/runs/{index}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RunResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_split_document(self, request, **kwargs):  # noqa: E501
        """Split document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_split_document(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: Original document name. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str format: Format to split.
        :param int _from: Start page.
        :param int to: End page.
        :param bool zip_output: ZipOutput or not.
        :param str fonts_location: Folder in filestorage with custom fonts.
        :return: SplitDocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.post_split_document_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.post_split_document_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def post_split_document_with_http_info(self, request, **kwargs):  # noqa: E501
        """Split document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_split_document_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param post_split_document_request request object with parameters
        :return: SplitDocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.format is not None:
            query_params.append((self.__downcase_first_letter('Format'), request.format))  # noqa: E501
        if request._from is not None:
            query_params.append((self.__downcase_first_letter('From'), request._from))  # noqa: E501
        if request.to is not None:
            query_params.append((self.__downcase_first_letter('To'), request.to))  # noqa: E501
        if request.zip_output is not None:
            query_params.append((self.__downcase_first_letter('ZipOutput'), request.zip_output))  # noqa: E501
        if request.fonts_location is not None:
            query_params.append((self.__downcase_first_letter('FontsLocation'), request.fonts_location))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/split', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SplitDocumentResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_update_document_bookmark(self, request, **kwargs):  # noqa: E501
        """Update document bookmark.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_update_document_bookmark(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param BookmarkData bookmark_data: with new bookmark data.             (required)
        :param str bookmark_name: The bookmark name. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :return: BookmarkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.post_update_document_bookmark_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.post_update_document_bookmark_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def post_update_document_bookmark_with_http_info(self, request, **kwargs):  # noqa: E501
        """Update document bookmark.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_update_document_bookmark_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param post_update_document_bookmark_request request object with parameters
        :return: BookmarkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.bookmark_name is not None:
            path_params[self.__downcase_first_letter('BookmarkName')] = request.bookmark_name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/bookmarks/{bookmarkName}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BookmarkResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_update_document_fields(self, request, **kwargs):  # noqa: E501
        """Update (reevaluate) fields in document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_update_document_fields(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.post_update_document_fields_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.post_update_document_fields_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def post_update_document_fields_with_http_info(self, request, **kwargs):  # noqa: E501
        """Update (reevaluate) fields in document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_update_document_fields_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param post_update_document_fields_request request object with parameters
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/updateFields', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DocumentResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_comment(self, request, **kwargs):  # noqa: E501
        """Adds comment to document, returns inserted comment&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.put_comment(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param Comment comment: Comment data. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :return: CommentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.put_comment_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.put_comment_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def put_comment_with_http_info(self, request, **kwargs):  # noqa: E501
        """Adds comment to document, returns inserted comment&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.put_comment_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param put_comment_request request object with parameters
        :return: CommentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/comments', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CommentResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_convert_document(self, request, **kwargs):  # noqa: E501
        """Convert document from request content to format specified.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.put_convert_document(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param file document: Converting document (required)
        :param str format: Format to convert. (required)
        :param str storage: File storage, which have to be used.
        :param str out_path: Path for saving operation result to the local storage.
        :param str document_file_name: This file name will be used when resulting document has dynamic field for document file name {filename}. If it is not setted, \"sourceFilename\" will be used instead. 
        :param str fonts_location: Folder in filestorage with custom fonts.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.put_convert_document_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.put_convert_document_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def put_convert_document_with_http_info(self, request, **kwargs):  # noqa: E501
        """Convert document from request content to format specified.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.put_convert_document_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param put_convert_document_request request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}

        query_params = []
        if request.format is not None:
            query_params.append((self.__downcase_first_letter('Format'), request.format))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.out_path is not None:
            query_params.append((self.__downcase_first_letter('OutPath'), request.out_path))  # noqa: E501
        if request.document_file_name is not None:
            query_params.append((self.__downcase_first_letter('DocumentFileName'), request.document_file_name))  # noqa: E501
        if request.fonts_location is not None:
            query_params.append((self.__downcase_first_letter('FontsLocation'), request.fonts_location))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}
        if request.document is not None:
            local_var_files[self.__downcase_first_letter('Document')] = request.document  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/convert', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_create_document(self, request, **kwargs):  # noqa: E501
        """Creates new document. Document is created with format which is recognized from file extensions.  Supported extentions: \&quot;.doc\&quot;, \&quot;.docx\&quot;, \&quot;.docm\&quot;, \&quot;.dot\&quot;, \&quot;.dotm\&quot;, \&quot;.dotx\&quot;, \&quot;.flatopc\&quot;, \&quot;.fopc\&quot;, \&quot;.flatopc_macro\&quot;, \&quot;.fopc_macro\&quot;, \&quot;.flatopc_template\&quot;, \&quot;.fopc_template\&quot;, \&quot;.flatopc_template_macro\&quot;, \&quot;.fopc_template_macro\&quot;, \&quot;.wordml\&quot;, \&quot;.wml\&quot;, \&quot;.rtf\&quot;  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.put_create_document(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str storage: File storage, which have to be used.
        :param str file_name: The file name.
        :param str folder: The document folder.
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.put_create_document_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.put_create_document_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def put_create_document_with_http_info(self, request, **kwargs):  # noqa: E501
        """Creates new document. Document is created with format which is recognized from file extensions.  Supported extentions: \&quot;.doc\&quot;, \&quot;.docx\&quot;, \&quot;.docm\&quot;, \&quot;.dot\&quot;, \&quot;.dotm\&quot;, \&quot;.dotx\&quot;, \&quot;.flatopc\&quot;, \&quot;.fopc\&quot;, \&quot;.flatopc_macro\&quot;, \&quot;.fopc_macro\&quot;, \&quot;.flatopc_template\&quot;, \&quot;.fopc_template\&quot;, \&quot;.flatopc_template_macro\&quot;, \&quot;.fopc_template_macro\&quot;, \&quot;.wordml\&quot;, \&quot;.wml\&quot;, \&quot;.rtf\&quot;  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.put_create_document_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param put_create_document_request request object with parameters
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_create_document" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.file_name is not None:
            query_params.append((self.__downcase_first_letter('FileName'), request.file_name))  # noqa: E501
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/create', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DocumentResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_document_field_names(self, request, **kwargs):  # noqa: E501
        """Read document field names.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.put_document_field_names(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param file template: File with template (required)
        :param bool use_non_merge_fields: Use non merge fields or not.
        :return: FieldNamesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.put_document_field_names_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.put_document_field_names_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def put_document_field_names_with_http_info(self, request, **kwargs):  # noqa: E501
        """Read document field names.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.put_document_field_names_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param put_document_field_names_request request object with parameters
        :return: FieldNamesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}

        query_params = []
        if request.use_non_merge_fields is not None:
            query_params.append((self.__downcase_first_letter('UseNonMergeFields'), request.use_non_merge_fields))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}
        if request.template is not None:
            local_var_files[self.__downcase_first_letter('Template')] = request.template  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/mailMergeFieldNames', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FieldNamesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_document_save_as_tiff(self, request, **kwargs):  # noqa: E501
        """Convert document to tiff with detailed settings and save result to storage.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.put_document_save_as_tiff(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param TiffSaveOptionsData save_options: Tiff save options. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str result_file: The resulting file name.
        :param bool use_anti_aliasing: Use antialiasing flag.
        :param bool use_high_quality_rendering: Use high quality flag.
        :param float image_brightness: Brightness for the generated images.
        :param str image_color_mode: Color mode for the generated images.
        :param float image_contrast: The contrast for the generated images.
        :param str numeral_format: The images numeral format.
        :param int page_count: Number of pages to render.
        :param int page_index: Page index to start rendering.
        :param str paper_color: Background image color.
        :param str pixel_format: The pixel format of generated images.
        :param float resolution: The resolution of generated images.
        :param float scale: Zoom factor for generated images.
        :param str tiff_compression: The compression tipe.
        :param str dml_rendering_mode: Optional, default is Fallback.
        :param str dml_effects_rendering_mode: Optional, default is Simplified.
        :param str tiff_binarization_method: Optional, Tiff binarization method, possible values are: FloydSteinbergDithering, Threshold.
        :param bool zip_output: Optional. A value determining zip output or not.
        :param str fonts_location: Folder in filestorage with custom fonts.
        :return: SaveResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.put_document_save_as_tiff_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.put_document_save_as_tiff_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def put_document_save_as_tiff_with_http_info(self, request, **kwargs):  # noqa: E501
        """Convert document to tiff with detailed settings and save result to storage.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.put_document_save_as_tiff_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param put_document_save_as_tiff_request request object with parameters
        :return: SaveResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.result_file is not None:
            query_params.append((self.__downcase_first_letter('ResultFile'), request.result_file))  # noqa: E501
        if request.use_anti_aliasing is not None:
            query_params.append((self.__downcase_first_letter('UseAntiAliasing'), request.use_anti_aliasing))  # noqa: E501
        if request.use_high_quality_rendering is not None:
            query_params.append((self.__downcase_first_letter('UseHighQualityRendering'), request.use_high_quality_rendering))  # noqa: E501
        if request.image_brightness is not None:
            query_params.append((self.__downcase_first_letter('ImageBrightness'), request.image_brightness))  # noqa: E501
        if request.image_color_mode is not None:
            query_params.append((self.__downcase_first_letter('ImageColorMode'), request.image_color_mode))  # noqa: E501
        if request.image_contrast is not None:
            query_params.append((self.__downcase_first_letter('ImageContrast'), request.image_contrast))  # noqa: E501
        if request.numeral_format is not None:
            query_params.append((self.__downcase_first_letter('NumeralFormat'), request.numeral_format))  # noqa: E501
        if request.page_count is not None:
            query_params.append((self.__downcase_first_letter('PageCount'), request.page_count))  # noqa: E501
        if request.page_index is not None:
            query_params.append((self.__downcase_first_letter('PageIndex'), request.page_index))  # noqa: E501
        if request.paper_color is not None:
            query_params.append((self.__downcase_first_letter('PaperColor'), request.paper_color))  # noqa: E501
        if request.pixel_format is not None:
            query_params.append((self.__downcase_first_letter('PixelFormat'), request.pixel_format))  # noqa: E501
        if request.resolution is not None:
            query_params.append((self.__downcase_first_letter('Resolution'), request.resolution))  # noqa: E501
        if request.scale is not None:
            query_params.append((self.__downcase_first_letter('Scale'), request.scale))  # noqa: E501
        if request.tiff_compression is not None:
            query_params.append((self.__downcase_first_letter('TiffCompression'), request.tiff_compression))  # noqa: E501
        if request.dml_rendering_mode is not None:
            query_params.append((self.__downcase_first_letter('DmlRenderingMode'), request.dml_rendering_mode))  # noqa: E501
        if request.dml_effects_rendering_mode is not None:
            query_params.append((self.__downcase_first_letter('DmlEffectsRenderingMode'), request.dml_effects_rendering_mode))  # noqa: E501
        if request.tiff_binarization_method is not None:
            query_params.append((self.__downcase_first_letter('TiffBinarizationMethod'), request.tiff_binarization_method))  # noqa: E501
        if request.zip_output is not None:
            query_params.append((self.__downcase_first_letter('ZipOutput'), request.zip_output))  # noqa: E501
        if request.fonts_location is not None:
            query_params.append((self.__downcase_first_letter('FontsLocation'), request.fonts_location))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/saveAs/tiff', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SaveResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_drawing_object(self, request, **kwargs):  # noqa: E501
        """Adds  drawing object to document, returns added  drawing object&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.put_drawing_object(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str drawing_object: Drawing object parameters (required)
        :param file image_file: File with image (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :param str node_path: Path to node, which contains collection of drawing objects.
        :return: DrawingObjectResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.put_drawing_object_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.put_drawing_object_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def put_drawing_object_with_http_info(self, request, **kwargs):  # noqa: E501
        """Adds  drawing object to document, returns added  drawing object&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.put_drawing_object_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param put_drawing_object_request request object with parameters
        :return: DrawingObjectResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if request.node_path is not None:
            query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}
        if request.drawing_object is not None:
            form_params.append((self.__downcase_first_letter('DrawingObject'), request.drawing_object))  # noqa: E501
        if request.image_file is not None:
            local_var_files[self.__downcase_first_letter('ImageFile')] = request.image_file  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/drawingObjects', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DrawingObjectResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_execute_mail_merge_online(self, request, **kwargs):  # noqa: E501
        """Execute document mail merge online.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.put_execute_mail_merge_online(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param file template: File with template (required)
        :param file data: File with mailmerge data (required)
        :param bool with_regions: With regions flag.
        :param str cleanup: Clean up options.
        :param str document_file_name: This file name will be used when resulting document has dynamic field for document file name {filename}. If it is not setted, \"template\" will be used instead. 
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.put_execute_mail_merge_online_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.put_execute_mail_merge_online_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def put_execute_mail_merge_online_with_http_info(self, request, **kwargs):  # noqa: E501
        """Execute document mail merge online.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.put_execute_mail_merge_online_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param put_execute_mail_merge_online_request request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}

        query_params = []
        if request.with_regions is not None:
            query_params.append((self.__downcase_first_letter('WithRegions'), request.with_regions))  # noqa: E501
        if request.cleanup is not None:
            query_params.append((self.__downcase_first_letter('Cleanup'), request.cleanup))  # noqa: E501
        if request.document_file_name is not None:
            query_params.append((self.__downcase_first_letter('DocumentFileName'), request.document_file_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}
        if request.template is not None:
            local_var_files[self.__downcase_first_letter('Template')] = request.template  # noqa: E501
        if request.data is not None:
            local_var_files[self.__downcase_first_letter('Data')] = request.data  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/executeMailMerge', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_execute_template_online(self, request, **kwargs):  # noqa: E501
        """Populate document template with data online.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.put_execute_template_online(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param file template: File with template (required)
        :param file data: File with mailmerge data (required)
        :param str cleanup: Clean up options.
        :param bool use_whole_paragraph_as_region: Gets or sets a value indicating whether paragraph with TableStart or              TableEnd field should be fully included into mail merge region or particular range between TableStart and TableEnd fields.              The default value is true.
        :param bool with_regions: Merge with regions or not. True by default
        :param str document_file_name: This file name will be used when resulting document has dynamic field for document file name {filename}.  If it is not setted, \"template\" will be used instead.  Note: if withRegions == true executeTemplate updates fields only inside regions
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.put_execute_template_online_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.put_execute_template_online_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def put_execute_template_online_with_http_info(self, request, **kwargs):  # noqa: E501
        """Populate document template with data online.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.put_execute_template_online_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param put_execute_template_online_request request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}

        query_params = []
        if request.cleanup is not None:
            query_params.append((self.__downcase_first_letter('Cleanup'), request.cleanup))  # noqa: E501
        if request.use_whole_paragraph_as_region is not None:
            query_params.append((self.__downcase_first_letter('UseWholeParagraphAsRegion'), request.use_whole_paragraph_as_region))  # noqa: E501
        if request.with_regions is not None:
            query_params.append((self.__downcase_first_letter('WithRegions'), request.with_regions))  # noqa: E501
        if request.document_file_name is not None:
            query_params.append((self.__downcase_first_letter('DocumentFileName'), request.document_file_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}
        if request.template is not None:
            local_var_files[self.__downcase_first_letter('Template')] = request.template  # noqa: E501
        if request.data is not None:
            local_var_files[self.__downcase_first_letter('Data')] = request.data  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/executeTemplate', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_field(self, request, **kwargs):  # noqa: E501
        """Adds field to document, returns inserted field&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.put_field(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param Field field: Field data. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :param str node_path: Path to node, which contains collection of fields.
        :param str insert_before_node: Field will be inserted before node with id=\"nodeId\".
        :return: FieldResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.put_field_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.put_field_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def put_field_with_http_info(self, request, **kwargs):  # noqa: E501
        """Adds field to document, returns inserted field&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.put_field_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param put_field_request request object with parameters
        :return: FieldResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if request.node_path is not None:
            query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501
        if request.insert_before_node is not None:
            query_params.append((self.__downcase_first_letter('InsertBeforeNode'), request.insert_before_node))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/fields', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FieldResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_footnote(self, request, **kwargs):  # noqa: E501
        """Adds footnote to document, returns added footnote&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.put_footnote(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param Footnote footnote_dto: Footnote data. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :param str node_path: Path to node, which contains collection of footnotes.
        :return: FootnoteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.put_footnote_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.put_footnote_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def put_footnote_with_http_info(self, request, **kwargs):  # noqa: E501
        """Adds footnote to document, returns added footnote&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.put_footnote_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param put_footnote_request request object with parameters
        :return: FootnoteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if request.node_path is not None:
            query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/footnotes', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FootnoteResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_form_field(self, request, **kwargs):  # noqa: E501
        """Adds form field to paragraph, returns added form field&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.put_form_field(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param FormField form_field: From field data. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :param str node_path: Path to node that contains collection of formfields.
        :param str insert_before_node: Form field will be inserted before node with index.
        :return: FormFieldResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.put_form_field_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.put_form_field_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def put_form_field_with_http_info(self, request, **kwargs):  # noqa: E501
        """Adds form field to paragraph, returns added form field&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.put_form_field_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param put_form_field_request request object with parameters
        :return: FormFieldResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if request.node_path is not None:
            query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501
        if request.insert_before_node is not None:
            query_params.append((self.__downcase_first_letter('InsertBeforeNode'), request.insert_before_node))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/formfields', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FormFieldResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_header_footer(self, request, **kwargs):  # noqa: E501
        """Insert to document header or footer.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.put_header_footer(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str header_footer_type: Type of header/footer. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :param str section_path: Path to parent section.
        :return: HeaderFooterResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.put_header_footer_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.put_header_footer_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def put_header_footer_with_http_info(self, request, **kwargs):  # noqa: E501
        """Insert to document header or footer.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.put_header_footer_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param put_header_footer_request request object with parameters
        :return: HeaderFooterResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if request.section_path is not None:
            query_params.append((self.__downcase_first_letter('SectionPath'), request.section_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{sectionPath}/headersfooters', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HeaderFooterResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_paragraph(self, request, **kwargs):  # noqa: E501
        """Adds paragraph to document, returns added paragraph&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.put_paragraph(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param ParagraphInsert paragraph: Paragraph data. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :param str node_path: Path to node which contains paragraphs.
        :param str insert_before_node: Paragraph will be inserted before node with index.
        :return: ParagraphResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.put_paragraph_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.put_paragraph_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def put_paragraph_with_http_info(self, request, **kwargs):  # noqa: E501
        """Adds paragraph to document, returns added paragraph&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.put_paragraph_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param put_paragraph_request request object with parameters
        :return: ParagraphResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if request.node_path is not None:
            query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501
        if request.insert_before_node is not None:
            query_params.append((self.__downcase_first_letter('InsertBeforeNode'), request.insert_before_node))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/paragraphs', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ParagraphResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_protect_document(self, request, **kwargs):  # noqa: E501
        """Protect document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.put_protect_document(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param ProtectionRequest protection_request: with protection settings.             (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :return: ProtectionDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.put_protect_document_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.put_protect_document_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def put_protect_document_with_http_info(self, request, **kwargs):  # noqa: E501
        """Protect document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.put_protect_document_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param put_protect_document_request request object with parameters
        :return: ProtectionDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/protection', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProtectionDataResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_run(self, request, **kwargs):  # noqa: E501
        """Adds run to document, returns added paragraph&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.put_run(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str paragraph_path: Path to parent paragraph. (required)
        :param Run run: Run data. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :param str insert_before_node: Paragraph will be inserted before node with index.
        :return: RunResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.put_run_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.put_run_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def put_run_with_http_info(self, request, **kwargs):  # noqa: E501
        """Adds run to document, returns added paragraph&#39;s data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.put_run_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param put_run_request request object with parameters
        :return: RunResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.paragraph_path is not None:
            path_params[self.__downcase_first_letter('ParagraphPath')] = request.paragraph_path  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if request.insert_before_node is not None:
            query_params.append((self.__downcase_first_letter('InsertBeforeNode'), request.insert_before_node))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{paragraphPath}/runs', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RunResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def reject_all_revisions(self, request, **kwargs):  # noqa: E501
        """Reject all revisions in document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.reject_all_revisions(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :return: RevisionsModificationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.reject_all_revisions_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.reject_all_revisions_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def reject_all_revisions_with_http_info(self, request, **kwargs):  # noqa: E501
        """Reject all revisions in document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.reject_all_revisions_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param reject_all_revisions_request request object with parameters
        :return: RevisionsModificationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/revisions/rejectAll', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RevisionsModificationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def render_drawing_object(self, request, **kwargs):  # noqa: E501
        """Renders drawing object to specified format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.render_drawing_object(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The file name. (required)
        :param str format: The destination format. (required)
        :param int index: Object's index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str node_path: Path to node, which contains drawing objects.
        :param str fonts_location: Folder in filestorage with custom fonts.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.render_drawing_object_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.render_drawing_object_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def render_drawing_object_with_http_info(self, request, **kwargs):  # noqa: E501
        """Renders drawing object to specified format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.render_drawing_object_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param render_drawing_object_request request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if request.format is not None:
            query_params.append((self.__downcase_first_letter('Format'), request.format))  # noqa: E501
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.node_path is not None:
            query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501
        if request.fonts_location is not None:
            query_params.append((self.__downcase_first_letter('FontsLocation'), request.fonts_location))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/drawingObjects/{index}/render', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def render_math_object(self, request, **kwargs):  # noqa: E501
        """Renders math object to specified format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.render_math_object(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The file name. (required)
        :param str format: The destination format. (required)
        :param int index: Object's index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str node_path: Path to node, which contains office math objects.
        :param str fonts_location: Folder in filestorage with custom fonts.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.render_math_object_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.render_math_object_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def render_math_object_with_http_info(self, request, **kwargs):  # noqa: E501
        """Renders math object to specified format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.render_math_object_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param render_math_object_request request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if request.format is not None:
            query_params.append((self.__downcase_first_letter('Format'), request.format))  # noqa: E501
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.node_path is not None:
            query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501
        if request.fonts_location is not None:
            query_params.append((self.__downcase_first_letter('FontsLocation'), request.fonts_location))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/OfficeMathObjects/{index}/render', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def render_page(self, request, **kwargs):  # noqa: E501
        """Renders page to specified format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.render_page(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The file name. (required)
        :param int page_index: Comment index (required)
        :param str format: The destination format. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str fonts_location: Folder in filestorage with custom fonts.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.render_page_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.render_page_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def render_page_with_http_info(self, request, **kwargs):  # noqa: E501
        """Renders page to specified format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.render_page_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param render_page_request request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.page_index is not None:
            path_params[self.__downcase_first_letter('PageIndex')] = request.page_index  # noqa: E501

        query_params = []
        if request.format is not None:
            query_params.append((self.__downcase_first_letter('Format'), request.format))  # noqa: E501
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.fonts_location is not None:
            query_params.append((self.__downcase_first_letter('FontsLocation'), request.fonts_location))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/pages/{pageIndex}/render', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def render_paragraph(self, request, **kwargs):  # noqa: E501
        """Renders paragraph to specified format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.render_paragraph(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The file name. (required)
        :param str format: The destination format. (required)
        :param int index: Object's index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str node_path: Path to node, which contains paragraphs.
        :param str fonts_location: Folder in filestorage with custom fonts.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.render_paragraph_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.render_paragraph_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def render_paragraph_with_http_info(self, request, **kwargs):  # noqa: E501
        """Renders paragraph to specified format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.render_paragraph_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param render_paragraph_request request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if request.format is not None:
            query_params.append((self.__downcase_first_letter('Format'), request.format))  # noqa: E501
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.node_path is not None:
            query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501
        if request.fonts_location is not None:
            query_params.append((self.__downcase_first_letter('FontsLocation'), request.fonts_location))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/paragraphs/{index}/render', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def render_table(self, request, **kwargs):  # noqa: E501
        """Renders table to specified format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.render_table(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The file name. (required)
        :param str format: The destination format. (required)
        :param int index: Object's index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str node_path: Path to node, which contains tables.
        :param str fonts_location: Folder in filestorage with custom fonts.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.render_table_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.render_table_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def render_table_with_http_info(self, request, **kwargs):  # noqa: E501
        """Renders table to specified format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.render_table_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param render_table_request request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if request.format is not None:
            query_params.append((self.__downcase_first_letter('Format'), request.format))  # noqa: E501
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.node_path is not None:
            query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501
        if request.fonts_location is not None:
            query_params.append((self.__downcase_first_letter('FontsLocation'), request.fonts_location))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/tables/{index}/render', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def reset_cache(self, request, **kwargs):  # noqa: E501
        """Resets font&#39;s cache.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.reset_cache(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.reset_cache_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.reset_cache_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def reset_cache_with_http_info(self, request, **kwargs):  # noqa: E501
        """Resets font&#39;s cache.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.reset_cache_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param reset_cache_request request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reset_cache" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/fonts/cache', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search(self, request, **kwargs):  # noqa: E501
        """Search text in document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.search(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str pattern: The regular expression used to find matches. (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :return: SearchResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.search_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.search_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def search_with_http_info(self, request, **kwargs):  # noqa: E501
        """Search text in document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.search_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param search_request request object with parameters
        :return: SearchResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501

        query_params = []
        if request.pattern is not None:
            query_params.append((self.__downcase_first_letter('Pattern'), request.pattern))  # noqa: E501
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SearchResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_border(self, request, **kwargs):  # noqa: E501
        """Updates border properties.               # noqa: E501

        'nodePath' should refer to node with cell or row  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_border(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param Border border_properties: Border properties (required)
        :param str node_path: Path to node with border(node should be cell or row). (required)
        :param int index: Object's index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :return: BorderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_border_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.update_border_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def update_border_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates border properties.               # noqa: E501

        'nodePath' should refer to node with cell or row  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_border_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param update_border_request request object with parameters
        :return: BorderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.node_path is not None:
            path_params[self.__downcase_first_letter('NodePath')] = request.node_path  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/borders/{index}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BorderResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_section_page_setup(self, request, **kwargs):  # noqa: E501
        """Update page setup of section.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_section_page_setup(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param int section_index: Section index (required)
        :param PageSetup page_setup: Page setup properties dto (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :return: SectionPageSetupResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_section_page_setup_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.update_section_page_setup_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def update_section_page_setup_with_http_info(self, request, **kwargs):  # noqa: E501
        """Update page setup of section.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_section_page_setup_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param update_section_page_setup_request request object with parameters
        :return: SectionPageSetupResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.section_index is not None:
            path_params[self.__downcase_first_letter('SectionIndex')] = request.section_index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/sections/{sectionIndex}/pageSetup', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SectionPageSetupResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_table_cell_format(self, request, **kwargs):  # noqa: E501
        """Updates a table cell format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_table_cell_format(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str table_row_path: Path to table row. (required)
        :param int index: Object's index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :param TableCellFormat format: The properties.
        :return: TableCellFormatResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_table_cell_format_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.update_table_cell_format_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def update_table_cell_format_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates a table cell format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_table_cell_format_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param update_table_cell_format_request request object with parameters
        :return: TableCellFormatResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.table_row_path is not None:
            path_params[self.__downcase_first_letter('TableRowPath')] = request.table_row_path  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{tableRowPath}/cells/{index}/cellformat', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TableCellFormatResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_table_properties(self, request, **kwargs):  # noqa: E501
        """Updates a table properties.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_table_properties(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param int index: Object's index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :param TableProperties properties: The properties.
        :param str node_path: Path to node, which contains tables.
        :return: TablePropertiesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_table_properties_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.update_table_properties_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def update_table_properties_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates a table properties.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_table_properties_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param update_table_properties_request request object with parameters
        :return: TablePropertiesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501
        if request.node_path is not None:
            query_params.append((self.__downcase_first_letter('NodePath'), request.node_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{nodePath}/tables/{index}/properties', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TablePropertiesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_table_row_format(self, request, **kwargs):  # noqa: E501
        """Updates a table row format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_table_row_format(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The document name. (required)
        :param str table_path: Path to table. (required)
        :param int index: Object's index (required)
        :param str folder: Original document folder.
        :param str storage: File storage, which have to be used.
        :param str load_encoding: Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param str password: Password for opening an encrypted document.
        :param str dest_file_name: Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param str revision_author: Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param str revision_date_time: The date and time to use for revisions.
        :param TableRowFormat format: Table row format.
        :return: TableRowFormatResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_table_row_format_with_http_info(request, **kwargs)  # noqa: E501
        (data) = self.update_table_row_format_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def update_table_row_format_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates a table row format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_table_row_format_with_http_info(self, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param update_table_row_format_request request object with parameters
        :return: TableRowFormatResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params.append('async')
        params.append('_return_http_data_only')
        params.append('_preload_content')
        params.append('_request_timeout')
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

        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('Name')] = request.name  # noqa: E501
        if request.table_path is not None:
            path_params[self.__downcase_first_letter('TablePath')] = request.table_path  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('Index')] = request.index  # noqa: E501

        query_params = []
        if request.folder is not None:
            query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if request.storage is not None:
            query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501
        if request.load_encoding is not None:
            query_params.append((self.__downcase_first_letter('LoadEncoding'), request.load_encoding))  # noqa: E501
        if request.password is not None:
            query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if request.dest_file_name is not None:
            query_params.append((self.__downcase_first_letter('DestFileName'), request.dest_file_name))  # noqa: E501
        if request.revision_author is not None:
            query_params.append((self.__downcase_first_letter('RevisionAuthor'), request.revision_author))  # noqa: E501
        if request.revision_date_time is not None:
            query_params.append((self.__downcase_first_letter('RevisionDateTime'), request.revision_date_time))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/words/{name}/{tablePath}/rows/{index}/rowformat', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TableRowFormatResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    # Helper method to convert first letter to downcase
    def __downcase_first_letter(self, s):
        if len(s) == 0:
            return str
        else:
            return s[0].lower() + s[1:]

    def __request_token(self):
        config = self.api_client.configuration
        api_version = config.api_version
        config.api_version = ''
        request_url = "/oauth2/token"
        post_data = "grant_type=client_credentials" + "&client_id=" + config.api_key['app_sid'] + "&client_secret=" + config.api_key['api_key']
        data, status_code, header = self.api_client.call_api(request_url, 'POST', body=post_data, response_type='object')
        self.api_client.configuration.access_token = data['access_token']
        self.api_client.configuration.api_version = api_version
        self.api_client.configuration.refresh_token = data['refresh_token']
 