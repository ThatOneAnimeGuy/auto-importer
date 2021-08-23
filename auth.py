import cloudscraper
from helpers import get_multi_level_value, create_scrapper_session, get_value

def get_all_sessions(config):
    sessions = {}

    username = get_multi_level_value(config, 'seiso', 'username', default = '')
    password = get_multi_level_value(config, 'seiso', 'password', default = '')
    if username != '' and password != '':
        session = get_auth_token_seiso(username, password)
        if session is not None:
            sessions['seiso'] = session
        else:
            print('Error fetching Seiso session id using login credentials')

    username = get_multi_level_value(config, 'patreon', 'email', default = '')
    password = get_multi_level_value(config, 'patreon', 'password', default = '')
    if username != '' and password != '':
        session = get_auth_token_patreon(username, password)
        if session is not None:
            sessions['patreon'] = [session]
        else:
            print('Error fetching Patreon session id using login credentials')

    extra_patreon_sessions = get_multi_level_value(config, 'fanita', 'session_ids')
    if extra_patreon_sessions is not None:
        if get_value(sessions, 'patreon') is None:
            sessions['patreon'] = []
        sessions['patreon'] += extra_patreon_sessions

    username = get_multi_level_value(config, 'fantia', 'email', default = '')
    password = get_multi_level_value(config, 'fantia', 'password', default = '')
    if username != '' and password != '':
        session = get_auth_token_fantia(username, password)
        if session is not None:
            sessions['fantia'] = [session]
        else:
            print('Error fetching Fantia session id using login credentials')

    extra_fanita_sessions = get_multi_level_value(config, 'fantia', 'session_ids')
    if extra_fanita_sessions is not None:
        if get_value(sessions, 'fantia') is None:
            sessions['fantia'] = []
        sessions['fantia'] += extra_fanita_sessions

    fanbox_sessions = get_multi_level_value(config, 'fanbox', 'session_ids')
    if fanbox_sessions is not None:
        sessions['fanbox'] = fanbox_sessions

    return sessions

def get_auth_token_seiso(username, password):
    scraper = create_scrapper_session()
    response = scraper.post('https://seiso.party/account/login', data = {'username': username, 'password': password})
    return response.cookies.get('session')

# def get_auth_token_kemono(username, password):
#     scraper = create_scrapper_session()
#     resp = scraper.post('https://kemono.party/account/login', files = {'username': username, 'password': password})
#     return response.cookies.get('session')

def get_auth_token_patreon(username, password):
    scraper = create_scrapper_session()
    data = {
        'data': {
            'type': 'user',
            'attributes': {
                'email': username,
                'password': password
            },
            'relationships': {}
        }
    }
    response = scraper.post('https://www.patreon.com/api/login', json = data)
    return response.cookies.get('session_id')

def get_auth_token_fanbox(config):
    return config.get.get('session_id')

def get_auth_token_fantia(username, password):
    scraper = create_scrapper_session()
    data = {
        'user': {
            'email': username,
            'password': password
        }
    }
    response = scraper.post('https://fantia.jp/sessions', data = data)
    return response.cookies.get('_session_id')
