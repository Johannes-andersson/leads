import tkinter as tk
from tkinter import filedialog, messagebox
import requests
import csv
from tkinter.ttk import Progressbar
import matplotlib.pyplot as plt
import time

# API configuration
API_KEY = 'YOU API KEY'
API_ENDPOINT = 'https://api.yelp.com/v3/businesses/search'


class YelpScraperApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lead Scraper")
        self.geometry("400x300")
        
        # Labels and Input fields
        tk.Label(self, text="Company Niche:").pack(pady=10)
        self.niche_entry = tk.Entry(self)
        self.niche_entry.pack(pady=5)

        tk.Label(self, text="Location:").pack(pady=10)
        self.location_entry = tk.Entry(self)
        self.location_entry.pack(pady=5)

        # Progress Bar
        self.progress_label = tk.Label(self, text="Progress")
        self.progress_label.pack(pady=10)
        
        self.progress = Progressbar(self, orient=tk.HORIZONTAL, length=300, mode='determinate')
        self.progress.pack(pady=10)

        # Save Button
        self.save_button = tk.Button(self, text="Save CSV", command=self.scrape_leads)
        self.save_button.pack(pady=20)

        # Graph placeholder
        self.fig, self.ax = plt.subplots()

    
    def scrape_leads(self):
        niche = self.niche_entry.get()
        location = self.location_entry.get()

        if not niche or not location:
            messagebox.showwarning("Input Error", "Please enter both a company niche and a location.")
            return
        
        # Set API headers and parameters
        headers = {
            'Authorization': f'Bearer {API_KEY}',
            'accept': 'application/json'
        }
        params = {
            'term': niche,
            'location': location,
            'limit': 20,  # Max results per request
            'sort_by': 'best_match'
        }
        
        
        leads = []
        try:
            response = requests.get(API_ENDPOINT, headers=headers, params=params)
            data = response.json()

            if 'businesses' not in data:
                messagebox.showerror("Error", "No results found. Check your input or API limits.")
                return
            
            total_results = len(data['businesses'])
            self.progress['maximum'] = total_results
            
            for idx, business in enumerate(data['businesses']):
                name = business.get('name')
                phone = business.get('display_phone', 'N/A')
                address = ', '.join(business['location'].get('display_address', []))
                leads.append([name, phone, address])
                
                
                self.progress['value'] = idx + 1
                self.update_idletasks()
                time.sleep(0.1)  
                
            # Save leads to CSV
            self.save_to_csv(leads)
            
            # Display progress in graph
            self.show_progress_graph(len(leads), total_results)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    
    
    def save_to_csv(self, leads):
        filepath = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if filepath:
            with open(filepath, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Business Name", "Phone", "Address"])
                writer.writerows(leads)
            messagebox.showinfo("Success", "Leads saved to CSV successfully.")
    
    # Function to show progress graph
    def show_progress_graph(self, completed, total):
        self.ax.clear()
        self.ax.bar(['Completed', 'Remaining'], [completed, total - completed], color=['green', 'red'])
        self.ax.set_title('Scraping Progress')
        plt.show()


if __name__ == "__main__":
    app = YelpScraperApp()
    app.mainloop()
