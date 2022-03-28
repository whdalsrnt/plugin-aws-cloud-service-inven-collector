import os
from spaceone.inventory.libs.common_parser import *
from spaceone.inventory.libs.schema.dynamic_widget import ChartWidget, CardWidget
from spaceone.inventory.libs.schema.dynamic_field import TextDyField, SearchField, EnumDyField, ListDyField
from spaceone.inventory.libs.schema.resource import CloudServiceTypeResource, CloudServiceTypeResponse, \
    CloudServiceTypeMeta

current_dir = os.path.abspath(os.path.dirname(__file__))

'''
 Instance
'''
instance_total_count_conf = os.path.join(current_dir, 'widget/instance_total_count.yaml')
instance_count_by_account_conf = os.path.join(current_dir, 'widget/instance_count_by_account.yaml')
instance_count_by_region_conf = os.path.join(current_dir, 'widget/instance_count_by_region.yaml')
instance_count_by_blueprint_conf = os.path.join(current_dir, 'widget/instance_count_by_blueprint.yaml')
instance_count_by_bundle_id_conf = os.path.join(current_dir, 'widget/instance_count_by_bundle_id.yaml')

cst_instance = CloudServiceTypeResource()
cst_instance.name = 'Instance'
cst_instance.provider = 'aws'
cst_instance.group = 'Lightsail'
cst_instance.labels = ['Compute']
cst_instance.is_primary = True
cst_instance.is_major = True
cst_instance.service_code = 'AmazonLightsail'
cst_instance.tags = {
    'spaceone:icon': 'https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/cloud-services/aws/Amazon-Lightsail.svg',
}

cst_instance._metadata = CloudServiceTypeMeta.set_meta(
    fields=[
        TextDyField.data_source('Name', 'name'),
        TextDyField.data_source('Blueprint', 'data.blueprint_name'),
        TextDyField.data_source('Bundle ID', 'data.bundle_id'),
        TextDyField.data_source('Core', 'data.hardware.cpu_count'),
        TextDyField.data_source('Memory', 'data.hardware.ram_size_in_gb'),
        EnumDyField.data_source('State', 'data.state.name', default_state={
            'safe': ['running'],
            'warning': ['provisioning'],
            'alert': ['stopped']
        }),

        TextDyField.data_source('Availability Zone', ']'),
        TextDyField.data_source('Public IP', 'data.public_ip_address'),
        TextDyField.data_source('Private IP', 'data.private_ip_address'),
        TextDyField.data_source('ARN', 'data.arn', options={
            'is_optional': True
        }),
        TextDyField.data_source('Support Code', 'data.support_code', options={
            'is_optional': True
        }),
        TextDyField.data_source('Region', 'data.location.region_name', options={
            'is_optional': True
        }),
        TextDyField.data_source('Is Static IP', 'data.is_static_ip', options={
            'is_optional': True
        }),
        TextDyField.data_source('Username', 'data.username', options={
            'is_optional': True
        }),
        TextDyField.data_source('SSH Key Name', 'data.ssh_key_name', options={
            'is_optional': True
        })
    ],
    search=[
        SearchField.set(name='Name', key='name'),
        SearchField.set(name='ARN', key='data.arn'),
        SearchField.set(name='Bundle ID', key='data.bundle_id'),
        SearchField.set(name='Blueprint', key='data.blueprint_name'),
        SearchField.set(name='CPU Core', key='data.hardware.cpu_count', data_type='integer'),
        SearchField.set(name='Memory', key='data.hardware.ram_size_in_gb', data_type='float'),
        SearchField.set(name='Availability Zone', key='data.location.availability_zone'),
        SearchField.set(name='Public IP', key='data.public_ip_address'),
        SearchField.set(name='Private IP', key='data.private_ip_address'),
        SearchField.set(name='Support Code', key='data.support_code'),
        SearchField.set(name='Is Static IP', key='data.is_static_ip', data_type='Boolean'),
        SearchField.set(name='Username', key='data.username'),
        SearchField.set(name='SSH Key name', key='data.ssh_key_name'),
    ],
    widget=[
        CardWidget.set(**get_data_from_yaml(instance_total_count_conf)),
        ChartWidget.set(**get_data_from_yaml(instance_count_by_account_conf)),
        ChartWidget.set(**get_data_from_yaml(instance_count_by_region_conf)),
        ChartWidget.set(**get_data_from_yaml(instance_count_by_blueprint_conf)),
        ChartWidget.set(**get_data_from_yaml(instance_count_by_bundle_id_conf)),
    ]
)

'''
 Disk
'''
disk_total_count_conf = os.path.join(current_dir, 'widget/disk_total_count.yaml')
disk_total_size_conf = os.path.join(current_dir, 'widget/disk_total_size.yaml')
disk_size_by_account_conf = os.path.join(current_dir, 'widget/disk_size_by_account.yaml')
disk_size_by_region_conf = os.path.join(current_dir, 'widget/disk_size_by_region.yaml')
disk_size_by_az_conf = os.path.join(current_dir, 'widget/disk_size_by_az.yaml')
disk_size_by_state_conf = os.path.join(current_dir, 'widget/disk_size_by_state.yaml')

cst_disk = CloudServiceTypeResource()
cst_disk.name = 'Disk'
cst_disk.provider = 'aws'
cst_disk.group = 'Lightsail'
cst_disk.labels = ['Compute', 'Storage']
cst_disk.is_primary = True
cst_disk.is_major = True
cst_disk.service_code = 'AmazonLightsail'
cst_disk.tags = {
    'spaceone:icon': 'https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/cloud-services/aws/Amazon-Lightsail.svg',
}

cst_disk._metadata = CloudServiceTypeMeta.set_meta(
    fields=[
        TextDyField.data_source('Name', 'name'),
        EnumDyField.data_source('State', 'data.state.name', default_state={
            'safe': ['in-use'],
            'available': ['available'],
            'warning': ['pending'],
            'disable': ['unknown'],
            'alert': ['error']
        }),
        TextDyField.data_source('Size', 'instance_size'),
        TextDyField.data_source('IOPS', 'data.iops'),
        TextDyField.data_source('Attached To', 'data.attached_to'),
        TextDyField.data_source('Availability Zone', 'data.location.availability_zone'),
        TextDyField.data_source('ARN', 'data.arn', options={
            'is_optional': True
        }),
        TextDyField.data_source('Support Code', 'data.support_code', options={
            'is_optional': True
        }),
        TextDyField.data_source('Region', 'data.location.region_name', options={
            'is_optional': True
        }),
        TextDyField.data_source('Is System Disk', 'data.is_system_disk', options={
            'is_optional': True
        }),
        TextDyField.data_source('Is Attached', 'data.is_attached', options={
            'is_optional': True
        }),
        TextDyField.data_source('Path', 'data.path', options={
            'is_optional': True
        }),
        TextDyField.data_source('GB In Use', 'data.gb_in_use', options={
            'is_optional': True
        }),
    ],
    search=[
        SearchField.set(name='Name', key='name'),
        SearchField.set(name='State', key='data.state.name'),
        SearchField.set(name='ARN', key='data.arn'),
        SearchField.set(name='Availability Zone', key='data.location.availability_zone'),
        SearchField.set(name='Size (GB)', key='instance_size', data_type='integer'),
        SearchField.set(name='In use (GB)', key='data.gb_in_use', data_type='integer'),
        SearchField.set(name='IOPS', key='data.iops', data_type='integer'),
        SearchField.set(name='Support Code', key='data.support_code'),
        SearchField.set(name='Attached to ', key='data.attached_to'),
        SearchField.set(name='Support Code', key='data.support_code'),
        SearchField.set(name='Is System Disk ', key='data.is_system_disk', data_type='Boolean'),
        SearchField.set(name='Path', key='data.path')
    ],
    widget=[
        CardWidget.set(**get_data_from_yaml(disk_total_count_conf)),
        CardWidget.set(**get_data_from_yaml(disk_total_size_conf)),
        ChartWidget.set(**get_data_from_yaml(disk_size_by_account_conf)),
        ChartWidget.set(**get_data_from_yaml(disk_size_by_region_conf)),
        ChartWidget.set(**get_data_from_yaml(disk_size_by_az_conf)),
        ChartWidget.set(**get_data_from_yaml(disk_size_by_state_conf))
    ]
)


'''
 Snapshot
'''
cst_snapshot = CloudServiceTypeResource()
cst_snapshot.name = 'Snapshot'
cst_snapshot.provider = 'aws'
cst_snapshot.group = 'Lightsail'
cst_snapshot.labels = ['Storage']
cst_snapshot.is_primary = True
cst_snapshot.is_major = True
cst_snapshot.service_code = 'AmazonLightsail'
cst_snapshot.tags = {
    'spaceone:icon': 'https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/cloud-services/aws/Amazon-Lightsail.svg',
}

cst_snapshot._metadata = CloudServiceTypeMeta.set_meta(
    fields=[
        TextDyField.data_source('Name', 'name'),
        TextDyField.data_source('State', 'data.state'),
        TextDyField.data_source('Size (GB)', 'data.size_in_gb'),
        TextDyField.data_source('Availability Zone', 'data.location.availability_zone'),
        TextDyField.data_source('ARN', 'data.arn', options={
            'is_optional': True
        }),
        TextDyField.data_source('Bundle ID', 'data.bundle_id', options={
            'is_optional': True
        }),
        TextDyField.data_source('Region', 'data.location.region_name', options={
            'is_optional': True
        }),
        TextDyField.data_source('Object Versioning', 'data.object_versioning', options={
            'is_optional': True
        }),
        ListDyField.data_source('Readonly Access Accounts', 'data.readonly_access_accounts', options={
            'delimiter': '<br>',
            'is_optional': True
        }),
        TextDyField.data_source('Access Log Config', 'data.access_log_config.enabled', options={
            'is_optional': True
        }),
    ],
    search=[
        SearchField.set(name='Name', key='name'),
        SearchField.set(name='ARN', key='data.arn'),
        SearchField.set(name='URL', key='data.url'),
        SearchField.set(name='Availability Zone', key='data.location.availability_zone'),
        SearchField.set(name='Bundle ID', key='data.bundle_id'),
        SearchField.set(name='Access Object', key='data.access_rules.get_object'),
        SearchField.set(name='Object Versioning ', key='data.object_versioning'),
        SearchField.set(name='Readonly Access Accounts', key='data.readonly_access_accounts'),
        SearchField.set(name='Access Log Config Enabled ', key='data.access_log_config.enabled', data_type='Boolean'),
        SearchField.set(name='Access Log Destination', key='data.access_log_config.destination')
    ],
    widget=[
    ]
)


'''
 Bucket
'''
bucket_total_count_conf = os.path.join(current_dir, 'widget/bucket_total_count.yaml')
bucket_count_by_region_conf = os.path.join(current_dir, 'widget/bucket_count_by_region.yaml')
bucket_count_by_account_conf = os.path.join(current_dir, 'widget/bucket_count_by_account.yaml')

cst_bucket = CloudServiceTypeResource()
cst_bucket.name = 'Bucket'
cst_bucket.provider = 'aws'
cst_bucket.group = 'Lightsail'
cst_bucket.labels = ['Storage']
cst_bucket.is_primary = True
cst_bucket.is_major = True
cst_bucket.service_code = 'AmazonLightsail'
cst_bucket.tags = {
    'spaceone:icon': 'https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/cloud-services/aws/Amazon-Lightsail.svg',
}

cst_bucket._metadata = CloudServiceTypeMeta.set_meta(
    fields=[
        TextDyField.data_source('Name', 'name'),
        TextDyField.data_source('State', 'data.state.code'),
        TextDyField.data_source('Object Access', 'data.access_rules.get_object'),
        TextDyField.data_source('URL', 'data.url'),
        TextDyField.data_source('Availability Zone', 'data.location.availability_zone'),
        TextDyField.data_source('ARN', 'data.arn', options={
            'is_optional': True
        }),
        TextDyField.data_source('Bundle ID', 'data.bundle_id', options={
            'is_optional': True
        }),
        TextDyField.data_source('Region', 'data.location.region_name', options={
            'is_optional': True
        }),
        TextDyField.data_source('Object Versioning', 'data.object_versioning', options={
            'is_optional': True
        }),
        ListDyField.data_source('Readonly Access Accounts', 'data.readonly_access_accounts', options={
            'delimiter': '<br>',
            'is_optional': True
        }),
        TextDyField.data_source('Access Log Config', 'data.access_log_config.enabled', options={
            'is_optional': True
        }),
    ],
    search=[
        SearchField.set(name='Name', key='name'),
        SearchField.set(name='ARN', key='data.arn'),
        SearchField.set(name='URL', key='data.url'),
        SearchField.set(name='Availability Zone', key='data.location.availability_zone'),
        SearchField.set(name='Bundle ID', key='data.bundle_id'),
        SearchField.set(name='Access Object', key='data.access_rules.get_object'),
        SearchField.set(name='Object Versioning ', key='data.object_versioning'),
        SearchField.set(name='Readonly Access Accounts', key='data.readonly_access_accounts'),
        SearchField.set(name='Access Log Config Enabled ', key='data.access_log_config.enabled', data_type='Boolean'),
        SearchField.set(name='Access Log Destination', key='data.access_log_config.destination')
    ],
    widget=[
        CardWidget.set(**get_data_from_yaml(bucket_total_count_conf)),
        ChartWidget.set(**get_data_from_yaml(bucket_count_by_region_conf)),
        ChartWidget.set(**get_data_from_yaml(bucket_count_by_account_conf)),
    ]
)

'''
 Static IP
'''
static_ip_total_count_conf = os.path.join(current_dir, 'widget/static_ip_total_count.yaml')
static_ip_count_by_region_conf = os.path.join(current_dir, 'widget/static_ip_count_by_region.yaml')
static_ip_count_by_account_conf = os.path.join(current_dir, 'widget/static_ip_count_by_account.yaml')

cst_ip = CloudServiceTypeResource()
cst_ip.name = 'StaticIP'
cst_ip.provider = 'aws'
cst_ip.group = 'Lightsail'
cst_ip.labels = ['Networking']
cst_ip.is_primary = True
cst_ip.is_major = True
cst_ip.service_code = 'AmazonLightsail'
cst_ip.tags = {
    'spaceone:icon': 'https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/cloud-services/aws/Amazon-Lightsail.svg',
}

cst_ip._metadata = CloudServiceTypeMeta.set_meta(
    fields=[
        TextDyField.data_source('Name', 'name'),
        TextDyField.data_source('IP Address', 'data.ip_address'),
        TextDyField.data_source('Attached to ', 'data.attached_to'),
        TextDyField.data_source('Availability Zone', 'data.location.availability_zone'),
        TextDyField.data_source('ARN', 'data.arn', options={
            'is_optional': True
        }),
        TextDyField.data_source('Region', 'data.location.region_name', options={
            'is_optional': True
        }),
        TextDyField.data_source('Is Attached', 'data.is_attached.enabled', options={
            'is_optional': True
        }),
    ],
    search=[
        SearchField.set(name='Name', key='name'),
        SearchField.set(name='IP Address', key='data.ip_address'),
        SearchField.set(name='ARN', key='data.arn'),
        SearchField.set(name='Support Code', key='data.support_code'),
        SearchField.set(name='Availability Zone', key='data.location.availability_zone'),
        SearchField.set(name='Is Attached', key='data.is_attached', data_type='Boolean'),
        SearchField.set(name='Attached to', key='data.attached_to')
    ],
    widget=[
        CardWidget.set(**get_data_from_yaml(static_ip_total_count_conf)),
        ChartWidget.set(**get_data_from_yaml(static_ip_count_by_region_conf)),
        ChartWidget.set(**get_data_from_yaml(static_ip_count_by_account_conf)),
    ]
)

'''
 Relation Database
'''
rdb_total_count_conf = os.path.join(current_dir, 'widget/rdb_total_count.yaml')
rdb_total_cpu_count_conf = os.path.join(current_dir, 'widget/rdb_total_cpu_count.yaml')
rdb_total_memory_size_conf = os.path.join(current_dir, 'widget/rdb_total_memory_size.yaml')
rdb_total_disk_size_conf = os.path.join(current_dir, 'widget/rdb_total_disk.yaml')
rdb_count_by_region_conf = os.path.join(current_dir, 'widget/rdb_count_by_region.yaml')
rdb_count_by_account_conf = os.path.join(current_dir, 'widget/rdb_count_by_account.yaml')

cst_rdb = CloudServiceTypeResource()
cst_rdb.name = 'Database'
cst_rdb.provider = 'aws'
cst_rdb.group = 'Lightsail'
cst_rdb.labels = ['Database']
cst_rdb.is_primary = True
cst_rdb.is_major = True
cst_rdb.service_code = 'AmazonLightsail'
cst_rdb.tags = {
    'spaceone:icon': 'https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/cloud-services/aws/Amazon-Lightsail.svg',
}

cst_rdb._metadata = CloudServiceTypeMeta.set_meta(
    fields=[
        TextDyField.data_source('Name', 'name'),
        TextDyField.data_source('Engine', 'data.engine'),
        EnumDyField.data_source('State', 'data.state', default_state={
            'safe': ['available'],
            'warning': ['creating', 'deleting', 'maintenance', 'modifying', 'rebooting',
                        'renaming', 'starting', 'stopping', 'upgrading'],
            'alert': ['failed', 'inaccessible-encryption-credentials', 'restore-error', 'stopped', 'storage-full']
        }),
        TextDyField.data_source('CPU ', 'data.hardware.cpu_count'),
        TextDyField.data_source('Memory ', 'data.hardware.ram_size_in_gb'),
        TextDyField.data_source('Disk (GB)', 'data.hardware.disk_size_in_gb'),
        TextDyField.data_source('Availability Zone', 'data.location.availability_zone'),
        TextDyField.data_source('ARN', 'data.arn', options={
            'is_optional': True
        }),
        TextDyField.data_source('Region', 'data.location.region_name', options={
            'is_optional': True
        }),
        TextDyField.data_source('Master Endpoint', 'data.master_endpoint.address', options={
            'is_optional': True
        }),
        TextDyField.data_source('Port', 'data.master_endpoint.port', options={
            'is_optional': True
        }),
        TextDyField.data_source('Blueprint ID', 'data.relation_database_blueprint_id', options={
            'is_optional': True
        }),
        TextDyField.data_source('Bundle ID', 'data.relation_database_bundle_id', options={
            'is_optional': True
        }),
        TextDyField.data_source('Engine Version', 'data.engine_version', options={
            'is_optional': True
        }),
        TextDyField.data_source('Master Database User', 'data.master_database_name', options={
            'is_optional': True
        }),
        TextDyField.data_source('Secondary Availability Zone', 'data.secondary_availability_zone', options={
            'is_optional': True
        }),
        TextDyField.data_source('Backup Retention Enabled', 'data.backup_retention_enabled', options={
            'is_optional': True
        }),
        TextDyField.data_source('CA Certificate Identifier', 'data.ca_certificate_identifier', options={
            'is_optional': True
        }),
        TextDyField.data_source('Publicly Accessible', 'data.publicly_accessible', options={
            'is_optional': True
        }),
    ],
    search=[
        SearchField.set(name='Name', key='name'),
        SearchField.set(name='State', key='data.state'),
        SearchField.set(name='Engine', key='data.engine'),
        SearchField.set(name='Engine Version', key='data.engine_version'),
        SearchField.set(name='ARN', key='data.arn'),
        SearchField.set(name='Support Code', key='data.support_code'),
        SearchField.set(name='Availability Zone', key='data.location.availability_zone'),
        SearchField.set(name='CPU', key='data.hardware.cpu_count', data_type='Integer'),
        SearchField.set(name='Memory', key='data.hardware.ram_size_in_gb', data_type='Float'),
        SearchField.set(name='Disk (GB)', key='data.hardware.disk_size_in_gb', data_type='Integer'),
        SearchField.set(name='Master Endpoint', key='data.master_endpoint.address'),
        SearchField.set(name='Port', key='data.master_endpoint.port', data_type='Integer'),
        SearchField.set(name='Blueprint ID', key='data.relation_database_blueprint_id'),
        SearchField.set(name='Bundle ID', key='data.support_code'),
        SearchField.set(name='Publicly Accessible', key='data.publicly_accessible', data_type='Boolean'),
        SearchField.set(name='Master Database User', key='data.master_database_name'),
        SearchField.set(name='Backup Retention Enabled', key='data.backup_retention_enabled'),
        SearchField.set(name='CA Certificate Identifier', key='data.ca_certificate_identifier'),
    ],
    widget=[
        CardWidget.set(**get_data_from_yaml(rdb_total_count_conf)),
        ChartWidget.set(**get_data_from_yaml(rdb_count_by_region_conf)),
        ChartWidget.set(**get_data_from_yaml(rdb_count_by_account_conf)),
    ]
)


'''
 Domain
'''
domain_total_count_conf = os.path.join(current_dir, 'widget/rdb_total_count.yaml')
domain_count_by_account_conf = os.path.join(current_dir, 'widget/rdb_count_by_account.yaml')

cst_domain = CloudServiceTypeResource()
cst_domain.name = 'Domain'
cst_domain.provider = 'aws'
cst_domain.group = 'Lightsail'
cst_domain.labels = ['Networking']
cst_domain.is_primary = True
cst_domain.is_major = True
cst_domain.service_code = 'AmazonLightsail'
cst_domain.tags = {
    'spaceone:icon': 'https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/cloud-services/aws/Amazon-Lightsail.svg',
}

cst_domain._metadata = CloudServiceTypeMeta.set_meta(
    fields=[
        TextDyField.data_source('Name', 'name'),
        TextDyField.data_source('Engine', 'data.engine'),
        EnumDyField.data_source('State', 'data.state', default_state={
            'safe': ['available'],
            'warning': ['creating', 'deleting', 'maintenance', 'modifying', 'rebooting',
                        'renaming', 'starting', 'stopping', 'upgrading'],
            'alert': ['failed', 'inaccessible-encryption-credentials', 'restore-error', 'stopped', 'storage-full']
        }),
        TextDyField.data_source('CPU ', 'data.hardware.cpu_count'),
        TextDyField.data_source('Memory ', 'data.hardware.ram_size_in_gb'),
        TextDyField.data_source('Disk (GB)', 'data.hardware.disk_size_in_gb'),
        TextDyField.data_source('Availability Zone', 'data.location.availability_zone'),
        TextDyField.data_source('ARN', 'data.arn', options={
            'is_optional': True
        }),
        TextDyField.data_source('Region', 'data.location.region_name', options={
            'is_optional': True
        }),
        TextDyField.data_source('Master Endpoint', 'data.master_endpoint.address', options={
            'is_optional': True
        }),
        TextDyField.data_source('Port', 'data.master_endpoint.port', options={
            'is_optional': True
        }),
        TextDyField.data_source('Blueprint ID', 'data.relation_database_blueprint_id', options={
            'is_optional': True
        }),
        TextDyField.data_source('Bundle ID', 'data.relation_database_bundle_id', options={
            'is_optional': True
        }),
        TextDyField.data_source('Engine Version', 'data.engine_version', options={
            'is_optional': True
        }),
        TextDyField.data_source('Master Database User', 'data.master_database_name', options={
            'is_optional': True
        }),
        TextDyField.data_source('Secondary Availability Zone', 'data.secondary_availability_zone', options={
            'is_optional': True
        }),
        TextDyField.data_source('Backup Retention Enabled', 'data.backup_retention_enabled', options={
            'is_optional': True
        }),
        TextDyField.data_source('CA Certificate Identifier', 'data.ca_certificate_identifier', options={
            'is_optional': True
        }),
        TextDyField.data_source('Publicly Accessible', 'data.publicly_accessible', options={
            'is_optional': True
        }),
    ],
    search=[
        SearchField.set(name='Name', key='name'),
        SearchField.set(name='State', key='data.state'),
        SearchField.set(name='Engine', key='data.engine'),
        SearchField.set(name='Engine Version', key='data.engine_version'),
        SearchField.set(name='ARN', key='data.arn'),
        SearchField.set(name='Support Code', key='data.support_code'),
        SearchField.set(name='Availability Zone', key='data.location.availability_zone'),
        SearchField.set(name='CPU', key='data.hardware.cpu_count', data_type='Integer'),
        SearchField.set(name='Memory', key='data.hardware.ram_size_in_gb', data_type='Float'),
        SearchField.set(name='Disk (GB)', key='data.hardware.disk_size_in_gb', data_type='Integer'),
        SearchField.set(name='Master Endpoint', key='data.master_endpoint.address'),
        SearchField.set(name='Port', key='data.master_endpoint.port', data_type='Integer'),
        SearchField.set(name='Blueprint ID', key='data.relation_database_blueprint_id'),
        SearchField.set(name='Bundle ID', key='data.support_code'),
        SearchField.set(name='Publicly Accessible', key='data.publicly_accessible', data_type='Boolean'),
        SearchField.set(name='Master Database User', key='data.master_database_name'),
        SearchField.set(name='Backup Retention Enabled', key='data.backup_retention_enabled'),
        SearchField.set(name='CA Certificate Identifier', key='data.ca_certificate_identifier'),
    ],
    widget=[
        CardWidget.set(**get_data_from_yaml(rdb_total_count_conf)),
        ChartWidget.set(**get_data_from_yaml(rdb_count_by_region_conf)),
        ChartWidget.set(**get_data_from_yaml(rdb_count_by_account_conf)),
    ]
)

CLOUD_SERVICE_TYPES = [
    CloudServiceTypeResponse({'resource': cst_instance}),
    CloudServiceTypeResponse({'resource': cst_disk}),
    CloudServiceTypeResponse({'resource': cst_snapshot}),
    CloudServiceTypeResponse({'resource': cst_bucket}),
    CloudServiceTypeResponse({'resource': cst_ip}),
    CloudServiceTypeResponse({'resource': cst_rdb}),
    CloudServiceTypeResponse({'resource': cst_domain}),
]
