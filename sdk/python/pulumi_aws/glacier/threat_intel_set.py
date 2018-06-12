# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class ThreatIntelSet(pulumi.CustomResource):
    """
    Provides a resource to manage a GuardDuty ThreatIntelSet.
    
    ~> **Note:** Currently in GuardDuty, users from member accounts cannot upload and further manage ThreatIntelSets. ThreatIntelSets that are uploaded by the master account are imposed on GuardDuty functionality in its member accounts. See the [GuardDuty API Documentation](https://docs.aws.amazon.com/guardduty/latest/ug/create-threat-intel-set.html)
    """
    def __init__(__self__, __name__, __opts__=None, activate=None, detector_id=None, format=None, location=None, name=None):
        """Create a ThreatIntelSet resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not activate:
            raise TypeError('Missing required property activate')
        elif not isinstance(activate, bool):
            raise TypeError('Expected property activate to be a bool')
        __self__.activate = activate
        """
        Specifies whether GuardDuty is to start using the uploaded ThreatIntelSet.
        """
        __props__['activate'] = activate

        if not detector_id:
            raise TypeError('Missing required property detector_id')
        elif not isinstance(detector_id, basestring):
            raise TypeError('Expected property detector_id to be a basestring')
        __self__.detector_id = detector_id
        """
        The detector ID of the GuardDuty.
        """
        __props__['detectorId'] = detector_id

        if not format:
            raise TypeError('Missing required property format')
        elif not isinstance(format, basestring):
            raise TypeError('Expected property format to be a basestring')
        __self__.format = format
        """
        The format of the file that contains the ThreatIntelSet. Valid values: `TXT` | `STIX` | `OTX_CSV` | `ALIEN_VAULT` | `PROOF_POINT` | `FIRE_EYE`
        """
        __props__['format'] = format

        if not location:
            raise TypeError('Missing required property location')
        elif not isinstance(location, basestring):
            raise TypeError('Expected property location to be a basestring')
        __self__.location = location
        """
        The URI of the file that contains the ThreatIntelSet.
        """
        __props__['location'] = location

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        The friendly name to identify the ThreatIntelSet.
        """
        __props__['name'] = name

        super(ThreatIntelSet, __self__).__init__(
            'aws:glacier/threatIntelSet:ThreatIntelSet',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'activate' in outs:
            self.activate = outs['activate']
        if 'detectorId' in outs:
            self.detector_id = outs['detectorId']
        if 'format' in outs:
            self.format = outs['format']
        if 'location' in outs:
            self.location = outs['location']
        if 'name' in outs:
            self.name = outs['name']