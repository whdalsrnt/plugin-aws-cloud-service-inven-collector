from spaceone.inventory.libs.schema.dynamic_field import TextDyField, ListDyField, BadgeItemDyField, BadgeDyField, EnumDyField
from spaceone.inventory.libs.schema.resource import CloudServiceTypeResource, CloudServiceTypeResponse, CloudServiceTypeMeta

cst_distribution = CloudServiceTypeResource()
cst_distribution.name = 'Distribution'
cst_distribution.provider = 'aws'
cst_distribution.group = 'CloudFront'
cst_distribution.tags = {
    'spaceone:icon': 'https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/cloud-services/aws/Amazon-CloudFront.svg',
    'spaceone:is_major': 'false',
}

cst_distribution._metadata = CloudServiceTypeMeta.set_fields(fields=[
    TextDyField.data_source('Id', 'data.id'),
    TextDyField.data_source('Domain Name', 'data.domain_name'),
    EnumDyField.data_source('Status', 'data.status', default_state={
        'safe': ['Deployed']
    }),
    ListDyField.data_source('CNAME', 'data.alias_icp_recordals', default_badge={
        'type': 'outline', 'sub_key': 'cname',
    }),
])

CLOUD_SERVICE_TYPES = [
    CloudServiceTypeResponse({'resource': cst_distribution}),
]