// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Provides a Step Function State Machine resource
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const aws_sfn_state_machine_sfn_state_machine = new aws.sfn.StateMachine("sfn_state_machine", {
 *     definition: aws_lambda_function_lambda.arn.apply(__arg0 => `{
 *   "Comment": "A Hello World example of the Amazon States Language using an AWS Lambda Function",
 *   "StartAt": "HelloWorld",
 *   "States": {
 *     "HelloWorld": {
 *       "Type": "Task",
 *       "Resource": "${__arg0%!v(PANIC=interface conversion: il.Node is nil, not *il.ResourceNode)}",
 *       "End": true
 *     }
 *   }
 * }
 * `),
 *     name: "my-state-machine",
 *     roleArn: aws_iam_role_iam_for_sfn.arn,
 * });
 * ```
 */
export class StateMachine extends pulumi.CustomResource {
    /**
     * Get an existing StateMachine resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: StateMachineState, opts?: pulumi.CustomResourceOptions): StateMachine {
        return new StateMachine(name, <any>state, { ...opts, id: id });
    }

    /**
     * The date the state machine was created.
     */
    public /*out*/ readonly creationDate: pulumi.Output<string>;
    /**
     * The Amazon States Language definition of the state machine.
     */
    public readonly definition: pulumi.Output<string>;
    /**
     * The name of the state machine.
     */
    public readonly name: pulumi.Output<string>;
    /**
     * The Amazon Resource Name (ARN) of the IAM role to use for this state machine.
     */
    public readonly roleArn: pulumi.Output<string>;
    /**
     * The current status of the state machine. Either "ACTIVE" or "DELETING".
     */
    public /*out*/ readonly status: pulumi.Output<string>;
    /**
     * Key-value mapping of resource tags
     */
    public readonly tags: pulumi.Output<{[key: string]: any} | undefined>;

    /**
     * Create a StateMachine resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: StateMachineArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: StateMachineArgs | StateMachineState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: StateMachineState = argsOrState as StateMachineState | undefined;
            inputs["creationDate"] = state ? state.creationDate : undefined;
            inputs["definition"] = state ? state.definition : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["roleArn"] = state ? state.roleArn : undefined;
            inputs["status"] = state ? state.status : undefined;
            inputs["tags"] = state ? state.tags : undefined;
        } else {
            const args = argsOrState as StateMachineArgs | undefined;
            if (!args || args.definition === undefined) {
                throw new Error("Missing required property 'definition'");
            }
            if (!args || args.roleArn === undefined) {
                throw new Error("Missing required property 'roleArn'");
            }
            inputs["definition"] = args ? args.definition : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["roleArn"] = args ? args.roleArn : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["creationDate"] = undefined /*out*/;
            inputs["status"] = undefined /*out*/;
        }
        super("aws:sfn/stateMachine:StateMachine", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering StateMachine resources.
 */
export interface StateMachineState {
    /**
     * The date the state machine was created.
     */
    readonly creationDate?: pulumi.Input<string>;
    /**
     * The Amazon States Language definition of the state machine.
     */
    readonly definition?: pulumi.Input<string>;
    /**
     * The name of the state machine.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The Amazon Resource Name (ARN) of the IAM role to use for this state machine.
     */
    readonly roleArn?: pulumi.Input<string>;
    /**
     * The current status of the state machine. Either "ACTIVE" or "DELETING".
     */
    readonly status?: pulumi.Input<string>;
    /**
     * Key-value mapping of resource tags
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
}

/**
 * The set of arguments for constructing a StateMachine resource.
 */
export interface StateMachineArgs {
    /**
     * The Amazon States Language definition of the state machine.
     */
    readonly definition: pulumi.Input<string>;
    /**
     * The name of the state machine.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The Amazon Resource Name (ARN) of the IAM role to use for this state machine.
     */
    readonly roleArn: pulumi.Input<string>;
    /**
     * Key-value mapping of resource tags
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
}
