# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class SshKey(pulumi.CustomResource):
    body: pulumi.Output[str]
    """
    The public key portion of an SSH key pair.
    """
    server_id: pulumi.Output[str]
    """
    The Server ID of the Transfer Server (e.g. `s-12345678`)
    """
    user_name: pulumi.Output[str]
    """
    The name of the user account that is assigned to one or more servers.
    """
    def __init__(__self__, __name__, __opts__=None, body=None, server_id=None, user_name=None):
        """
        Provides a AWS Transfer User SSH Key resource.
        
        
        ```hcl
        resource "aws_transfer_server" "foo" {
        	identity_provider_type = "SERVICE_MANAGED"
        
        	tags {
        		NAME     = "tf-acc-test-transfer-server"
        	}
        }
        
        
        resource "aws_iam_role" "foo" {
        	name = "tf-test-transfer-user-iam-role-%s"
        
        	assume_role_policy = <<EOF
        {
        	"Version": "2012-10-17",
        	"Statement": [
        		{
        		"Effect": "Allow",
        		"Principal": {
        			"Service": "transfer.amazonaws.com"
        		},
        		"Action": "sts:AssumeRole"
        		}
        	]
        }
        EOF
        }
        
        resource "aws_iam_role_policy" "foo" {
        	name = "tf-test-transfer-user-iam-policy-%s"
        	role = "${aws_iam_role.foo.id}"
        	policy = <<POLICY
        {
        	"Version": "2012-10-17",
        	"Statement": [
        		{
        			"Sid": "AllowFullAccesstoS3",
        			"Effect": "Allow",
        			"Action": [
        				"s3:*"
        			],
        			"Resource": "*"
        		}
        	]
        }
        POLICY
        }
        
        
        resource "aws_transfer_user" "foo" {
        	server_id      = "${aws_transfer_server.foo.id}"
        	user_name      = "tftestuser"
        	role           = "${aws_iam_role.foo.arn}"
        
        	tags {
        		NAME = "tftestuser"
        	}
        }
        
        resource "aws_transfer_ssh_key" "foo" {
        	server_id = "${aws_transfer_server.foo.id}"
        	user_name = "${aws_transfer_user.foo.user_name}"
        	body 	  = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD3F6tyPEFEzV0LX3X8BsXdMsQz1x2cEikKDEY0aIj41qgxMCP/iteneqXSIFZBp5vizPvaoIR3Um9xK7PGoW8giupGn+EPuxIA4cDM4vzOqOkiMPhz5XK0whEjkVzTo4+S0puvDZuwIsdiW9mxhJc7tgBNL0cYlWSYVkz4G/fslNfRPW5mYAM49f4fhtxPb5ok4Q2Lg9dPKVHO/Bgeu5woMc7RY0p1ej6D4CKFE6lymSDJpW0YHX/wqE9+cfEauh7xZcG0q9t2ta6F6fmX0agvpFyZo8aFbXeUBr7osSCJNgvavWbM/06niWrOvYX2xwWdhXmXSrbX8ZbabVohBK41 example@example.com"
        }
        
        ```
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] body: The public key portion of an SSH key pair.
        :param pulumi.Input[str] server_id: The Server ID of the Transfer Server (e.g. `s-12345678`)
        :param pulumi.Input[str] user_name: The name of the user account that is assigned to one or more servers.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not body:
            raise TypeError('Missing required property body')
        __props__['body'] = body

        if not server_id:
            raise TypeError('Missing required property server_id')
        __props__['server_id'] = server_id

        if not user_name:
            raise TypeError('Missing required property user_name')
        __props__['user_name'] = user_name

        super(SshKey, __self__).__init__(
            'aws:transfer/sshKey:SshKey',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

