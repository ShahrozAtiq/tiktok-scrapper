# TikTok Scraper

This Python script uses Selenium to scrape data from TikTok videos and saves the data to a CSV file.

## Setup

1. Install Python 3.
2. Install the required packages by running `pip install selenium pandas`.
3. Download and install the appropriate version of the ChromeDriver for your Chrome browser: https://sites.google.com/a/chromium.org/chromedriver/downloads
4. Update the `driver_path` variable in the script to point to the location of the ChromeDriver on your system.

## Usage

1. Run the script by running `python tiktok_scraper.py` in the terminal.
2. Enter a search query when prompted.
3. The script will scrape the data for all the search results and save it to a CSV file named `tiktok_data.csv`.

## Data Scraped

The following data is scraped from each TikTok video:
- Video description
- Number of likes
- Number of comments
- User profile information (username, nickname, followers, following, likes)

## Example Output
![Alt Text](output.png)

## Contact Me

<table>
  <tr>
    <td align="center"><a href="https://www.upwork.com/freelancers/~01c437b099d917194b" title="View my Upwork profile"><img src="https://img.icons8.com/external-tal-revivo-shadow-tal-revivo/48/null/external-upwork-a-global-freelancing-platform-where-professionals-connect-and-collaborate-remotely-logo-shadow-tal-revivo.png" alt="Upwork Icon"/></a></td>
    <td align="center"><a href="mailto:shahrozatiq@outlook.com" title="Send me an email"><img src="https://img.icons8.com/fluent/48/000000/email-open.png" alt="Email Icon"/></a></td>
    <td align="center"><a href="#" title="Join my Discord server"><img src="https://img.icons8.com/color/48/000000/discord-new-logo.png" alt="Discord Icon"/></a></td>
    <td align="center"><a href="skype:live:.cid.d443850fdc6504ea?chat" title="Chat with me on Skype"><img src="https://img.icons8.com/color/48/000000/skype--v1.png" alt="Skype Icon"/></a></td>
    <td align="center"><a href="https://www.linkedin.com/in/shahroz-atiq-73335b270/" title="Connect with me on LinkedIn"><img src="https://img.icons8.com/color/48/000000/linkedin.png" alt="LinkedIn Icon"/></a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://www.upwork.com/freelancers/~01c437b099d917194b">View my Upwork profile</a></td>
    <td align="center"><a href="mailto:shahrozatiq@outlook.com">Send me an email</br>shahrozatiq@outlook.com</a></td>
    <td align="center"><a href="#">Chat on discord</br>shz#1259</a></td>
    <td align="center">Chat with me on Skype<a href="skype:live:.cid.d443850fdc6504ea?chat"></br>live:.cid.d443850fdc6504ea</a></td>
    <td align="center"><a href="https://www.linkedin.com/in/shahroz-atiq-73335b270/">Connect with me on LinkedIn</a></td>
  </tr>
</table>

## Disclaimer

This script is intended for educational purposes only. Use of this script may violate TikTok's terms of service. Use at your own risk.

