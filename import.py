import config
import auth
import requests
import cloudscraper
import time
from helpers import get_value, create_scrapper_session, get_random_ddg_cookie
from fake_useragent import UserAgent

ua = UserAgent()
headers = {
    'X-Source-Script': 'auto-importer v1.0',
    'User-Agent': ua.random
}

def main():
    run = True
    while run:
        print('Starting import...')
        conf = config.read_config()
        sessions = auth.get_all_sessions(conf)
        if get_value(conf, 'debug', False):
            print(f'All sessions found: {sessions}')

        import_seiso(sessions)
        import_kemono(sessions)

        if not get_value(conf, 'run_forever', False):
            run = False
            continue

        sleep_hours = get_value(conf, 'run_every_X_hours', 24)
        print(f'Sleeping for {sleep_hours} hours')
        sleep_seconds = sleep_hours * 60 * 60
        time.sleep(sleep_seconds)

def import_seiso(sessions):
    jar = requests.cookies.RequestsCookieJar()
    session = get_value(sessions, 'seiso')
    if session is not None:
        jar.set('session', session)
    jar.set('__ddg2', get_random_ddg_cookie())

    fanbox_sessions = get_value(sessions, 'fanbox')
    if fanbox_sessions is not None:
        for session in fanbox_sessions:
            submit_session('seiso.party', 'fanbox', session, jar)

    fantia_sessions = get_value(sessions, 'fantia')
    if fantia_sessions is not None:
        for session in fantia_sessions:
            submit_session('seiso.party', 'fantia', session, jar)

    patreon_sessions = get_value(sessions, 'patreon')
    if patreon_sessions is not None:
        for session in patreon_sessions:
            submit_session('seiso.party', 'patreon', session, jar)

def import_kemono(sessions):
    jar = requests.cookies.RequestsCookieJar()
    jar.set('__ddg2', get_random_ddg_cookie())

    fanbox_sessions = get_value(sessions, 'fanbox')
    if fanbox_sessions is not None:
        for session in fanbox_sessions:
            submit_session('kemono.party', 'fanbox', session, jar)

    fantia_sessions = get_value(sessions, 'fantia')
    if fantia_sessions is not None:
        for session in fantia_sessions:
            submit_session('kemono.party', 'fantia', session, jar)

    patreon_sessions = get_value(sessions, 'patreon')
    if patreon_sessions is not None:
        for session in patreon_sessions:
            submit_session('kemono.party', 'patreon', session, jar)

def submit_session(site, service, session, jar = None):
    scraper = create_scrapper_session(status_forcelist = (500, 502, 504, 423, 429, 403))
    scraper.post(f'https://{site}/api/import', cookies = jar, data = {'service': service, 'session_key': session}, headers = headers)
    print(f'Importing {service} session to {site}')

if __name__ == '__main__':
    main()
