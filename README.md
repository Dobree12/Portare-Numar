---

# Telephone Number Information Retrieval

This Python script allows users to retrieve information about telephone numbers in Romania and find the corresponding country for a given phone prefix.

## Requirements

- Python 3.x
- Requests library (`pip install requests`)
- BeautifulSoup library (`pip install beautifulsoup4`)

## Usage

### Number Information Retrieval

1. Run the script.
2. Enter a 10-digit phone number when prompted.
3. The script will fetch information about the operator, initial operator, current date, and number type associated with the entered phone number.
4. If the information is found, it will be displayed; otherwise, an error message will be shown.

### Country Prefix Lookup

1. Ensure you have a text file named `country_prefixes.txt` in the same directory as the script.
2. The file should contain country prefixes in the format: `prefix:country`.
3. Run the script.
4. Enter a prefix when prompted.
5. The script will output the corresponding country associated with the entered prefix if found; otherwise, it will display a message indicating that the prefix is not associated with any known country.

## Notes

- This script relies on web scraping to retrieve information about telephone numbers. Please use it responsibly and respect the terms of service of the website being scraped (`https://www.portabilitate.ro`).
- Using data from the official website of the National Authority for Management and Regulation in Communications of Romania (ANCOM), available at(`https://www.ancom.ro/legislatie-organizare-ancom_5620#`).
- For the country prefix lookup functionality, ensure the `country_prefixes.txt` file is properly formatted with one prefix-country pair per line separated by a colon (`:`).

---
## Created by Dobree12.

Feel free to customize this project to your liking! 
