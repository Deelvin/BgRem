import requests
import os
import mimetypes

API_KEY = os.getenv('BGREM_KEY')
URL = 'https://bgrem.deelvin.com/api/v1'

def upload_videos(fp, back_id=None):
    action = 'videos'
    with open(fp, "rb") as f:
        files = {"file": (os.path.basename(fp), f, mimetypes.MimeTypes().guess_type(fp)[0])}
        headers = {'Authorization': f'Bearer {API_KEY}'}
        data = {
                'background_id': back_id,
            }
        r = requests.post(f'{URL}/{action}', headers=headers, files=files, data=data)
        return r.json()['id']


def get_video_by_id(id):
    action = 'videos'
    r = requests.get(f'{URL}/{action}/{id}', headers={'Authorization': f'Bearer {API_KEY}'})
    return r.json()


def delete_video_by_id(id):
    action = 'videos'
    r = requests.delete(f'{URL}/{action}/{id}', headers={'Authorization': f'Bearer {API_KEY}'})
    return print(r.json())


def main():
    result_id = upload_videos('./john.mp4', back_id='8da750a2-1bf6-4867-bd16-81e16de710dd')
    status = ''
    while status != 'done':
        status = get_video_by_id(result_id)['status']
        if status == 'error':
            print('There was error while working with file!')
            return
    print(f'Result url is: {get_video_by_id(result_id)["result_url"]}')
    delete_video_by_id(result_id)
    return


if __name__ == '__main__':
    main()


