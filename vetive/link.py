"""
    Handles the communications with youtube
"""
from enum import Enum


class YoutubeInformationType(Enum):
    """Enum for the types of youtube informations to get"""

    SNIPPET = "snippet"
    STATISTICS = "statistics"


def make_youtube_link(
    video_id: str, api_key: str, youtube_information_type: YoutubeInformationType
) -> str:
    """Make the necessary url string prefix to get
    information back from youtube
    """
    _prefix_url = "https://www.googleapis.com/youtube/videos?part="
    youtube_video_url = (
        f"{_prefix_url}{youtube_information_type.value}&id={video_id}&key={api_key}"
    )
    return youtube_video_url
