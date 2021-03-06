# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class DefaultSecurityGroup(pulumi.CustomResource):
    arn: pulumi.Output[str]
    egress: pulumi.Output[list]
    """
    Can be specified multiple times for each
    egress rule. Each egress block supports fields documented below.
    """
    ingress: pulumi.Output[list]
    """
    Can be specified multiple times for each
    ingress rule. Each ingress block supports fields documented below.
    """
    name: pulumi.Output[str]
    """
    The name of the security group
    """
    owner_id: pulumi.Output[str]
    """
    The owner ID.
    """
    revoke_rules_on_delete: pulumi.Output[bool]
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the resource.
    """
    vpc_id: pulumi.Output[str]
    """
    The VPC ID. **Note that changing
    the `vpc_id` will _not_ restore any default security group rules that were
    modified, added, or removed.** It will be left in its current state
    """
    def __init__(__self__, __name__, __opts__=None, egress=None, ingress=None, revoke_rules_on_delete=None, tags=None, vpc_id=None):
        """
        Provides a resource to manage the default AWS Security Group.
        
        For EC2 Classic accounts, each region comes with a Default Security Group.
        Additionally, each VPC created in AWS comes with a Default Security Group that can be managed, but not
        destroyed. **This is an advanced resource**, and has special caveats to be aware
        of when using it. Please read this document in its entirety before using this
        resource.
        
        The `aws_default_security_group` behaves differently from normal resources, in that
        Terraform does not _create_ this resource, but instead "adopts" it
        into management. We can do this because these default security groups cannot be
        destroyed, and are created with a known set of default ingress/egress rules.
        
        When Terraform first adopts the Default Security Group, it **immediately removes all
        ingress and egress rules in the Security Group**. It then proceeds to create any rules specified in the
        configuration. This step is required so that only the rules specified in the
        configuration are created.
        
        This resource treats its inline rules as absolute; only the rules defined
        inline are created, and any additions/removals external to this resource will
        result in diff shown. For these reasons, this resource is incompatible with the
        `aws_security_group_rule` resource.
        
        For more information about Default Security Groups, see the AWS Documentation on
        [Default Security Groups][aws-default-security-groups].
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[list] egress: Can be specified multiple times for each
               egress rule. Each egress block supports fields documented below.
        :param pulumi.Input[list] ingress: Can be specified multiple times for each
               ingress rule. Each ingress block supports fields documented below.
        :param pulumi.Input[bool] revoke_rules_on_delete
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] vpc_id: The VPC ID. **Note that changing
               the `vpc_id` will _not_ restore any default security group rules that were
               modified, added, or removed.** It will be left in its current state
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['egress'] = egress

        __props__['ingress'] = ingress

        __props__['revoke_rules_on_delete'] = revoke_rules_on_delete

        __props__['tags'] = tags

        __props__['vpc_id'] = vpc_id

        __props__['arn'] = None
        __props__['name'] = None
        __props__['owner_id'] = None

        super(DefaultSecurityGroup, __self__).__init__(
            'aws:ec2/defaultSecurityGroup:DefaultSecurityGroup',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

