headers  = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'x-nba-stats-token': 'true',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'x-nba-stats-origin': 'stats',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://stats.nba.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}


columns_list=['PLAYER_ID',
    'PLAYER_NAME',
    'NICKNAME',
    'TEAM_ID',
    'TEAM_ABBREVIATION',
    'AGE',
    'GP',
    'W',
    'L',
    'W_PCT',
    'MIN',
    'FGM',
    'FGA',
    'FG_PCT',
    'FG3M',
    'FG3A',
    'FG3_PCT',
    'FTM',
    'FTA',
    'FT_PCT',
    'OREB',
    'DREB',
    'REB',
    'AST',
    'TOV',
    'STL',
    'BLK',
    'BLKA',
    'PF',
    'PFD',
    'PTS',
    'PLUS_MINUS',
    'NBA_FANTASY_PTS',
    'DD2',
    'TD3',
    'WNBA_FANTASY_PTS',
    'GP_RANK',
    'W_RANK',
    'L_RANK',
    'W_PCT_RANK',
    'MIN_RANK',
    'FGM_RANK',
    'FGA_RANK',
    'FG_PCT_RANK',
    'FG3M_RANK',
    'FG3A_RANK',
    'FG3_PCT_RANK',
    'FTM_RANK',
    'FTA_RANK',
    'FT_PCT_RANK',
    'OREB_RANK',
    'DREB_RANK',
    'REB_RANK',
    'AST_RANK',
    'TOV_RANK',
    'STL_RANK',
    'BLK_RANK',
    'BLKA_RANK',
    'PF_RANK',
    'PFD_RANK',
    'PTS_RANK',
    'PLUS_MINUS_RANK',
    'NBA_FANTASY_PTS_RANK',
    'DD2_RANK',
    'TD3_RANK',
    'WNBA_FANTASY_PTS_RANK',
    'CFID',
    'CFPARAMS']


season_list = [
	'1996-97',
	'1997-98',
	'1998-99',
	'1999-00',
	'2000-01',
	'2001-02',
	'2002-03',
	'2003-04',
	'2004-05',
	'2005-06',
	'2006-07',
	'2007-08',
	'2008-09',
	'2009-10',
	'2010-11',
	'2011-12',
	'2012-13',
	'2013-14',
	'2014-15',
	'2015-16',
	'2016-17',
	'2017-18',
	'2018-19',
	'2019-20',
    '2020-21',
    '2021-22',
    '2022-23'
]

p_headers= ['PERSON_ID',
    'PLAYER_LAST_NAME',
    'PLAYER_FIRST_NAME',
    'PLAYER_SLUG',
    'TEAM_ID',
    'TEAM_SLUG',
    'IS_DEFUNCT',
    'TEAM_CITY',
    'TEAM_NAME',
    'TEAM_ABBREVIATION',
    'JERSEY_NUMBER',
    'POSITION',
    'HEIGHT',
    'WEIGHT',
    'COLLEGE',
    'COUNTRY',
    'DRAFT_YEAR',
    'DRAFT_ROUND',
    'DRAFT_NUMBER',
    'ROSTER_STATUS',
    'PTS',
    'REB',
    'AST',
    'STATS_TIMEFRAME',
    'FROM_YEAR',
    'TO_YEAR']