# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class SecurityGroupRule(pulumi.CustomResource):
    cidr_blocks: pulumi.Output[list]
    """
    List of CIDR blocks. Cannot be specified with `source_security_group_id`.
    """
    description: pulumi.Output[str]
    """
    Description of the rule.
    """
    from_port: pulumi.Output[int]
    """
    The start port (or ICMP type number if protocol is "icmp").
    """
    ipv6_cidr_blocks: pulumi.Output[list]
    """
    List of IPv6 CIDR blocks.
    """
    prefix_list_ids: pulumi.Output[list]
    """
    List of prefix list IDs (for allowing access to VPC endpoints).
    Only valid with `egress`.
    """
    protocol: pulumi.Output[str]
    """
    The protocol. If not icmp, tcp, udp, or all use the [protocol number](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml)
    """
    security_group_id: pulumi.Output[str]
    """
    The security group to apply this rule to.
    """
    self: pulumi.Output[bool]
    """
    If true, the security group itself will be added as
    a source to this ingress rule.
    """
    source_security_group_id: pulumi.Output[str]
    """
    The security group id to allow access to/from,
    depending on the `type`. Cannot be specified with `cidr_blocks`.
    """
    to_port: pulumi.Output[int]
    """
    The end port (or ICMP code if protocol is "icmp").
    """
    type: pulumi.Output[str]
    """
    The type of rule being created. Valid options are `ingress` (inbound)
    or `egress` (outbound).
    """
    def __init__(__self__, __name__, __opts__=None, cidr_blocks=None, description=None, from_port=None, ipv6_cidr_blocks=None, prefix_list_ids=None, protocol=None, security_group_id=None, self=None, source_security_group_id=None, to_port=None, type=None):
        """
        Provides a security group rule resource. Represents a single `ingress` or
        `egress` group rule, which can be added to external Security Groups.
        
        > **NOTE on Security Groups and Security Group Rules:** Terraform currently
        provides both a standalone Security Group Rule resource (a single `ingress` or
        `egress` rule), and a Security Group resource with `ingress` and `egress` rules
        defined in-line. At this time you cannot use a Security Group with in-line rules
        in conjunction with any Security Group Rule resources. Doing so will cause
        a conflict of rule settings and will overwrite rules.
        
        > **NOTE:** Setting `protocol = "all"` or `protocol = -1` with `from_port` and `to_port` will result in the EC2 API creating a security group rule with all ports open. This API behavior cannot be controlled by Terraform and may generate warnings in the future.
        
        > **NOTE:** Referencing Security Groups across VPC peering has certain restrictions. More information is available in the [VPC Peering User Guide](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-security-groups.html).
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[list] cidr_blocks: List of CIDR blocks. Cannot be specified with `source_security_group_id`.
        :param pulumi.Input[str] description: Description of the rule.
        :param pulumi.Input[int] from_port: The start port (or ICMP type number if protocol is "icmp").
        :param pulumi.Input[list] ipv6_cidr_blocks: List of IPv6 CIDR blocks.
        :param pulumi.Input[list] prefix_list_ids: List of prefix list IDs (for allowing access to VPC endpoints).
               Only valid with `egress`.
        :param pulumi.Input[str] protocol: The protocol. If not icmp, tcp, udp, or all use the [protocol number](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml)
        :param pulumi.Input[str] security_group_id: The security group to apply this rule to.
        :param pulumi.Input[bool] self: If true, the security group itself will be added as
               a source to this ingress rule.
        :param pulumi.Input[str] source_security_group_id: The security group id to allow access to/from,
               depending on the `type`. Cannot be specified with `cidr_blocks`.
        :param pulumi.Input[int] to_port: The end port (or ICMP code if protocol is "icmp").
        :param pulumi.Input[str] type: The type of rule being created. Valid options are `ingress` (inbound)
               or `egress` (outbound).
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['cidr_blocks'] = cidr_blocks

        __props__['description'] = description

        if not from_port:
            raise TypeError('Missing required property from_port')
        __props__['from_port'] = from_port

        __props__['ipv6_cidr_blocks'] = ipv6_cidr_blocks

        __props__['prefix_list_ids'] = prefix_list_ids

        if not protocol:
            raise TypeError('Missing required property protocol')
        __props__['protocol'] = protocol

        if not security_group_id:
            raise TypeError('Missing required property security_group_id')
        __props__['security_group_id'] = security_group_id

        __props__['self'] = self

        __props__['source_security_group_id'] = source_security_group_id

        if not to_port:
            raise TypeError('Missing required property to_port')
        __props__['to_port'] = to_port

        if not type:
            raise TypeError('Missing required property type')
        __props__['type'] = type

        super(SecurityGroupRule, __self__).__init__(
            'aws:ec2/securityGroupRule:SecurityGroupRule',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

