# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class Fleet(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    Fleet ARN.
    """
    build_id: pulumi.Output[str]
    """
    ID of the Gamelift Build to be deployed on the fleet.
    """
    description: pulumi.Output[str]
    """
    Human-readable description of the fleet.
    """
    ec2_inbound_permissions: pulumi.Output[list]
    """
    Range of IP addresses and port settings that permit inbound traffic to access server processes running on the fleet. See below.
    """
    ec2_instance_type: pulumi.Output[str]
    """
    Name of an EC2 instance type. e.g. `t2.micro`
    """
    log_paths: pulumi.Output[list]
    metric_groups: pulumi.Output[list]
    """
    List of names of metric groups to add this fleet to. A metric group tracks metrics across all fleets in the group. Defaults to `default`.
    """
    name: pulumi.Output[str]
    """
    The name of the fleet.
    """
    new_game_session_protection_policy: pulumi.Output[str]
    """
    Game session protection policy to apply to all instances in this fleet. e.g. `FullProtection`. Defaults to `NoProtection`.
    """
    operating_system: pulumi.Output[str]
    """
    Operating system of the fleet's computing resources.
    """
    resource_creation_limit_policy: pulumi.Output[dict]
    """
    Policy that limits the number of game sessions an individual player can create over a span of time for this fleet. See below.
    """
    runtime_configuration: pulumi.Output[dict]
    """
    Instructions for launching server processes on each instance in the fleet. See below.
    """
    def __init__(__self__, __name__, __opts__=None, build_id=None, description=None, ec2_inbound_permissions=None, ec2_instance_type=None, metric_groups=None, name=None, new_game_session_protection_policy=None, resource_creation_limit_policy=None, runtime_configuration=None):
        """
        Provides a Gamelift Fleet resource.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] build_id: ID of the Gamelift Build to be deployed on the fleet.
        :param pulumi.Input[str] description: Human-readable description of the fleet.
        :param pulumi.Input[list] ec2_inbound_permissions: Range of IP addresses and port settings that permit inbound traffic to access server processes running on the fleet. See below.
        :param pulumi.Input[str] ec2_instance_type: Name of an EC2 instance type. e.g. `t2.micro`
        :param pulumi.Input[list] metric_groups: List of names of metric groups to add this fleet to. A metric group tracks metrics across all fleets in the group. Defaults to `default`.
        :param pulumi.Input[str] name: The name of the fleet.
        :param pulumi.Input[str] new_game_session_protection_policy: Game session protection policy to apply to all instances in this fleet. e.g. `FullProtection`. Defaults to `NoProtection`.
        :param pulumi.Input[dict] resource_creation_limit_policy: Policy that limits the number of game sessions an individual player can create over a span of time for this fleet. See below.
        :param pulumi.Input[dict] runtime_configuration: Instructions for launching server processes on each instance in the fleet. See below.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not build_id:
            raise TypeError('Missing required property build_id')
        __props__['build_id'] = build_id

        __props__['description'] = description

        __props__['ec2_inbound_permissions'] = ec2_inbound_permissions

        if not ec2_instance_type:
            raise TypeError('Missing required property ec2_instance_type')
        __props__['ec2_instance_type'] = ec2_instance_type

        __props__['metric_groups'] = metric_groups

        __props__['name'] = name

        __props__['new_game_session_protection_policy'] = new_game_session_protection_policy

        __props__['resource_creation_limit_policy'] = resource_creation_limit_policy

        __props__['runtime_configuration'] = runtime_configuration

        __props__['arn'] = None
        __props__['log_paths'] = None
        __props__['operating_system'] = None

        super(Fleet, __self__).__init__(
            'aws:gamelift/fleet:Fleet',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

