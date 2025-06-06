
Built by https://www.blackbox.ai

---

# PC Games Key Scraper

## Project Overview
PC Games Key Scraper is a Python-based web scraper designed to extract product information from the PCGamesKey online store. It leverages the power of the Clouds scraper and BeautifulSoup libraries to navigate web pages and obtain product details, including names, prices, descriptions, images, and categories. The scraped data is stored in a CSV file for easy access.

## Installation
To set up the project, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/username/pcgameskey-scraper.git
   cd pcgameskey-scraper
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

### Dependencies
You will need the following libraries, which can be found in `requirements.txt`:
- `beautifulsoup4`
- `cloudscraper`
- `Flask`
- `lxml`
- `requests`

### Note
Make sure you have Python 3.6 or higher installed on your machine.

## Usage
To run the scraper, you can either run it directly from the command line or through the Flask web interface.

### Command Line
To run the scraper via the command line, execute:
```bash
python main.py
```

### Flask Web Interface
1. **Start the Flask server**:
   Run the following command in your terminal:
   ```bash
   python main.py
   ```

2. **Access the dashboard**:
   Open your web browser and go to `http://127.0.0.1:8000` to access the dashboard. From there, you can trigger the scraping process and download the generated CSV file.

## Features
- **Product Scraping**: Collects product name, price, image URL, description, and categories from the PCGamesKey store.
- **CSV Export**: Saves the scraped data into a CSV file (`products.csv`) for easy access and manipulation.
- **Error Handling**: Includes robust error handling and logging to track the scraping process.
- **Flask Interface**: Provides a simple web interface to initiate scraping and download results.

## Project Structure
```
pcgameskey-scraper/
├── config.py               # Configuration file for URLs and other settings
├── main.py                 # Flask app serving the web interface
├── scraper.py              # The main scraping logic and data extraction
├── utils.py                # Utility functions for text cleaning and logging
├── requirements.txt        # Python package dependencies
├── templates/              # HTML templates for the Flask app
│   └── dashboard.html      # Dashboard template file
└── debug_*                 # Debugging files for testing
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.