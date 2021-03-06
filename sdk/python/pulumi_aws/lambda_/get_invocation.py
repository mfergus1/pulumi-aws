# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class GetInvocationResult(object):
    """
    A collection of values returned by getInvocation.
    """
    def __init__(__self__, result=None, result_map=None, id=None):
        if result and not isinstance(result, str):
            raise TypeError('Expected argument result to be a str')
        __self__.result = result
        """
        A result of the lambda function invocation.
        """
        if result_map and not isinstance(result_map, dict):
            raise TypeError('Expected argument result_map to be a dict')
        __self__.result_map = result_map
        """
        This field is set only if result is a map of primitive types.
        """
        if id and not isinstance(id, str):
            raise TypeError('Expected argument id to be a str')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_invocation(function_name=None, input=None, qualifier=None):
    """
    Use this data source to invoke custom lambda functions as data source.
    The lambda function is invoked with [RequestResponse](https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html#API_Invoke_RequestSyntax)
    invocation type.
    """
    __args__ = dict()

    __args__['functionName'] = function_name
    __args__['input'] = input
    __args__['qualifier'] = qualifier
    __ret__ = await pulumi.runtime.invoke('aws:lambda/getInvocation:getInvocation', __args__)

    return GetInvocationResult(
        result=__ret__.get('result'),
        result_map=__ret__.get('resultMap'),
        id=__ret__.get('id'))
