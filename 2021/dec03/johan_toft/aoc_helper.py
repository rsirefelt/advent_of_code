import os


def download_advent_of_code_input(year, day):
    """Download the advent of code input for the given year and day."""
    import requests
    # Check if input file exists
    if os.path.isfile(f"input.txt"):
        print("Input file already exists, skipping download.")
        return

    url = f"https://adventofcode.com/{year}/day/{day}/input"
    session_cookie = os.environ.get("SESSION_COOKIE")

    if session_cookie is None:
        print("Please set the SESSION_COOKIE environment variable.")
        return

    headers = {
        "Cookie": f"session={session_cookie}",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    }
    # Use requests to download the input file
    r = requests.get(url, headers=headers, stream=True)

    # Save the input file
    with open("input.txt", "wb") as f:
        f.write(r.content)
