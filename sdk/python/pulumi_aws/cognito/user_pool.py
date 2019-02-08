# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class UserPool(pulumi.CustomResource):
    admin_create_user_config: pulumi.Output[dict]
    """
    The configuration for AdminCreateUser requests.
    """
    alias_attributes: pulumi.Output[list]
    """
    Attributes supported as an alias for this user pool. Possible values: phone_number, email, or preferred_username. Conflicts with `username_attributes`.
    """
    arn: pulumi.Output[str]
    """
    The ARN of the user pool.
    """
    auto_verified_attributes: pulumi.Output[list]
    """
    The attributes to be auto-verified. Possible values: email, phone_number.
    """
    creation_date: pulumi.Output[str]
    """
    The date the user pool was created.
    """
    device_configuration: pulumi.Output[dict]
    """
    The configuration for the user pool's device tracking.
    """
    email_configuration: pulumi.Output[dict]
    """
    The Email Configuration.
    """
    email_verification_message: pulumi.Output[str]
    """
    A string representing the email verification message. Must contain the `{####}` placeholder. **NOTE:** - If `email_verification_message` and `verification_message_template.email_message` are specified and the values are different, either one is prioritized and updated.
    """
    email_verification_subject: pulumi.Output[str]
    """
    A string representing the email verification subject. **NOTE:** - If `email_verification_subject` and `verification_message_template.email_subject` are specified and the values are different, either one is prioritized and updated.
    """
    endpoint: pulumi.Output[str]
    """
    The endpoint name of the user pool. Example format: cognito-idp.REGION.amazonaws.com/xxxx_yyyyy
    """
    lambda_config: pulumi.Output[dict]
    """
    A container for the AWS Lambda triggers associated with the user pool.
    """
    last_modified_date: pulumi.Output[str]
    """
    The date the user pool was last modified.
    """
    mfa_configuration: pulumi.Output[str]
    """
    Set to enable multi-factor authentication. Must be one of the following values (ON, OFF, OPTIONAL)
    """
    name: pulumi.Output[str]
    """
    The name of the attribute.
    """
    password_policy: pulumi.Output[dict]
    """
    A container for information about the user pool password policy.
    """
    schemas: pulumi.Output[list]
    """
    A container with the schema attributes of a user pool. Maximum of 50 attributes.
    """
    sms_authentication_message: pulumi.Output[str]
    """
    A string representing the SMS authentication message.
    """
    sms_configuration: pulumi.Output[dict]
    """
    The SMS Configuration.
    """
    sms_verification_message: pulumi.Output[str]
    """
    A string representing the SMS verification message.
    """
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the User Pool.
    """
    username_attributes: pulumi.Output[list]
    """
    Specifies whether email addresses or phone numbers can be specified as usernames when a user signs up. Conflicts with `alias_attributes`.
    """
    verification_message_template: pulumi.Output[dict]
    """
    The verification message templates configuration.
    """
    def __init__(__self__, resource_name, opts=None, admin_create_user_config=None, alias_attributes=None, auto_verified_attributes=None, device_configuration=None, email_configuration=None, email_verification_message=None, email_verification_subject=None, lambda_config=None, mfa_configuration=None, name=None, password_policy=None, schemas=None, sms_authentication_message=None, sms_configuration=None, sms_verification_message=None, tags=None, username_attributes=None, verification_message_template=None, __name__=None, __opts__=None):
        """
        Provides a Cognito User Pool resource.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[dict] admin_create_user_config: The configuration for AdminCreateUser requests.
        :param pulumi.Input[list] alias_attributes: Attributes supported as an alias for this user pool. Possible values: phone_number, email, or preferred_username. Conflicts with `username_attributes`.
        :param pulumi.Input[list] auto_verified_attributes: The attributes to be auto-verified. Possible values: email, phone_number.
        :param pulumi.Input[dict] device_configuration: The configuration for the user pool's device tracking.
        :param pulumi.Input[dict] email_configuration: The Email Configuration.
        :param pulumi.Input[str] email_verification_message: A string representing the email verification message. Must contain the `{####}` placeholder. **NOTE:** - If `email_verification_message` and `verification_message_template.email_message` are specified and the values are different, either one is prioritized and updated.
        :param pulumi.Input[str] email_verification_subject: A string representing the email verification subject. **NOTE:** - If `email_verification_subject` and `verification_message_template.email_subject` are specified and the values are different, either one is prioritized and updated.
        :param pulumi.Input[dict] lambda_config: A container for the AWS Lambda triggers associated with the user pool.
        :param pulumi.Input[str] mfa_configuration: Set to enable multi-factor authentication. Must be one of the following values (ON, OFF, OPTIONAL)
        :param pulumi.Input[str] name: The name of the attribute.
        :param pulumi.Input[dict] password_policy: A container for information about the user pool password policy.
        :param pulumi.Input[list] schemas: A container with the schema attributes of a user pool. Maximum of 50 attributes.
        :param pulumi.Input[str] sms_authentication_message: A string representing the SMS authentication message.
        :param pulumi.Input[dict] sms_configuration: The SMS Configuration.
        :param pulumi.Input[str] sms_verification_message: A string representing the SMS verification message.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the User Pool.
        :param pulumi.Input[list] username_attributes: Specifies whether email addresses or phone numbers can be specified as usernames when a user signs up. Conflicts with `alias_attributes`.
        :param pulumi.Input[dict] verification_message_template: The verification message templates configuration.
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

        __props__['admin_create_user_config'] = admin_create_user_config

        __props__['alias_attributes'] = alias_attributes

        __props__['auto_verified_attributes'] = auto_verified_attributes

        __props__['device_configuration'] = device_configuration

        __props__['email_configuration'] = email_configuration

        __props__['email_verification_message'] = email_verification_message

        __props__['email_verification_subject'] = email_verification_subject

        __props__['lambda_config'] = lambda_config

        __props__['mfa_configuration'] = mfa_configuration

        __props__['name'] = name

        __props__['password_policy'] = password_policy

        __props__['schemas'] = schemas

        __props__['sms_authentication_message'] = sms_authentication_message

        __props__['sms_configuration'] = sms_configuration

        __props__['sms_verification_message'] = sms_verification_message

        __props__['tags'] = tags

        __props__['username_attributes'] = username_attributes

        __props__['verification_message_template'] = verification_message_template

        __props__['arn'] = None
        __props__['creation_date'] = None
        __props__['endpoint'] = None
        __props__['last_modified_date'] = None

        super(UserPool, __self__).__init__(
            'aws:cognito/userPool:UserPool',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

