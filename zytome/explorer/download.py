import os

import requests
from tqdm import tqdm


def download_with_progress(url: str, out_path: str, chunk_size: int = 8192):
    response = requests.get(url, stream=True)
    response.raise_for_status()

    total = int(response.headers.get("content-length", 0))

    with open(out_path, "wb") as f, tqdm(
        total=total,
        unit="B",
        unit_scale=True,
        unit_divisor=1024,
        desc=f"Downloading {os.path.basename(out_path)}",
    ) as bar:
        for chunk in response.iter_content(chunk_size=chunk_size):
            size = f.write(chunk)
            bar.update(size)
