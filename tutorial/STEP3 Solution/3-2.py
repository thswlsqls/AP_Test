import boto3

personalizeRt = boto3.client('personalize-runtime')
personalize = boto3.client('personalize')

### 이상 공통 ##

# 다음 코드를 사용하여 솔루션 버전을 생성합니다.
# 이전 단계의 solution_arn을 파라미터로 전달합니다. 다음 코드는 솔루션 버전을 만듭니다.
# 학습 중에 코드는 DescribeSolutionVersion 작업을 사용하여 솔루션 버전의 상태를 검색합니다.
# 학습이 완료되면 메서드는 새 솔루션 버전의 ARN을 반환합니다. 나중에 사용하기 위해 이 ARN을 저장합니다.

import time
import json

create_solution_version_response = personalize.create_solution_version(
    solutionArn='solution_arn'
)

solution_version_arn = create_solution_version_response['solutionVersionArn']
print(json.dumps(create_solution_version_response, indent=2))

max_time = time.time() + 3 * 60 * 60  # 3 hours
while time.time() < max_time:
    describe_solution_version_response = personalize.describe_solution_version(
        solutionVersionArn=solution_version_arn
    )
    status = describe_solution_version_response["solutionVersion"]["status"]
    print("SolutionVersion: {}".format(status))

    if status == "ACTIVE" or status == "CREATE FAILED":
        break

    time.sleep(60)