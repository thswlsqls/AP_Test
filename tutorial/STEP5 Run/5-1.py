import boto3

personalizeRt = boto3.client('personalize-runtime')
personalize = boto3.client('personalize')

### 이상 공통 ###

# 캠페인을 생성한 후 이 캠페인을 사용하여 추천을 받을 수 있습니다.
# 다음 코드는 캠페인에서 추천을 받고 각 추천 항목의 ID를 인쇄하는 방법을 보여줍니다.
# 이전 단계에서 생성한 캠페인의 ARN을 전달합니다.
#사용자 ID의 경우 학습 데이터에서 가져온 사용자 ID(예123:)를 전달합니다.

response = personalizeRt.get_recommendations(
    campaignArn = 'arn:aws:personalize:ap-northeast-2:962369067237:campaign/my-campaign-v1-20240129',
    userId = '123',
    numResults = 10
)

print("Recommended items")
for item in response['itemList']:
    print (item['itemId'])