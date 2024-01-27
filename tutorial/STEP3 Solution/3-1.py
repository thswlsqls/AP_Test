import boto3

personalizeRt = boto3.client('personalize-runtime')
personalize = boto3.client('personalize')

### 이상 공통 ##

# 데이터를 가져온 후 다음과 같이 솔루션과 솔루션 버전을 생성합니다. 솔루션에는 모델을 학습하기 위한 구성이 포함되어 있으며 솔루션 버전은 학습된 모델입니다.
# 다음 코드를 사용하여 새 솔루션을 생성합니다.
# 이전의 dataset_group_arn, 솔루션 이름, 사용자-개인 맞춤 레시피의 ARN(arn:aws:personalize:::recipe/aws-user-personalization)을 파라미터로 전달합니다.
# 새 솔루션의 ARN을 저장해 두었다가 나중에 사용할 수 있습니다.

create_solution_response = personalize.create_solution(
  name='solution name',
  recipeArn= 'arn:aws:personalize:::recipe/aws-user-personalization',
  datasetGroupArn = 'dataset group arn'
)
solution_arn = create_solution_response['solutionArn']
print('solution_arn: ', solution_arn)