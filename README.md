# BgRem API
BgRem API service allows you to upload and use backgrounds, both default and your own, and work with videos and images in variety of formats.
With our API you can use our service in your environment anywhere within your project.

By use of this repository, you agree to BgRem [Terms of Service](https://bgrem.deelvin.com/terms_of_use/) and [Privacy Policy](https://bgrem.deelvin.com/privacy_policy/).

## Examples and usage
### Actions overview
To get started first you need to get API key. You can obtain a trial key [here](https://bgrem.deelvin.com/application_programming_interface/).

![Alt Text](https://media.giphy.com/media/HbNnYwTNtQ9aH2W9FU/giphy.gif)


To start trial you should launch `python3 api_samples.py -h` from your project directory. After this command you will see list of arguments for 
further use of sample API calls

Here is list of possible actions that you can use with argument -a:
- **get_videos** - Returns all videos belonging to your profile
- **get_backgrounds** - Retuns all backgrounds
- **upload_video** - Upload video with required arg -f File path, and optional -i Background id
- **upload_background** - Upload background with required arg -f File path
- **delete_video_by_id** - Delete video with arg -i of background id
- **get_video_by_id** - Get one video by its video id (arg -i)

![Alt Text](https://media.giphy.com/media/rEFEwSQR9wV1jdRgUb/giphy.gif)

### Example project
In directory _demo_proj_ you can see script with example usage of our API. By launching `python3 ./demo_proj/john_lost.py` you script will upload a video _john.mp4_ from same directory and also send saple background id to command. After video uploading video to server and removing background with our cloud worker script will return url to download resulting video. After returning link removal task will be deleted from your uploads.

![Alt Text](https://media.giphy.com/media/ZNrA2xoYn0M8OV5b3v/giphy.gif)

## Further information
If you having troubles understanding responses or requests – refer to our [documentation page](https://bgrem.deelvin.com/application_programming_interface/documentation/). To read more about BgRem API you can visit our **BLOG ARTICLE**. After using our trial period be sure to subscribe to fully featured developer plan of our API!

