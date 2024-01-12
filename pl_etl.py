import requests
import pandas as pd
import boto3


def run_pl_etl():

    s3 = boto3.resource(
        service_name='s3',
        region_name='us-east-2',
        aws_access_key_id='ENTER YOUR KEY',
        aws_secret_access_key='ENTER YOUR KEY'
    )

    # Replace 'YOUR_API_TOKEN' with your actual API token
    headers = {
        'X-Auth-Token': 'ENTER YOUR KEY'
    }

    # Endpoint for Premier League matches (The competition ID for the Premier League is 2021)
    url = 'https://api.football-data.org/v2/competitions/PL/matches?status=SCHEDULED'

    # Make the API call
    response = requests.get(url, headers=headers)
    match_list = []
    # Check if the request was successful
    if response.status_code == 200:
        # Parse and display the data
        data = response.json()

        for match in data['matches']:
            match_info = {'home_team': match['homeTeam']['name'],
                          'away_team': match['awayTeam']['name'],
                          'match_date': match['utcDate']
                          }
            match_list.append(match_info)

            print(f"{match['homeTeam']['name']} vs {match['awayTeam']['name']} on {match['utcDate']}")
    else:
        print("Failed to retrieve data:", response.status_code)

    df = pd.DataFrame(match_list)
    df.to_csv("Premier_League_Matches.csv")
    s3.Bucket('Your-S3-bucket-name').upload_file(Filename='Premier_League_Matches.csv', Key='Premier_League_Matches.csv')


