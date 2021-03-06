# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class Database(pulumi.CustomResource):
    bucket: pulumi.Output[str]
    """
    Name of s3 bucket to save the results of the query execution.
    """
    encryption_configuration: pulumi.Output[dict]
    """
    The encryption key block AWS Athena uses to decrypt the data in S3, such as an AWS Key Management Service (AWS KMS) key. An `encryption_configuration` block is documented below.
    """
    force_destroy: pulumi.Output[bool]
    """
    A boolean that indicates all tables should be deleted from the database so that the database can be destroyed without error. The tables are *not* recoverable.
    """
    name: pulumi.Output[str]
    """
    Name of the database to create.
    """
    def __init__(__self__, __name__, __opts__=None, bucket=None, encryption_configuration=None, force_destroy=None, name=None):
        """
        Provides an Athena database.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] bucket: Name of s3 bucket to save the results of the query execution.
        :param pulumi.Input[dict] encryption_configuration: The encryption key block AWS Athena uses to decrypt the data in S3, such as an AWS Key Management Service (AWS KMS) key. An `encryption_configuration` block is documented below.
        :param pulumi.Input[bool] force_destroy: A boolean that indicates all tables should be deleted from the database so that the database can be destroyed without error. The tables are *not* recoverable.
        :param pulumi.Input[str] name: Name of the database to create.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not bucket:
            raise TypeError('Missing required property bucket')
        __props__['bucket'] = bucket

        __props__['encryption_configuration'] = encryption_configuration

        __props__['force_destroy'] = force_destroy

        __props__['name'] = name

        super(Database, __self__).__init__(
            'aws:athena/database:Database',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

