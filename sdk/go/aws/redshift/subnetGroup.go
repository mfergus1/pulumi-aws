// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package redshift

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Creates a new Amazon Redshift subnet group. You must provide a list of one or more subnets in your existing Amazon Virtual Private Cloud (Amazon VPC) when creating Amazon Redshift subnet group.
type SubnetGroup struct {
	s *pulumi.ResourceState
}

// NewSubnetGroup registers a new resource with the given unique name, arguments, and options.
func NewSubnetGroup(ctx *pulumi.Context,
	name string, args *SubnetGroupArgs, opts ...pulumi.ResourceOpt) (*SubnetGroup, error) {
	if args == nil || args.SubnetIds == nil {
		return nil, errors.New("missing required argument 'SubnetIds'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["description"] = nil
		inputs["name"] = nil
		inputs["subnetIds"] = nil
		inputs["tags"] = nil
	} else {
		inputs["description"] = args.Description
		inputs["name"] = args.Name
		inputs["subnetIds"] = args.SubnetIds
		inputs["tags"] = args.Tags
	}
	s, err := ctx.RegisterResource("aws:redshift/subnetGroup:SubnetGroup", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &SubnetGroup{s: s}, nil
}

// GetSubnetGroup gets an existing SubnetGroup resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSubnetGroup(ctx *pulumi.Context,
	name string, id pulumi.ID, state *SubnetGroupState, opts ...pulumi.ResourceOpt) (*SubnetGroup, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["description"] = state.Description
		inputs["name"] = state.Name
		inputs["subnetIds"] = state.SubnetIds
		inputs["tags"] = state.Tags
	}
	s, err := ctx.ReadResource("aws:redshift/subnetGroup:SubnetGroup", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &SubnetGroup{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *SubnetGroup) URN() *pulumi.URNOutput {
	return r.s.URN
}

// ID is this resource's unique identifier assigned by its provider.
func (r *SubnetGroup) ID() *pulumi.IDOutput {
	return r.s.ID
}

// The description of the Redshift Subnet group. Defaults to "Managed by Terraform".
func (r *SubnetGroup) Description() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["description"])
}

// The name of the Redshift Subnet group.
func (r *SubnetGroup) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// An array of VPC subnet IDs.
func (r *SubnetGroup) SubnetIds() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["subnetIds"])
}

// A mapping of tags to assign to the resource.
func (r *SubnetGroup) Tags() *pulumi.MapOutput {
	return (*pulumi.MapOutput)(r.s.State["tags"])
}

// Input properties used for looking up and filtering SubnetGroup resources.
type SubnetGroupState struct {
	// The description of the Redshift Subnet group. Defaults to "Managed by Terraform".
	Description interface{}
	// The name of the Redshift Subnet group.
	Name interface{}
	// An array of VPC subnet IDs.
	SubnetIds interface{}
	// A mapping of tags to assign to the resource.
	Tags interface{}
}

// The set of arguments for constructing a SubnetGroup resource.
type SubnetGroupArgs struct {
	// The description of the Redshift Subnet group. Defaults to "Managed by Terraform".
	Description interface{}
	// The name of the Redshift Subnet group.
	Name interface{}
	// An array of VPC subnet IDs.
	SubnetIds interface{}
	// A mapping of tags to assign to the resource.
	Tags interface{}
}