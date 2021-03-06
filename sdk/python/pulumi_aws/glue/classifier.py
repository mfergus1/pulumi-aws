# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class Classifier(pulumi.CustomResource):
    grok_classifier: pulumi.Output[dict]
    """
    A classifier that uses grok patterns. Defined below.
    """
    json_classifier: pulumi.Output[dict]
    """
    A classifier for JSON content. Defined below.
    """
    name: pulumi.Output[str]
    """
    The name of the classifier.
    """
    xml_classifier: pulumi.Output[dict]
    """
    A classifier for XML content. Defined below.
    """
    def __init__(__self__, __name__, __opts__=None, grok_classifier=None, json_classifier=None, name=None, xml_classifier=None):
        """
        Provides a Glue Classifier resource.
        
        > **NOTE:** It is only valid to create one type of classifier (grok, JSON, or XML). Changing classifier types will recreate the classifier.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[dict] grok_classifier: A classifier that uses grok patterns. Defined below.
        :param pulumi.Input[dict] json_classifier: A classifier for JSON content. Defined below.
        :param pulumi.Input[str] name: The name of the classifier.
        :param pulumi.Input[dict] xml_classifier: A classifier for XML content. Defined below.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['grok_classifier'] = grok_classifier

        __props__['json_classifier'] = json_classifier

        __props__['name'] = name

        __props__['xml_classifier'] = xml_classifier

        super(Classifier, __self__).__init__(
            'aws:glue/classifier:Classifier',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

