from riotwatcher import RiotWatcher
from pprint import pprint
import os
import json

def AddChampList():
    '''
    チャンピオンIDとチャンピオン名を紐づける
    '''
    champion_list = {} #{ID:["チャンピオンの名前"]
    with open('champion.json',encoding="utf-8") as f:
        # jsonファイルを読み込む
        df = json.load(f)
        for i in df["data"]:
            champion_list[int(df["data"][i]["key"])] = [df["data"][i]["name"]]
    return champion_list


def AddSummonerMatchList(summoner):
    '''
    summonerのアカウントIDを基にマッチングリストを出力する。
    '''
    recentmatchlists = watcher.match.matchlist_by_account(my_region, summoner['accountId'], '420',begin_index=0,end_index=1)


    for matches in recentmatchlists['matches']:
        champid = matches['champion']
        matches['champion'] = clist[champid][0]
        pprint(matches)



# 社内ネットワーク使用時のプロキシ認証設定
os.environ["https_proxy"] = "http://U645051:tomoyori0817@127.0.0.1:8080"

APIKey = 'RGAPI-439e0fe4-ff47-4abf-beb8-5d7b61e7f1be'


my_region = 'jp1' # 日本鯖はjp1
summoner_name = 'suntomoon'

watcher = RiotWatcher(APIKey)
# summoner_nameで定義したアカウント情報を取得
me = watcher.summoner.by_name(my_region, summoner_name)
# pprint(me)

# チャンピオンリストを作成
clist = AddChampList()


# マッチングリストを出力
AddSummonerMatchList(me)




ent = watcher.league.by_summoner(my_region, me['id'])
leagueId = ent[1]['leagueId']

recentmatchlists = watcher.match.matchlist_by_account(my_region, me['accountId'], '420',begin_index=0,end_index=1)
matchid_list = []
for match in recentmatchlists['matches']:
    matchid_list.append(match['gameId'])
    print(match['gameId'])

for list in matchid_list:

    timeline = watcher.match.timeline_by_match(my_region, list)
    frames = timeline['frames'][1]
    events = frames['events']
    for timestamp in frames:
        print(timestamp)
    #participant = frames['participantFrames']
    #print(participant)


'''
matches_list =[]
for x in matches:
    matches_list.append(watcher.match.by_id(my_region, x['gameId']))

pprint(matches_list)
'''