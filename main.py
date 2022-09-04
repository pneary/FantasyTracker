import os
from dotenv import load_dotenv
from espn_api.football import League

# report data is a list of (string, int)
# final report print
def print_report(report_data):
    for (team, num_transactions) in report_data.items():
        print('TEAM NAME: ' + team.team_name)
        print('Number of Transactions: ' + f'{num_transactions}')
        print("Total Money Owed: $" + f'{num_transactions * 2}' + '.00')
        print ('\n')

# get number of transactions for a given user_id
def get_num_transactions():
    activity = get_recent_activity()
    transactions = {}
    for action in activity:
        team = action.actions[0][0]
        if team in transactions.keys():
            transactions[team] = transactions[team] + 1
        else:
            transactions[team] = 0
    return transactions

def get_recent_activity():
    activity = league.recent_activity(msg_type='added')
    return activity

if __name__ == '__main__':
    load_dotenv()
    league = League(league_id=84319430,
                    year=2021,
                    espn_s2=os.getenv('ESPN_S2'),
                    swid=os.getenv('SWID'))
    print_report(get_num_transactions())
