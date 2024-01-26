## 1. 1단계: Python 환경을 확인하고 boto3 클라이언트 만들기
import boto3

personalizeRt = boto3.client('personalize-runtime')
personalize = boto3.client('personalize')

response = personalize.list_recipes()

# for recipe in response['recipes']:
#     print (recipe)

response = personalizeRt.get_recommendations(
    campaignArn = 'arn:aws:personalize:ap-northeast-2:962369067237:campaign/campaignName4_2104',
    userId = '123',
    numResults = 10
)

print("Recommended items")
for item in response['itemList']:
    print (item['itemId'])


