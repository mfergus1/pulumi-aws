# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class LogDestinationPolicy(pulumi.CustomResource):
    access_policy: pulumi.Output[str]
    """
    The policy document. This is a JSON formatted string.
    """
    destination_name: pulumi.Output[str]
    """
    A name for the subscription filter
    """
    def __init__(__self__, resource_name, opts=None, access_policy=None, destination_name=None, __name__=None, __opts__=None):
        """
        Provides a CloudWatch Logs destination policy resource.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_policy: The policy document. This is a JSON formatted string.
        :param pulumi.Input[str] destination_name: A name for the subscription filter
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if not resource_name:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(resource_name, str):
            raise TypeError('Expected resource name to be a string')
        if opts and not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if access_policy is None:
            raise TypeError('Missing required property access_policy')
        __props__['access_policy'] = access_policy

        if destination_name is None:
            raise TypeError('Missing required property destination_name')
        __props__['destination_name'] = destination_name

        super(LogDestinationPolicy, __self__).__init__(
            'aws:cloudwatch/logDestinationPolicy:LogDestinationPolicy',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

