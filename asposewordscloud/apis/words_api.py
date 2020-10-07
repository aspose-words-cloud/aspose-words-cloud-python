# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="words_api.py">
#   Copyright (c) 2020 Aspose.Words for Cloud
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

    :param app_sid: app sid of client.
    :param app_key: app key of client.
    """
    def __init__(self, app_sid, app_key):
        if len(app_sid) == 0:
            raise ValueError("app_sid could not be an empty string.")
        
        if len(app_sid) == 0:
            raise ValueError("app_sid could not be an empty string.")
        
        self.api_client = ApiClient()
        self.api_client.configuration.api_key['api_key'] = app_key
        self.api_client.configuration.api_key['app_sid'] = app_sid

    def accept_all_revisions(self, request, **kwargs):  # noqa: E501
        """Accepts all revisions in document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.accept_all_revisions_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.accept_all_revisions_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def accept_all_revisions_with_http_info(self, request, **kwargs):  # noqa: E501
        """Accepts all revisions in document.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def append_document(self, request, **kwargs):  # noqa: E501
        """Appends documents to original document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : Original document name. (required)
        :param document_list DocumentEntryList : DocumentEntryList with a list of documents to append. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.append_document_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.append_document_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.append_document_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.append_document_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def append_document_with_http_info(self, request, **kwargs):  # noqa: E501
        """Appends documents to original document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request AppendDocumentRequest object with parameters
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
                    " to method append_document" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def apply_style_to_document_element(self, request, **kwargs):  # noqa: E501
        """Apply a style to the document node.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param style_apply StyleApply : Style to apply. (required)
        :param styled_node_path str : The path to the node that supports a style. Supported node types: ParagraphFormat, List, ListLevel, Table. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: WordsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.apply_style_to_document_element_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.apply_style_to_document_element_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.apply_style_to_document_element_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.apply_style_to_document_element_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def apply_style_to_document_element_with_http_info(self, request, **kwargs):  # noqa: E501
        """Apply a style to the document node.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request ApplyStyleToDocumentElementRequest object with parameters
        :return: WordsResponse
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
                    " to method apply_style_to_document_element" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def build_report(self, request, **kwargs):  # noqa: E501
        """Executes document "build report" operation.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The template name. (required)
        :param data str : A string providing a data to populate the specified template. The string must be of one of the following types: xml, json, csv. (required)
        :param report_engine_settings ReportEngineSettings : An object providing a settings of report engine. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved with autogenerated name.
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.build_report_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.build_report_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.build_report_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.build_report_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def build_report_with_http_info(self, request, **kwargs):  # noqa: E501
        """Executes document "build report" operation.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request BuildReportRequest object with parameters
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
                    " to method build_report" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def build_report_online(self, request, **kwargs):  # noqa: E501
        """Executes document "build report" online operation.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param template file : File with template. (required)
        :param data str : A string providing a data to populate the specified template. The string must be of one of the following types: xml, json, csv. (required)
        :param report_engine_settings ReportEngineSettings : An object providing a settings of report engine. (required)
        :param document_file_name str : This file name will be used when resulting document has dynamic field for document file name {filename}. If it is not set, "template" will be used instead.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.build_report_online_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.build_report_online_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.build_report_online_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.build_report_online_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def build_report_online_with_http_info(self, request, **kwargs):  # noqa: E501
        """Executes document "build report" online operation.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request BuildReportOnlineRequest object with parameters
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
                    " to method build_report_online" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def classify(self, request, **kwargs):  # noqa: E501
        """Classifies raw text.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param text str : Text to classify. (required)
        :param best_classes_count str : Number of the best classes to return.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.classify_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.classify_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def classify_with_http_info(self, request, **kwargs):  # noqa: E501
        """Classifies raw text.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def classify_document(self, request, **kwargs):  # noqa: E501
        """Classifies document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param document_name str : The document name. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.classify_document_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.classify_document_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def classify_document_with_http_info(self, request, **kwargs):  # noqa: E501
        """Classifies document.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def compare_document(self, request, **kwargs):  # noqa: E501
        """Compares document with original document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : Original document name. (required)
        :param compare_data CompareData : CompareData with a document to compare. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.compare_document_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.compare_document_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.compare_document_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.compare_document_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def compare_document_with_http_info(self, request, **kwargs):  # noqa: E501
        """Compares document with original document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request CompareDocumentRequest object with parameters
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
                    " to method compare_document" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def convert_document(self, request, **kwargs):  # noqa: E501
        """Converts document from the request's content to the specified format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param document file : Converting document. (required)
        :param format str : Format to convert. (required)
        :param storage str : Original document storage.
        :param out_path str : Path for saving operation result to the local storage.
        :param file_name_field_value str : This file name will be used when resulting document has dynamic field for document file name {filename}. If it is not set, "sourceFilename" will be used instead.
        :param fonts_location str : Folder in filestorage with custom fonts.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.convert_document_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.convert_document_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.convert_document_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.convert_document_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def convert_document_with_http_info(self, request, **kwargs):  # noqa: E501
        """Converts document from the request's content to the specified format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request ConvertDocumentRequest object with parameters
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
                    " to method convert_document" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def copy_file(self, request, **kwargs):  # noqa: E501
        """Copy file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param dest_path str : Destination file path. (required)
        :param src_path str : Source file's path e.g. '/Folder 1/file.ext' or '/Bucket/Folder 1/file.ext'. (required)
        :param src_storage_name str : Source storage name.
        :param dest_storage_name str : Destination storage name.
        :param version_id str : File version ID to copy.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.copy_file_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.copy_file_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.copy_file_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.copy_file_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def copy_file_with_http_info(self, request, **kwargs):  # noqa: E501
        """Copy file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request CopyFileRequest object with parameters
        :return: None
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
                    " to method copy_file" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def copy_folder(self, request, **kwargs):  # noqa: E501
        """Copy folder.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param dest_path str : Destination folder path e.g. '/dst'. (required)
        :param src_path str : Source folder path e.g. /Folder1. (required)
        :param src_storage_name str : Source storage name.
        :param dest_storage_name str : Destination storage name.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.copy_folder_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.copy_folder_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.copy_folder_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.copy_folder_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def copy_folder_with_http_info(self, request, **kwargs):  # noqa: E501
        """Copy folder.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request CopyFolderRequest object with parameters
        :return: None
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
                    " to method copy_folder" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def copy_style(self, request, **kwargs):  # noqa: E501
        """Copy and insert a new style to the document, returns a copied style.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param style_copy StyleCopy : Style to copy. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: StyleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.copy_style_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.copy_style_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.copy_style_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.copy_style_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def copy_style_with_http_info(self, request, **kwargs):  # noqa: E501
        """Copy and insert a new style to the document, returns a copied style.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request CopyStyleRequest object with parameters
        :return: StyleResponse
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
                    " to method copy_style" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def create_document(self, request, **kwargs):  # noqa: E501
        """Creates new document. Document is created with format which is recognized from file extensions. Supported extensions: ".doc", ".docx", ".docm", ".dot", ".dotm", ".dotx", ".flatopc", ".fopc", ".flatopc_macro", ".fopc_macro", ".flatopc_template", ".fopc_template", ".flatopc_template_macro", ".fopc_template_macro", ".wordml", ".wml", ".rtf".  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param storage str : Original document storage.
        :param file_name str : The document name.
        :param folder str : The document folder.
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.create_document_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.create_document_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.create_document_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.create_document_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def create_document_with_http_info(self, request, **kwargs):  # noqa: E501
        """Creates new document. Document is created with format which is recognized from file extensions. Supported extensions: ".doc", ".docx", ".docm", ".dot", ".dotm", ".dotx", ".flatopc", ".fopc", ".flatopc_macro", ".fopc_macro", ".flatopc_template", ".fopc_template", ".flatopc_template_macro", ".fopc_template_macro", ".wordml", ".wml", ".rtf".  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request CreateDocumentRequest object with parameters
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
                    " to method create_document" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def create_folder(self, request, **kwargs):  # noqa: E501
        """Create the folder.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param path str : Target folder's path e.g. Folder1/Folder2/. The folders will be created recursively. (required)
        :param storage_name str : Storage name.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.create_folder_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.create_folder_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.create_folder_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.create_folder_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def create_folder_with_http_info(self, request, **kwargs):  # noqa: E501
        """Create the folder.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request CreateFolderRequest object with parameters
        :return: None
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
                    " to method create_folder" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def create_or_update_document_property(self, request, **kwargs):  # noqa: E501
        """Adds new or update existing document property.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param property_name str : The property name. (required)
        :param _property DocumentPropertyCreateOrUpdate : The property with new value. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.create_or_update_document_property_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.create_or_update_document_property_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def create_or_update_document_property_with_http_info(self, request, **kwargs):  # noqa: E501
        """Adds new or update existing document property.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def delete_all_paragraph_tab_stops(self, request, **kwargs):  # noqa: E501
        """Remove all tab stops.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param index int : Object index. (required)
        :param node_path str : Path to the node which contains paragraph.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :return: TabStopsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_all_paragraph_tab_stops_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_all_paragraph_tab_stops_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.delete_all_paragraph_tab_stops_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_all_paragraph_tab_stops_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_all_paragraph_tab_stops_with_http_info(self, request, **kwargs):  # noqa: E501
        """Remove all tab stops.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request DeleteAllParagraphTabStopsRequest object with parameters
        :return: TabStopsResponse
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
                    " to method delete_all_paragraph_tab_stops" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def delete_border(self, request, **kwargs):  # noqa: E501
        """'nodePath' should refer to paragraph, cell or row.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param border_type str : Border type. (required)
        :param node_path str : Path to the node with border(node should be paragraph, cell or row).
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.delete_border_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_border_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_border_with_http_info(self, request, **kwargs):  # noqa: E501
        """'nodePath' should refer to paragraph, cell or row.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def delete_borders(self, request, **kwargs):  # noqa: E501
        """'nodePath' should refer to paragraph, cell or row.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param node_path str : Path to the node with borders(node should be paragraph, cell or row).
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.delete_borders_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_borders_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_borders_with_http_info(self, request, **kwargs):  # noqa: E501
        """'nodePath' should refer to paragraph, cell or row.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def delete_comment(self, request, **kwargs):  # noqa: E501
        """Removes comment from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param comment_index int : The comment index. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: None
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.delete_comment_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_comment_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_comment_with_http_info(self, request, **kwargs):  # noqa: E501
        """Removes comment from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request DeleteCommentRequest object with parameters
        :return: None
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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def delete_document_property(self, request, **kwargs):  # noqa: E501
        """Deletes document property.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param property_name str : The property name. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: None
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.delete_document_property_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_document_property_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_document_property_with_http_info(self, request, **kwargs):  # noqa: E501
        """Deletes document property.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request DeleteDocumentPropertyRequest object with parameters
        :return: None
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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def delete_drawing_object(self, request, **kwargs):  # noqa: E501
        """Removes drawing object from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param index int : Object index. (required)
        :param node_path str : Path to the node, which contains collection of drawing objects.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: None
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
                self.api_client.request_token()
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
        :return: None
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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def delete_field(self, request, **kwargs):  # noqa: E501
        """Deletes field from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param index int : Object index. (required)
        :param node_path str : Path to the node, which contains collection of fields.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: None
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.delete_field_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_field_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_field_with_http_info(self, request, **kwargs):  # noqa: E501
        """Deletes field from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request DeleteFieldRequest object with parameters
        :return: None
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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def delete_fields(self, request, **kwargs):  # noqa: E501
        """Removes fields from section paragraph.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param node_path str : Path to the node, which contains collection of fields.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: None
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.delete_fields_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_fields_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_fields_with_http_info(self, request, **kwargs):  # noqa: E501
        """Removes fields from section paragraph.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request DeleteFieldsRequest object with parameters
        :return: None
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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def delete_file(self, request, **kwargs):  # noqa: E501
        """Delete file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param path str : Path of the file including file name and extension e.g. /Folder1/file.ext. (required)
        :param storage_name str : Storage name.
        :param version_id str : File version ID to delete.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_file_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_file_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.delete_file_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_file_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_file_with_http_info(self, request, **kwargs):  # noqa: E501
        """Delete file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request DeleteFileRequest object with parameters
        :return: None
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
                    " to method delete_file" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def delete_folder(self, request, **kwargs):  # noqa: E501
        """Delete folder.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param path str : Folder path e.g. /Folder1s. (required)
        :param storage_name str : Storage name.
        :param recursive bool : Enable to delete folders, subfolders and files.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_folder_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_folder_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.delete_folder_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_folder_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_folder_with_http_info(self, request, **kwargs):  # noqa: E501
        """Delete folder.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request DeleteFolderRequest object with parameters
        :return: None
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
                    " to method delete_folder" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def delete_footnote(self, request, **kwargs):  # noqa: E501
        """Removes footnote from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param index int : Object index. (required)
        :param node_path str : Path to the node, which contains collection of footnotes.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: None
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
                self.api_client.request_token()
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
        :return: None
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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def delete_form_field(self, request, **kwargs):  # noqa: E501
        """Removes form field from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param index int : Object index. (required)
        :param node_path str : Path to the node that contains collection of formfields.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: None
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
                self.api_client.request_token()
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
        :return: None
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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def delete_header_footer(self, request, **kwargs):  # noqa: E501
        """Deletes header/footer from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param section_path str : Path to parent section. (required)
        :param index int : Object index. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: None
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.delete_header_footer_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_header_footer_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_header_footer_with_http_info(self, request, **kwargs):  # noqa: E501
        """Deletes header/footer from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request DeleteHeaderFooterRequest object with parameters
        :return: None
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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def delete_headers_footers(self, request, **kwargs):  # noqa: E501
        """Deletes document headers and footers.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param section_path str : Path to parent section. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :param headers_footers_types str : List of types of headers and footers.
        :return: None
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.delete_headers_footers_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_headers_footers_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_headers_footers_with_http_info(self, request, **kwargs):  # noqa: E501
        """Deletes document headers and footers.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request DeleteHeadersFootersRequest object with parameters
        :return: None
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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def delete_macros(self, request, **kwargs):  # noqa: E501
        """Removes macros from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_macros_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_macros_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.delete_macros_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_macros_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_macros_with_http_info(self, request, **kwargs):  # noqa: E501
        """Removes macros from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request DeleteMacrosRequest object with parameters
        :return: None
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
                    " to method delete_macros" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def delete_office_math_object(self, request, **kwargs):  # noqa: E501
        """Removes OfficeMath object from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param index int : Object index. (required)
        :param node_path str : Path to the node, which contains collection of OfficeMath objects.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: None
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
                self.api_client.request_token()
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
        :return: None
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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def delete_paragraph(self, request, **kwargs):  # noqa: E501
        """Removes paragraph from section.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The file name. (required)
        :param index int : Object index. (required)
        :param node_path str : Path to the node which contains paragraphs.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: None
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.delete_paragraph_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_paragraph_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_paragraph_with_http_info(self, request, **kwargs):  # noqa: E501
        """Removes paragraph from section.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request DeleteParagraphRequest object with parameters
        :return: None
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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def delete_paragraph_list_format(self, request, **kwargs):  # noqa: E501
        """Delete paragraph list format, returns updated list format properties.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param index int : Object index. (required)
        :param node_path str : Path to the node which contains paragraphs.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: ParagraphListFormatResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_paragraph_list_format_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_paragraph_list_format_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.delete_paragraph_list_format_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_paragraph_list_format_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_paragraph_list_format_with_http_info(self, request, **kwargs):  # noqa: E501
        """Delete paragraph list format, returns updated list format properties.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request DeleteParagraphListFormatRequest object with parameters
        :return: ParagraphListFormatResponse
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
                    " to method delete_paragraph_list_format" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def delete_paragraph_tab_stop(self, request, **kwargs):  # noqa: E501
        """Remove the i-th tab stop.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param position float : a tab stop position to remove. (required)
        :param index int : Object index. (required)
        :param node_path str : Path to the node which contains paragraph.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :return: TabStopsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_paragraph_tab_stop_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_paragraph_tab_stop_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.delete_paragraph_tab_stop_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_paragraph_tab_stop_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_paragraph_tab_stop_with_http_info(self, request, **kwargs):  # noqa: E501
        """Remove the i-th tab stop.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request DeleteParagraphTabStopRequest object with parameters
        :return: TabStopsResponse
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
                    " to method delete_paragraph_tab_stop" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def delete_run(self, request, **kwargs):  # noqa: E501
        """Removes run from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param paragraph_path str : Path to parent paragraph. (required)
        :param index int : Object index. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: None
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
                self.api_client.request_token()
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
        :return: None
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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def delete_section(self, request, **kwargs):  # noqa: E501
        """Removes section from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param section_index int : Section index. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_section_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_section_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.delete_section_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_section_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_section_with_http_info(self, request, **kwargs):  # noqa: E501
        """Removes section from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request DeleteSectionRequest object with parameters
        :return: None
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
                    " to method delete_section" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def delete_table(self, request, **kwargs):  # noqa: E501
        """Deletes a table.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param index int : Object index. (required)
        :param node_path str : Path to the node, which contains tables.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: None
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.delete_table_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_table_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_table_with_http_info(self, request, **kwargs):  # noqa: E501
        """Deletes a table.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request DeleteTableRequest object with parameters
        :return: None
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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def delete_table_cell(self, request, **kwargs):  # noqa: E501
        """Deletes a table cell.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param table_row_path str : Path to table row. (required)
        :param index int : Object index. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: None
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.delete_table_cell_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_table_cell_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_table_cell_with_http_info(self, request, **kwargs):  # noqa: E501
        """Deletes a table cell.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request DeleteTableCellRequest object with parameters
        :return: None
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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def delete_table_row(self, request, **kwargs):  # noqa: E501
        """Deletes a table row.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param table_path str : Path to table. (required)
        :param index int : Object index. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: None
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.delete_table_row_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_table_row_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_table_row_with_http_info(self, request, **kwargs):  # noqa: E501
        """Deletes a table row.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request DeleteTableRowRequest object with parameters
        :return: None
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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def delete_watermark(self, request, **kwargs):  # noqa: E501
        """Deletes watermark (for deleting last watermark from the document).  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_watermark_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_watermark_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.delete_watermark_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_watermark_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_watermark_with_http_info(self, request, **kwargs):  # noqa: E501
        """Deletes watermark (for deleting last watermark from the document).  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request DeleteWatermarkRequest object with parameters
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
                    " to method delete_watermark" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def download_file(self, request, **kwargs):  # noqa: E501
        """Download file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param path str : Path of the file including the file name and extension e.g. /folder1/file.ext. (required)
        :param storage_name str : Storage name.
        :param version_id str : File version ID to download.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.download_file_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.download_file_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.download_file_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.download_file_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def download_file_with_http_info(self, request, **kwargs):  # noqa: E501
        """Download file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request DownloadFileRequest object with parameters
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
                    " to method download_file" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def execute_mail_merge(self, request, **kwargs):  # noqa: E501
        """Executes document mail merge operation.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The template name. (required)
        :param data str : Mail merge data.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param with_regions bool : With regions flag.
        :param mail_merge_data_file str : Mail merge data file.
        :param cleanup str : Clean up options.
        :param use_whole_paragraph_as_region bool : Gets or sets a value indicating whether paragraph with TableStart or. TableEnd field should be fully included into mail merge region or particular range between TableStart and TableEnd fields. The default value is true.
        :param dest_file_name str : Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved with autogenerated name.
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.execute_mail_merge_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.execute_mail_merge_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.execute_mail_merge_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.execute_mail_merge_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def execute_mail_merge_with_http_info(self, request, **kwargs):  # noqa: E501
        """Executes document mail merge operation.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request ExecuteMailMergeRequest object with parameters
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
                    " to method execute_mail_merge" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def execute_mail_merge_online(self, request, **kwargs):  # noqa: E501
        """Executes document mail merge online.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param template file : File with template. (required)
        :param data file : File with mailmerge data. (required)
        :param with_regions bool : With regions flag.
        :param cleanup str : Clean up options.
        :param document_file_name str : This file name will be used when resulting document has dynamic field for document file name {filename}. If it is not set, "template" will be used instead.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.execute_mail_merge_online_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.execute_mail_merge_online_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.execute_mail_merge_online_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.execute_mail_merge_online_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def execute_mail_merge_online_with_http_info(self, request, **kwargs):  # noqa: E501
        """Executes document mail merge online.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request ExecuteMailMergeOnlineRequest object with parameters
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
                    " to method execute_mail_merge_online" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_available_fonts(self, request, **kwargs):  # noqa: E501
        """Gets the list of fonts, available for document processing.  # noqa: E501

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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_available_fonts_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_available_fonts_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_available_fonts_with_http_info(self, request, **kwargs):  # noqa: E501
        """Gets the list of fonts, available for document processing.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_bookmark_by_name(self, request, **kwargs):  # noqa: E501
        """Reads document bookmark data by its name.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param bookmark_name str : The bookmark name. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :return: BookmarkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_bookmark_by_name_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_bookmark_by_name_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_bookmark_by_name_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_bookmark_by_name_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_bookmark_by_name_with_http_info(self, request, **kwargs):  # noqa: E501
        """Reads document bookmark data by its name.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetBookmarkByNameRequest object with parameters
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
                    " to method get_bookmark_by_name" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_bookmarks(self, request, **kwargs):  # noqa: E501
        """Reads document bookmarks common info.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :return: BookmarksResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_bookmarks_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_bookmarks_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_bookmarks_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_bookmarks_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_bookmarks_with_http_info(self, request, **kwargs):  # noqa: E501
        """Reads document bookmarks common info.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetBookmarksRequest object with parameters
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
                    " to method get_bookmarks" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_border(self, request, **kwargs):  # noqa: E501
        """'nodePath' should refer to paragraph, cell or row.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param border_type str : Border type. (required)
        :param node_path str : Path to the node with border(node should be paragraph, cell or row).
        :param folder str : Original document folder.
        :param storage str : Original document storage.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_border_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_border_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_border_with_http_info(self, request, **kwargs):  # noqa: E501
        """'nodePath' should refer to paragraph, cell or row.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_borders(self, request, **kwargs):  # noqa: E501
        """'nodePath' should refer to paragraph, cell or row.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param node_path str : Path to the node with borders (node should be paragraph, cell or row).
        :param folder str : Original document folder.
        :param storage str : Original document storage.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_borders_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_borders_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_borders_with_http_info(self, request, **kwargs):  # noqa: E501
        """'nodePath' should refer to paragraph, cell or row.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_comment(self, request, **kwargs):  # noqa: E501
        """Gets comment from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param comment_index int : The comment index. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_comment_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_comment_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_comment_with_http_info(self, request, **kwargs):  # noqa: E501
        """Gets comment from document.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_comments(self, request, **kwargs):  # noqa: E501
        """Gets comments from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_comments_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_comments_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_comments_with_http_info(self, request, **kwargs):  # noqa: E501
        """Gets comments from document.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_document(self, request, **kwargs):  # noqa: E501
        """Reads document common info.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param document_name str : The document name. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_document_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_document_with_http_info(self, request, **kwargs):  # noqa: E501
        """Reads document common info.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_document_drawing_object_by_index(self, request, **kwargs):  # noqa: E501
        """Reads document drawing object common info by its index or convert to format specified.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param index int : Object index. (required)
        :param node_path str : Path to the node, which contains collection of drawing objects.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_document_drawing_object_by_index_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_drawing_object_by_index_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_document_drawing_object_by_index_with_http_info(self, request, **kwargs):  # noqa: E501
        """Reads document drawing object common info by its index or convert to format specified.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_document_drawing_object_image_data(self, request, **kwargs):  # noqa: E501
        """Reads drawing object image data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param index int : Object index. (required)
        :param node_path str : Path to the node, which contains collection of drawing objects.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_document_drawing_object_image_data_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_drawing_object_image_data_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_document_drawing_object_image_data_with_http_info(self, request, **kwargs):  # noqa: E501
        """Reads drawing object image data.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_document_drawing_object_ole_data(self, request, **kwargs):  # noqa: E501
        """Gets drawing object OLE data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param index int : Object index. (required)
        :param node_path str : Path to the node, which contains collection of drawing objects.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_document_drawing_object_ole_data_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_drawing_object_ole_data_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_document_drawing_object_ole_data_with_http_info(self, request, **kwargs):  # noqa: E501
        """Gets drawing object OLE data.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_document_drawing_objects(self, request, **kwargs):  # noqa: E501
        """Reads document drawing objects common info.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param node_path str : Path to the node, which contains collection of drawing objects.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_document_drawing_objects_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_drawing_objects_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_document_drawing_objects_with_http_info(self, request, **kwargs):  # noqa: E501
        """Reads document drawing objects common info.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_document_field_names(self, request, **kwargs):  # noqa: E501
        """Reads document field names.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The template name. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param use_non_merge_fields bool : If true, result includes "mustache" field names.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_document_field_names_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_field_names_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_document_field_names_with_http_info(self, request, **kwargs):  # noqa: E501
        """Reads document field names.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_document_field_names_online(self, request, **kwargs):  # noqa: E501
        """Reads document field names.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param template file : File with template. (required)
        :param use_non_merge_fields bool : Use non merge fields or not.
        :return: FieldNamesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_document_field_names_online_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_field_names_online_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_document_field_names_online_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_field_names_online_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_document_field_names_online_with_http_info(self, request, **kwargs):  # noqa: E501
        """Reads document field names.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetDocumentFieldNamesOnlineRequest object with parameters
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
                    " to method get_document_field_names_online" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_document_hyperlink_by_index(self, request, **kwargs):  # noqa: E501
        """Reads document hyperlink by its index.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param hyperlink_index int : The hyperlink index. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_document_hyperlink_by_index_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_hyperlink_by_index_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_document_hyperlink_by_index_with_http_info(self, request, **kwargs):  # noqa: E501
        """Reads document hyperlink by its index.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_document_hyperlinks(self, request, **kwargs):  # noqa: E501
        """Reads document hyperlinks common info.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_document_hyperlinks_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_hyperlinks_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_document_hyperlinks_with_http_info(self, request, **kwargs):  # noqa: E501
        """Reads document hyperlinks common info.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_document_properties(self, request, **kwargs):  # noqa: E501
        """Reads document properties info.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document's name. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_document_properties_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_properties_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_document_properties_with_http_info(self, request, **kwargs):  # noqa: E501
        """Reads document properties info.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_document_property(self, request, **kwargs):  # noqa: E501
        """Reads document property info by the property name.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param property_name str : The property name. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_document_property_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_property_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_document_property_with_http_info(self, request, **kwargs):  # noqa: E501
        """Reads document property info by the property name.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_document_protection(self, request, **kwargs):  # noqa: E501
        """Reads document protection common info.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_document_protection_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_protection_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_document_protection_with_http_info(self, request, **kwargs):  # noqa: E501
        """Reads document protection common info.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_document_statistics(self, request, **kwargs):  # noqa: E501
        """Reads document statistics.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param include_comments bool : Support including/excluding comments from the WordCount. Default value is "false".
        :param include_footnotes bool : Support including/excluding footnotes from the WordCount. Default value is "false".
        :param include_text_in_shapes bool : Support including/excluding shape's text from the WordCount. Default value is "false".
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_document_statistics_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_statistics_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_document_statistics_with_http_info(self, request, **kwargs):  # noqa: E501
        """Reads document statistics.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_document_with_format(self, request, **kwargs):  # noqa: E501
        """Exports the document into the specified format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param format str : The destination format. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param out_path str : Path to save the result.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_document_with_format_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_with_format_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_document_with_format_with_http_info(self, request, **kwargs):  # noqa: E501
        """Exports the document into the specified format.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_field(self, request, **kwargs):  # noqa: E501
        """Gets field from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param index int : Object index. (required)
        :param node_path str : Path to the node, which contains collection of fields.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_field_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_field_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_field_with_http_info(self, request, **kwargs):  # noqa: E501
        """Gets field from document.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_fields(self, request, **kwargs):  # noqa: E501
        """Get fields from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param node_path str : Path to the node, which contains collection of fields.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
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
                self.api_client.request_token()
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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_files_list(self, request, **kwargs):  # noqa: E501
        """Get all files and folders within a folder.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param path str : Folder path e.g. /Folder1. (required)
        :param storage_name str : Storage name.
        :return: FilesList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_files_list_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_files_list_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_files_list_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_files_list_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_files_list_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get all files and folders within a folder.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetFilesListRequest object with parameters
        :return: FilesList
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
                    " to method get_files_list" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_footnote(self, request, **kwargs):  # noqa: E501
        """Reads footnote by index.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param index int : Object index. (required)
        :param node_path str : Path to the node, which contains collection of footnotes.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_footnote_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_footnote_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_footnote_with_http_info(self, request, **kwargs):  # noqa: E501
        """Reads footnote by index.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_footnotes(self, request, **kwargs):  # noqa: E501
        """Gets footnotes from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param node_path str : Path to the node, which contains collection of footnotes.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_footnotes_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_footnotes_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_footnotes_with_http_info(self, request, **kwargs):  # noqa: E501
        """Gets footnotes from document.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_form_field(self, request, **kwargs):  # noqa: E501
        """Returns representation of an one of the form field.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param index int : Object index. (required)
        :param node_path str : Path to the node that contains collection of formfields.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
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
                self.api_client.request_token()
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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_form_fields(self, request, **kwargs):  # noqa: E501
        """Gets form fields from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param node_path str : Path to the node containing collection of form fields.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_form_fields_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_form_fields_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_form_fields_with_http_info(self, request, **kwargs):  # noqa: E501
        """Gets form fields from document.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_header_footer(self, request, **kwargs):  # noqa: E501
        """Returns a header/footer from the document by index.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param header_footer_index int : Header/footer index. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_header_footer_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_header_footer_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_header_footer_with_http_info(self, request, **kwargs):  # noqa: E501
        """Returns a header/footer from the document by index.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_header_footer_of_section(self, request, **kwargs):  # noqa: E501
        """Returns a header/footer from the document section.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param header_footer_index int : Header/footer index. (required)
        :param section_index int : Section index. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_header_footer_of_section_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_header_footer_of_section_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_header_footer_of_section_with_http_info(self, request, **kwargs):  # noqa: E501
        """Returns a header/footer from the document section.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_header_footers(self, request, **kwargs):  # noqa: E501
        """Returns a list of header/footers from the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param section_path str : Path to parent section. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_header_footers_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_header_footers_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_header_footers_with_http_info(self, request, **kwargs):  # noqa: E501
        """Returns a list of header/footers from the document.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_list(self, request, **kwargs):  # noqa: E501
        """This resource represents one of the lists contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param list_id int : List unique identifier. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :return: ListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_list_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_list_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_list_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_list_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_list_with_http_info(self, request, **kwargs):  # noqa: E501
        """This resource represents one of the lists contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetListRequest object with parameters
        :return: ListResponse
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
                    " to method get_list" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_lists(self, request, **kwargs):  # noqa: E501
        """Returns a list of lists that are contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :return: ListsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_lists_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_lists_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_lists_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_lists_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_lists_with_http_info(self, request, **kwargs):  # noqa: E501
        """Returns a list of lists that are contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetListsRequest object with parameters
        :return: ListsResponse
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
                    " to method get_lists" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_office_math_object(self, request, **kwargs):  # noqa: E501
        """Reads OfficeMath object by index.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param index int : Object index. (required)
        :param node_path str : Path to the node, which contains collection of OfficeMath objects.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_office_math_object_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_office_math_object_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_office_math_object_with_http_info(self, request, **kwargs):  # noqa: E501
        """Reads OfficeMath object by index.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_office_math_objects(self, request, **kwargs):  # noqa: E501
        """Gets OfficeMath objects from document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param node_path str : Path to the node, which contains collection of OfficeMath objects.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_office_math_objects_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_office_math_objects_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_office_math_objects_with_http_info(self, request, **kwargs):  # noqa: E501
        """Gets OfficeMath objects from document.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_paragraph(self, request, **kwargs):  # noqa: E501
        """This resource represents one of the paragraphs contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param index int : Object index. (required)
        :param node_path str : Path to the node which contains paragraphs.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :return: ParagraphResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_paragraph_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_paragraph_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_paragraph_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_paragraph_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_paragraph_with_http_info(self, request, **kwargs):  # noqa: E501
        """This resource represents one of the paragraphs contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetParagraphRequest object with parameters
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
                    " to method get_paragraph" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_paragraph_format(self, request, **kwargs):  # noqa: E501
        """Represents all the formatting for a paragraph.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param index int : Object index. (required)
        :param node_path str : Path to the node which contains paragraphs.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :return: ParagraphFormatResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_paragraph_format_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_paragraph_format_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_paragraph_format_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_paragraph_format_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_paragraph_format_with_http_info(self, request, **kwargs):  # noqa: E501
        """Represents all the formatting for a paragraph.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetParagraphFormatRequest object with parameters
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
                    " to method get_paragraph_format" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_paragraph_list_format(self, request, **kwargs):  # noqa: E501
        """Represents list format for a paragraph.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param index int : Object index. (required)
        :param node_path str : Path to the node which contains paragraphs.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :return: ParagraphListFormatResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_paragraph_list_format_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_paragraph_list_format_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_paragraph_list_format_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_paragraph_list_format_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_paragraph_list_format_with_http_info(self, request, **kwargs):  # noqa: E501
        """Represents list format for a paragraph.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetParagraphListFormatRequest object with parameters
        :return: ParagraphListFormatResponse
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
                    " to method get_paragraph_list_format" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_paragraphs(self, request, **kwargs):  # noqa: E501
        """Returns a list of paragraphs that are contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param node_path str : Path to the node which contains paragraphs.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :return: ParagraphLinkCollectionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_paragraphs_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_paragraphs_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_paragraphs_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_paragraphs_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_paragraphs_with_http_info(self, request, **kwargs):  # noqa: E501
        """Returns a list of paragraphs that are contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetParagraphsRequest object with parameters
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
                    " to method get_paragraphs" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_paragraph_tab_stops(self, request, **kwargs):  # noqa: E501
        """Get all tab stops for the paragraph.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param index int : Object index. (required)
        :param node_path str : Path to the node which contains paragraph.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :return: TabStopsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_paragraph_tab_stops_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_paragraph_tab_stops_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_paragraph_tab_stops_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_paragraph_tab_stops_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_paragraph_tab_stops_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get all tab stops for the paragraph.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetParagraphTabStopsRequest object with parameters
        :return: TabStopsResponse
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
                    " to method get_paragraph_tab_stops" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_range_text(self, request, **kwargs):  # noqa: E501
        """Gets the text from the range.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document. (required)
        :param range_start_identifier str : The range start identifier. Identifier is the value of the "nodeId" field, which every document node has, extended with the prefix "id". It looks like "id0.0.7". Also values like "image5" and "table3" can be used as an identifier for images and tables, where the number is an index of the image/table. (required)
        :param range_end_identifier str : The range end identifier.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :return: RangeTextResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_range_text_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_range_text_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_range_text_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_range_text_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_range_text_with_http_info(self, request, **kwargs):  # noqa: E501
        """Gets the text from the range.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetRangeTextRequest object with parameters
        :return: RangeTextResponse
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
                    " to method get_range_text" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_run(self, request, **kwargs):  # noqa: E501
        """This resource represents run of text contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param paragraph_path str : Path to parent paragraph. (required)
        :param index int : Object index. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :return: RunResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_run_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_run_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_run_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_run_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_run_with_http_info(self, request, **kwargs):  # noqa: E501
        """This resource represents run of text contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetRunRequest object with parameters
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
                    " to method get_run" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_run_font(self, request, **kwargs):  # noqa: E501
        """This resource represents font of run.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param paragraph_path str : Path to parent paragraph. (required)
        :param index int : Object index. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :return: FontResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_run_font_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_run_font_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_run_font_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_run_font_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_run_font_with_http_info(self, request, **kwargs):  # noqa: E501
        """This resource represents font of run.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetRunFontRequest object with parameters
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
                    " to method get_run_font" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_runs(self, request, **kwargs):  # noqa: E501
        """This resource represents collection of runs in the paragraph.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param paragraph_path str : Path to parent paragraph. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :return: RunsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_runs_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_runs_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_runs_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_runs_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_runs_with_http_info(self, request, **kwargs):  # noqa: E501
        """This resource represents collection of runs in the paragraph.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetRunsRequest object with parameters
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
                    " to method get_runs" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_section(self, request, **kwargs):  # noqa: E501
        """Gets document section by index.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param section_index int : Section index. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_section_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_section_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_section_with_http_info(self, request, **kwargs):  # noqa: E501
        """Gets document section by index.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_section_page_setup(self, request, **kwargs):  # noqa: E501
        """Gets page setup of section.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param section_index int : Section index. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_section_page_setup_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_section_page_setup_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_section_page_setup_with_http_info(self, request, **kwargs):  # noqa: E501
        """Gets page setup of section.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_sections(self, request, **kwargs):  # noqa: E501
        """Returns a list of sections that are contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_sections_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_sections_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_sections_with_http_info(self, request, **kwargs):  # noqa: E501
        """Returns a list of sections that are contained in the document.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_style(self, request, **kwargs):  # noqa: E501
        """This resource represents one of the styles contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param style_name str : Style name. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :return: StyleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_style_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_style_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_style_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_style_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_style_with_http_info(self, request, **kwargs):  # noqa: E501
        """This resource represents one of the styles contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetStyleRequest object with parameters
        :return: StyleResponse
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
                    " to method get_style" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_style_from_document_element(self, request, **kwargs):  # noqa: E501
        """Gets a style from the document node.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param styled_node_path str : The path to the node that supports a style. Supported node types: ParagraphFormat, List, ListLevel, Table. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :return: StyleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_style_from_document_element_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_style_from_document_element_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_style_from_document_element_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_style_from_document_element_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_style_from_document_element_with_http_info(self, request, **kwargs):  # noqa: E501
        """Gets a style from the document node.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetStyleFromDocumentElementRequest object with parameters
        :return: StyleResponse
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
                    " to method get_style_from_document_element" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_styles(self, request, **kwargs):  # noqa: E501
        """Returns a list of styles contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :return: StylesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_styles_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_styles_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_styles_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_styles_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_styles_with_http_info(self, request, **kwargs):  # noqa: E501
        """Returns a list of styles contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetStylesRequest object with parameters
        :return: StylesResponse
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
                    " to method get_styles" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_table(self, request, **kwargs):  # noqa: E501
        """Returns a table.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param index int : Object index. (required)
        :param node_path str : Path to the node, which contains tables.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_table_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_table_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_table_with_http_info(self, request, **kwargs):  # noqa: E501
        """Returns a table.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_table_cell(self, request, **kwargs):  # noqa: E501
        """Returns a table cell.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param table_row_path str : Path to table row. (required)
        :param index int : Object index. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_table_cell_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_table_cell_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_table_cell_with_http_info(self, request, **kwargs):  # noqa: E501
        """Returns a table cell.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_table_cell_format(self, request, **kwargs):  # noqa: E501
        """Returns a table cell format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param table_row_path str : Path to table row. (required)
        :param index int : Object index. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_table_cell_format_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_table_cell_format_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_table_cell_format_with_http_info(self, request, **kwargs):  # noqa: E501
        """Returns a table cell format.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_table_properties(self, request, **kwargs):  # noqa: E501
        """Returns a table properties.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param index int : Object index. (required)
        :param node_path str : Path to the node, which contains tables.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_table_properties_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_table_properties_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_table_properties_with_http_info(self, request, **kwargs):  # noqa: E501
        """Returns a table properties.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_table_row(self, request, **kwargs):  # noqa: E501
        """Returns a table row.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param table_path str : Path to table. (required)
        :param index int : Object index. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_table_row_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_table_row_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_table_row_with_http_info(self, request, **kwargs):  # noqa: E501
        """Returns a table row.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_table_row_format(self, request, **kwargs):  # noqa: E501
        """Returns a table row format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param table_path str : Path to table. (required)
        :param index int : Object index. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_table_row_format_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_table_row_format_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_table_row_format_with_http_info(self, request, **kwargs):  # noqa: E501
        """Returns a table row format.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def get_tables(self, request, **kwargs):  # noqa: E501
        """Returns a list of tables that are contained in the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param node_path str : Path to the node, which contains tables.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.get_tables_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_tables_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_tables_with_http_info(self, request, **kwargs):  # noqa: E501
        """Returns a list of tables that are contained in the document.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def insert_comment(self, request, **kwargs):  # noqa: E501
        """Adds comment to document, returns inserted comment data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param comment CommentInsert : The comment data. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: CommentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.insert_comment_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.insert_comment_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.insert_comment_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.insert_comment_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def insert_comment_with_http_info(self, request, **kwargs):  # noqa: E501
        """Adds comment to document, returns inserted comment data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request InsertCommentRequest object with parameters
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
                    " to method insert_comment" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def insert_drawing_object(self, request, **kwargs):  # noqa: E501
        """Adds drawing object to document, returns added  drawing object's data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param drawing_object DrawingObjectInsert : Drawing object parameters. (required)
        :param image_file file : File with image. (required)
        :param node_path str : Path to the node, which contains collection of drawing objects.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: DrawingObjectResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.insert_drawing_object_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.insert_drawing_object_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.insert_drawing_object_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.insert_drawing_object_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def insert_drawing_object_with_http_info(self, request, **kwargs):  # noqa: E501
        """Adds drawing object to document, returns added  drawing object's data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request InsertDrawingObjectRequest object with parameters
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
                    " to method insert_drawing_object" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def insert_field(self, request, **kwargs):  # noqa: E501
        """Adds field to document, returns inserted field's data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param field FieldInsert : Field data. (required)
        :param node_path str : Path to the node, which contains collection of fields.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :param insert_before_node str : Field will be inserted before node with id="nodeId".
        :return: FieldResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.insert_field_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.insert_field_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.insert_field_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.insert_field_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def insert_field_with_http_info(self, request, **kwargs):  # noqa: E501
        """Adds field to document, returns inserted field's data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request InsertFieldRequest object with parameters
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
                    " to method insert_field" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def insert_footnote(self, request, **kwargs):  # noqa: E501
        """Adds footnote to document, returns added footnote's data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param footnote_dto FootnoteInsert : Footnote data. (required)
        :param node_path str : Path to the node, which contains collection of footnotes.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: FootnoteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.insert_footnote_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.insert_footnote_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.insert_footnote_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.insert_footnote_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def insert_footnote_with_http_info(self, request, **kwargs):  # noqa: E501
        """Adds footnote to document, returns added footnote's data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request InsertFootnoteRequest object with parameters
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
                    " to method insert_footnote" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def insert_form_field(self, request, **kwargs):  # noqa: E501
        """Adds form field to paragraph, returns added form field's data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param form_field FormField : From field data. (required)
        :param node_path str : Path to the node that contains collection of formfields.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :param insert_before_node str : Form field will be inserted before node with index.
        :return: FormFieldResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.insert_form_field_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.insert_form_field_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.insert_form_field_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.insert_form_field_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def insert_form_field_with_http_info(self, request, **kwargs):  # noqa: E501
        """Adds form field to paragraph, returns added form field's data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request InsertFormFieldRequest object with parameters
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
                    " to method insert_form_field" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def insert_header_footer(self, request, **kwargs):  # noqa: E501
        """Inserts to document header or footer.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param header_footer_type str : Type of header/footer. (required)
        :param section_path str : Path to parent section. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: HeaderFooterResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.insert_header_footer_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.insert_header_footer_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.insert_header_footer_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.insert_header_footer_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def insert_header_footer_with_http_info(self, request, **kwargs):  # noqa: E501
        """Inserts to document header or footer.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request InsertHeaderFooterRequest object with parameters
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
                    " to method insert_header_footer" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def insert_list(self, request, **kwargs):  # noqa: E501
        """Adds list to document, returns added list's data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param list_insert ListInsert : List to insert. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: ListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.insert_list_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.insert_list_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.insert_list_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.insert_list_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def insert_list_with_http_info(self, request, **kwargs):  # noqa: E501
        """Adds list to document, returns added list's data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request InsertListRequest object with parameters
        :return: ListResponse
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
                    " to method insert_list" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def insert_or_update_paragraph_tab_stop(self, request, **kwargs):  # noqa: E501
        """Insert or resplace tab stop if a tab stop with the position exists.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param dto TabStopInsert : Paragraph tab stop. (required)
        :param index int : Object index. (required)
        :param node_path str : Path to the node which contains paragraph.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :return: TabStopsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.insert_or_update_paragraph_tab_stop_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.insert_or_update_paragraph_tab_stop_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.insert_or_update_paragraph_tab_stop_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.insert_or_update_paragraph_tab_stop_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def insert_or_update_paragraph_tab_stop_with_http_info(self, request, **kwargs):  # noqa: E501
        """Insert or resplace tab stop if a tab stop with the position exists.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request InsertOrUpdateParagraphTabStopRequest object with parameters
        :return: TabStopsResponse
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
                    " to method insert_or_update_paragraph_tab_stop" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def insert_page_numbers(self, request, **kwargs):  # noqa: E501
        """Inserts document page numbers.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : A document name. (required)
        :param page_number PageNumber : PageNumber with the page numbers settings. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.insert_page_numbers_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.insert_page_numbers_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.insert_page_numbers_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.insert_page_numbers_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def insert_page_numbers_with_http_info(self, request, **kwargs):  # noqa: E501
        """Inserts document page numbers.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request InsertPageNumbersRequest object with parameters
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
                    " to method insert_page_numbers" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def insert_paragraph(self, request, **kwargs):  # noqa: E501
        """Adds paragraph to document, returns added paragraph's data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param paragraph ParagraphInsert : Paragraph data. (required)
        :param node_path str : Path to the node which contains paragraphs.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :param insert_before_node str : Paragraph will be inserted before node with index.
        :return: ParagraphResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.insert_paragraph_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.insert_paragraph_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.insert_paragraph_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.insert_paragraph_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def insert_paragraph_with_http_info(self, request, **kwargs):  # noqa: E501
        """Adds paragraph to document, returns added paragraph's data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request InsertParagraphRequest object with parameters
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
                    " to method insert_paragraph" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def insert_run(self, request, **kwargs):  # noqa: E501
        """Adds run to document, returns added paragraph's data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param paragraph_path str : Path to parent paragraph. (required)
        :param run RunInsert : Run data. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
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
                return self.insert_run_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.insert_run_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.insert_run_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.insert_run_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def insert_run_with_http_info(self, request, **kwargs):  # noqa: E501
        """Adds run to document, returns added paragraph's data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request InsertRunRequest object with parameters
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
                    " to method insert_run" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def insert_style(self, request, **kwargs):  # noqa: E501
        """Adds a style to the document, returns an added style.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param style_insert StyleInsert : Style to insert. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: StyleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.insert_style_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.insert_style_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.insert_style_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.insert_style_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def insert_style_with_http_info(self, request, **kwargs):  # noqa: E501
        """Adds a style to the document, returns an added style.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request InsertStyleRequest object with parameters
        :return: StyleResponse
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
                    " to method insert_style" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def insert_table(self, request, **kwargs):  # noqa: E501
        """Adds table to document, returns added table's data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param table TableInsert : Table parameters/. (required)
        :param node_path str : Path to the node, which contains tables.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.insert_table_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.insert_table_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def insert_table_with_http_info(self, request, **kwargs):  # noqa: E501
        """Adds table to document, returns added table's data.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def insert_table_cell(self, request, **kwargs):  # noqa: E501
        """Adds table cell to table, returns added cell's data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param cell TableCellInsert : Table cell parameters/. (required)
        :param table_row_path str : Path to table row. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.insert_table_cell_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.insert_table_cell_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def insert_table_cell_with_http_info(self, request, **kwargs):  # noqa: E501
        """Adds table cell to table, returns added cell's data.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def insert_table_row(self, request, **kwargs):  # noqa: E501
        """Adds table row to table, returns added row's data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param row TableRowInsert : Table row parameters/. (required)
        :param table_path str : Path to table. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.insert_table_row_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.insert_table_row_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def insert_table_row_with_http_info(self, request, **kwargs):  # noqa: E501
        """Adds table row to table, returns added row's data.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def insert_watermark_image(self, request, **kwargs):  # noqa: E501
        """Inserts document watermark image.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param image_file file : File with image.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
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
                return self.insert_watermark_image_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.insert_watermark_image_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.insert_watermark_image_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.insert_watermark_image_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def insert_watermark_image_with_http_info(self, request, **kwargs):  # noqa: E501
        """Inserts document watermark image.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request InsertWatermarkImageRequest object with parameters
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
                    " to method insert_watermark_image" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def insert_watermark_text(self, request, **kwargs):  # noqa: E501
        """Inserts document watermark text.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param watermark_text WatermarkText : WatermarkText with the watermark data. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.insert_watermark_text_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.insert_watermark_text_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.insert_watermark_text_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.insert_watermark_text_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def insert_watermark_text_with_http_info(self, request, **kwargs):  # noqa: E501
        """Inserts document watermark text.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request InsertWatermarkTextRequest object with parameters
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
                    " to method insert_watermark_text" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def load_web_document(self, request, **kwargs):  # noqa: E501
        """Loads new document from web into the file with any supported format of data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param data LoadWebDocumentData : Parameters of loading. (required)
        :param storage str : Original document storage.
        :return: SaveResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.load_web_document_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.load_web_document_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.load_web_document_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.load_web_document_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def load_web_document_with_http_info(self, request, **kwargs):  # noqa: E501
        """Loads new document from web into the file with any supported format of data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request LoadWebDocumentRequest object with parameters
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
                    " to method load_web_document" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def move_file(self, request, **kwargs):  # noqa: E501
        """Move file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param dest_path str : Destination file path e.g. '/dest.ext'. (required)
        :param src_path str : Source file's path e.g. '/Folder 1/file.ext' or '/Bucket/Folder 1/file.ext'. (required)
        :param src_storage_name str : Source storage name.
        :param dest_storage_name str : Destination storage name.
        :param version_id str : File version ID to move.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.move_file_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.move_file_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.move_file_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.move_file_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def move_file_with_http_info(self, request, **kwargs):  # noqa: E501
        """Move file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request MoveFileRequest object with parameters
        :return: None
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
                    " to method move_file" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def move_folder(self, request, **kwargs):  # noqa: E501
        """Move folder.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param dest_path str : Destination folder path to move to e.g '/dst'. (required)
        :param src_path str : Source folder path e.g. /Folder1. (required)
        :param src_storage_name str : Source storage name.
        :param dest_storage_name str : Destination storage name.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.move_folder_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.move_folder_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.move_folder_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.move_folder_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def move_folder_with_http_info(self, request, **kwargs):  # noqa: E501
        """Move folder.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request MoveFolderRequest object with parameters
        :return: None
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
                    " to method move_folder" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def optimize_document(self, request, **kwargs):  # noqa: E501
        """Allows to optimize the document contents as well as default Aspose.Words behavior to a particular versions of MS Word.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param options OptimizationOptions : The document optimization options. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.optimize_document_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.optimize_document_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.optimize_document_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.optimize_document_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def optimize_document_with_http_info(self, request, **kwargs):  # noqa: E501
        """Allows to optimize the document contents as well as default Aspose.Words behavior to a particular versions of MS Word.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request OptimizeDocumentRequest object with parameters
        :return: None
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
                    " to method optimize_document" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def protect_document(self, request, **kwargs):  # noqa: E501
        """Protects document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param protection_request ProtectionRequest : ProtectionRequest with protection settings. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :return: ProtectionDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.protect_document_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.protect_document_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.protect_document_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.protect_document_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def protect_document_with_http_info(self, request, **kwargs):  # noqa: E501
        """Protects document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request ProtectDocumentRequest object with parameters
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
                    " to method protect_document" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def reject_all_revisions(self, request, **kwargs):  # noqa: E501
        """Rejects all revisions in document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.reject_all_revisions_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.reject_all_revisions_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def reject_all_revisions_with_http_info(self, request, **kwargs):  # noqa: E501
        """Rejects all revisions in document.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def remove_range(self, request, **kwargs):  # noqa: E501
        """Removes the range from the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document. (required)
        :param range_start_identifier str : The range start identifier. Identifier is the value of the "nodeId" field, which every document node has, extended with the prefix "id". It looks like "id0.0.7". Also values like "image5" and "table3" can be used as an identifier for images and tables, where the number is an index of the image/table. (required)
        :param range_end_identifier str : The range end identifier.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.remove_range_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.remove_range_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.remove_range_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.remove_range_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def remove_range_with_http_info(self, request, **kwargs):  # noqa: E501
        """Removes the range from the document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request RemoveRangeRequest object with parameters
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
                    " to method remove_range" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def render_drawing_object(self, request, **kwargs):  # noqa: E501
        """Renders drawing object to specified format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param format str : The destination format. (required)
        :param index int : Object index. (required)
        :param node_path str : Path to the node, which contains drawing objects.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
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
                return self.render_drawing_object_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.render_drawing_object_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def render_math_object(self, request, **kwargs):  # noqa: E501
        """Renders math object to specified format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param format str : The destination format. (required)
        :param index int : Object index. (required)
        :param node_path str : Path to the node, which contains office math objects.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
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
                return self.render_math_object_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.render_math_object_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def render_page(self, request, **kwargs):  # noqa: E501
        """Renders page to specified format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param page_index int : Comment index. (required)
        :param format str : The destination format. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
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
                self.api_client.request_token()
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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def render_paragraph(self, request, **kwargs):  # noqa: E501
        """Renders paragraph to specified format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param format str : The destination format. (required)
        :param index int : Object index. (required)
        :param node_path str : Path to the node, which contains paragraphs.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
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
                return self.render_paragraph_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.render_paragraph_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def render_table(self, request, **kwargs):  # noqa: E501
        """Renders table to specified format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param format str : The destination format. (required)
        :param index int : Object index. (required)
        :param node_path str : Path to the node, which contains tables.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
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
                return self.render_table_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.render_table_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def replace_text(self, request, **kwargs):  # noqa: E501
        """Replaces document text.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param replace_text ReplaceTextParameters : ReplaceTextResponse with the replace operation settings. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: ReplaceTextResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.replace_text_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.replace_text_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.replace_text_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.replace_text_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def replace_text_with_http_info(self, request, **kwargs):  # noqa: E501
        """Replaces document text.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request ReplaceTextRequest object with parameters
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
                    " to method replace_text" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def replace_with_text(self, request, **kwargs):  # noqa: E501
        """Replaces the content in the range.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document. (required)
        :param range_start_identifier str : The range start identifier. Identifier is the value of the "nodeId" field, which every document node has, extended with the prefix "id". It looks like "id0.0.7". Also values like "image5" and "table3" can be used as an identifier for images and tables, where the number is an index of the image/table. (required)
        :param range_text ReplaceRange : Model with text for replacement. (required)
        :param range_end_identifier str : The range end identifier.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.replace_with_text_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.replace_with_text_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.replace_with_text_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.replace_with_text_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def replace_with_text_with_http_info(self, request, **kwargs):  # noqa: E501
        """Replaces the content in the range.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request ReplaceWithTextRequest object with parameters
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
                    " to method replace_with_text" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def reset_cache(self, request, **kwargs):  # noqa: E501
        """Resets font's cache.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :return: None
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.reset_cache_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.reset_cache_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def reset_cache_with_http_info(self, request, **kwargs):  # noqa: E501
        """Resets font's cache.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request ResetCacheRequest object with parameters
        :return: None
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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def save_as(self, request, **kwargs):  # noqa: E501
        """Converts document to destination format with detailed settings and saves result to storage.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param save_options_data SaveOptionsData : Save options. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param fonts_location str : Folder in filestorage with custom fonts.
        :return: SaveResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.save_as_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.save_as_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.save_as_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.save_as_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def save_as_with_http_info(self, request, **kwargs):  # noqa: E501
        """Converts document to destination format with detailed settings and saves result to storage.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request SaveAsRequest object with parameters
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
                    " to method save_as" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def save_as_range(self, request, **kwargs):  # noqa: E501
        """Saves the selected range as a new document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document. (required)
        :param range_start_identifier str : The range start identifier. Identifier is the value of the "nodeId" field, which every document node has, extended with the prefix "id". It looks like "id0.0.7". Also values like "image5" and "table3" can be used as an identifier for images and tables, where the number is an index of the image/table. (required)
        :param document_parameters RangeDocument : Parameters of a new document. (required)
        :param range_end_identifier str : The range end identifier.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.save_as_range_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.save_as_range_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.save_as_range_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.save_as_range_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def save_as_range_with_http_info(self, request, **kwargs):  # noqa: E501
        """Saves the selected range as a new document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request SaveAsRangeRequest object with parameters
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
                    " to method save_as_range" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def save_as_tiff(self, request, **kwargs):  # noqa: E501
        """Converts document to tiff with detailed settings and saves result to storage.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param save_options TiffSaveOptionsData : Tiff save options. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
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
                return self.save_as_tiff_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.save_as_tiff_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.save_as_tiff_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.save_as_tiff_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def save_as_tiff_with_http_info(self, request, **kwargs):  # noqa: E501
        """Converts document to tiff with detailed settings and saves result to storage.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request SaveAsTiffRequest object with parameters
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
                    " to method save_as_tiff" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def search(self, request, **kwargs):  # noqa: E501
        """Searches text in document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param pattern str : The regular expression used to find matches. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.search_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.search_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def search_with_http_info(self, request, **kwargs):  # noqa: E501
        """Searches text in document.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def split_document(self, request, **kwargs):  # noqa: E501
        """Splits document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : Original document name. (required)
        :param format str : Format to split. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
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
                return self.split_document_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.split_document_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.split_document_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.split_document_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def split_document_with_http_info(self, request, **kwargs):  # noqa: E501
        """Splits document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request SplitDocumentRequest object with parameters
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
                    " to method split_document" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def unprotect_document(self, request, **kwargs):  # noqa: E501
        """Unprotects document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param protection_request ProtectionRequest : ProtectionRequest with protection settings. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :return: ProtectionDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.unprotect_document_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.unprotect_document_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.unprotect_document_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.unprotect_document_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def unprotect_document_with_http_info(self, request, **kwargs):  # noqa: E501
        """Unprotects document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request UnprotectDocumentRequest object with parameters
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
                    " to method unprotect_document" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def update_bookmark(self, request, **kwargs):  # noqa: E501
        """Updates document bookmark.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param bookmark_data BookmarkData : BookmarkData with new bookmark data. (required)
        :param bookmark_name str : The bookmark name. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: BookmarkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.update_bookmark_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_bookmark_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.update_bookmark_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_bookmark_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def update_bookmark_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates document bookmark.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request UpdateBookmarkRequest object with parameters
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
                    " to method update_bookmark" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def update_border(self, request, **kwargs):  # noqa: E501
        """'nodePath' should refer to paragraph, cell or row.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param border_properties Border : Border properties. (required)
        :param border_type str : Border type. (required)
        :param node_path str : Path to the node with border(node should be paragraph, cell or row).
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.update_border_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_border_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def update_border_with_http_info(self, request, **kwargs):  # noqa: E501
        """'nodePath' should refer to paragraph, cell or row.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def update_comment(self, request, **kwargs):  # noqa: E501
        """Updates the comment, returns updated comment data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param comment_index int : The comment index. (required)
        :param comment CommentUpdate : The comment data. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: CommentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.update_comment_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_comment_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.update_comment_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_comment_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def update_comment_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates the comment, returns updated comment data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request UpdateCommentRequest object with parameters
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
                    " to method update_comment" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def update_drawing_object(self, request, **kwargs):  # noqa: E501
        """Updates drawing object, returns updated  drawing object's data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param drawing_object DrawingObjectUpdate : Drawing object parameters. (required)
        :param image_file file : File with image. (required)
        :param index int : Object index. (required)
        :param node_path str : Path to the node, which contains collection of drawing objects.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: DrawingObjectResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.update_drawing_object_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_drawing_object_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.update_drawing_object_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_drawing_object_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def update_drawing_object_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates drawing object, returns updated  drawing object's data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request UpdateDrawingObjectRequest object with parameters
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
                    " to method update_drawing_object" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def update_field(self, request, **kwargs):  # noqa: E501
        """Updates field's properties, returns updated field's data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param field FieldUpdate : Field data. (required)
        :param index int : Object index. (required)
        :param node_path str : Path to the node, which contains collection of fields.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: FieldResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.update_field_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_field_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.update_field_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_field_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def update_field_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates field's properties, returns updated field's data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request UpdateFieldRequest object with parameters
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
                    " to method update_field" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def update_fields(self, request, **kwargs):  # noqa: E501
        """Updates (reevaluate) fields in document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :return: DocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.update_fields_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_fields_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.update_fields_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_fields_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def update_fields_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates (reevaluate) fields in document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request UpdateFieldsRequest object with parameters
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
                    " to method update_fields" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def update_footnote(self, request, **kwargs):  # noqa: E501
        """Updates footnote's properties, returns updated run's data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param footnote_dto FootnoteUpdate : Footnote data. (required)
        :param index int : Object index. (required)
        :param node_path str : Path to the node, which contains collection of footnotes.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: FootnoteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.update_footnote_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_footnote_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.update_footnote_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_footnote_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def update_footnote_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates footnote's properties, returns updated run's data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request UpdateFootnoteRequest object with parameters
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
                    " to method update_footnote" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def update_form_field(self, request, **kwargs):  # noqa: E501
        """Updates properties of form field, returns updated form field.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param form_field FormField : From field data. (required)
        :param index int : Object index. (required)
        :param node_path str : Path to the node that contains collection of formfields.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: FormFieldResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.update_form_field_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_form_field_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.update_form_field_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_form_field_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def update_form_field_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates properties of form field, returns updated form field.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request UpdateFormFieldRequest object with parameters
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
                    " to method update_form_field" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def update_list(self, request, **kwargs):  # noqa: E501
        """Updates list properties, returns updated list.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param list_update ListUpdate : List object. (required)
        :param list_id int : List unique identifier. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: ListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.update_list_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_list_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.update_list_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_list_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def update_list_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates list properties, returns updated list.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request UpdateListRequest object with parameters
        :return: ListResponse
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
                    " to method update_list" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def update_list_level(self, request, **kwargs):  # noqa: E501
        """Updates list level in document list, returns updated list.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param list_update ListLevelUpdate : List object. (required)
        :param list_id int : List unique identifier. (required)
        :param list_level int : List level identifier. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: ListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.update_list_level_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_list_level_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.update_list_level_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_list_level_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def update_list_level_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates list level in document list, returns updated list.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request UpdateListLevelRequest object with parameters
        :return: ListResponse
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
                    " to method update_list_level" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def update_paragraph_format(self, request, **kwargs):  # noqa: E501
        """Updates paragraph format properties, returns updated format properties.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param dto ParagraphFormatUpdate : Paragraph format object. (required)
        :param index int : Object index. (required)
        :param node_path str : Path to the node which contains paragraphs.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: ParagraphFormatResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.update_paragraph_format_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_paragraph_format_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.update_paragraph_format_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_paragraph_format_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def update_paragraph_format_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates paragraph format properties, returns updated format properties.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request UpdateParagraphFormatRequest object with parameters
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
                    " to method update_paragraph_format" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def update_paragraph_list_format(self, request, **kwargs):  # noqa: E501
        """Updates paragraph list format properties, returns updated list format properties.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param dto ListFormatUpdate : Paragraph format object. (required)
        :param index int : Object index. (required)
        :param node_path str : Path to the node which contains paragraphs.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: ParagraphListFormatResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.update_paragraph_list_format_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_paragraph_list_format_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.update_paragraph_list_format_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_paragraph_list_format_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def update_paragraph_list_format_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates paragraph list format properties, returns updated list format properties.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request UpdateParagraphListFormatRequest object with parameters
        :return: ParagraphListFormatResponse
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
                    " to method update_paragraph_list_format" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def update_run(self, request, **kwargs):  # noqa: E501
        """Updates run's properties, returns updated run's data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param run RunUpdate : Run data. (required)
        :param paragraph_path str : Path to parent paragraph. (required)
        :param index int : Object index. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: RunResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.update_run_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_run_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.update_run_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_run_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def update_run_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates run's properties, returns updated run's data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request UpdateRunRequest object with parameters
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
                    " to method update_run" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def update_run_font(self, request, **kwargs):  # noqa: E501
        """Updates font properties, returns updated font data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param font_dto Font : Font dto object. (required)
        :param paragraph_path str : Path to parent paragraph. (required)
        :param index int : Object index. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: FontResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.update_run_font_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_run_font_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.update_run_font_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_run_font_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def update_run_font_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates font properties, returns updated font data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request UpdateRunFontRequest object with parameters
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
                    " to method update_run_font" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def update_section_page_setup(self, request, **kwargs):  # noqa: E501
        """Updates page setup of section.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param section_index int : Section index. (required)
        :param page_setup PageSetup : Page setup properties dto. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
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
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.update_section_page_setup_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_section_page_setup_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def update_section_page_setup_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates page setup of section.  # noqa: E501

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
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def update_style(self, request, **kwargs):  # noqa: E501
        """Updates style properties, returns an updated style.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param style_update StyleUpdate : Style properties to update. (required)
        :param style_name str : Style name. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
        :return: StyleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.update_style_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_style_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.update_style_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_style_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def update_style_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates style properties, returns an updated style.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request UpdateStyleRequest object with parameters
        :return: StyleResponse
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
                    " to method update_style" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def update_table_cell_format(self, request, **kwargs):  # noqa: E501
        """Updates a table cell format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param format TableCellFormat : The properties. (required)
        :param table_row_path str : Path to table row. (required)
        :param index int : Object index. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
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
                self.api_client.request_token()
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
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def update_table_properties(self, request, **kwargs):  # noqa: E501
        """Updates a table properties.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param properties TableProperties : The properties. (required)
        :param index int : Object index. (required)
        :param node_path str : Path to the node, which contains tables.
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
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
                self.api_client.request_token()
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
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def update_table_row_format(self, request, **kwargs):  # noqa: E501
        """Updates a table row format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param format TableRowFormat : Table row format. (required)
        :param table_path str : Path to table. (required)
        :param index int : Object index. (required)
        :param folder str : Original document folder.
        :param storage str : Original document storage.
        :param load_encoding str : Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
        :param password str : Password for opening an encrypted document.
        :param dest_file_name str : Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
        :param revision_author str : Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
        :param revision_date_time str : The date and time to use for revisions.
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
                self.api_client.request_token()
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
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def upload_file(self, request, **kwargs):  # noqa: E501
        """Upload file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param file_content file : File to upload. (required)
        :param path str : Path where to upload including filename and extension e.g. /file.ext or /Folder 1/file.ext If the content is multipart and path does not contains the file name it tries to get them from filename parameter from Content-Disposition header. (required)
        :param storage_name str : Storage name.
        :return: FilesUploadResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.upload_file_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.upload_file_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.api_client.request_token()
                if kwargs.get('is_async'):
                    return self.upload_file_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.upload_file_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def upload_file_with_http_info(self, request, **kwargs):  # noqa: E501
        """Upload file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request UploadFileRequest object with parameters
        :return: FilesUploadResult
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
                    " to method upload_file" % key
                )
            params[key] = val
        del params['kwargs']
        http_params = request.create_http_request(self.api_client)

        # HTTP header `Accept`
        http_params['header_params']['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501
        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            http_params['path'],
            http_params['method'],
            http_params['query_params'],
            http_params['header_params'],
            body=http_params['body'],
            post_params=http_params['form_params'],
            response_type=http_params['response_type'],  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=http_params['collection_formats'])

    def batch(self, *requests):  # noqa: E501
        if requests is None:
            return None

        if len(requests) == 0:
            return None

        post_params=[]
        for request in requests:
            post_params.append(self.api_client.request_to_batch_part(request))

        header_params={'Content-Type': 'multipart/form-data'}
        response = self.api_client.call_api(
            resource_path="/v4.0/words/batch",
            method='PUT',
            post_params=post_params,
            header_params=header_params,
            response_type='multipart',  # noqa: E501
            auth_settings=['JWT'],
            _return_http_data_only=True)
        return self.api_client.deserialize_multipart(response, requests)
