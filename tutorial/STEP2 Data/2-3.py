import boto3

personalizeRt = boto3.client('personalize-runtime')
personalize = boto3.client('personalize')

### 이상 공통 ##

# 다음 코드를 사용하여 새 데이터 세트 그룹에 상호작용 데이터 세트를 만듭니다. 데이터 세트에 이름을 지정하고 이전 단계의 schema_arn 및 dataset_group_arn를 입력합니다.

response = personalize.create_dataset(
    name = 'datase_name',
    schemaArn = 'schema_arn',
    datasetGroupArn = 'dataset_group_arn',
    datasetType = 'Interactions'
)

dataset_arn = response['datasetArn']

