{
  "Images": [
    {
      "Architecture": "x86_64",
      "CreationDate": "2018-12-20T18:43:06.000Z",
      "ImageId": "ami-000af9f92529fce03",
      "ImageLocation": "701085748382/plannexo-docker-apps",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-07f7ed164d946cd1f",
            "VolumeSize": 30,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "Docker da App do Plannexo",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "plannexo-docker-apps",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Platform",
          "Value": "plannexo"
        },
        {
          "Key": "Owner",
          "Value": "plannexo"
        },
        {
          "Key": "Product",
          "Value": "plannexo20"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2020-01-10T17:11:45.000Z",
      "ImageId": "ami-001f88625ce14cddf",
      "ImageLocation": "701085748382/plannexo-integration-plannexo-02-10012020",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0a83eb34aba20f568",
            "VolumeSize": 8,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "Backup Semanal",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "plannexo-integration-plannexo-02-10012020",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Platform",
          "Value": "plannexo"
        },
        {
          "Key": "Owner",
          "Value": "plannexo"
        },
        {
          "Key": "Product",
          "Value": "plannexo-integracao"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-11-21T17:01:11.000Z",
      "ImageId": "ami-003b8cf299ae80958",
      "ImageLocation": "701085748382/wazuh-manager-21-11-2019-desativado",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-01761268209157914",
            "VolumeSize": 300,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdb",
          "VirtualName": "ephemeral0"
        },
        {
          "DeviceName": "/dev/sdc",
          "VirtualName": "ephemeral1"
        }
      ],
      "Description": "wazuh-manager-21-11-2019-desativado",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "wazuh-manager-21-11-2019-desativado",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2020-01-10T17:15:53.000Z",
      "ImageId": "ami-00567f174f7fc98d8",
      "ImageLocation": "701085748382/plannexo-api-integrration-01-10012020",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-07b8b6366ed28b2d0",
            "VolumeSize": 20,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "Bkp Semanal",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "plannexo-api-integrration-01-10012020",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Owner",
          "Value": "plannexo"
        },
        {
          "Key": "Product",
          "Value": "plannexo-integracao"
        },
        {
          "Key": "Platform",
          "Value": "plannexo"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-11-08T21:45:06.000Z",
      "ImageId": "ami-005ac2816c9eb65e5",
      "ImageLocation": "701085748382/elastic-graylog-frontend-01-bkp-08112019",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-01b1b27e426fae90b",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdb",
          "VirtualName": "ephemeral0"
        },
        {
          "DeviceName": "/dev/sdc",
          "VirtualName": "ephemeral1"
        }
      ],
      "Description": "elastic-graylog-frontend-01-bkp-08112019",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "elastic-graylog-frontend-01-bkp-08112019",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Owner",
          "Value": "graylog"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Platform",
          "Value": "infrastructure"
        },
        {
          "Key": "Service",
          "Value": "AMI"
        },
        {
          "Key": "Product",
          "Value": "graylog"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2020-02-11T12:50:51.000Z",
      "ImageId": "ami-0075d79a2afb74393",
      "ImageLocation": "701085748382/inst-wordpress-admin-01-desativado",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-037813c05f51de69e",
            "VolumeSize": 8,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdb",
          "VirtualName": "ephemeral0"
        },
        {
          "DeviceName": "/dev/sdc",
          "VirtualName": "ephemeral1"
        }
      ],
      "Description": "",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "inst-wordpress-admin-01-desativado",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Owner",
          "Value": "servicos"
        },
        {
          "Key": "Product",
          "Value": "bionexo"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Service",
          "Value": "AMI-web"
        },
        {
          "Key": "Country",
          "Value": "global"
        },
        {
          "Key": "Platform",
          "Value": "infrastructure"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2020-02-10T14:23:21.000Z",
      "ImageId": "ami-00a0c71308f6df062",
      "ImageLocation": "701085748382/kafka-node1-desligado",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0c0b33dd1c0646abd",
            "VolumeSize": 8,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "kafka-node1-desligado",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Platform",
          "Value": "kafka"
        },
        {
          "Key": "Product",
          "Value": "kafka"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Owner",
          "Value": "analytics"
        },
        {
          "Key": "Service",
          "Value": "AMI"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2020-01-10T17:14:56.000Z",
      "ImageId": "ami-00a21fa04bb9351b7",
      "ImageLocation": "701085748382/Plannexo-NewPentaho-Prod-10012020",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-099f2f6bb21ad6946",
            "VolumeSize": 15,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "Plannexo-NewPentaho-Prod-10012020",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-08-29T12:08:42.000Z",
      "ImageId": "ami-00d78d92d0fd73d5a",
      "ImageLocation": "701085748382/zabbix-server-backup",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-0ef8b23402e333326",
            "VolumeSize": 60,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "zabbix-server-backup",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-08-02T23:51:54.000Z",
      "ImageId": "ami-010562935985a357b",
      "ImageLocation": "701085748382/web-server-astrein-02082019",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "Platform": "windows",
      "PlatformDetails": "Windows",
      "UsageOperation": "RunInstances:0002",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0fe3607b09e30b3ab",
            "VolumeSize": 50,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "web-server-astrein-02082019",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "web-server-astrein-02082019",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2018-11-09T11:26:23.000Z",
      "ImageId": "ami-0131e5b7d438556bd",
      "ImageLocation": "701085748382/probr-lira-backup-remove",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-02a58ebe9e6916875",
            "VolumeSize": 30,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "probr-lira-backup-remove",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-10-17T17:24:02.000Z",
      "ImageId": "ami-016faef467aad840c",
      "ImageLocation": "701085748382/prod-institucionais-internacionais-17-10-2019",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-08fc94c059f1cd32b",
            "VolumeSize": 8,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdf",
          "Ebs": {
            "DeleteOnTermination": false,
            "Iops": 100,
            "SnapshotId": "snap-06db5ca19eef2f0a7",
            "VolumeSize": 6,
            "VolumeType": "io1",
            "Encrypted": false
          }
        }
      ],
      "Description": "imagem para subir novo ambiente institucionais internacionais pois atual esta com problema",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "prod-institucionais-internacionais-17-10-2019",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2020-01-20T16:42:13.000Z",
      "ImageId": "ami-01a88215f2d9668ef",
      "ImageLocation": "701085748382/sandbox-br-publinexo-privado-publico - apps1-20012020",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-074c66e1feb9654ff",
            "VolumeSize": 8,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "backup-antes-da-remocao",
      "Hypervisor": "xen",
      "Name": "sandbox-br-publinexo-privado-publico - apps1-20012020",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2020-01-10T17:20:31.000Z",
      "ImageId": "ami-01b602797d9cdb4fc",
      "ImageLocation": "701085748382/plannexo-integration-orchestrator-01-10012020",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-015873f1959a12057",
            "VolumeSize": 20,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "Backup Semanal",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "plannexo-integration-orchestrator-01-10012020",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Owner",
          "Value": "plannexo"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Product",
          "Value": "plannexo-integracao"
        },
        {
          "Key": "Platform",
          "Value": "plannexo"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2020-02-10T14:22:58.000Z",
      "ImageId": "ami-01d6cf9cea83dcf96",
      "ImageLocation": "701085748382/kafka-node2-desligado",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0b2f97a9cc27217c2",
            "VolumeSize": 8,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "kafka-node2-desligado",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Owner",
          "Value": "analytics"
        },
        {
          "Key": "Service",
          "Value": "AMI"
        },
        {
          "Key": "Platform",
          "Value": "kafka"
        },
        {
          "Key": "Product",
          "Value": "kafka"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Country",
          "Value": "br"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2018-08-22T01:34:12.000Z",
      "ImageId": "ami-01d80d9d3313a0e7b",
      "ImageLocation": "701085748382/backup-pre-update",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0283f29de41440e63",
            "VolumeSize": 16,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdf",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-03806c82a64965cd5",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdg",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-0c9339bb3fd4698f9",
            "VolumeSize": 12,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "",
      "Hypervisor": "xen",
      "Name": "backup-pre-update",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Service",
          "Value": "AMI"
        },
        {
          "Key": "Platform",
          "Value": "bionexo"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Owner",
          "Value": "bionexo"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Product",
          "Value": "bionexo"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-07-23T19:29:04.000Z",
      "ImageId": "ami-01e1a23b0a9e935f7",
      "ImageLocation": "701085748382/FrontEnd-Graylog-kibana",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-002139dd0bcc212de",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdb",
          "VirtualName": "ephemeral0"
        },
        {
          "DeviceName": "/dev/sdc",
          "VirtualName": "ephemeral1"
        }
      ],
      "Description": "AMI 23-07-2019",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "FrontEnd-Graylog-kibana",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Name",
          "Value": "Graylog/Kibana"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Product",
          "Value": "graylog"
        },
        {
          "Key": "Owner",
          "Value": "graylog"
        },
        {
          "Key": "Platform",
          "Value": "infrastructure"
        },
        {
          "Key": "Service",
          "Value": "AMI-elasticsearsh"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-04-24T15:04:08.000Z",
      "ImageId": "ami-01eac9ea78e1feb59",
      "ImageLocation": "701085748382/docker_app_1_20190424",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-039ea36b5aa7e1bfe",
            "VolumeSize": 30,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "ultima imagem do docker app antes de dar terminate",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "docker_app_1_20190424",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Product",
          "Value": "undefined"
        },
        {
          "Key": "Owner",
          "Value": "regene"
        },
        {
          "Key": "Platform",
          "Value": "bionexo"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-10-07T03:10:02.000Z",
      "ImageId": "ami-01f2c009dd377d146",
      "ImageLocation": "701085748382/JenkinsProd_i-07e7b08944c255297_07-10-2019",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-099648a1e836ec29a",
            "VolumeSize": 500,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "AMI Backup Daily JenkinsProd",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "JenkinsProd_i-07e7b08944c255297_07-10-2019",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Service",
          "Value": "AMI"
        },
        {
          "Key": "Country",
          "Value": "global"
        },
        {
          "Key": "Platform",
          "Value": "infrastructure"
        },
        {
          "Key": "Product",
          "Value": "infrastructure"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Owner",
          "Value": "engenharia"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2020-01-10T17:14:54.000Z",
      "ImageId": "ami-01fc4f86be1a5acce",
      "ImageLocation": "701085748382/Plannexo-Rstudio-Prod-v2-10012020",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0270e676fd1b3de91",
            "VolumeSize": 50,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "Bkp Semanal",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "Plannexo-Rstudio-Prod-v2-10012020",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-07-03T13:45:03.000Z",
      "ImageId": "ami-02085759ea761217a",
      "ImageLocation": "701085748382/prod-app Plannexo Migracao",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0a54f5c563f85ed02",
            "VolumeSize": 30,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "prod-app Plannexo Migracao",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-05-21T09:06:10.000Z",
      "ImageId": "ami-025e782bbeb31fd00",
      "ImageLocation": "701085748382/Plannexo_pentaho_20190521",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0f228055e155d19dc",
            "VolumeSize": 15,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "Image Pentaho Plannexo before install RStudio",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "Plannexo_pentaho_20190521",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2020-02-10T14:02:28.000Z",
      "ImageId": "ami-026b94b285caac9a0",
      "ImageLocation": "701085748382/plannexo-integration-sync-03-desligado",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-095067be98224ec55",
            "VolumeSize": 8,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "plannexo-integration-sync-03-desligado",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Owner",
          "Value": "plannexo"
        },
        {
          "Key": "Product",
          "Value": "plannexo-integracao"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Platform",
          "Value": "plannexo"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-07-05T01:14:02.000Z",
      "ImageId": "ami-027ef930ed3a2c9c0",
      "ImageLocation": "701085748382/migracao-plannexo20190704",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0b9e40ce0d7de1906",
            "VolumeSize": 30,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "migracao-plannexo20190704",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "migracao-plannexo20190704",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Platform",
          "Value": "plannexo"
        },
        {
          "Key": "Product",
          "Value": "plannexo"
        },
        {
          "Key": "Service",
          "Value": "AMI"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Owner",
          "Value": "plannexo"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-11-25T21:15:21.000Z",
      "ImageId": "ami-02a5c62ef23deee6d",
      "ImageLocation": "701085748382/ami-prod-br-database",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "PlatformDetails": "Red Hat Enterprise Linux",
      "UsageOperation": "RunInstances:0010",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-083537441a600c206",
            "VolumeSize": 50,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdd",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-0b77c21e8f0a0cf44",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdb",
          "VirtualName": "ephemeral0"
        },
        {
          "DeviceName": "/dev/sdc",
          "VirtualName": "ephemeral1"
        }
      ],
      "Description": "ami-prod-br-database",
      "Hypervisor": "xen",
      "Name": "ami-prod-br-database",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "Tags": [
        {
          "Key": "Owner",
          "Value": "classica"
        },
        {
          "Key": "Product",
          "Value": "bionexo"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Name",
          "Value": "AMI-db-prodbr-25112019"
        },
        {
          "Key": "Service",
          "Value": "AMI"
        },
        {
          "Key": "Platform",
          "Value": "infrastructure"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2020-01-31T13:54:13.000Z",
      "ImageId": "ami-02adbba78dddc2cc9",
      "ImageLocation": "701085748382/infrastructure-prod-mail-ap1-desativado",
      "ImageType": "machine",
      "Public": false,
      "KernelId": "aki-919dcaf8",
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-097a0867b11e5a706",
            "VolumeSize": 8,
            "VolumeType": "standard",
            "Encrypted": false
          }
        }
      ],
      "Description": "",
      "Hypervisor": "xen",
      "Name": "infrastructure-prod-mail-ap1-desativado",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "Tags": [
        {
          "Key": "Service",
          "Value": "AMI-smtp"
        },
        {
          "Key": "Country",
          "Value": "global"
        },
        {
          "Key": "Owner",
          "Value": "servicos"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Platform",
          "Value": "infrastructure"
        },
        {
          "Key": "Product",
          "Value": "infrastructure"
        }
      ],
      "VirtualizationType": "paravirtual"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2018-11-14T18:35:53.000Z",
      "ImageId": "ami-030743f97bb893a9b",
      "ImageLocation": "701085748382/Plannexo-pentaho-14112018",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-06761486cab917e64",
            "VolumeSize": 10,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "PLannexo Pentaho 14112018",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "Plannexo-pentaho-14112018",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Name",
          "Value": "Plannexo-pentaho-14112018"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2020-01-09T21:50:30.000Z",
      "ImageId": "ami-036684da1fbaf0d38",
      "ImageLocation": "701085748382/Plannexo - APP - NewProd-3",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-06d732b851aee96cb",
            "VolumeSize": 30,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "Plannexo - APP - NewProd-3",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "Plannexo - APP - NewProd-3",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Product",
          "Value": "plannexo20"
        },
        {
          "Key": "Owner",
          "Value": "plannexo"
        },
        {
          "Key": "Platform",
          "Value": "plannexo"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2020-01-09T21:48:12.000Z",
      "ImageId": "ami-0378c61174c900983",
      "ImageLocation": "701085748382/Plannexo - APP - NewProd-2",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-0f46c0de2d185495b",
            "VolumeSize": 30,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "Plannexo - APP - NewProd-2",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "Plannexo - APP - NewProd-2",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Platform",
          "Value": "plannexo"
        },
        {
          "Key": "Product",
          "Value": "plannexo20"
        },
        {
          "Key": "Owner",
          "Value": "plannexo"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2020-01-20T16:41:12.000Z",
      "ImageId": "ami-03d125fc9d0e00f81",
      "ImageLocation": "701085748382/sandbox-br-publinexo-privado-publico-20012020",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-06606b9c62f6e47fe",
            "VolumeSize": 30,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "backup-antes-da-remocao",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "sandbox-br-publinexo-privado-publico-20012020",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-09-04T17:19:42.000Z",
      "ImageId": "ami-03d7d1a1894ff55b0",
      "ImageLocation": "701085748382/bionexo-elasticsearch-prod-1567617453",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0ba43b86af57b3718",
            "VolumeSize": 8,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "bionexo-elasticsearch-prod-1567617453",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Service",
          "Value": "AMI"
        },
        {
          "Key": "Owner",
          "Value": "bionexo"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Product",
          "Value": "bionexo"
        },
        {
          "Key": "Platform",
          "Value": "elasticsearch"
        },
        {
          "Key": "Country",
          "Value": "global"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-11-05T21:08:35.000Z",
      "ImageId": "ami-03daee0f46c9f3e45",
      "ImageLocation": "701085748382/Plannexo_RStudio_upgrade",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-00486a8ec6f90ac85",
            "VolumeSize": 50,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "Plannexo_RStudio_upgrade",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "Plannexo_RStudio_upgrade",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2020-01-31T13:51:15.000Z",
      "ImageId": "ami-03e26cf5071db9be1",
      "ImageLocation": "701085748382/Relay-SMTP_BR_OFF-desligada",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-045b51e359cbc904b",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "Relay-SMTP_BR_OFF-desligada",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2018-10-26T22:30:08.000Z",
      "ImageId": "ami-0404489ead2938086",
      "ImageLocation": "701085748382/Nat_2D_20181026_backup",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-08068220dbeaa9f4e",
            "VolumeSize": 20,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "Nat_2D_20181026_backup",
      "Hypervisor": "xen",
      "Name": "Nat_2D_20181026_backup",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Name",
          "Value": "Nat_2D_20181026_backup"
        },
        {
          "Key": "Country",
          "Value": "global"
        },
        {
          "Key": "Platform",
          "Value": "infrastructure"
        },
        {
          "Key": "Product",
          "Value": "infrastructure"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Owner",
          "Value": "engenharia"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2020-02-10T13:59:47.000Z",
      "ImageId": "ami-0407fa17d808e672d",
      "ImageLocation": "701085748382/plannexo-integration-symc-05-desligado",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0d79fc551e732559c",
            "VolumeSize": 8,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "plannexo-integration-symc-05-desligado",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Owner",
          "Value": "plannexo"
        },
        {
          "Key": "Platform",
          "Value": "plannexo"
        },
        {
          "Key": "Product",
          "Value": "plannexo-integracao"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2020-01-10T17:26:28.000Z",
      "ImageId": "ami-044d1c38297b9a545",
      "ImageLocation": "701085748382/plannexo-integration-sync-04-10012020",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-07844e732ceaedbd1",
            "VolumeSize": 8,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "Bkp Semanal",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "plannexo-integration-sync-04-10012020",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Platform",
          "Value": "plannexo"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Product",
          "Value": "plannexo-integracao"
        },
        {
          "Key": "Owner",
          "Value": "plannexo"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-02-27T21:40:24.000Z",
      "ImageId": "ami-0463aef5208b80a1e",
      "ImageLocation": "701085748382/mstr-is-01020190227",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "ProductCodes": [
        {
          "ProductCodeId": "aw0evgkw8e5c1q413zgy5pjce",
          "ProductCodeType": "marketplace"
        }
      ],
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-05637b544e0d308f6",
            "VolumeSize": 32,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdf",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-089990be72fd2351c",
            "VolumeSize": 30,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdg",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-07796e54a79ea488b",
            "VolumeSize": 20,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "Backup de aumento de instancia",
      "EnaSupport": false,
      "Hypervisor": "xen",
      "Name": "mstr-is-01020190227",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "Tags": [
        {
          "Key": "Owner",
          "Value": "analytics"
        },
        {
          "Key": "Service",
          "Value": "AMI-mstr-is-01020190227"
        },
        {
          "Key": "Name",
          "Value": "MSTR AMI IS1"
        },
        {
          "Key": "Product",
          "Value": "bioanalytics"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Platform",
          "Value": "analytics"
        },
        {
          "Key": "Country",
          "Value": "br"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2020-01-10T17:12:43.000Z",
      "ImageId": "ami-0477b89bd8bc8b877",
      "ImageLocation": "701085748382/Plannexo - APP -SANDBOX-10012020",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-07c035ddccd078806",
            "VolumeSize": 30,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "Bkp semanal",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "Plannexo - APP -SANDBOX-10012020",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Environment",
          "Value": "sandbox"
        },
        {
          "Key": "Owner",
          "Value": "plannexo"
        },
        {
          "Key": "Product",
          "Value": "plannexo20"
        },
        {
          "Key": "Platform",
          "Value": "plannexo"
        },
        {
          "Key": "Country",
          "Value": "br"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2020-01-10T17:23:33.000Z",
      "ImageId": "ami-047e2e7de83504df4",
      "ImageLocation": "701085748382/plannexo-integration-sync-05-10012020",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-02a106571db18a3ce",
            "VolumeSize": 8,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "Backup Mensal",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "plannexo-integration-sync-05-10012020",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Product",
          "Value": "plannexo-integracao"
        },
        {
          "Key": "Owner",
          "Value": "plannexo"
        },
        {
          "Key": "Platform",
          "Value": "plannexo"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-06-10T18:40:32.000Z",
      "ImageId": "ami-04ad6c325f1a91da6",
      "ImageLocation": "701085748382/Plannexo-app-prod-backup-10-06-2019",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0ad2426d1e1135601",
            "VolumeSize": 30,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "Backup do Plannexo-APP-PROD",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "Plannexo-app-prod-backup-10-06-2019",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Platform",
          "Value": "plannexo"
        },
        {
          "Key": "Product",
          "Value": "plannexo20"
        },
        {
          "Key": "Environment",
          "Value": "sandbox"
        },
        {
          "Key": "Owner",
          "Value": "plannexo"
        },
        {
          "Key": "Name",
          "Value": "Plannexo-app-prod-backup-10-06-2019"
        },
        {
          "Key": "Country",
          "Value": "br"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-06-10T18:45:22.000Z",
      "ImageId": "ami-04be95fb162b5a078",
      "ImageLocation": "701085748382/Planexxo-NewPentaho-Prod-Backup-10-06-2019",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-059cc6d6f3a3e615d",
            "VolumeSize": 15,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "Backup do NewPentaho-Prod",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "Planexxo-NewPentaho-Prod-Backup-10-06-2019",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Owner",
          "Value": "plannexo"
        },
        {
          "Key": "Platform",
          "Value": "plannexo"
        },
        {
          "Key": "Product",
          "Value": "plannexo-integracao"
        },
        {
          "Key": "Name",
          "Value": "Planexxo-NewPentaho-Prod-Backup-10-06-2019"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Country",
          "Value": "br"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-08-14T14:34:17.000Z",
      "ImageId": "ami-052ea475d3c43b2e8",
      "ImageLocation": "701085748382/plannexo-Rstudio-bkp-140819",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0a853d766b93830c1",
            "VolumeSize": 10,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "plannexo-Rstudio-bkp-140819",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-11-14T18:00:58.000Z",
      "ImageId": "ami-0561bd93e819fa193",
      "ImageLocation": "701085748382/brweb-ami-14112019",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-035151a4b1c849d5e",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "brweb-ami",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "brweb-ami-14112019",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Service",
          "Value": "snapshot"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Product",
          "Value": "bionexo"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Owner",
          "Value": "classica"
        },
        {
          "Key": "Platform",
          "Value": "classica"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2020-01-10T17:08:37.000Z",
      "ImageId": "ami-056ac0cd57ba48d86",
      "ImageLocation": "701085748382/plannexo-integration-plannexo-01-10012020",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-037a1223f41f642b1",
            "VolumeSize": 8,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "bkp semanal",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "plannexo-integration-plannexo-01-10012020",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Product",
          "Value": "plannexo-integracao"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Owner",
          "Value": "plannexo"
        },
        {
          "Key": "Platform",
          "Value": "plannexo"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2020-02-10T14:36:45.000Z",
      "ImageId": "ami-061b1d8b92f98b402",
      "ImageLocation": "701085748382/prod-br-classica-brapp3-desativado",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-064edfad482db55cf",
            "VolumeSize": 30,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdg",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-0e1c0b24a554d43d9",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdf",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-08a7ddf06233bcc09",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "",
      "Hypervisor": "xen",
      "Name": "prod-br-classica-brapp3-desativado",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2020-01-10T00:40:07.000Z",
      "ImageId": "ami-06213836736847a0c",
      "ImageLocation": "701085748382/Plannexo-APP-Prod-09-01",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-006482ba4559e66a0",
            "VolumeSize": 40,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "Plannexo-APP-Prod-09-01",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Platform",
          "Value": "plannexo"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Product",
          "Value": "plannexo20"
        },
        {
          "Key": "Owner",
          "Value": "plannexo"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2020-01-20T16:40:26.000Z",
      "ImageId": "ami-0644d48eaefed9a42",
      "ImageLocation": "701085748382/publinexo-privado-publico-decreto-old-20012020",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-00c56c5eda0ac1086",
            "VolumeSize": 70,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "Backup-antes-da-remocao",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "publinexo-privado-publico-decreto-old-20012020",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-07-31T16:01:22.000Z",
      "ImageId": "ami-064d199c54210ae51",
      "ImageLocation": "701085748382/snapshot-graylog-31-07",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-092a388aedf1dcca9",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdb",
          "VirtualName": "ephemeral0"
        },
        {
          "DeviceName": "/dev/sdc",
          "VirtualName": "ephemeral1"
        }
      ],
      "Description": "graylog-31-07",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "snapshot-graylog-31-07",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-10-10T00:37:01.000Z",
      "ImageId": "ami-0677096c159820e4d",
      "ImageLocation": "701085748382/reindex-09/10",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-068899b99eb0d9a40",
            "VolumeSize": 50,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "reindex-09/10",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "reindex-09/10",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Name",
          "Value": "reindex-09/10"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2020-01-10T17:13:24.000Z",
      "ImageId": "ami-06a31e39cef31fb1e",
      "ImageLocation": "701085748382/integration-data-acquirer-spdm-10012020",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0ff3caff39f9f0b57",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "Backup Semanal",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "integration-data-acquirer-spdm-10012020",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Service",
          "Value": "AMI"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Owner",
          "Value": "plannexo"
        },
        {
          "Key": "Product",
          "Value": "integration"
        },
        {
          "Key": "Platform",
          "Value": "plannexo"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-08-29T22:48:05.000Z",
      "ImageId": "ami-06a74a10caefabf66",
      "ImageLocation": "701085748382/web-server-astrein-29082019",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "Platform": "windows",
      "PlatformDetails": "Windows",
      "UsageOperation": "RunInstances:0002",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0e9a3821ecae7b4b3",
            "VolumeSize": 50,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "web-server-astrein-29082019",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "web-server-astrein-29082019",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2018-12-07T19:25:48.000Z",
      "ImageId": "ami-06b0b65cb0a511537",
      "ImageLocation": "701085748382/nifi-base-image",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0dd13c37992d91334",
            "VolumeSize": 8,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdb",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-03dc0df79cd0b54d5",
            "VolumeSize": 350,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "nifi-base-image",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "nifi-base-image",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Product",
          "Value": "undefined"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Owner",
          "Value": "undefined"
        },
        {
          "Key": "Platform",
          "Value": "infrastructure"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-01-07T13:01:32.000Z",
      "ImageId": "ami-06bb68cb6f0bbd40c",
      "ImageLocation": "701085748382/wp02-preterminate",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-011d5c7a77219d6db",
            "VolumeSize": 8,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdb",
          "VirtualName": "ephemeral0"
        },
        {
          "DeviceName": "/dev/sdc",
          "VirtualName": "ephemeral1"
        }
      ],
      "Description": "",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "wp02-preterminate",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2020-01-10T17:13:45.000Z",
      "ImageId": "ami-075e1391ec866f9a0",
      "ImageLocation": "701085748382/plannexo-integration-orchestrator-02-10012020",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0ad4bfe3f82fdf80d",
            "VolumeSize": 20,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "bkp semanal",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "plannexo-integration-orchestrator-02-10012020",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Product",
          "Value": "plannexo-integracao"
        },
        {
          "Key": "Platform",
          "Value": "plannexo"
        },
        {
          "Key": "Owner",
          "Value": "plannexo"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2020-01-31T13:25:56.000Z",
      "ImageId": "ami-077dc2515b13b1612",
      "ImageLocation": "701085748382/prod-br-satelities-docnexo01-desligamento",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-07ea9d838a39b93d2",
            "VolumeSize": 30,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "prod-br-satelities-docnexo01-desligamento",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-04-24T15:04:39.000Z",
      "ImageId": "ami-079162ee68bb895c3",
      "ImageLocation": "701085748382/dockerp_app_2_20190424",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-00dc8c3057c6e2aa9",
            "VolumeSize": 30,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "ultima imagem do docker antes de terminate",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "dockerp_app_2_20190424",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Platform",
          "Value": "infrastructure"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Owner",
          "Value": "engenharia"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Product",
          "Value": "bionexo"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-06-10T18:38:15.000Z",
      "ImageId": "ami-07a1ca2d32e0e7831",
      "ImageLocation": "701085748382/Rstudio-backup-10-06-2019",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0006de178f1732d58",
            "VolumeSize": 10,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "Backup do Rstudio",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "Rstudio-backup-10-06-2019",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Name",
          "Value": "Plannexo-Rstudio-app-prod-backup-10-06-2019"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-12-07T22:42:29.000Z",
      "ImageId": "ami-07a8da4e7892a2024",
      "ImageLocation": "701085748382/brapp2-ami-07122019",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-0dda72fdbb4e8580c",
            "VolumeSize": 22,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdf",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-0d88f22e45ceb54df",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdg",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-0cca5c7ad373cb2a4",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "brapp2-ami",
      "Hypervisor": "xen",
      "Name": "brapp2-ami-07122019",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Owner",
          "Value": "classica"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Service",
          "Value": "AMI-web"
        },
        {
          "Key": "Product",
          "Value": "bionexo"
        },
        {
          "Key": "Name",
          "Value": "brapp2-ami-07122019"
        },
        {
          "Key": "Platform",
          "Value": "classica"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-09-30T16:00:21.000Z",
      "ImageId": "ami-07b848d0fc23d0e5d",
      "ImageLocation": "701085748382/zabbix01-antigo-30-09-2019",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-093fa9fbceb4b9f65",
            "VolumeSize": 60,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "zabbix01-antigo-30-09-2019",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-10-05T03:10:03.000Z",
      "ImageId": "ami-07d402b7e5d396907",
      "ImageLocation": "701085748382/JenkinsProd_i-07e7b08944c255297_05-10-2019",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-019d96bd4afee505f",
            "VolumeSize": 500,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "AMI Backup Daily JenkinsProd",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "JenkinsProd_i-07e7b08944c255297_05-10-2019",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Owner",
          "Value": "engenharia"
        },
        {
          "Key": "Country",
          "Value": "global"
        },
        {
          "Key": "Platform",
          "Value": "infrastructure"
        },
        {
          "Key": "Product",
          "Value": "infrastructure"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-02-13T18:40:03.000Z",
      "ImageId": "ami-081487df111710e88",
      "ImageLocation": "701085748382/plannexo_app_20190213",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0f632fa199744cc64",
            "VolumeSize": 30,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "Backup para troca de certificado",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "plannexo_app_20190213",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-09-20T03:10:03.000Z",
      "ImageId": "ami-081b5e0dc36984bc1",
      "ImageLocation": "701085748382/Zabbix_i-0ff73bbe212df5dbf_20-09-2019",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0b21c2e567c31681e",
            "VolumeSize": 16,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdf",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-02b8d982624a3cd4d",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdg",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-0a4dd025ae31b11fc",
            "VolumeSize": 12,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "AMI Backup Daily Zabbix",
      "Hypervisor": "xen",
      "Name": "Zabbix_i-0ff73bbe212df5dbf_20-09-2019",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2018-12-17T11:59:05.000Z",
      "ImageId": "ami-082ca5698e875339e",
      "ImageLocation": "701085748382/nifi-node3-img",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-045b95fbe2838483f",
            "VolumeSize": 8,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdb",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-013b4d5720cb93081",
            "VolumeSize": 350,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "nifi-node3-img",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "nifi-node3-img",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Product",
          "Value": "undefined"
        },
        {
          "Key": "Platform",
          "Value": "infrastructure"
        },
        {
          "Key": "Owner",
          "Value": "undefined"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2018-12-13T22:08:23.000Z",
      "ImageId": "ami-0844fc2c1b5360992",
      "ImageLocation": "701085748382/plannexo-docker-prod",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-06f5f1d263bececc3",
            "VolumeSize": 30,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "plannexo docker producao app 1",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "plannexo-docker-prod",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Product",
          "Value": "plannexo20"
        },
        {
          "Key": "Owner",
          "Value": "plannexo"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Name",
          "Value": "Plannexo - Docker - App 1"
        },
        {
          "Key": "Platform",
          "Value": "plannexo"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2020-01-10T17:22:50.000Z",
      "ImageId": "ami-08b707507e98b8c27",
      "ImageLocation": "701085748382/plannexo-integration-sync-03-10012020",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0f4abc1bbfc978604",
            "VolumeSize": 8,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "Bkp Semanal",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "plannexo-integration-sync-03-10012020",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Product",
          "Value": "plannexo-integracao"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Owner",
          "Value": "plannexo"
        },
        {
          "Key": "Platform",
          "Value": "plannexo"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-02-20T13:14:59.000Z",
      "ImageId": "ami-08b97d08dc1028f42",
      "ImageLocation": "701085748382/cronjobs1",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0ad909e4eb7e2e7c6",
            "VolumeSize": 8,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "02/2019",
      "Hypervisor": "xen",
      "Name": "cronjobs1",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Product",
          "Value": "bionexo"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Owner",
          "Value": "infrastructure"
        },
        {
          "Key": "Platform",
          "Value": "infrastructure"
        },
        {
          "Key": "Service",
          "Value": "AMI"
        },
        {
          "Key": "Country",
          "Value": "global"
        },
        {
          "Key": "Name",
          "Value": "infrastructure-prod:cronjobs1"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2020-01-29T14:21:29.000Z",
      "ImageId": "ami-08bb98353cf6cf2d8",
      "ImageLocation": "701085748382/prod-wordpress-app02-pulson-bkp",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0f82762cf0f3ea6cd",
            "VolumeSize": 8,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdf",
          "Ebs": {
            "DeleteOnTermination": false,
            "Iops": 100,
            "SnapshotId": "snap-0b16db93a8f04f8ac",
            "VolumeSize": 6,
            "VolumeType": "io1",
            "Encrypted": false
          }
        }
      ],
      "Description": "",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "prod-wordpress-app02-pulson-bkp",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-10-04T03:10:03.000Z",
      "ImageId": "ami-08e8ccbf3cf4a6e3c",
      "ImageLocation": "701085748382/JenkinsProd_i-07e7b08944c255297_04-10-2019",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-07e5938a60de776ea",
            "VolumeSize": 500,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "AMI Backup Daily JenkinsProd",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "JenkinsProd_i-07e7b08944c255297_04-10-2019",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Service",
          "Value": "AMI"
        },
        {
          "Key": "Country",
          "Value": "global"
        },
        {
          "Key": "Platform",
          "Value": "infrastructure"
        },
        {
          "Key": "Product",
          "Value": "infrastructure"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Owner",
          "Value": "engenharia"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2018-12-17T11:58:47.000Z",
      "ImageId": "ami-0931149286cd7cb75",
      "ImageLocation": "701085748382/nifi-node2-img",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0166d476ba0087f61",
            "VolumeSize": 8,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdb",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-086fd42f7e68d6ea6",
            "VolumeSize": 350,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "nifi-node2-img",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "nifi-node2-img",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Product",
          "Value": "undefined"
        },
        {
          "Key": "Owner",
          "Value": "undefined"
        },
        {
          "Key": "Platform",
          "Value": "infrastructure"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-08-28T12:55:32.000Z",
      "ImageId": "ami-095f90325cfe8aab2",
      "ImageLocation": "701085748382/pulso-bionexo28082019",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-080ef701bd5dcecf1",
            "VolumeSize": 8,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdf",
          "Ebs": {
            "DeleteOnTermination": false,
            "Iops": 100,
            "SnapshotId": "snap-01bdf1cd9ed2bf5b0",
            "VolumeSize": 6,
            "VolumeType": "io1",
            "Encrypted": false
          }
        }
      ],
      "Description": "",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "pulso-bionexo28082019",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-01-14T19:24:51.000Z",
      "ImageId": "ami-097b61cc1c640269d",
      "ImageLocation": "701085748382/nifi-node-padrao",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0768f5bc4360aa943",
            "VolumeSize": 8,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdb",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-048736018f4e42b71",
            "VolumeSize": 350,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "nifi-node-padrao",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "nifi-node-padrao",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Product",
          "Value": "undefined"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Platform",
          "Value": "infrastructure"
        },
        {
          "Key": "Owner",
          "Value": "undefined"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2020-02-04T17:23:10.000Z",
      "ImageId": "ami-09868167d5e177cc0",
      "ImageLocation": "701085748382/new-brapp1",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-0e0114e58a545263a",
            "VolumeSize": 22,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/xvdg",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-0a367bb94cac4f595",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdf",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-0f480e03ef1bbb880",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "new-brapp1",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Product",
          "Value": "classica"
        },
        {
          "Key": "Owner",
          "Value": "classica"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Platform",
          "Value": "bionexo"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-07-30T10:47:34.000Z",
      "ImageId": "ami-099a59003efbc38c6",
      "ImageLocation": "701085748382/astrein-bkp-2019-07-30",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "Platform": "windows",
      "PlatformDetails": "Windows",
      "UsageOperation": "RunInstances:0002",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0317c83c5771d2921",
            "VolumeSize": 50,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "Imagem criada para o backup antes da atualizacao da Astrein.",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "astrein-bkp-2019-07-30",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Owner",
          "Value": "engenharia"
        },
        {
          "Key": "Product",
          "Value": "infrastructure"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Service",
          "Value": "AMI-web"
        },
        {
          "Key": "Platform",
          "Value": "infrastructure"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-05-02T16:53:13.000Z",
      "ImageId": "ami-09eff51f27e2fa6d3",
      "ImageLocation": "701085748382/plannexo_openvpn_final_20190502",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-06efe9cb7bc216b1f",
            "VolumeSize": 8,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "Imagem final da OpenVPN do plannexo",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "plannexo_openvpn_final_20190502",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Service",
          "Value": "nat-vpn"
        },
        {
          "Key": "Platform",
          "Value": "plannexo"
        },
        {
          "Key": "Owner",
          "Value": "plannexo"
        },
        {
          "Key": "Product",
          "Value": "plannexo"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-05-13T18:33:39.000Z",
      "ImageId": "ami-0a29879aa6728d939",
      "ImageLocation": "701085748382/publinexo_13052019",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-059b8ba3d1542aab1",
            "VolumeSize": 30,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "Publinexo_13052019",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "publinexo_13052019",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-05-27T21:44:26.000Z",
      "ImageId": "ami-0a30bc0004e7dd6ed",
      "ImageLocation": "701085748382/rundeck1-snapshot-20190527",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-09274700f0554fef5",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "rundeck1-snapshot-20190527",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "rundeck1-snapshot-20190527",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2017-10-11T13:01:48.000Z",
      "ImageId": "ami-0a408e70",
      "ImageLocation": "701085748382/orig_ec2_inst_i-01513792fde579715-mstr-backup-ami-2017-10-11",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "Platform": "windows",
      "PlatformDetails": "Windows",
      "UsageOperation": "RunInstances:0002",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0b6dcb0695583872b",
            "VolumeSize": 50,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "Mstr Developer Windows - Backup - Source EC2 Inst - i-01513792fde579715",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "orig_ec2_inst_i-01513792fde579715-mstr-backup-ami-2017-10-11",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "Tags": [
        {
          "Key": "Product",
          "Value": "bioanalytics"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Platform",
          "Value": "analytics"
        },
        {
          "Key": "Owner",
          "Value": "analytics"
        },
        {
          "Key": "Name",
          "Value": "Mstr Developer"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-05-27T14:47:34.000Z",
      "ImageId": "ami-0a42d70836984b4bd",
      "ImageLocation": "701085748382/rundeck-27052019-snapshot",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0717bfa2051eef7c1",
            "VolumeSize": 30,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "rundeck-27052019-snapshot",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "rundeck-27052019-snapshot",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-02-27T21:41:19.000Z",
      "ImageId": "ami-0a500ed4ccb5b05ab",
      "ImageLocation": "701085748382/mstr-is02-20190227",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "ProductCodes": [
        {
          "ProductCodeId": "aw0evgkw8e5c1q413zgy5pjce",
          "ProductCodeType": "marketplace"
        }
      ],
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-066fa9c50d25a906b",
            "VolumeSize": 32,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "backup aumento de instancia",
      "EnaSupport": false,
      "Hypervisor": "xen",
      "Name": "mstr-is02-20190227",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "Tags": [
        {
          "Key": "Service",
          "Value": "AMI-mstr-is02-20190227"
        },
        {
          "Key": "Product",
          "Value": "bioanalytics"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Name",
          "Value": "MSTR AMI IS2"
        },
        {
          "Key": "Platform",
          "Value": "analytics"
        },
        {
          "Key": "Owner",
          "Value": "analytics"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-10-07T22:45:55.000Z",
      "ImageId": "ami-0a737762537b1af85",
      "ImageLocation": "701085748382/backup-rundeck",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-02f6517e4c3e559bb",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "backup-rundeck",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Country",
          "Value": "global"
        },
        {
          "Key": "Service",
          "Value": "AMI"
        },
        {
          "Key": "Platform",
          "Value": "infrastructure"
        },
        {
          "Key": "Product",
          "Value": "infrastructure"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Owner",
          "Value": "engenharia"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-11-21T21:21:39.000Z",
      "ImageId": "ami-0a7f4d1ebbe1a5fb9",
      "ImageLocation": "701085748382/bkp bd apex",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "PlatformDetails": "Red Hat Enterprise Linux",
      "UsageOperation": "RunInstances:0010",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0a8854a8b65ac2962",
            "VolumeSize": 50,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdd",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-07ab63ad9b6dc4980",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/xvdf",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-0f4bf54887f036a1b",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "bkp bd apex",
      "Hypervisor": "xen",
      "Name": "bkp bd apex",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "Tags": [
        {
          "Key": "Country",
          "Value": "global"
        },
        {
          "Key": "Name",
          "Value": "AMI-db-apex-25112019"
        },
        {
          "Key": "Owner",
          "Value": "analytics"
        },
        {
          "Key": "Service",
          "Value": "AMI"
        },
        {
          "Key": "Platform",
          "Value": "infrastructure"
        },
        {
          "Key": "Product",
          "Value": "bionexo"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2020-01-20T19:31:46.000Z",
      "ImageId": "ami-0ae24b5fd94f9cc1c",
      "ImageLocation": "701085748382/beta-institucionais-internacionais-01-20012020",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0aff549f97d945a8c",
            "VolumeSize": 8,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdf",
          "Ebs": {
            "DeleteOnTermination": false,
            "Iops": 100,
            "SnapshotId": "snap-07e6dcc9972c758e6",
            "VolumeSize": 6,
            "VolumeType": "io1",
            "Encrypted": false
          }
        }
      ],
      "Description": "AMI-Remocao-Maquina",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "beta-institucionais-internacionais-01-20012020",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Owner",
          "Value": "internacional"
        },
        {
          "Key": "Service",
          "Value": "AMI"
        },
        {
          "Key": "Product",
          "Value": "institucional"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Platform",
          "Value": "institucional"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2020-01-31T14:08:32.000Z",
      "ImageId": "ami-0b33ef48dcd878e47",
      "ImageLocation": "701085748382/srv-int-logs-desativado",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-04360c9ed44fc0b36",
            "VolumeSize": 30,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "srv-int-logs-desativado",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-09-30T16:01:13.000Z",
      "ImageId": "ami-0b6241c0656f3afbf",
      "ImageLocation": "701085748382/monitoring2-2019-09-30",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0511cb87feea72d4c",
            "VolumeSize": 16,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdf",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-0ac988ab5352ee271",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdg",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-06b5d77d627301a10",
            "VolumeSize": 12,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "",
      "Hypervisor": "xen",
      "Name": "monitoring2-2019-09-30",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Platform",
          "Value": "infrastructure"
        },
        {
          "Key": "Product",
          "Value": "infrastructure"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Service",
          "Value": "AMI"
        },
        {
          "Key": "Owner",
          "Value": "engenharia"
        },
        {
          "Key": "Country",
          "Value": "global"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2020-01-10T17:25:27.000Z",
      "ImageId": "ami-0b90b417ec553f124",
      "ImageLocation": "701085748382/plannexo-integration-sync-02-10012020",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0b8ba7e3a976d46f7",
            "VolumeSize": 20,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "Bkp Semanal",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "plannexo-integration-sync-02-10012020",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Platform",
          "Value": "plannexo"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Product",
          "Value": "plannexo-integracao"
        },
        {
          "Key": "Owner",
          "Value": "plannexo"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2018-09-15T12:03:13.000Z",
      "ImageId": "ami-0ba8e86f046822e4e",
      "ImageLocation": "701085748382/pre-migracao",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-00cd574a0c0b4973b",
            "VolumeSize": 16,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdf",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-0bd4b8afa149e2ffd",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdg",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-0ef2f43818335c52f",
            "VolumeSize": 12,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "",
      "Hypervisor": "xen",
      "Name": "pre-migracao",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-10-06T03:10:03.000Z",
      "ImageId": "ami-0bc8d9876a3fab3ec",
      "ImageLocation": "701085748382/JenkinsProd_i-07e7b08944c255297_06-10-2019",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0a21f9f3db5d94ea5",
            "VolumeSize": 500,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "AMI Backup Daily JenkinsProd",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "JenkinsProd_i-07e7b08944c255297_06-10-2019",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Owner",
          "Value": "engenharia"
        },
        {
          "Key": "Service",
          "Value": "AMI"
        },
        {
          "Key": "Product",
          "Value": "infrastructure"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Country",
          "Value": "global"
        },
        {
          "Key": "Platform",
          "Value": "infrastructure"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2020-01-20T16:37:26.000Z",
      "ImageId": "ami-0bda16a2766553546",
      "ImageLocation": "701085748382/sandbox.publinexo.es.PublicIP-20012020",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0365792c96fe69782",
            "VolumeSize": 12,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "",
      "Hypervisor": "xen",
      "Name": "sandbox.publinexo.es.PublicIP-20012020",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-11-04T12:25:14.000Z",
      "ImageId": "ami-0c13c7d8793bc4ccc",
      "ImageLocation": "701085748382/sandbox-br-classica-201911040925",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-05a2fb13555371416",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdb",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0d0a2a43ec8ceec53",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "",
      "Hypervisor": "xen",
      "Name": "sandbox-br-classica-201911040925",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2020-01-10T17:16:37.000Z",
      "ImageId": "ami-0c568f2236da96f93",
      "ImageLocation": "701085748382/Plannexo-APP-NewProd-4-10012020",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0125705dae2d7e155",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdb",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-0ab3f9db135691260",
            "VolumeSize": 30,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdf",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-0fe46e1380ca52b01",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "Backup Semanal",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "Plannexo-APP-NewProd-4-10012020",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Owner",
          "Value": "plannexo"
        },
        {
          "Key": "Platform",
          "Value": "plannexo"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Product",
          "Value": "plannexo20"
        },
        {
          "Key": "Country",
          "Value": "br"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2020-01-10T17:18:18.000Z",
      "ImageId": "ami-0c66ad06c6c4d0dd2",
      "ImageLocation": "701085748382/plannexo-integration-sync-01-10012020",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-06a7909ae9e8d0706",
            "VolumeSize": 20,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "Backup Semanal",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "plannexo-integration-sync-01-10012020",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Product",
          "Value": "plannexo-integracao"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Owner",
          "Value": "plannexo"
        },
        {
          "Key": "Platform",
          "Value": "plannexo"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2018-12-07T18:40:08.000Z",
      "ImageId": "ami-0c96236d49c2c68f6",
      "ImageLocation": "701085748382/prod-nifi-img",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-027cc4d15344142e4",
            "VolumeSize": 8,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdb",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-02abfc45613adf883",
            "VolumeSize": 350,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "prod-nifi-img",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "prod-nifi-img",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2020-01-10T20:37:24.000Z",
      "ImageId": "ami-0c9a49cd7baac97a6",
      "ImageLocation": "701085748382/Plannexo - APP - NewProd - 4 Deploy 10012020",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-023b127fd5a9aa060",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdb",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-00012b75ad5ddf5cb",
            "VolumeSize": 30,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdf",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-0d1db4bf81f7affcd",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "Plannexo - APP - NewProd - 4 Deploy 10012020",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Platform",
          "Value": "plannexo"
        },
        {
          "Key": "Owner",
          "Value": "plannexo"
        },
        {
          "Key": "Product",
          "Value": "plannexo20"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-11-14T19:22:25.000Z",
      "ImageId": "ami-0ca92d11e1d4dc50d",
      "ImageLocation": "701085748382/apache-ami-14112019",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0efc369c463e91f44",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdb",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-05c8ec57f8b9a5770",
            "VolumeSize": 50,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "apache ami",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "apache-ami-14112019",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Name",
          "Value": "prod-br-classica - Apache24_WS_A_14112019"
        },
        {
          "Key": "Owner",
          "Value": "classica"
        },
        {
          "Key": "Platform",
          "Value": "classica"
        },
        {
          "Key": "Product",
          "Value": "bionexo"
        },
        {
          "Key": "Service",
          "Value": "snapshot"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-11-05T14:15:26.000Z",
      "ImageId": "ami-0cd8b1ae9e80dc270",
      "ImageLocation": "701085748382/Plannexo-R-backup",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0c2c1c96928cfb815",
            "VolumeSize": 10,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "Plannexo-R-backup",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2020-01-10T14:43:18.000Z",
      "ImageId": "ami-0ceca22b3f2a5ec2c",
      "ImageLocation": "701085748382/plannexo-app-newprod-10-01-2020",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0784864f36474b98a",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdb",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-019a337327db9cdd7",
            "VolumeSize": 30,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdf",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-0233e4435de9be4c6",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "plannexo-app-newprod-10-01-2020",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Product",
          "Value": "plannexo20"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Owner",
          "Value": "plannexo"
        },
        {
          "Key": "Platform",
          "Value": "plannexo"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2020-01-10T17:16:47.000Z",
      "ImageId": "ami-0d265572cf9577a0d",
      "ImageLocation": "701085748382/plannexo-api-integrration-02-10012020",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-03943cf027db26580",
            "VolumeSize": 20,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "Bkp Semanal",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "plannexo-api-integrration-02-10012020",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Owner",
          "Value": "plannexo"
        },
        {
          "Key": "Product",
          "Value": "plannexo-integracao"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Platform",
          "Value": "plannexo"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-10-21T17:38:55.000Z",
      "ImageId": "ami-0dd0dd02e20ca5638",
      "ImageLocation": "701085748382/ampla-elasticsearch-prod-1571679424",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-09e54aaa118ccaecc",
            "VolumeSize": 8,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "ampla-elasticsearch-prod-1571679424",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Service",
          "Value": "ampla"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Platform",
          "Value": "publinexo-priv"
        },
        {
          "Key": "Owner",
          "Value": "publinexo"
        },
        {
          "Key": "Product",
          "Value": "publinexo"
        },
        {
          "Key": "Country",
          "Value": "br"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2018-11-09T11:26:07.000Z",
      "ImageId": "ami-0df7ecf53002c4e0d",
      "ImageLocation": "701085748382/sandbox-lira-backup-remove",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-06e415937085b1a7c",
            "VolumeSize": 20,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "sandbox-lira-backup-remove",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-07-25T19:52:43.000Z",
      "ImageId": "ami-0e113a2f6f07dd481",
      "ImageLocation": "701085748382/sirio-teste",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-02e2cad6af74c8545",
            "VolumeSize": 22,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdf",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-013d90e4fcb45f32d",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdg",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-0150166e38ea2af99",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "teste deploy sirio",
      "Hypervisor": "xen",
      "Name": "sirio-teste",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Name",
          "Value": "sirio-teste-deploy"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-12-07T22:43:24.000Z",
      "ImageId": "ami-0e3d1c6c6a0b7260d",
      "ImageLocation": "701085748382/brapp3-ami-07122019",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-04725f86512e22357",
            "VolumeSize": 30,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdg",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-03e7da45488486cc3",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdf",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-0f34c374db445f431",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "brapp3 ami",
      "Hypervisor": "xen",
      "Name": "brapp3-ami-07122019",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Name",
          "Value": "brapp3-ami-07122019"
        },
        {
          "Key": "Platform",
          "Value": "classica"
        },
        {
          "Key": "Owner",
          "Value": "classica"
        },
        {
          "Key": "Product",
          "Value": "bionexo"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Service",
          "Value": "AMI-web"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2020-02-10T14:23:43.000Z",
      "ImageId": "ami-0e8964cfeaea92fcd",
      "ImageLocation": "701085748382/kafka-node3-desligado",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-048d5b96fd658d997",
            "VolumeSize": 8,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "kafka-node3-desligado",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Product",
          "Value": "kafka"
        },
        {
          "Key": "Owner",
          "Value": "analytics"
        },
        {
          "Key": "Service",
          "Value": "AMI"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Platform",
          "Value": "kafka"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-08-27T22:17:19.000Z",
      "ImageId": "ami-0e8e6f0df26422e6e",
      "ImageLocation": "701085748382/elastic-regene-frontend-02-270819",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0e23897aba50f7bbc",
            "VolumeSize": 30,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdb",
          "VirtualName": "ephemeral0"
        },
        {
          "DeviceName": "/dev/sdc",
          "VirtualName": "ephemeral1"
        }
      ],
      "Description": "elastic-regene-frontend-02-270819",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "elastic-regene-frontend-02-270819",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Product",
          "Value": "regene"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Service",
          "Value": "AMI-elastic"
        },
        {
          "Key": "Owner",
          "Value": "regene"
        },
        {
          "Key": "Platform",
          "Value": "infrastructure"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2020-01-29T14:14:07.000Z",
      "ImageId": "ami-0ebb6b0605edd3f7c",
      "ImageLocation": "701085748382/prod-institucionais-internacionais",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-098f3ec04214f875d",
            "VolumeSize": 8,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdf",
          "Ebs": {
            "DeleteOnTermination": false,
            "Iops": 100,
            "SnapshotId": "snap-0055e50c59beeb5d0",
            "VolumeSize": 6,
            "VolumeType": "io1",
            "Encrypted": false
          }
        }
      ],
      "Description": "",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "prod-institucionais-internacionais",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2020-02-10T14:00:19.000Z",
      "ImageId": "ami-0ef796f6c09a23ff1",
      "ImageLocation": "701085748382/planexxo-integration-sync-04-desligado",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-00b73705dbfb931ac",
            "VolumeSize": 8,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "planexxo-integration-sync-04-desligado",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Platform",
          "Value": "plannexo"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Owner",
          "Value": "plannexo"
        },
        {
          "Key": "Product",
          "Value": "plannexo-integracao"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-12-27T16:07:22.000Z",
      "ImageId": "ami-0f58788c8913f492e",
      "ImageLocation": "701085748382/ami-bioanalytics-apps-1-27122019",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-072294127a15c6c9f",
            "VolumeSize": 20,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "ami-bioanalytics-apps-1-27122019",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "ami-bioanalytics-apps-1-27122019",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Service",
          "Value": "dw"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Platform",
          "Value": "analytics"
        },
        {
          "Key": "Name",
          "Value": "ami-bioanalytics-apps"
        },
        {
          "Key": "Product",
          "Value": "bioanalytics"
        },
        {
          "Key": "Owner",
          "Value": "analytics"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2018-12-17T11:58:17.000Z",
      "ImageId": "ami-0f995dfb5dc5a95d2",
      "ImageLocation": "701085748382/nifi-node1-img",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0985e3472eab75c85",
            "VolumeSize": 8,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdb",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-03af9155e3f33f041",
            "VolumeSize": 350,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "nifi-node1-img",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "nifi-node1-img",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Owner",
          "Value": "undefined"
        },
        {
          "Key": "Product",
          "Value": "undefined"
        },
        {
          "Key": "Platform",
          "Value": "infrastructure"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-07-19T19:08:51.000Z",
      "ImageId": "ami-0fa7f6e54719a5db6",
      "ImageLocation": "701085748382/graylog-r5.2xlarge",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0218a0cc93fa9776d",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdb",
          "VirtualName": "ephemeral0"
        },
        {
          "DeviceName": "/dev/sdc",
          "VirtualName": "ephemeral1"
        }
      ],
      "Description": "backup do graylog",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "graylog-r5.2xlarge",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Product",
          "Value": "graylog"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Service",
          "Value": "AMI-elasticsearsh"
        },
        {
          "Key": "Platform",
          "Value": "infrastructure"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Owner",
          "Value": "graylog"
        },
        {
          "Key": "Name",
          "Value": "Graylog"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2020-01-31T13:26:23.000Z",
      "ImageId": "ami-0fb9138b6b11ceb40",
      "ImageLocation": "701085748382/prod-br-satelites-docnexo02-desligamento",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-03b52a825e5046f02",
            "VolumeSize": 30,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "prod-br-satelites-docnexo02-desligamento",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2020-02-04T01:06:22.000Z",
      "ImageId": "ami-0fd9ae6b731cec0a6",
      "ImageLocation": "701085748382/snap-brapp2-03022020",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-0ddffe3cb140e5d70",
            "VolumeSize": 22,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdf",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-0a371aadb58f40def",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdg",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-0c0b1dff97eea6da1",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "",
      "Hypervisor": "xen",
      "Name": "snap-brapp2-03022020",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2019-10-03T03:10:03.000Z",
      "ImageId": "ami-0ffd4bf2fff11e386",
      "ImageLocation": "701085748382/JenkinsProd_i-07e7b08944c255297_03-10-2019",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0799b690c9477c3db",
            "VolumeSize": 500,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "AMI Backup Daily JenkinsProd",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "JenkinsProd_i-07e7b08944c255297_03-10-2019",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Owner",
          "Value": "engenharia"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Service",
          "Value": "AMI"
        },
        {
          "Key": "Country",
          "Value": "global"
        },
        {
          "Key": "Platform",
          "Value": "infrastructure"
        },
        {
          "Key": "Product",
          "Value": "infrastructure"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2016-04-21T13:59:07.000Z",
      "ImageId": "ami-11f4ed7b",
      "ImageLocation": "701085748382/microstrategy_10_3_20160421",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "Platform": "windows",
      "PlatformDetails": "Windows",
      "UsageOperation": "RunInstances:0002",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-7cb9ec78",
            "VolumeSize": 80,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "Backup da instancia do Microstrategy 10.3 atualizado",
      "Hypervisor": "xen",
      "Name": "microstrategy_10_3_20160421",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "Tags": [
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Platform",
          "Value": "analytcis"
        },
        {
          "Key": "Product",
          "Value": "analytcis"
        },
        {
          "Key": "Service",
          "Value": "AMI-microstrategy_10_3_20160421"
        },
        {
          "Key": "Owner",
          "Value": "analytcis"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2018-03-12T21:19:54.000Z",
      "ImageId": "ami-3869af45",
      "ImageLocation": "701085748382/bastion-plannexo",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-077179236dda62e21",
            "VolumeSize": 30,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "bastion-plannexo",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "bastion-plannexo",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Service",
          "Value": "AMI"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Platform",
          "Value": "bionexo"
        },
        {
          "Key": "Product",
          "Value": "bionexo"
        },
        {
          "Key": "Owner",
          "Value": "bionexo"
        },
        {
          "Key": "Country",
          "Value": "global"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2018-05-07T14:02:15.000Z",
      "ImageId": "ami-3adf5c45",
      "ImageLocation": "701085748382/plannexo-prod-backup_07052018",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-07a7fc7d64adffec6",
            "VolumeSize": 30,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "plannexo-prod-backup_07052018",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "plannexo-prod-backup_07052018",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Name",
          "Value": "Manuten\u00e7\u00e3o Plannexo"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2017-07-11T11:41:32.000Z",
      "ImageId": "ami-43858755",
      "ImageLocation": "701085748382/MST20170711",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "Platform": "windows",
      "PlatformDetails": "Windows",
      "UsageOperation": "RunInstances:0002",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-5a5459ee",
            "VolumeSize": 90,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "MST20170711",
      "Hypervisor": "xen",
      "Name": "MST20170711",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "Tags": [
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Platform",
          "Value": "analytics"
        },
        {
          "Key": "Owner",
          "Value": "analytics"
        },
        {
          "Key": "Product",
          "Value": "bioanalytics"
        },
        {
          "Key": "Name",
          "Value": "MSTR20170711"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Service",
          "Value": "AMI-MSTR20170711"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2018-02-28T20:37:25.000Z",
      "ImageId": "ami-44ec1939",
      "ImageLocation": "701085748382/plannexo.linux.280220181736",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-04386c3a0ce5acc5c",
            "VolumeSize": 30,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "AMI Plannexo - Linux - 28/02/2018 17:36",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "plannexo.linux.280220181736",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2016-01-08T21:11:32.000Z",
      "ImageId": "ami-4b94cd21",
      "ImageLocation": "701085748382/IMG_HOSPITALCENTER_20160108",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-dea068dc",
            "VolumeSize": 8,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdb",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-6d2c8668",
            "VolumeSize": 150,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/xvdc",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-9d455feb",
            "VolumeSize": 40,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "Image Backup HospitalCenter",
      "Hypervisor": "xen",
      "Name": "IMG_HOSPITALCENTER_20160108",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Product",
          "Value": "hospitalcenter"
        },
        {
          "Key": "Service",
          "Value": "AMI-storage"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2016-08-09T18:59:49.000Z",
      "ImageId": "ami-4cb7285b",
      "ImageLocation": "701085748382/BKP_php-app-1-emerg",
      "ImageType": "machine",
      "Public": false,
      "KernelId": "aki-88aa75e1",
      "OwnerId": "701085748382",
      "ProductCodes": [
        {
          "ProductCodeId": "aacglxeowvn5hy8sznltowyqe",
          "ProductCodeType": "marketplace"
        }
      ],
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-7ccbace1",
            "VolumeSize": 20,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "BKP_php-app-1-emerg - Uso Desconhecido",
      "Hypervisor": "xen",
      "Name": "BKP_php-app-1-emerg",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "Tags": [
        {
          "Key": "Service",
          "Value": "AMI-storage"
        },
        {
          "Key": "Product",
          "Value": "bionexo"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Name",
          "Value": "BKP_php-app-1-emerg - Uso Desconhecido"
        }
      ],
      "VirtualizationType": "paravirtual"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2018-05-02T12:21:21.000Z",
      "ImageId": "ami-4fe35830",
      "ImageLocation": "701085748382/Sandbox_BR_2018-05-02",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0fccd028df7f277f3",
            "VolumeSize": 22,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdb",
          "VirtualName": "ephemeral0"
        }
      ],
      "Description": "Sandbox_BR_2018-05-02",
      "Hypervisor": "xen",
      "Name": "Sandbox_BR_2018-05-02",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Name",
          "Value": "Ultima verso do Apache22 ON em Sandbox-BR"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2016-03-07T21:42:22.000Z",
      "ImageId": "ami-530b3139",
      "ImageLocation": "701085748382/hospitalcenter_bkp_20160307",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-db99a4cc",
            "VolumeSize": 8,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdb",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-f39b88e8",
            "VolumeSize": 150,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/xvdc",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-f987f1e0",
            "VolumeSize": 40,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "hospitalcenter_bkp_20160307",
      "Hypervisor": "xen",
      "Name": "hospitalcenter_bkp_20160307",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Product",
          "Value": "hospitalcenter"
        },
        {
          "Key": "Service",
          "Value": "AMI-storage"
        },
        {
          "Key": "Name",
          "Value": "Backup HospitalCenter"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2017-10-20T12:21:38.000Z",
      "ImageId": "ami-57538f2d",
      "ImageLocation": "701085748382/template-pudin",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "PlatformDetails": "Red Hat Enterprise Linux",
      "UsageOperation": "RunInstances:0010",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-09532cf2585b01f0f",
            "VolumeSize": 10,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdb",
          "VirtualName": "ephemeral0"
        }
      ],
      "Description": "Backup EC2 template-pudin",
      "Hypervisor": "xen",
      "Name": "template-pudin",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2018-01-03T15:26:45.000Z",
      "ImageId": "ami-59722523",
      "ImageLocation": "701085748382/plannexo-last",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "Platform": "windows",
      "PlatformDetails": "Windows",
      "UsageOperation": "RunInstances:0002",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0989a5817835555a3",
            "VolumeSize": 80,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "plannexo-last",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "Tags": [
        {
          "Key": "Owner",
          "Value": "plannexo"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Platform",
          "Value": "plannexo"
        },
        {
          "Key": "Product",
          "Value": "undefined"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2018-05-08T14:46:40.000Z",
      "ImageId": "ami-5d189a22",
      "ImageLocation": "701085748382/OpenVPN-plannexo",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-08afe15aa0b8174bf",
            "VolumeSize": 8,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "OpenVPN-plannexo",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "OpenVPN-plannexo",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Platform",
          "Value": "plannexo"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Owner",
          "Value": "plannexo"
        },
        {
          "Key": "Product",
          "Value": "plannexo-integracao"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2018-07-20T10:45:04.000Z",
      "ImageId": "ami-619e9a1e",
      "ImageLocation": "701085748382/RelaySMTP_OFF_bkp_2018-07-20",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-02ed50dff6302eac8",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "RelaySMTP_OFF_bkp_2018-07-20",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "RelaySMTP_OFF_bkp_2018-07-20",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Name",
          "Value": "RelaySMTP_OFF_bkp_2018-07-20"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2017-10-11T13:01:38.000Z",
      "ImageId": "ami-625e9018",
      "ImageLocation": "701085748382/orig_ec2_inst_i-049ddc48b747264f5-mstr-backup-ami-2017-10-11",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "ProductCodes": [
        {
          "ProductCodeId": "aw0evgkw8e5c1q413zgy5pjce",
          "ProductCodeType": "marketplace"
        }
      ],
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-085efc1a90d62010b",
            "VolumeSize": 32,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "Mstr WebServer/Tomcat 1 - Backup - Source EC2 Inst - i-049ddc48b747264f5",
      "EnaSupport": false,
      "Hypervisor": "xen",
      "Name": "orig_ec2_inst_i-049ddc48b747264f5-mstr-backup-ami-2017-10-11",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "Tags": [
        {
          "Key": "Owner",
          "Value": "analytics"
        },
        {
          "Key": "Name",
          "Value": "Mstr WS1"
        },
        {
          "Key": "Platform",
          "Value": "analytics"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Product",
          "Value": "bioanalytics"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2017-10-11T13:01:44.000Z",
      "ImageId": "ami-655e901f",
      "ImageLocation": "701085748382/orig_ec2_inst_i-0065eb1b460912e50-mstr-backup-ami-2017-10-11",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "ProductCodes": [
        {
          "ProductCodeId": "aw0evgkw8e5c1q413zgy5pjce",
          "ProductCodeType": "marketplace"
        }
      ],
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-04b8e37121ca8feac",
            "VolumeSize": 32,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "Mstr WebServer/Tomcat 2 - Backup - Source EC2 Inst - i-0065eb1b460912e50",
      "EnaSupport": false,
      "Hypervisor": "xen",
      "Name": "orig_ec2_inst_i-0065eb1b460912e50-mstr-backup-ami-2017-10-11",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "Tags": [
        {
          "Key": "Name",
          "Value": "Mstr WS2"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Product",
          "Value": "bioanalytics"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Platform",
          "Value": "analytics"
        },
        {
          "Key": "Owner",
          "Value": "analytics"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2016-08-16T18:29:46.000Z",
      "ImageId": "ami-6d62f87a",
      "ImageLocation": "701085748382/Sandbox_BR_CO_BioID_20160816_v2",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-207c09ba",
            "VolumeSize": 22,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdb",
          "VirtualName": "ephemeral0"
        }
      ],
      "Description": "Sandbox_BR_CO_BioID_20160816_v2",
      "Hypervisor": "xen",
      "Name": "Sandbox_BR_CO_BioID_20160816_v2",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Name",
          "Value": "Sandbox_BR_CO_BioID_20160816_v2"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2018-05-03T19:17:56.000Z",
      "ImageId": "ami-71ed680e",
      "ImageLocation": "701085748382/brapp2_20180503",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-01435b998651f9b30",
            "VolumeSize": 22,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdf",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-0e8886f6c70fce3ce",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdg",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-0facd846896fc0756",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "brapp2_20180503",
      "Hypervisor": "xen",
      "Name": "brapp2_20180503",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Platform",
          "Value": "classica"
        },
        {
          "Key": "Product",
          "Value": "bionexo"
        },
        {
          "Key": "Service",
          "Value": "AMI-web"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Owner",
          "Value": "classica"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2017-04-03T14:48:23.000Z",
      "ImageId": "ami-7b47c16d",
      "ImageLocation": "701085748382/Elastc_CleanUP_20170403",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0326ea1f09622d527",
            "VolumeSize": 20,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "Elastc_CleanUP_20170403",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "Elastc_CleanUP_20170403",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Name",
          "Value": "Elastc_CleanUP_20170403"
        },
        {
          "Key": "Platform",
          "Value": "infrastructure"
        },
        {
          "Key": "Product",
          "Value": "undefined"
        },
        {
          "Key": "Owner",
          "Value": "undefined"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2017-08-08T14:31:25.000Z",
      "ImageId": "ami-7d83ad06",
      "ImageLocation": "701085748382/last-img-nat-1d",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-003065b728201647e",
            "VolumeSize": 8,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "Ultima img antes de terminar inst. NAT-1d",
      "Hypervisor": "xen",
      "Name": "last-img-nat-1d",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Platform",
          "Value": "NAT-1d"
        },
        {
          "Key": "Product",
          "Value": "NAT-1d"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Service",
          "Value": "last-img-nat-1d"
        },
        {
          "Key": "Owner",
          "Value": "NAT-1d"
        },
        {
          "Key": "Country",
          "Value": "global"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2017-10-20T13:30:37.000Z",
      "ImageId": "ami-8b4b97f1",
      "ImageLocation": "701085748382/Mandela-Test",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "Platform": "windows",
      "PlatformDetails": "Windows",
      "UsageOperation": "RunInstances:0002",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0be00441596cfb9fd",
            "VolumeSize": 30,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "Mandela-Test",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "Mandela-Test",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Owner",
          "Value": "Mandela-Test"
        },
        {
          "Key": "Service",
          "Value": "AMI"
        },
        {
          "Key": "Environment",
          "Value": "teste"
        },
        {
          "Key": "Platform",
          "Value": "Mandela-Test"
        },
        {
          "Key": "Product",
          "Value": "Mandela-Test"
        },
        {
          "Key": "Country",
          "Value": "br"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2017-03-30T13:59:00.000Z",
      "ImageId": "ami-8c209b9a",
      "ImageLocation": "701085748382/teste-spark-01-all-in-one",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0df8d34d8281f7aaf",
            "VolumeSize": 20,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "Imagem para teste de carga do Spark (todas as configs em uma maquina)",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "teste-spark-01-all-in-one",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2017-10-11T13:01:36.000Z",
      "ImageId": "ami-8c428cf6",
      "ImageLocation": "701085748382/orig_ec2_inst_i-0e84b5b1fe87d5db7-mstr-backup-ami-2017-10-11",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "ProductCodes": [
        {
          "ProductCodeId": "aw0evgkw8e5c1q413zgy5pjce",
          "ProductCodeType": "marketplace"
        }
      ],
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-0563ca871363d6c28",
            "VolumeSize": 32,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "Mstr Inteligency Server 1 - Backup - Source EC2 Inst - i-0e84b5b1fe87d5db7",
      "EnaSupport": false,
      "Hypervisor": "xen",
      "Name": "orig_ec2_inst_i-0e84b5b1fe87d5db7-mstr-backup-ami-2017-10-11",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "Tags": [
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Product",
          "Value": "bioanalytics"
        },
        {
          "Key": "Platform",
          "Value": "analytics"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Owner",
          "Value": "analytics"
        },
        {
          "Key": "Name",
          "Value": "Mstr IS1"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2015-10-20T09:47:42.000Z",
      "ImageId": "ami-9f0456fa",
      "ImageLocation": "701085748382/windows_microstrategy_9",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "Platform": "windows",
      "PlatformDetails": "Windows",
      "UsageOperation": "RunInstances:0002",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-467dd5d1",
            "VolumeSize": 50,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "Servidor Microstrategy 9",
      "Hypervisor": "xen",
      "Name": "windows_microstrategy_9",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "Tags": [
        {
          "Key": "Name",
          "Value": "MicroStrategy 9 - Windows"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2018-07-19T23:02:48.000Z",
      "ImageId": "ami-a3898cdc",
      "ImageLocation": "701085748382/mail-ap-20180719",
      "ImageType": "machine",
      "Public": false,
      "KernelId": "aki-919dcaf8",
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0a4ebb7d80c7681c2",
            "VolumeSize": 30,
            "VolumeType": "standard",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdi",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-0fa98b881bf200051",
            "VolumeSize": 20,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "reboot event on amazon",
      "Hypervisor": "xen",
      "Name": "mail-ap-20180719",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "Tags": [
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Owner",
          "Value": "servicos"
        },
        {
          "Key": "Service",
          "Value": "AMI"
        },
        {
          "Key": "Country",
          "Value": "global"
        },
        {
          "Key": "Platform",
          "Value": "infrastructure"
        },
        {
          "Key": "Product",
          "Value": "infrastructure"
        },
        {
          "Key": "Name",
          "Value": "mail-ap-20180719"
        }
      ],
      "VirtualizationType": "paravirtual"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2018-03-12T21:28:57.000Z",
      "ImageId": "ami-a86fa9d5",
      "ImageLocation": "701085748382/hnsg-redepublica-windows",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "Platform": "windows",
      "PlatformDetails": "Windows",
      "UsageOperation": "RunInstances:0002",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0ca8ea5e0b0765420",
            "VolumeSize": 80,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "hnsg-redepublica-windows",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "hnsg-redepublica-windows",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "Tags": [
        {
          "Key": "Platform",
          "Value": "infrastructure"
        },
        {
          "Key": "Product",
          "Value": "undefined"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Owner",
          "Value": "undefined"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2015-09-09T18:00:55.000Z",
      "ImageId": "ami-afff91ca",
      "ImageLocation": "701085748382/pudin-ambari-agent-2015090902",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "PlatformDetails": "Red Hat Enterprise Linux",
      "UsageOperation": "RunInstances:0010",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-be1869f6",
            "VolumeSize": 10,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdb",
          "VirtualName": "ephemeral0"
        }
      ],
      "Description": "pudin-ambari-agent-2015090902",
      "Hypervisor": "xen",
      "Name": "pudin-ambari-agent-2015090902",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2018-01-09T18:13:16.000Z",
      "ImageId": "ami-b42e77ce",
      "ImageLocation": "701085748382/last-stable-plannexo-windows",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "Platform": "windows",
      "PlatformDetails": "Windows",
      "UsageOperation": "RunInstances:0002",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0c46d4eb3f292ff2e",
            "VolumeSize": 80,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "last-stable-plannexo-windows",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "Tags": [
        {
          "Key": "Owner",
          "Value": "plannexo"
        },
        {
          "Key": "Platform",
          "Value": "plannexo"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Product",
          "Value": "plannexo10"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2018-03-14T17:15:34.000Z",
      "ImageId": "ami-b89557c5",
      "ImageLocation": "701085748382/plannexo-iam-20180314",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-053b2c670dac46f80",
            "VolumeSize": 30,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "http,php,linux",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "plannexo-iam-20180314",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Product",
          "Value": "plannexo20"
        },
        {
          "Key": "Owner",
          "Value": "plannexo"
        },
        {
          "Key": "Platform",
          "Value": "plannexo"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2017-10-11T13:01:40.000Z",
      "ImageId": "ami-d05f91aa",
      "ImageLocation": "701085748382/orig_ec2_inst_i-0344568996671bf90-mstr-backup-ami-2017-10-11",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "ProductCodes": [
        {
          "ProductCodeId": "aw0evgkw8e5c1q413zgy5pjce",
          "ProductCodeType": "marketplace"
        }
      ],
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-0455dfcd3f4be3953",
            "VolumeSize": 32,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "Mstr Inteligency Server 2 - Backup - Source EC2 Inst - i-0344568996671bf90",
      "EnaSupport": false,
      "Hypervisor": "xen",
      "Name": "orig_ec2_inst_i-0344568996671bf90-mstr-backup-ami-2017-10-11",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "Tags": [
        {
          "Key": "Product",
          "Value": "bioanalytics"
        },
        {
          "Key": "Owner",
          "Value": "analytics"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Platform",
          "Value": "analytics"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Name",
          "Value": "Mstr IS2"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2016-02-02T16:07:09.000Z",
      "ImageId": "ami-d2a887b8",
      "ImageLocation": "701085748382/projectOrion_1.0",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "PlatformDetails": "Red Hat Enterprise Linux",
      "UsageOperation": "RunInstances:0010",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-3a86013f",
            "VolumeSize": 50,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdd",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-4d1d6d26",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/xvdab",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-834a1ee8",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/xvdad",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-da679290",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/xvdae",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-dadc69ae",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/xvdac",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-5fac105e",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/xvdaa",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-ba92dcb8",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/xvdo",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-a10adbee",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/xvdp",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-35febd41",
            "VolumeSize": 50,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdb",
          "VirtualName": "ephemeral0"
        },
        {
          "DeviceName": "/dev/sdc",
          "VirtualName": "ephemeral1"
        }
      ],
      "Description": "Project Orion DB - (image from Oracle production - baseline from database version)",
      "Hypervisor": "xen",
      "Name": "projectOrion_1.0",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2018-07-12T11:03:14.000Z",
      "ImageId": "ami-d8e3d2a7",
      "ImageLocation": "701085748382/SandboxApache24_BR",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-03de46e5a641470f8",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdb",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0a84bdbeacd7d9274",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "SandboxApache24_BR",
      "Hypervisor": "xen",
      "Name": "SandboxApache24_BR",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Name",
          "Value": "SandboxApache24_BR"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2018-07-28T14:30:10.000Z",
      "ImageId": "ami-d9919aa6",
      "ImageLocation": "701085748382/astrein_first_install",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "Platform": "windows",
      "PlatformDetails": "Windows",
      "UsageOperation": "RunInstances:0002",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/sda1",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0e5a3fdb04c673c27",
            "VolumeSize": 50,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "Astrein IIS First Install at Julho 2018",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "astrein_first_install",
      "RootDeviceName": "/dev/sda1",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Platform",
          "Value": "infrastructure"
        },
        {
          "Key": "Name",
          "Value": "Astrein IIS First Install"
        },
        {
          "Key": "Service",
          "Value": "AMI-web"
        },
        {
          "Key": "Owner",
          "Value": "engenharia"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Product",
          "Value": "infrastructure"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2018-03-02T17:19:50.000Z",
      "ImageId": "ami-e011e79d",
      "ImageLocation": "701085748382/plannexo-hnsg-20180302",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-09134ce3ae1d87c2d",
            "VolumeSize": 30,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "iam to regenerate qa environment",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "plannexo-hnsg-20180302",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Product",
          "Value": "plannexo20"
        },
        {
          "Key": "Platform",
          "Value": "plannexo"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Owner",
          "Value": "plannexo"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2018-06-28T13:45:20.000Z",
      "ImageId": "ami-eb5d0594",
      "ImageLocation": "701085748382/bkp_rundeck",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-0827c5ac386334c6d",
            "VolumeSize": 30,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "bkp_rundeck",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "bkp_rundeck",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Product",
          "Value": "infrastructure"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Country",
          "Value": "global"
        },
        {
          "Key": "Owner",
          "Value": "engenharia"
        },
        {
          "Key": "Service",
          "Value": "AMI"
        },
        {
          "Key": "Platform",
          "Value": "infrastructure"
        }
      ],
      "VirtualizationType": "hvm"
    },
    {
      "Architecture": "x86_64",
      "CreationDate": "2017-04-19T18:42:40.000Z",
      "ImageId": "ami-fbb92bed",
      "ImageLocation": "701085748382/oradock-image-test",
      "ImageType": "machine",
      "Public": false,
      "OwnerId": "701085748382",
      "State": "available",
      "BlockDeviceMappings": [
        {
          "DeviceName": "/dev/xvda",
          "Ebs": {
            "DeleteOnTermination": true,
            "SnapshotId": "snap-e05da198",
            "VolumeSize": 8,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdb",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-90e3ff21",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        },
        {
          "DeviceName": "/dev/sdc",
          "Ebs": {
            "DeleteOnTermination": false,
            "SnapshotId": "snap-b3f6b9ae",
            "VolumeSize": 100,
            "VolumeType": "gp2",
            "Encrypted": false
          }
        }
      ],
      "Description": "",
      "EnaSupport": true,
      "Hypervisor": "xen",
      "Name": "oradock-image-test",
      "RootDeviceName": "/dev/xvda",
      "RootDeviceType": "ebs",
      "SriovNetSupport": "simple",
      "Tags": [
        {
          "Key": "Name",
          "Value": "oradock-restore-validation-image-test"
        },
        {
          "Key": "Product",
          "Value": "bionexo"
        },
        {
          "Key": "Country",
          "Value": "br"
        },
        {
          "Key": "Environment",
          "Value": "prod"
        },
        {
          "Key": "Service",
          "Value": "database"
        }
      ],
      "VirtualizationType": "hvm"
    }
  ],
  "ResponseMetadata": {
    "RequestId": "5129a8e9-c938-4085-a786-d136ef211a59",
    "HTTPStatusCode": 200,
    "HTTPHeaders": {
      "content-type": "text/xml;charset=UTF-8",
      "transfer-encoding": "chunked",
      "vary": "accept-encoding",
      "date": "Wed, 12 Feb 2020 22:38:48 GMT",
      "server": "AmazonEC2"
    },
    "RetryAttempts": 0
  }
}

Process finished with exit code 0
