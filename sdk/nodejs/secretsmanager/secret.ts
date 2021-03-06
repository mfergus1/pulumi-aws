// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Provides a resource to manage AWS Secrets Manager secret metadata. To manage a secret value, see the [`aws_secretsmanager_secret_version` resource](https://www.terraform.io/docs/providers/aws/r/secretsmanager_secret_version.html).
 */
export class Secret extends pulumi.CustomResource {
    /**
     * Get an existing Secret resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SecretState, opts?: pulumi.CustomResourceOptions): Secret {
        return new Secret(name, <any>state, { ...opts, id: id });
    }

    /**
     * Amazon Resource Name (ARN) of the secret.
     */
    public /*out*/ readonly arn: pulumi.Output<string>;
    /**
     * A description of the secret.
     */
    public readonly description: pulumi.Output<string | undefined>;
    /**
     * Specifies the ARN or alias of the AWS KMS customer master key (CMK) to be used to encrypt the secret values in the versions stored in this secret. If you don't specify this value, then Secrets Manager defaults to using the AWS account's default CMK (the one named `aws/secretsmanager`). If the default KMS CMK with that name doesn't yet exist, then AWS Secrets Manager creates it for you automatically the first time.
     */
    public readonly kmsKeyId: pulumi.Output<string | undefined>;
    /**
     * Specifies the friendly name of the new secret. The secret name can consist of uppercase letters, lowercase letters, digits, and any of the following characters: `/_+=.@-` Conflicts with `name_prefix`.
     */
    public readonly name: pulumi.Output<string>;
    /**
     * Creates a unique name beginning with the specified prefix. Conflicts with `name`.
     */
    public readonly namePrefix: pulumi.Output<string>;
    /**
     * A valid JSON document representing a [resource policy](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_resource-based-policies.html). For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html).
     */
    public readonly policy: pulumi.Output<string | undefined>;
    /**
     * Specifies the number of days that AWS Secrets Manager waits before it can delete the secret. This value can be `0` to force deletion without recovery or range from `7` to `30` days. The default value is `30`.
     */
    public readonly recoveryWindowInDays: pulumi.Output<number | undefined>;
    /**
     * Specifies whether automatic rotation is enabled for this secret.
     */
    public /*out*/ readonly rotationEnabled: pulumi.Output<boolean>;
    /**
     * Specifies the ARN of the Lambda function that can rotate the secret.
     */
    public readonly rotationLambdaArn: pulumi.Output<string | undefined>;
    /**
     * A structure that defines the rotation configuration for this secret. Defined below.
     */
    public readonly rotationRules: pulumi.Output<{ automaticallyAfterDays: number } | undefined>;
    /**
     * Specifies a key-value map of user-defined tags that are attached to the secret.
     */
    public readonly tags: pulumi.Output<{[key: string]: any} | undefined>;

    /**
     * Create a Secret resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: SecretArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: SecretArgs | SecretState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: SecretState = argsOrState as SecretState | undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["kmsKeyId"] = state ? state.kmsKeyId : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["namePrefix"] = state ? state.namePrefix : undefined;
            inputs["policy"] = state ? state.policy : undefined;
            inputs["recoveryWindowInDays"] = state ? state.recoveryWindowInDays : undefined;
            inputs["rotationEnabled"] = state ? state.rotationEnabled : undefined;
            inputs["rotationLambdaArn"] = state ? state.rotationLambdaArn : undefined;
            inputs["rotationRules"] = state ? state.rotationRules : undefined;
            inputs["tags"] = state ? state.tags : undefined;
        } else {
            const args = argsOrState as SecretArgs | undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["kmsKeyId"] = args ? args.kmsKeyId : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["namePrefix"] = args ? args.namePrefix : undefined;
            inputs["policy"] = args ? args.policy : undefined;
            inputs["recoveryWindowInDays"] = args ? args.recoveryWindowInDays : undefined;
            inputs["rotationLambdaArn"] = args ? args.rotationLambdaArn : undefined;
            inputs["rotationRules"] = args ? args.rotationRules : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["arn"] = undefined /*out*/;
            inputs["rotationEnabled"] = undefined /*out*/;
        }
        super("aws:secretsmanager/secret:Secret", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Secret resources.
 */
export interface SecretState {
    /**
     * Amazon Resource Name (ARN) of the secret.
     */
    readonly arn?: pulumi.Input<string>;
    /**
     * A description of the secret.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * Specifies the ARN or alias of the AWS KMS customer master key (CMK) to be used to encrypt the secret values in the versions stored in this secret. If you don't specify this value, then Secrets Manager defaults to using the AWS account's default CMK (the one named `aws/secretsmanager`). If the default KMS CMK with that name doesn't yet exist, then AWS Secrets Manager creates it for you automatically the first time.
     */
    readonly kmsKeyId?: pulumi.Input<string>;
    /**
     * Specifies the friendly name of the new secret. The secret name can consist of uppercase letters, lowercase letters, digits, and any of the following characters: `/_+=.@-` Conflicts with `name_prefix`.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Creates a unique name beginning with the specified prefix. Conflicts with `name`.
     */
    readonly namePrefix?: pulumi.Input<string>;
    /**
     * A valid JSON document representing a [resource policy](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_resource-based-policies.html). For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html).
     */
    readonly policy?: pulumi.Input<string>;
    /**
     * Specifies the number of days that AWS Secrets Manager waits before it can delete the secret. This value can be `0` to force deletion without recovery or range from `7` to `30` days. The default value is `30`.
     */
    readonly recoveryWindowInDays?: pulumi.Input<number>;
    /**
     * Specifies whether automatic rotation is enabled for this secret.
     */
    readonly rotationEnabled?: pulumi.Input<boolean>;
    /**
     * Specifies the ARN of the Lambda function that can rotate the secret.
     */
    readonly rotationLambdaArn?: pulumi.Input<string>;
    /**
     * A structure that defines the rotation configuration for this secret. Defined below.
     */
    readonly rotationRules?: pulumi.Input<{ automaticallyAfterDays: pulumi.Input<number> }>;
    /**
     * Specifies a key-value map of user-defined tags that are attached to the secret.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
}

/**
 * The set of arguments for constructing a Secret resource.
 */
export interface SecretArgs {
    /**
     * A description of the secret.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * Specifies the ARN or alias of the AWS KMS customer master key (CMK) to be used to encrypt the secret values in the versions stored in this secret. If you don't specify this value, then Secrets Manager defaults to using the AWS account's default CMK (the one named `aws/secretsmanager`). If the default KMS CMK with that name doesn't yet exist, then AWS Secrets Manager creates it for you automatically the first time.
     */
    readonly kmsKeyId?: pulumi.Input<string>;
    /**
     * Specifies the friendly name of the new secret. The secret name can consist of uppercase letters, lowercase letters, digits, and any of the following characters: `/_+=.@-` Conflicts with `name_prefix`.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Creates a unique name beginning with the specified prefix. Conflicts with `name`.
     */
    readonly namePrefix?: pulumi.Input<string>;
    /**
     * A valid JSON document representing a [resource policy](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_resource-based-policies.html). For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html).
     */
    readonly policy?: pulumi.Input<string>;
    /**
     * Specifies the number of days that AWS Secrets Manager waits before it can delete the secret. This value can be `0` to force deletion without recovery or range from `7` to `30` days. The default value is `30`.
     */
    readonly recoveryWindowInDays?: pulumi.Input<number>;
    /**
     * Specifies the ARN of the Lambda function that can rotate the secret.
     */
    readonly rotationLambdaArn?: pulumi.Input<string>;
    /**
     * A structure that defines the rotation configuration for this secret. Defined below.
     */
    readonly rotationRules?: pulumi.Input<{ automaticallyAfterDays: pulumi.Input<number> }>;
    /**
     * Specifies a key-value map of user-defined tags that are attached to the secret.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
}
