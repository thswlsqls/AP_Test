import boto3

personalizeRt = boto3.client('personalize-runtime')
personalize = boto3.client('personalize')

### 이상 공통 ###
# 솔루션 버전을 생성한 후 Amazon Personalize 캠페인을 통해 배포합니다. 다음 코드를 사용하여 솔루션 버전을 배포하는 캠페인을 생성합니다.
# 파라미터로 캠페인 이름, solution_version_arn을 전달합니다. 메서드는 새 캠페인의 Amazon 리소스 이름(ARN)을 반환합니다. 나중에 사용하기 위해 이 ARN을 저장합니다.

response = personalize.create_campaign(
    name = 'campaign name',
    solutionVersionArn = 'solution version arn'
)

arn = response['campaignArn']

description = personalize.describe_campaign(campaignArn = arn)['campaign']
print('Name: ' + description['name'])
print('ARN: ' + description['campaignArn'])
print('Status: ' + description['status'])