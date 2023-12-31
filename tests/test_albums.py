import pytest
from utils.albums import AlbumRouter as Album

def test_search_album():
    case = Album()
    case.albumName=None
    result = case.search_album()
    assert result == None


