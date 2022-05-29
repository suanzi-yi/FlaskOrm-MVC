import requests
import json
import csv
import pandas as pd
import numpy as np

def task1():#三大位置得分top50球员的数据比较
    url_all='https://m.china.nba.cn/stats2/league/playerstats.json?conference=All&country=All&individual=All&locale=zh_CN&pageIndex=0&position=All&qualified=false&season=2021&seasonType=4&split=All+Team&statType=points&team=All&total=perGame'
    url_guard='https://m.china.nba.cn/stats2/league/playerstats.json?conference=All&country=All&individual=All&locale=zh_CN&pageIndex=0&position=G&qualified=false&season=2021&seasonType=4&split=All+Team&statType=points&team=All&total=perGame'
    url_forward='https://m.china.nba.cn/stats2/league/playerstats.json?conference=All&country=All&individual=All&locale=zh_CN&pageIndex=0&position=F&qualified=false&season=2021&seasonType=4&split=All+Team&statType=points&team=All&total=perGame'
    url_centre='https://m.china.nba.cn/stats2/league/playerstats.json?conference=All&country=All&individual=All&locale=zh_CN&pageIndex=0&position=C&qualified=false&season=2021&seasonType=4&split=All+Team&statType=points&team=All&total=perGame'
    A_data=getData(url_all)
    G_data=getData(url_guard)
    F_data=getData(url_forward)
    C_data=getData(url_centre)
    writeData(A_data,'A')
    writeData(G_data,'G')
    writeData(F_data,'F')
    writeData(C_data,'C')
    A_list=analysis('A')
    G_list=analysis('G')
    F_list=analysis('F')
    C_list=analysis('C')
    list=[A_list,G_list,F_list,C_list]
    list=np.round(list,2)
    list=list.tolist()
    print("task1:",list)
    return list

def getData(url):
    response = requests.get(url, headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53'
    })
    json_data = json.loads(response.text)
    playerList = []
    for item in json_data['payload']['players']:
        player_dataDict = {}
        # 球员名字
        name = item['playerProfile']['code']
        # 球队
        team = item['teamProfile']['displayAbbr']
        # 位置
        position = item['playerProfile']['position']
        # 出场次数
        games = item['statAverage']['games']
        # 先发
        gamesStarted = item['statAverage']['gamesStarted']
        # 分钟
        mins = item['statAverage']['minsPg']
        # 三分命中
        tpm = item['statAverage']['tppct']
        # 罚球命中
        ftm = item['statAverage']['ftpct']
        # 进攻
        offRebs = item['statAverage']['offRebsPg']
        # 防守
        defRebs = item['statAverage']['defRebsPg']
        # 篮板
        rebs = item['statAverage']['rebsPg']
        # 助攻
        assists = item['statAverage']['assistsPg']
        # 抢断
        steals = item['statAverage']['stealsPg']
        # 盖帽
        blocks = item['statAverage']['blocksPg']
        # 失误
        turnovers = item['statAverage']['turnoversPg']
        # 犯规
        fouls = item['statAverage']['foulsPg']
        # 得分
        points = item['statAverage']['pointsPg']
        player_dataDict['球员'] = name
        player_dataDict['球队'] = team
        player_dataDict['位置'] = position
        player_dataDict['场次'] = games
        player_dataDict['先发'] = gamesStarted
        player_dataDict['出场时间'] = mins
        player_dataDict['三分命中率'] = tpm
        player_dataDict['罚球命中率'] = ftm
        player_dataDict['进攻效率'] = offRebs
        player_dataDict['防守效率'] = defRebs
        player_dataDict['篮板'] = rebs
        player_dataDict['助攻'] = assists
        player_dataDict['抢断'] = steals
        player_dataDict['盖帽'] = blocks
        player_dataDict['失误'] = turnovers
        player_dataDict['犯规'] = fouls
        player_dataDict['得分'] = points
        print(player_dataDict)
        playerList.append(player_dataDict)
    return playerList
def writeData(playerList,position):
    with open('{}_data.csv'.format(position),'w',encoding='utf-8',newline='')as f:
        write=csv.DictWriter(f, fieldnames=['球员','球队','位置','场次','先发','出场时间','三分命中率','罚球命中率',
                                            '进攻效率','防守效率','篮板','助攻',
                                            '抢断','盖帽','失误','犯规','得分'])
        write.writeheader()
        for each in playerList:
            write.writerow(each)

#读取csv 返回大链表，四个折线数据[[能力值],[],[],[]]
def analysis(position):
    df=pd.read_csv('{}_data.csv'.format(position))
    data=df.loc[:,'出场时间':'得分']
    M=data.mean()
    # print(M)
    mean_array=np.array(M)
    mean_list=mean_array.tolist()
    return mean_list


#抓取单个球员 返回 [{value:0 name:三分},[]] 从一个赛季的所有对局来计算球员能力值
def task2(name):
    url = 'https://m.china.nba.cn/stats2/player/stats.json?locale=zh_CN&playerCode={}'.format(name) #根据name构造爬取的url
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53'
    }
    response = requests.get(url, headers=headers)
    json_data = json.loads(response.text)
    playerList = []
    for item in json_data['payload']['player']['stats']['seasonGames']:
        player_dataDict = {}
        #对阵
        opp = item['profile']['oppTeamProfile']['displayAbbr']
        #成败
        win = item['profile']['winOrLoss']
        #比分
        score0 = item['profile']['teamScore']
        score1 = item['profile']['oppTeamScore']
        #数据
        points = item['statTotal']['points']
        time = item['statTotal']['mins']
        lanban = item['statTotal']['rebs']
        zhugong = item['statTotal']['assists']
        qiangduan = item['statTotal']['steals']
        gaimao = item['statTotal']['blocks']
        mingzhong = item['statTotal']['fgpct']
        sanfenmingzhong = item['statTotal']['tppct']
        faqiumingzhong = item['statTotal']['ftpct']
        shiwu = item['statTotal']['turnovers']
        fangui = item['statTotal']['offRebs']

        player_dataDict['得分'] = points
        player_dataDict['篮板'] = lanban
        player_dataDict['助攻'] = zhugong
        player_dataDict['抢断'] = qiangduan
        player_dataDict['盖帽'] = gaimao
        player_dataDict['总命中率'] = mingzhong
        player_dataDict['三分命中率'] = sanfenmingzhong
        player_dataDict['罚球命中率'] = faqiumingzhong
        player_dataDict['失误'] = shiwu
        player_dataDict['犯规'] = fangui
        # print(player_dataDict)
        playerList.append(player_dataDict)
    v1 = getvalue(playerList,'得分')
    d1 = {'value':v1,'name':'得分'}

    v2 = getvalue(playerList,'篮板')
    d2 = {'value': v2, 'name': '篮板'}

    v3 = getvalue(playerList, '助攻')
    d3 = {'value': v3, 'name': '助攻'}

    v4 = getvalue(playerList, '抢断')
    d4 = {'value': v4, 'name': '抢断'}

    v5 = getvalue(playerList, '盖帽')
    d5 = {'value': v5, 'name': '盖帽'}

    v6 = getvalue(playerList, '总命中率')
    d6 = {'value': v6, 'name': '总命中率'}

    v7 = getvalue(playerList, '三分命中率')
    d7 = {'value': v7, 'name': '三分命中率'}

    v8 = getvalue(playerList, '罚球命中率')
    d8 = {'value': v8, 'name': '罚球命中率'}

    v9 = getvalue(playerList, '失误')
    d9 = {'value':v9,'name':'失误'}

    v10 = getvalue(playerList, '犯规')
    d10 = {'value': v10, 'name': '犯规'}
    list_v=[v1,v2,v3,v4,v5,v6,v7,v8,v9,v10]
    list=[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10]
    # print('task2:',list)
    return list,list_v

def getvalue(playerlist,name):
    for i in playerlist:
        list = []
        for i in playerlist:
            list.append(i['{}'.format(name)])
    value = sum(list) / len(list)
    value=np.round(value,2)
    return value


#5个顶尖球员 多项能力堆积图 [[三分的能力],[——的能力],[]] 归一化
def task3():
    ability1=[]#得分
    ability2=[]#效率
    ability3=[]#进攻
    ability4=[]#防守
    ability5=[]#团队
    _,list=task2('giannis_antetokounmpo')
    ability(list,ability1)
    # print(ability1)
    _,list=task2('kevin_durant')
    ability(list, ability2)

    _, list =task2('stephen_curry')
    ability(list, ability3)

    _, list = task2('chris_paul')
    ability(list, ability4)

    _, list =task2('joel_embiid')
    ability(list, ability5)

    M=[ability1,ability2,ability3,ability4,ability5]
    np1=np.array(M)
    # print(np1)

    a1 = ((np1[:, 0] - np1[:, 0].min()) / (np1[:, 0].max() - np1[:, 0].min()) + 4) * 4
    a2 = ((np1[:, 1] - np1[:, 1].min()) / (np1[:, 1].max() - np1[:, 1].min()) + 4) * 4
    a3 = ((np1[:, 2] - np1[:, 2].min()) / (np1[:, 2].max() - np1[:, 2].min()) + 4) * 4
    a4 = ((np1[:, 3] - np1[:, 3].min()) / (np1[:, 3].max() - np1[:, 3].min()) + 4) * 4
    a5 = ((np1[:, 4] - np1[:, 4].min()) / (np1[:, 4].max() - np1[:, 4].min()) + 4) * 4
    list=[a1.tolist(),a2.tolist(),a3.tolist(),a4.tolist(),a5.tolist()]
    list=np.round(list,2).tolist()
    print('task3:',list)
    return list

def ability(list,A):#计算能力值
    A.append(list[0])#得分
    A.append((list[5]+list[6]+list[7])/3)#效率
    A.append((list[0]+list[1]+list[3])/3)#进攻
    A.append((list[1]+list[4]+list[9])/3)#防守
    A.append(list[2])

def task4():#三大位置得分top50球员的数据比较
    url_all='https://m.china.nba.cn/stats2/league/playerstats.json?conference=All&country=All&individual=All&locale=zh_CN&pageIndex=0&position=All&qualified=false&season=2021&seasonType=4&split=All+Team&statType=points&team=All&total=perGame'
    url_guard='https://m.china.nba.cn/stats2/league/playerstats.json?conference=All&country=All&individual=All&locale=zh_CN&pageIndex=0&position=G&qualified=false&season=2021&seasonType=4&split=All+Team&statType=points&team=All&total=perGame'
    url_forward='https://m.china.nba.cn/stats2/league/playerstats.json?conference=All&country=All&individual=All&locale=zh_CN&pageIndex=0&position=F&qualified=false&season=2021&seasonType=4&split=All+Team&statType=points&team=All&total=perGame'
    url_centre='https://m.china.nba.cn/stats2/league/playerstats.json?conference=All&country=All&individual=All&locale=zh_CN&pageIndex=0&position=C&qualified=false&season=2021&seasonType=4&split=All+Team&statType=points&team=All&total=perGame'
    A_data=getData2(url_all)
    G_data=getData2(url_guard)
    F_data=getData2(url_forward)
    C_data=getData2(url_centre)
    list=A_data
    # print(list)
    return  list

def getData2(url):
    response = requests.get(url, headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53'
    })
    json_data = json.loads(response.text)
    playerList = []
    for item in json_data['payload']['players']:
        player_dataDict = {}
        # 球员名字
        name = item['playerProfile']['code']
        # 球队
        team = item['teamProfile']['displayAbbr']
        # 位置
        position = item['playerProfile']['position']
        # 出场次数
        games = item['statAverage']['games']
        # 先发
        gamesStarted = item['statAverage']['gamesStarted']
        # 分钟
        mins = item['statAverage']['minsPg']
        # 三分命中
        tpm = item['statAverage']['tppct']
        # 罚球命中
        ftm = item['statAverage']['ftpct']
        # 进攻
        offRebs = item['statAverage']['offRebsPg']
        # 防守
        defRebs = item['statAverage']['defRebsPg']
        # 篮板
        rebs = item['statAverage']['rebsPg']
        # 助攻
        assists = item['statAverage']['assistsPg']
        # 抢断
        steals = item['statAverage']['stealsPg']
        # 盖帽
        blocks = item['statAverage']['blocksPg']
        # 失误
        turnovers = item['statAverage']['turnoversPg']
        # 犯规
        fouls = item['statAverage']['foulsPg']
        # 得分
        points = item['statAverage']['pointsPg']
        player_dataDict['球员'] = name
        player_dataDict['球队'] = team
        player_dataDict['位置'] = position
        player_dataDict['场次'] = games
        player_dataDict['先发'] = gamesStarted
        player_dataDict['出场时间'] = mins
        player_dataDict['三分命中率'] = tpm
        player_dataDict['罚球命中率'] = ftm
        player_dataDict['进攻效率'] = offRebs
        player_dataDict['防守效率'] = defRebs
        player_dataDict['篮板'] = rebs
        player_dataDict['助攻'] = assists
        player_dataDict['抢断'] = steals
        player_dataDict['盖帽'] = blocks
        player_dataDict['失误'] = turnovers
        player_dataDict['犯规'] = fouls
        player_dataDict['得分'] = points
        print(player_dataDict)
        playerList.append(player_dataDict)
    return playerList
if __name__ == "__main__":
    # task1()
    # l,_=task2('giannis_antetokounmpo')
    # print('task2',l)
    # task3()
    task4()


