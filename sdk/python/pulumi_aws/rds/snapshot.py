# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class Snapshot(pulumi.CustomResource):
    allocated_storage: pulumi.Output[int]
    """
    Specifies the allocated storage size in gigabytes (GB).
    """
    availability_zone: pulumi.Output[str]
    """
    Specifies the name of the Availability Zone the DB instance was located in at the time of the DB snapshot.
    """
    db_instance_identifier: pulumi.Output[str]
    """
    The DB Instance Identifier from which to take the snapshot.
    """
    db_snapshot_arn: pulumi.Output[str]
    """
    The Amazon Resource Name (ARN) for the DB snapshot.
    """
    db_snapshot_identifier: pulumi.Output[str]
    """
    The Identifier for the snapshot.
    """
    encrypted: pulumi.Output[bool]
    """
    Specifies whether the DB snapshot is encrypted.
    """
    engine: pulumi.Output[str]
    """
    Specifies the name of the database engine.
    """
    engine_version: pulumi.Output[str]
    """
    Specifies the version of the database engine.
    """
    iops: pulumi.Output[int]
    """
    Specifies the Provisioned IOPS (I/O operations per second) value of the DB instance at the time of the snapshot.
    """
    kms_key_id: pulumi.Output[str]
    """
    The ARN for the KMS encryption key.
    """
    license_model: pulumi.Output[str]
    """
    License model information for the restored DB instance.
    """
    option_group_name: pulumi.Output[str]
    """
    Provides the option group name for the DB snapshot.
    """
    port: pulumi.Output[int]
    snapshot_type: pulumi.Output[str]
    source_db_snapshot_identifier: pulumi.Output[str]
    """
    The DB snapshot Arn that the DB snapshot was copied from. It only has value in case of cross customer or cross region copy.
    """
    source_region: pulumi.Output[str]
    """
    The region that the DB snapshot was created in or copied from.
    """
    status: pulumi.Output[str]
    """
    Specifies the status of this DB snapshot.
    """
    storage_type: pulumi.Output[str]
    """
    Specifies the storage type associated with DB snapshot.
    """
    tags: pulumi.Output[dict]
    """
    Key-value mapping of resource tags
    """
    vpc_id: pulumi.Output[str]
    """
    Specifies the storage type associated with DB snapshot.
    """
    def __init__(__self__, __name__, __opts__=None, db_instance_identifier=None, db_snapshot_identifier=None, tags=None):
        """
        Manages a RDS database instance snapshot. For managing RDS database cluster snapshots, see the [`aws_db_cluster_snapshot` resource](https://www.terraform.io/docs/providers/aws/r/db_cluster_snapshot.html).
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] db_instance_identifier: The DB Instance Identifier from which to take the snapshot.
        :param pulumi.Input[str] db_snapshot_identifier: The Identifier for the snapshot.
        :param pulumi.Input[dict] tags: Key-value mapping of resource tags
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not db_instance_identifier:
            raise TypeError('Missing required property db_instance_identifier')
        __props__['db_instance_identifier'] = db_instance_identifier

        if not db_snapshot_identifier:
            raise TypeError('Missing required property db_snapshot_identifier')
        __props__['db_snapshot_identifier'] = db_snapshot_identifier

        __props__['tags'] = tags

        __props__['allocated_storage'] = None
        __props__['availability_zone'] = None
        __props__['db_snapshot_arn'] = None
        __props__['encrypted'] = None
        __props__['engine'] = None
        __props__['engine_version'] = None
        __props__['iops'] = None
        __props__['kms_key_id'] = None
        __props__['license_model'] = None
        __props__['option_group_name'] = None
        __props__['port'] = None
        __props__['snapshot_type'] = None
        __props__['source_db_snapshot_identifier'] = None
        __props__['source_region'] = None
        __props__['status'] = None
        __props__['storage_type'] = None
        __props__['vpc_id'] = None

        super(Snapshot, __self__).__init__(
            'aws:rds/snapshot:Snapshot',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

