# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class RuleGroup(pulumi.CustomResource):
    activated_rules: pulumi.Output[list]
    """
    A list of activated rules, see below
    """
    metric_name: pulumi.Output[str]
    """
    A friendly name for the metrics from the rule group
    """
    name: pulumi.Output[str]
    """
    A friendly name of the rule group
    """
    def __init__(__self__, __name__, __opts__=None, activated_rules=None, metric_name=None, name=None):
        """
        Provides a WAF Regional Rule Group Resource
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[list] activated_rules: A list of activated rules, see below
        :param pulumi.Input[str] metric_name: A friendly name for the metrics from the rule group
        :param pulumi.Input[str] name: A friendly name of the rule group
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['activated_rules'] = activated_rules

        if not metric_name:
            raise TypeError('Missing required property metric_name')
        __props__['metric_name'] = metric_name

        __props__['name'] = name

        super(RuleGroup, __self__).__init__(
            'aws:wafregional/ruleGroup:RuleGroup',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

