#Author: God Bennett
#A bug with the original python library "https://github.com/gurugaurav/bing_image_downloader", as found to be described in issue "https://github.com/gurugaurav/bing_image_downloader/issues/4". Solution does what a commenter claimed to have done as a workaround.

import downloader

#invoke downloader to download 1000 real car interiors
#d = downloader.download("concept car white interior", limit=1000, output_dir='concept', adult_filter_off=True, force_replace=False, timeout=60)

#invoke downoloader to download 1000 concept car interiors
d = downloader.download("car interior sketch", limit=1000, output_dir='sketch', adult_filter_off=True, force_replace=False, timeout=60)
