from urllib.request import urlretrieve
from urllib.parse import urlparse
from pathlib import Path, PurePath

def get_current_path():
    data_path = Path(__file__).parent
    if not data_path.exists() or not data_path.is_dir():
        raise ValueError("Data directory does not exist")
    return data_path.absolute()

def download_url(url, file_path = None):
    parsed_url = urlparse(url)
    if parsed_url.scheme not in ["http", "https"]:
        raise ValueError("Invalid URL")
    target_path = None
    if file_path is not None:
        target_path = Path(file_path).absolute()
    else:
        url_path = PurePath(parsed_url.path)
        url_name = url_path.name
        if len(url_path.suffix) < 1:
            raise ValueError("Invalid URL, must contain filename if no file_path is given")
        target_path = get_current_path() / url_name
    if target_path.exists():
        return
    print(f"Downloading \"{url}\" to \"{target_path}\"")
    urlretrieve(url=url, filename=target_path)

urls = [
    "https://raw.githubusercontent.com/rasbt/LLMs-from-scratch/main/ch02/01_main-chapter-code/the-verdict.txt",
]


for url in urls:
    download_url(url)

