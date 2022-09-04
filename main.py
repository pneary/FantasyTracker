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
    league = League(league_id=84319430,
                    year=2021,
                    espn_s2='AEA%2F05DiuZwGD1ltUQSwGFPFWz%2F%2FwNSpL9%2FetbgcU3kaKGdyc5V9I4f7RmchIWXqL2ttcWdHHbkaA9paqx87xPm%2BflyZhOmlreMqM5Aine2XsOWlXvjCjKAeMJJQ%2F%2BL9yjNklvXZflunkMP7zrvaZ3dj5LAqBFI2xyMavr58woKmvyMBkB6wrkiqK4n2GfRSrHiVZx%2FaLKLcbaVY34oUJXnPlOliNOTqDsUwmYiOXQ%2BOcHoNOoK5Xq7a2ZADeSitoa%2FrLvmbrDi35rraKZEbTtYG',
                    swid='5D1AFE30-CD32-48AA-BA37-C760CD50024C')
    print_report(get_num_transactions())
