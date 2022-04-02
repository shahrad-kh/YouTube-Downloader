from pathlib import Path
from typing import Union

from pytube import YouTube
from pytube.cli import on_progress as op


class youtube_video:
    """ Download a youtube video or just it's audio
    """
    def __init__(self, url: str):
        self.url = url

    def download(self, path: Union[str, Path], only_audio=False):
        """download the highest resolution of a youtube video or
        just it's audio to path
        Args:
            path (str, Path): path to downloaded video
            only_aduio (bool, optional): _description_. Defaults to False.
        """
        path = Path(path)
        yt = YouTube(self.url, on_progress_callback=op)

        if(only_audio):
            yt.streams.filter(only_audio=True).first().download(path)
        else:
            yt.streams.get_lowest_resolution().download(path)

        print(f'{yt.title} downloaded at {path}')


if __name__ == '__main__':
    video = youtube_video(input('Enter youtube video url: '))
    type_ = input('Download audio only? (y/n): ')
    path = input('Enter path to download: ')
    if(type_ == 'y'):
        video.download(path, only_audio=True)
    else:
        video.download(path)
