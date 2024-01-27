# 필수 조건을 완료한 후 다음 Python 예제를 실행하여 환경이 올바르게 구성되었는지 확인합니다.
# 또한 이 코드는 이 자습서에서 사용하는 Amazon Personalize boto3 클라이언트를 생성합니다.
# 환경이 올바르게 구성된 경우 사용 가능한 레시피 목록이 표시되고 이 자습서의 다른 Python 예제를 실행할 수 있습니다.

import boto3

personalizeRt = boto3.client('personalize-runtime')
personalize = boto3.client('personalize')

response = personalize.list_recipes()

for recipe in response['recipes']:
    print (recipe)