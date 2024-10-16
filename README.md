This Python application scrapes Yelp for business leads based on a specified niche (e.g., "restaurants," "software companies") and location (e.g., "San Francisco, CA"). The results are saved as a CSV file with details like business name, phone number, and address.

Table of Contents
Features
Requirements
Installation
Usage
License
Features
User-Friendly GUI: Built with Tkinter for easy interaction.
Scrapes Yelp: Collects information about businesses based on specified niche and location.
Progress Tracking: A progress bar and visual graph display the scraping progress.
CSV Export: Saves the results to a CSV file in a user-selected location.
Requirements
Python 3.9+
Required Python packages:
requests
tkinter (built into Python)
csv (built into Python)
matplotlib
Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/yelp-lead-scraper.git
cd yelp-lead-scraper
Set Up Environment:

You may want to set up a virtual environment:
bash
Copy code
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
Install Required Packages:

bash
Copy code
pip install -r requirements.txt
Set Up API Key:

This application uses the Yelp API to fetch business data. You will need a Yelp API key:
Go to Yelp's Developer Portal and sign up or log in to create an API key.
Replace API_KEY in the code with your actual API key, or load it securely from an environment variable.
Run the Application:

bash
Copy code
python leads.py
Usage
Enter the Niche and Location:

Input the desired business niche (e.g., "restaurants") and location (e.g., "New York, NY") into the GUI.
Scrape and Save:

Click "Save CSV" to start scraping.
Choose a location to save the CSV file.
View Progress:

The progress bar shows the scraping status. A graph will display completed vs. remaining businesses after the scrape.
Results:

The saved CSV file will contain the following columns:
Business Name
Phone
Address
