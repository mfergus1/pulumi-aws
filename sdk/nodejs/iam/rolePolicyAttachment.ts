// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

import {ARN} from "../index";
import {Role} from "./role";

/**
 * Attaches a Managed IAM Policy to an IAM role
 * 
 * > **NOTE:** The usage of this resource conflicts with the `aws_iam_policy_attachment` resource and will permanently show a difference if both are defined.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const aws_iam_policy_policy = new aws.iam.Policy("policy", {
 *     description: "A test policy",
 *     name: "test-policy",
 *     policy: `{
 *   "Version": "2012-10-17",
 *   "Statement": [
 *     {
 *       "Action": [
 *         "ec2:Describe*"
 *       ],
 *       "Effect": "Allow",
 *       "Resource": "*"
 *     }
 *   ]
 * }
 * `,
 * });
 * const aws_iam_role_role = new aws.iam.Role("role", {
 *     assumeRolePolicy: `    {
 *       "Version": "2012-10-17",
 *       "Statement": [
 *         {
 *           "Action": "sts:AssumeRole",
 *           "Principal": {
 *             "Service": "ec2.amazonaws.com"
 *           },
 *           "Effect": "Allow",
 *           "Sid": ""
 *         }
 *       ]
 *     }
 * `,
 *     name: "test-role",
 * });
 * const aws_iam_role_policy_attachment_test_attach = new aws.iam.RolePolicyAttachment("test-attach", {
 *     policyArn: aws_iam_policy_policy.arn,
 *     role: aws_iam_role_role.name,
 * });
 * ```
 */
export class RolePolicyAttachment extends pulumi.CustomResource {
    /**
     * Get an existing RolePolicyAttachment resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RolePolicyAttachmentState, opts?: pulumi.CustomResourceOptions): RolePolicyAttachment {
        return new RolePolicyAttachment(name, <any>state, { ...opts, id: id });
    }

    /**
     * The ARN of the policy you want to apply
     */
    public readonly policyArn: pulumi.Output<ARN>;
    /**
     * The role the policy should be applied to
     */
    public readonly role: pulumi.Output<Role>;

    /**
     * Create a RolePolicyAttachment resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: RolePolicyAttachmentArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: RolePolicyAttachmentArgs | RolePolicyAttachmentState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: RolePolicyAttachmentState = argsOrState as RolePolicyAttachmentState | undefined;
            inputs["policyArn"] = state ? state.policyArn : undefined;
            inputs["role"] = state ? state.role : undefined;
        } else {
            const args = argsOrState as RolePolicyAttachmentArgs | undefined;
            if (!args || args.policyArn === undefined) {
                throw new Error("Missing required property 'policyArn'");
            }
            if (!args || args.role === undefined) {
                throw new Error("Missing required property 'role'");
            }
            inputs["policyArn"] = args ? args.policyArn : undefined;
            inputs["role"] = args ? args.role : undefined;
        }
        super("aws:iam/rolePolicyAttachment:RolePolicyAttachment", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering RolePolicyAttachment resources.
 */
export interface RolePolicyAttachmentState {
    /**
     * The ARN of the policy you want to apply
     */
    readonly policyArn?: pulumi.Input<ARN>;
    /**
     * The role the policy should be applied to
     */
    readonly role?: pulumi.Input<Role>;
}

/**
 * The set of arguments for constructing a RolePolicyAttachment resource.
 */
export interface RolePolicyAttachmentArgs {
    /**
     * The ARN of the policy you want to apply
     */
    readonly policyArn: pulumi.Input<ARN>;
    /**
     * The role the policy should be applied to
     */
    readonly role: pulumi.Input<Role>;
}
