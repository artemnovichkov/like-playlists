# Like playlists

![Status](https://github.com/artemnovichkov/like-playlists/workflows/Make%20playlist/badge.svg)

<p align="center">
  <a href="https://music.yandex.com/users/art3mnovichkov/playlists/1060">
      <img src=".github/logo.png" width="480" max-width="90%" />
  </a>
</p>

Here is a simple script that creates a playlists with songs you liked in previous month

## Features
- Works with Yandex.Music via [yandex-music-api](https://github.com/MarshalX/yandex-music-api)
- Runs on Github Actions, triggers by cron and every push to default branch for testings
- Written in python by me who don't know python 

## Setup
1. Fork this repo
2. Go to the repo **Settings > Secrets** and add the following environment variables
   - **LOGIN:** The login for Yandex.Music account.
   - **PASSWORD**: The password for Yandex.Music account.


## Author

Artem Novichkov, novichkoff93@gmail.com

## License

The project is available under the MIT license. See the LICENSE file for more info.
