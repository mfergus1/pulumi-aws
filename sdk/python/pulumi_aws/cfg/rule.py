# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class Rule(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    The ARN of the config rule
    """
    description: pulumi.Output[str]
    """
    Description of the rule
    """
    input_parameters: pulumi.Output[str]
    """
    A string in JSON format that is passed to the AWS Config rule Lambda function.
    """
    maximum_execution_frequency: pulumi.Output[str]
    """
    The frequency that you want AWS Config to run evaluations for a rule that
    is triggered periodically. If specified, requires `message_type` to be `ScheduledNotification`.
    """
    name: pulumi.Output[str]
    """
    The name of the rule
    """
    rule_id: pulumi.Output[str]
    """
    The ID of the config rule
    """
    scope: pulumi.Output[dict]
    """
    Scope defines which resources can trigger an evaluation for the rule as documented below.
    """
    source: pulumi.Output[dict]
    """
    Source specifies the rule owner, the rule identifier, and the notifications that cause
    the function to evaluate your AWS resources as documented below.
    """
    def __init__(__self__, resource_name, opts=None, description=None, input_parameters=None, maximum_execution_frequency=None, name=None, scope=None, source=None, __name__=None, __opts__=None):
        """
        Provides an AWS Config Rule.
        
        > **Note:** Config Rule requires an existing [Configuration Recorder](https://www.terraform.io/docs/providers/aws/r/config_configuration_recorder.html) to be present. Use of `depends_on` is recommended (as shown below) to avoid race conditions.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description of the rule
        :param pulumi.Input[str] input_parameters: A string in JSON format that is passed to the AWS Config rule Lambda function.
        :param pulumi.Input[str] maximum_execution_frequency: The frequency that you want AWS Config to run evaluations for a rule that
               is triggered periodically. If specified, requires `message_type` to be `ScheduledNotification`.
        :param pulumi.Input[str] name: The name of the rule
        :param pulumi.Input[dict] scope: Scope defines which resources can trigger an evaluation for the rule as documented below.
        :param pulumi.Input[dict] source: Source specifies the rule owner, the rule identifier, and the notifications that cause
               the function to evaluate your AWS resources as documented below.
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

        __props__['description'] = description

        __props__['input_parameters'] = input_parameters

        __props__['maximum_execution_frequency'] = maximum_execution_frequency

        __props__['name'] = name

        __props__['scope'] = scope

        if source is None:
            raise TypeError('Missing required property source')
        __props__['source'] = source

        __props__['arn'] = None
        __props__['rule_id'] = None

        super(Rule, __self__).__init__(
            'aws:cfg/rule:Rule',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

