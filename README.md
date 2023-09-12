# Open LLM Leaderboard Scraper

The Open LLM Leaderboard Scraper is a Python script that allows you to scrape and export data from the Open LLM Leaderboard.

## Table of Contents
- [Introduction](#open-llm-leaderboard-scraper)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Export Options](#export-options)
- [Output Files](#output-files)
  
## Prerequisites

Before using the scraper, ensure you have the following prerequisites installed:

- Python 3.x
- Required Python packages 


# Usage
To use the Open LLM Leaderboard Scraper, follow these steps:

1. Clone the repository or download the script (main.py) to your local machine.
   
```bash
git clone https://github.com/Weyaxi/scrape-open-llm-leaderboard
```
2. Open a terminal or command prompt and navigate to the script's directory.
```bash
cd scrape-open-llm-leaderboard
```

3. Install the required packages using this command:

```bash
pip3 install -r requirements.txt
```

4. Run the script using the following command:

```bash
python3 main.py [options]
```

# Export Options

The script supports three export options:

- `-csv`: Export data to a CSV file.
- `-html`: Export data to an HTML file.
- `-json`: Export data to a JSON file.

You can use these options to specify the desired export format(s). For example, to export data in both CSV and HTML formats, run the following command:

```bash
python3 main.py -csv -html
```

If no export options are provided, the script will default to exporting data in CSV format.

# Output Files

The scraper will generate one or more output files based on the export options selected. The output files will be named as follows:

- `open-llm-leaderboard.csv`: Contains the scraped data in CSV format.
- `open-llm-leaderboard.html`: Contains the scraped data in HTML format.
- `open-llm-leaderboard.json`: Contains the scraped data in JSON format.

You can find these files in the same directory where you run the script.

