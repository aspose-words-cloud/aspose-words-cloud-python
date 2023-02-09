# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="api_client.py">
#   Copyright (c) 2023 Aspose.Words for Cloud
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

import datetime
import email.parser
import io
import json
import mimetypes
from multiprocessing.pool import ThreadPool
from requests_toolbelt.multipart import decoder
import os
import re
import tempfile
import uuid

# python 2 and python 3 compatibility library
from urllib.parse import urlencode
from six.moves.urllib.parse import quote
import six
from urllib3 import encode_multipart_formdata

from asposewordscloud.configuration import Configuration
import asposewordscloud.models
from asposewordscloud import rest


class ApiClient(object):
    """Generic API client

    Swagger generic API client. This client handles the client-
    server communication, and is invariant across implementations.

    :param configuration: .Configuration object for this client
    :param header_name: a header to pass when making calls to the API.
    :param header_value: a header value to pass when making calls to
        the API.
    :param cookie: a cookie to include in the header when making calls
        to the API
    """

    PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types
    NATIVE_TYPES_MAPPING = {
        'int': int,
        'long': int if six.PY3 else long,  #pylint: disable=undefined-variable
        'float': float,
        'str': str,
        'bool': bool,
        'date': datetime.date,
        'datetime': datetime.datetime,
        'object': object,
    }

    def __init__(self, configuration=None, header_name=None, header_value=None,
                 cookie=None):
        if configuration is None:
            configuration = Configuration()
        self.configuration = configuration

        self.pool = None
        self.rest_client = rest.RESTClientObject(configuration)
        self.default_headers = {'x-aspose-client': 'python sdk', 'x-aspose-version': '23.2'}
        if header_name is not None:
            self.default_headers[header_name] = header_value
        self.cookie = cookie
        # Set default User-Agent.
        self.user_agent = 'python sdk 23.2'

    def __del__(self):
        if not self.pool is None:
            self.pool.close()
            self.pool.join()

    @property
    def user_agent(self):
        """User agent for this API client"""
        return self.default_headers['User-Agent']

    @user_agent.setter
    def user_agent(self, value):
        self.default_headers['User-Agent'] = value

    def set_default_header(self, header_name, header_value):
        """Setting default header"""
        self.default_headers[header_name] = header_value

    def request_token(self):
        config = self.configuration
        request_url = "/connect/token"
        body = 'grant_type=client_credentials&client_id=' + config.client_secret['client_id'] + '&client_secret=' + config.client_secret['client_secret']

        header_params = {'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}

        if self.cookie:
            header_params['Cookie'] = self.cookie
        if header_params:
            header_params = self.sanitize_for_serialization(header_params)
            header_params = dict(self.parameters_to_tuples(header_params,
                                                           {}))

        # remove optional path parameters
        resource_path = request_url.replace('//', '/')

        # request url
        url = ''
        if six.PY3:
            url = self.configuration.host + resource_path
        else:
            url = (self.configuration.host + resource_path).encode('utf8')

        # perform request and return response
        response_data = self.request(
            'POST', url, query_params=[], headers=header_params,
            post_params=None, body=body,
            _preload_content=True,
            _request_timeout=None)

        return_data = self.deserialize(response_data.data, response_data.getheaders(), 'object')
        access_token = return_data['access_token'] if six.PY3 else return_data['access_token'].encode('utf8')
        self.configuration.access_token = access_token

    def __call_api(
            self, resource_path, method,
            query_params=None, header_params=None, body=None, post_params=None,
            response_type=None, auth_settings=None,
            collection_formats=None,
            _preload_content=True, _request_timeout=None):
        """Call api method"""
        config = self.configuration

        if config.access_token is None or config.access_token == "":
            self.request_token()

        # header parameters
        header_params = header_params or {}
        header_params.update(self.default_headers)
        header_params['Authorization'] = "Bearer " + self.configuration.access_token
        if self.cookie:
            header_params['Cookie'] = self.cookie
        if header_params:
            header_params = self.sanitize_for_serialization(header_params)
            header_params = dict(self.parameters_to_tuples(header_params, collection_formats))

        # query parameters
        if query_params:
            query_params = self.sanitize_for_serialization(query_params)
            query_params = self.parameters_to_tuples(query_params, collection_formats)

        # post parameters
        if post_params:
            if len(post_params) == 1:
                post_params = self.prepare_post_parameters(post_params)
                body = post_params[0][1][1]
                header_params['Content-Type'] = post_params[0][1][2]
                post_params = None
            elif len(post_params) > 1:
                post_params = self.prepare_post_parameters(post_params)
                post_params = self.sanitize_for_serialization(post_params)
                post_params = self.parameters_to_tuples(post_params, collection_formats)
                header_params['Content-Type'] = 'multipart/form-data'

        # auth setting
        self.update_params_for_auth(header_params, query_params, auth_settings)

        # body
        if body:
            body = self.sanitize_for_serialization(body)

        # request url
        url = ''
        if six.PY3:
            url = self.configuration.host + resource_path
        else:
            url = (self.configuration.host + resource_path).encode('utf8')

        # perform request and return response
        response_data = self.request(
            method, url, query_params=query_params, headers=header_params,
            post_params=post_params, body=body,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout)

        self.last_response = response_data

        return response_data

    def sanitize_for_serialization(self, obj):
        """Builds a JSON POST object.

        If obj is None, return None.
        If obj is str, int, long, float, bool, return directly.
        If obj is datetime.datetime, datetime.date
            convert to string in iso8601 format.
        If obj is list, sanitize each element in the list.
        If obj is dict, return the dict.
        If obj is swagger model, return the properties dict.

        :param obj: The data to serialize.
        :return: The serialized form of data.
        """
        if obj is None:
            return None
        elif isinstance(obj, self.PRIMITIVE_TYPES):
            return obj
        elif isinstance(obj, list):
            return [self.sanitize_for_serialization(sub_obj)
                    for sub_obj in obj]
        elif isinstance(obj, tuple):
            return tuple(self.sanitize_for_serialization(sub_obj)
                         for sub_obj in obj)
        elif isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()
        elif isinstance(obj, bytearray):
            return obj

        if isinstance(obj, dict):
            obj_dict = obj
        else:
            # Convert model obj to dict except
            # attributes `swagger_types`, `attribute_map`
            # and attributes which value is not None.
            # Convert attribute name to json key in
            # model definition for request.
            obj_dict = {obj.attribute_map[attr]: getattr(obj, attr)
                        for attr, _ in six.iteritems(obj.swagger_types)
                        if getattr(obj, attr) is not None}

        return {key: self.sanitize_for_serialization(val)
                for key, val in six.iteritems(obj_dict)}

    def getFilenameFromHeaders(self, headers):
        disposition = ""
        if b'Content-Disposition' in headers:
            disposition = headers[b'Content-Disposition']
            if type(disposition) != str:
                disposition = disposition.decode("utf-8") 
        elif "Content-Disposition" in headers:
            disposition = headers["Content-Disposition"]
        else:
            return ""

        dispparts = disposition.split(";")
        for dispart in dispparts:
            subparts = dispart.split("=")
            if len(subparts) == 2 and subparts[0].strip(" \"") == "filename":
                return subparts[1].strip(" \"")
        return ""

    def findMultipartByName(self, multipart, name):
        for part in multipart:
            disposition = ""
            if b'Content-Disposition' in part.headers:
                disposition = part.headers[b'Content-Disposition']
                if type(disposition) != str:
                    disposition = disposition.decode("utf-8") 
            elif "Content-Disposition" in part.headers:
                disposition = part.headers["Content-Disposition"]

            dispparts = disposition.split(";")
            for dispart in dispparts:
                subparts = dispart.split("=")
                if len(subparts) == 2 and subparts[0].strip(" \"") == "name" and subparts[1].strip(" \"") == name:
                    return part
        return None

    def deserialize_multipart(self, without_intermediate_results, multipart, requests):
        if without_intermediate_results:
            if len(multipart.parts) != 1:
                raise rest.ApiException(status=0, reason="Response must have one part.")
        else:
            if len(multipart.parts) != len(requests):
                raise rest.ApiException(status=0, reason="Response parts and requests count mismatch.")

        id_to_requests = {}
        for r in requests:
            id_to_requests[r.id] = r

        results = []
        for part in multipart.parts:
            try:
                data = part.content
                packet_parts = data.split(b"\r\n\r\n", 1)
                header_parts = packet_parts[0].split(b"\r\n")
                code = int(header_parts[0].split(b" ", 1)[0].decode('UTF-8'))
                body = packet_parts[1]

                headers = {}
                if len(header_parts) > 1:
                    for header_line in header_parts[1:]:
                        header_line_parts = header_line.decode('UTF-8').split(':', 1)
                        if len(header_line_parts) == 2:
                            headers[header_line_parts[0].strip()] = header_line_parts[1].strip()

                response_type = id_to_requests[headers["RequestId"]].get_response_type()

                result = None
                if code == 200:
                    if response_type != 'None':
                        result = self.deserialize(body, headers, response_type)
                else:
                    result = rest.ApiException(status=code, reason=body.decode('UTF-8'))

                results.append(result)
            except:
                raise rest.ApiException(status=0, reason="Response part is invalid.")

        return results

    def deserialize_files_collection(self, data, headers):
        result = {}
        if b'Content-Type' in headers.keys() and headers[b'Content-Type'].decode("utf-8").startswith("multipart/mixed"):
            parts = decoder.MultipartDecoder(data, headers[b'Content-Type'].decode("utf-8"), 'UTF-8').parts
            for part in parts:
                result[self.getFilenameFromHeaders(part.headers)] = self.deserialize_file(part.content, part.headers)
        elif "Content-Type" in headers.keys() and headers["Content-Type"].startswith("multipart/mixed"):
            parts = decoder.MultipartDecoder(data, headers["Content-Type"], 'UTF-8').parts
            for part in parts:
                result[self.getFilenameFromHeaders(part.headers)] = self.deserialize_file(part.content, part.headers)
        else:
            result[self.getFilenameFromHeaders(headers)] = self.deserialize_file(data, headers)

        return result

    def deserialize(self, data, headers, response_type):
        """Deserializes response into an object.

        :param response: RESTResponse object to be deserialized.
        :param response_type: class literal for
            deserialized object, or string of class name.

        :return: deserialized object.
        """
        # handle file downloading
        # save response body into a tmp file and return the instance
        if response_type == "file":
            return self.deserialize_file(data, headers)

        if response_type == "files_collection":
            return self.deserialize_files_collection(data, headers)

        if response_type == "multipart":
            if b'Content-Type' in headers:
                return decoder.MultipartDecoder(data, headers[b'Content-Type'], 'UTF-8')
            if "Content-Type" in headers:
                return decoder.MultipartDecoder(data, headers["Content-Type"], 'UTF-8')

        # fetch data from response object
        if six.PY3:
            data = data.decode('utf8')
        try:
            data = json.loads(data)
        except:
            pass

        return self.__deserialize(data, response_type)

    def __deserialize(self, data, klass):
        """Deserializes dict, list, str into an object.

        :param data: dict, list or str.
        :param klass: class literal, or string of class name.

        :return: object.
        """
        if data is None:
            return None

        if type(klass) == str:
            if klass == 'None':
                return None

            if klass.startswith('list['):
                sub_kls = re.match(r'list\[(.*)\]', klass).group(1)
                return [self.__deserialize(sub_data, sub_kls)
                        for sub_data in data]

            if klass.startswith('dict('):
                sub_kls = re.match(r'dict\(([^,]*), (.*)\)', klass).group(2)
                return {k: self.__deserialize(v, sub_kls)
                        for k, v in six.iteritems(data)}

            # convert str to class
            if klass in self.NATIVE_TYPES_MAPPING:
                klass = self.NATIVE_TYPES_MAPPING[klass]
            else:
                klass = getattr(asposewordscloud.models, klass)

        if klass in self.PRIMITIVE_TYPES:
            return self.__deserialize_primitive(data, klass)
        elif klass == object:
            return self.__deserialize_object(data)
        elif klass == datetime.date:
            return self.__deserialize_date(data)
        elif klass == datetime.datetime:
            return self.__deserialize_datatime(data)
        else:
            return self.__deserialize_model(data, klass)

    def call_api(self, resource_path, method,
                 query_params=None, header_params=None,
                 body=None, post_params=None,
                 response_type=None, auth_settings=None, is_async=None,
                 collection_formats=None,
                 _preload_content=True, _request_timeout=None):
        """Makes the HTTP request (synchronous) and returns deserialized data.

        To make an async request, set the async parameter.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
        :param response: Response data type.
        :param files dict: key -> filename, value -> filepath,
            for `multipart/form-data`.
        :param is_async bool: execute request asynchronously
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return:
            If is_async parameter is True,
            the request will be called asynchronously.
            The method will return the request thread.
            If parameter is_async is False or missing,
            then the method will return the response directly.
        """
        if not is_async:
            return self.__call_api(resource_path, method,
                                   query_params, header_params,
                                   body, post_params,
                                   response_type, auth_settings,
                                   collection_formats,
                                   _preload_content, _request_timeout)
        else:
            if self.pool is None:
                self.pool = ThreadPool()
            thread = self.pool.apply_async(self.__call_api, (resource_path,
                                                             method, query_params,
                                                             header_params, body,
                                                             post_params,
                                                             response_type, auth_settings,
                                                             collection_formats,
                                                             _preload_content, _request_timeout))
        return thread

    def request(self, method, url, query_params=None, headers=None,
                post_params=None, body=None, _preload_content=True,
                _request_timeout=None):
        """Makes the HTTP request using RESTClient."""
        return self.rest_client.request(method, url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def parameters_to_tuples(self, params, collection_formats):
        """Get parameters as list of tuples, formatting collections.

        :param params: Parameters as dict or list of two-tuples
        :param dict collection_formats: Parameter collection formats
        :return: Parameters as list of tuples, collections formatted
        """
        new_params = []
        if collection_formats is None:
            collection_formats = {}
        for k, v in six.iteritems(params) if isinstance(params, dict) else params:  # noqa: E501
            if k in collection_formats:
                collection_format = collection_formats[k]
                if collection_format == 'multi':
                    new_params.extend((k, value) for value in v)
                else:
                    if collection_format == 'ssv':
                        delimiter = ' '
                    elif collection_format == 'tsv':
                        delimiter = '\t'
                    elif collection_format == 'pipes':
                        delimiter = '|'
                    else:  # csv is the default
                        delimiter = ','
                    new_params.append(
                        (k, delimiter.join(str(value) for value in v)))
            else:
                new_params.append((k, v))
        return new_params

    def prepare_post_parameters(self, post_params=None):
        """Builds form parameters.

        :param post_params: Normal form parameters.
        :param files: File parameters.
        :return: Form parameters with files. 
        """
        params = []

        if post_params:
                for k, v, t in post_params:
                    if t == 'multipart':
                        params.append(tuple([k, tuple([None, v, 'application/http; msgtype=request'])]))

                    if t == 'string':
                        params.append(tuple([k, tuple([None, v, 'text/plain'])]))

                    if t == 'json':
                        params.append(tuple([k, tuple([None, v.to_json(), 'application/json'])]))

                    if t == 'file':
                        if not v:
                            continue
                        file_names = v if type(v) is list else [v]
                        for n in file_names:
                            if isinstance(n, io.StringIO):
                                params.append(tuple([k, tuple(['document', n.getvalue(), 'application/octet-stream'])]))
                            else:
                                filename = os.path.basename(n.name)
                                filedata = n.read()
                                mimetype = (mimetypes.guess_type(filename)[0] or 'application/octet-stream')
                                params.append(tuple([k, tuple([filename, filedata, mimetype])]))

        return params

    def select_header_accept(self, accepts):
        """Returns `Accept` based on an array of accepts provided.

        :param accepts: List of headers.
        :return: Accept (e.g. application/json).
        """
        if not accepts:
            return

        accepts = [x.lower() for x in accepts]

        if 'application/json' in accepts:
            return 'application/json'
        else:
            return ', '.join(accepts)

    def select_header_content_type(self, content_types):
        """Returns `Content-Type` based on an array of content_types provided.

        :param content_types: List of content-types.
        :return: Content-Type (e.g. application/json).
        """
        if not content_types:
            return 'application/json'

        content_types = [x.lower() for x in content_types]

        if 'application/json' in content_types or '*/*' in content_types:
            return 'application/json'
        else:
            return content_types[0]

    def update_params_for_auth(self, headers, querys, auth_settings):
        """Updates header and query params based on authentication setting.

        :param headers: Header parameters dict to be updated.
        :param querys: Query parameters tuple list to be updated.
        :param auth_settings: Authentication setting identifiers list.
        """
        if not auth_settings:
            return

        for auth in auth_settings:
            auth_setting = self.configuration.auth_settings().get(auth)
            if auth_setting:
                if not auth_setting['value']:
                    continue
                elif auth_setting['in'] == 'header':
                    headers[auth_setting['key']] = auth_setting['value']
                elif auth_setting['in'] == 'query':
                    querys.append((auth_setting['key'], auth_setting['value']))
                else:
                    raise ValueError(
                        'Authentication token must be in `query` or `header`'
                    )

    def deserialize_file(self, data, headers):
        return data

    def __deserialize_primitive(self, data, klass):
        """Deserializes string to primitive type.

        :param data: str.
        :param klass: class literal.

        :return: int, long, float, str, bool.
        """
        try:
            return klass(data)
        except UnicodeEncodeError:
            if not six.PY3:
                return data.encode('utf8')
            return six.u(data)
        except TypeError:
            return data

    def __deserialize_object(self, value):
        """Return a original value.

        :return: object.
        """
        return value

    def __deserialize_date(self, string):
        """Deserializes string to date.

        :param string: str.
        :return: date.
        """
        try:
            from dateutil.parser import parse
            return parse(string).date()
        except ImportError:
            return string
        except ValueError:
            raise rest.ApiException(
                status=0,
                reason="Failed to parse `{0}` as date object".format(string)
            )

    def __deserialize_datatime(self, string):
        """Deserializes string to datetime.

        The string should be in iso8601 datetime format.

        :param string: str.
        :return: datetime.
        """
        try:
            from dateutil.parser import parse
            return parse(string)
        except ImportError:
            return string
        except ValueError:
            raise rest.ApiException(
                status=0,
                reason=(
                    "Failed to parse `{0}` as datetime object"
                    .format(string)
                )
            )

    def __deserialize_model(self, data, klass):
        """Deserializes list or dict to model.

        :param data: dict, list.
        :param klass: class literal.
        :return: model object.
        """
        if klass is None: 
            return data

        if not klass.swagger_types and not hasattr(klass,
                                                   'get_real_child_model'):
            return data

        kwargs = {}
        if klass.swagger_types is not None:
            for attr, attr_type in six.iteritems(klass.swagger_types):
                if (data is not None and
                        klass.attribute_map[attr] in data and
                        isinstance(data, (list, dict))):
                    value = data[klass.attribute_map[attr]]
                    kwargs[attr] = self.__deserialize(value, attr_type)

        instance = klass(**kwargs)

        if hasattr(instance, 'get_real_child_model'):
            klass_name = instance.get_real_child_model(data)
            if klass_name:
                instance = self.__deserialize(data, klass_name)
        return instance

    def request_to_batch_part(self, request, encryptor):
        http_request = request.create_http_request(self)
        if http_request['form_params'] and http_request['body']:
            raise ValueError("body parameter cannot be used with post_params parameter.")

        self.handle_password(http_request, encryptor)

        url = http_request['path'][len('/v4.0/words/'):]
        if http_request['query_params']:
            url += '?' + urlencode(http_request['query_params'])

        body = http_request['body']
        if http_request['form_params']:
            post_params = self.prepare_post_parameters(http_request['form_params'])
            if len(post_params) == 1:
                body = post_params[0][1][1]
                http_request['header_params']['Content-Type'] = post_params[0][1][2]
                http_request['form_params'] = {}
            elif len(post_params) > 1:
                post_params = self.sanitize_for_serialization(post_params)
                post_params = self.parameters_to_tuples(post_params, http_request['collection_formats'])
                body, content_type = encode_multipart_formdata(post_params)
                http_request['header_params']['Content-Type'] = content_type

        if body:
            body = self.sanitize_for_serialization(body)
            if isinstance(body, str):
                body = body.encode('UTF-8')

        result = bytearray()
        result.extend(http_request['method'].encode('UTF-8'))
        result.extend(' '.encode('UTF-8'))
        result.extend(url.encode('UTF-8'))
        result.extend(' \r\n'.encode('UTF-8'))
        for key, value in http_request['header_params'].items():
            result.extend(key.encode('UTF-8'))
            result.extend(': '.encode('UTF-8'))
            result.extend(value.encode('UTF-8'))
            result.extend('\r\n'.encode('UTF-8'))

        result.extend('\r\n'.encode('UTF-8'))

        if body:
            result.extend(body)

        return [None, result, 'multipart']

    def handle_password(self, http_params, encryptor):

        index = -1
        for i in range(len(http_params['query_params'])):
            k, v = http_params['query_params'][i]
            if k == 'password':
                index = i
                break

        if index > -1:
            k,v = http_params['query_params'].pop(index)
            http_params['query_params'].append(('encryptedPassword', encryptor.encrypt(v)))