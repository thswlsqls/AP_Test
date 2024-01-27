import boto3

personalizeRt = boto3.client('personalize-runtime')
personalize = boto3.client('personalize')

### 이상 공통 ##

# 다음 코드를 사용하여 데이터 세트 그룹을 생성합니다. dataset group name을 데이터 세트 그룹의 이름으로 바꿉니다.

response = personalize.create_dataset_group(name = 'dataset group name')
dataset_group_arn = response['datasetGroupArn']

description = personalize.describe_dataset_group(datasetGroupArn = dataset_group_arn)['datasetGroup']

print('Name: ' + description['name'])
print('ARN: ' + description['datasetGroupArn'])
print('Status: ' + description['status'])