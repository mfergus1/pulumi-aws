# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class ThingType(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    The ARN of the created AWS IoT Thing Type.
    """
    deprecated: pulumi.Output[bool]
    """
    Whether the thing type is deprecated. If true, no new things could be associated with this type.
    """
    name: pulumi.Output[str]
    """
    The name of the thing type.
    """
    properties: pulumi.Output[dict]
    def __init__(__self__, __name__, __opts__=None, deprecated=None, name=None, properties=None):
        """
        Creates and manages an AWS IoT Thing Type.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[bool] deprecated: Whether the thing type is deprecated. If true, no new things could be associated with this type.
        :param pulumi.Input[str] name: The name of the thing type.
        :param pulumi.Input[dict] properties
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['deprecated'] = deprecated

        __props__['name'] = name

        __props__['properties'] = properties

        __props__['arn'] = None

        super(ThingType, __self__).__init__(
            'aws:iot/thingType:ThingType',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

