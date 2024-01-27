import boto3

personalizeRt = boto3.client('personalize-runtime')
personalize = boto3.client('personalize')

### 이상 공통 ##

# 다음 코드를 사용한 데이터 세트 가져오기 작업으로 데이터를 가져옵니다. 코드는 describe_dataset_import_job 메서드를 사용하여 작업 상태를 추적합니다.

# 작업 이름, 이전 단계의 dataset_arn, 학습 데이터를 저장한 Amazon S3 버킷 경로(s3://bucket name/folder name/ratings.csv),
# IAM 서비스 역할의 ARN 등을 파라미터로 전달합니다. 시작하기 전제 조건의 일부로 이 역할을 생성했습니다. Amazon Personalize에는 버킷에 액세스할 수 있는 권한이 필요합니다.
# Amazon Personalize에 Amazon S3 리소스에 대한 액세스 권한 부여 단원을 참조하세요.

import time
response = personalize.create_dataset_import_job(
    jobName = 'JobName',
    datasetArn = 'dataset_arn',
    dataSource = {'dataLocation' :'s3://bucket/file.csv'},
    roleArn = 'role_arn',
    importMode = 'FULL'
)

dataset_interactions_import_job_arn = response['datasetImportJobArn']

description = personalize.describe_dataset_import_job(
    datasetImportJobArn = dataset_interactions_import_job_arn)['datasetImportJob']

print('Name: ' + description['jobName'])
print('ARN: ' + description['datasetImportJobArn'])
print('Status: ' + description['status'])

max_time = time.time() + 3* 60 * 60  # 3 hours
while time.time() < max_time:
    describe_dataset_import_job_response = personalize.describe_dataset_import_job(
        datasetImportJobArn=dataset_interactions_import_job_arn
    )
    status = describe_dataset_import_job_response["datasetImportJob"]['status']
    print("Interactions DatasetImportJob: {}".format(status))

    if status == "ACTIVE" or status == "CREATE FAILED":
        break

    time.sleep(60)