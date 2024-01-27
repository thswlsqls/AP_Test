import boto3

personalizeRt = boto3.client('personalize-runtime')
personalize = boto3.client('personalize')

### 이상 공통 ##

# Amazon Personalize boto3 클라이언트를 생성하고 환경을 확인했으면, 시작하기 전제 조건 완료 시 생성한 과거 데이터를 가져옵니다.
# 과거 데이터를 Amazon Personalize로 가져오려면 다음과 같이 합니다.

# 다음 코드를 사용하여 Amazon Personalize에서 스키마를 생성합니다. getting-started-schema을 스키마의 이름으로 바꿉니다.
import json
schema = {
  "type": "record",
  "name": "Interactions",
  "namespace": "com.amazonaws.personalize.schema",
  "fields": [
      {
          "name": "USER_ID",
          "type": "string"
      },
      {
          "name": "ITEM_ID",
          "type": "string"
      },
      {
          "name": "TIMESTAMP",
          "type": "long"
      }
  ],
  "version": "1.0"
}

create_interactions_schema_response = personalize.create_schema(
    name='getting-started-schema',
    schema=json.dumps(schema)
)

interactions_schema_arn = create_interactions_schema_response['schemaArn']
print(json.dumps(create_interactions_schema_response, indent=2))
