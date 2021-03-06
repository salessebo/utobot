from bs4 import BeautifulSoup
import pandas as pd

class Parser():
    def __init__(self):
        pass
    
    def throne(html_data):
        table_data = pd.read_html(html_data)
        df1 = table_data[0][[0,1]]
        df2 = table_data[0][[2,3]]
        df2.columns= [0,1]
        throne_data = pd.concat([df1,df2], ignore_index=True).set_index(0)[1]

        soup = BeautifulSoup(html_data, 'lxml')
        spells = [x.get_text(strip=True) for x in soup.find_all("p") if x.get_text(strip=True).startswith('Spell')][0].split(':')[1]
        spells = [x.split('(') for x in spells.split(')')][:-1]
        throne_data['Spells'] = {x: int(y.split()[0].replace('-', '0')) for x,y in spells}
        throne_data['Networth'] = int(throne_data['Networth'].split()[0].replace(',',''))
        throne_data['Building Eff.'] = int(throne_data['Building Eff.'].replace('%',''))
        throne_data['Stealth'] = int(throne_data['Thieves'].split()[1].replace('%','').replace('(','').replace(')',''))
        throne_data['Mana'] =  int(throne_data['Wizards'].split()[1].replace('%','').replace('(','').replace(')',''))
        throne_data['Thieves'] = int(throne_data['Thieves'].split()[0].replace(',',''))
        throne_data['Wizards'] = int(throne_data['Wizards'].split()[0].replace(',',''))
        personalities = {'Hero':'War Hero',
                        'Rogue':'Rogue'}
        throne_data['Personality'] = [personalities[x] for x in personalities if x in throne_data['Ruler']][0]
        honor_ranks = {'Noble': 'Lord', 'Lord':'Lord', 'Baron':'Baron'}
        throne_data['Honor'] = [honor_ranks[x] for x in honor_ranks if x in throne_data['Ruler']][0]
        throne_data['Land'] = int(throne_data['Land'])
        throne_data['Peasants'] = int(throne_data['Peasants'])
        throne_data['Money'] = int(throne_data['Money'])
        throne_data['Food'] = int(throne_data['Food'])
        throne_data['Runes'] = int(throne_data['Runes'])
        throne_data['Trade Balance'] = int(throne_data['Trade Balance'])
        throne_data['Networth'] = int(throne_data['Networth'])
        throne_data['Soldiers'] = int(throne_data['Soldiers'])
        throne_data['Griffins'] = int(throne_data['Griffins'])
        throne_data['Harpies'] = int(throne_data['Harpies'])
        throne_data['Drakes'] = int(throne_data['Drakes'])
        throne_data['War Horses'] = int(throne_data['War Horses'])
        throne_data['Prisoners'] = int(throne_data['Prisoners'])
        throne_data['Off. Points'] = int(throne_data['Off. Points'])
        throne_data['Def. Points'] = int(throne_data['Def. Points'])
        
        return throne_data.to_dict()


    def build(data_html):
        table_data = pd.read_html(data_html)
        
        construction = {}
        construction['Construction Time'] = int(table_data[0].iloc[2][1].split()[0])
        construction['Construction Cost'] = int(table_data[0].iloc[0][3].split('gc')[0])
        construction['Raze Cost'] = int(table_data[0].iloc[2][3].split('gc')[0])
        
        df0 = pd.DataFrame([{'Building': 'Barren', 'You Own': int(table_data[0].iloc[1][1].split()[0]), 'In Progress': 0}])
        df1 = table_data[1][['Building', 'You Own', 'In Progress']]
        df2 = table_data[1][['Building.1', 'You Own.1', 'In Progress.1']]
        df2.columns= ['Building', 'You Own', 'In Progress']
        buildings = pd.concat([df0,df1,df2], ignore_index=True).set_index('Building').dropna().astype('int32')    
        buildings['You Own+'] = buildings['You Own'] + buildings['In Progress']
        buildings['Percent'] = round(100*buildings['You Own'] / buildings['You Own+'].sum(),1)
        buildings['Percent+'] = round(100*buildings['You Own+'] / buildings['You Own+'].sum(),1).dropna() 
        buildings = buildings.loc[~(buildings==0).all(axis=1)].T.to_dict()

        return {'buildings':buildings, 'construction':construction}

    def science(data_html):
        df = pd.read_html(data_html)
        effects_df = df[1].drop(labels=[0,7,14], axis=0).set_index('Science Type')[['Number of books','Effect']]
        effects_df['Effect'] = effects_df['Effect'].str.split('%').str[0].str[1:].astype(float)
        effects_df['Number of books'] = effects_df['Number of books'].astype(int)
        economy = ['Alchemy','Tools','Housing','Production','Bookkeeping','Artisan']
        military = ['Strategy','Siege','Tactics','Valor','Heroism','Resilience']
        arcane = ['Crime','Channeling','Shielding','Cunning','Invocation']
        scientists_df = df[1].iloc[[0,7,14]]['Effect']
        summary_df = pd.DataFrame()
        summary_df['Category'] = scientists_df.str.split('-').str[0]
        summary_df['Scientists'] = scientists_df.str.split('-').str[1].str.split().str[0].astype(int)
        summary_df['Books'] = [effects_df.loc[economy].sum()[0].astype(int),effects_df.loc[military].sum()[0].astype(int), effects_df.loc[arcane].sum()[0].astype(int)]
        summary_df['Stacked'] = scientists_df.str.split('-').str[2].str.split().str[0].str.replace(',','').astype(int)
        total = pd.DataFrame([{'Category':'Total', 'Scientists':summary_df['Scientists'].sum(), 'Books':effects_df.sum()[0].astype(int), 'Stacked':summary_df['Stacked'].sum()}])
        summary_df = pd.concat([summary_df,total]).set_index('Category')

        return {'Sciences':effects_df.T.to_dict(), 'Scientists':summary_df.T.to_dict()}

