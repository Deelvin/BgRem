import requests
import os
import mimetypes
from functools import partial
from pprint import pprint

API_KEY = os.getenv('BGREM_KEY')
URL = 'https://bgrem.deelvin.com/api/v1'


def get_backgrounds():
    action = 'backgrounds'
    r = requests.get(f'{URL}/{action}', headers={'Authorization': f'Bearer {API_KEY}'})
    return pprint(r.json())


def get_videos():
    action = 'videos'
    r = requests.get(f'{URL}/{action}', headers={'Authorization': f'Bearer {API_KEY}'})
    return pprint(r.json())


def upload_background(fp):
    action = 'backgrounds'
    with open(fp, 'rb') as f:
        files = {'file': (os.path.basename(fp), f, mimetypes.MimeTypes().guess_type(fp)[0])}
        headers = {'Authorization': f'Bearer {API_KEY}'}
        r = requests.post(f'{URL}/{action}', headers=headers, files=files)
    return pprint(r.json())


def upload_videos(fp, back_id=None):
    action = 'videos'
    with open(fp, "rb") as f:
        files = {"file": (os.path.basename(fp), f, mimetypes.MimeTypes().guess_type(fp)[0])}
        headers = {'Authorization': f'Bearer {API_KEY}'}
        data = {
                'background_id': back_id,
            }
        r = requests.post(f'{URL}/{action}', headers=headers, files=files, data=data)
        return pprint(r.json())


def get_video_by_id(id):
    action = 'videos'
    r = requests.get(f'{URL}/{action}/{id}', headers={'Authorization': f'Bearer {API_KEY}'})
    return pprint(r.json())


def delete_video_by_id(id):
    action = 'videos'
    r = requests.delete(f'{URL}/{action}/{id}', headers={'Authorization': f'Bearer {API_KEY}'})
    return pprint(r.json())


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='API tutorial for bg removal')
    parser.add_argument('-a', help='Chosen action')
    parser.add_argument('-f', help='Path to file')
    parser.add_argument('-i', help='Id')
    args = parser.parse_args()

    action_dict = {'get_videos': get_videos,
                   'get_backgrounds': get_backgrounds,
                   'upload_video': partial(upload_videos, args.f, back_id=args.i),
                   'upload_background': partial(upload_background, args.f),
                   'delete_video_by_id': partial(delete_video_by_id, args.i),
                   'get_video_by_id': partial(get_video_by_id, args.i)}

    action_dict[args.a]()

