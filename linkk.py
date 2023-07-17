import requests
from bs4 import BeautifulSoup

# Initialize a list to store the Udemy links
udemy_links = []
pag = 3

# Loop through the range of page numbers (1 to 10)
for page_num in range(1, pag+1):
    # URL of the page to scrape
    url = f"https://www.onlinecourses.ooo/page/{page_num}/"

    # Send a GET request to the URL
    response = requests.get(url)

    # Create BeautifulSoup object from the response content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the div with class "eq_grid pt5 rh-flex-eq-height col_wrap_three"
    div = soup.find("div", class_="eq_grid pt5 rh-flex-eq-height col_wrap_three")

    # Find all the article elements within the div
    articles = div.find_all("article")

    # Loop through the articles and extract the Udemy links
    for article in articles:
        # Find the <a> element within the article
        a_element = article.find("a")
        # Get the href attribute value
        href = a_element.get("href")

        # Send a GET request to the href link
        course_page_response = requests.get(href)

        # Create BeautifulSoup object from the course page response content
        course_page_soup = BeautifulSoup(course_page_response.content, "html.parser")

        # Find the <a> element with class "btn_offer_block re_track_btn"
        udemy_link_element = course_page_soup.find("a", class_="btn_offer_block re_track_btn")

        # Check if the Udemy link element exists
        if udemy_link_element:
            # Get the href attribute value (Udemy link)
            udemy_link = udemy_link_element.get("href")

            # Add the Udemy link to the list
            udemy_links.append(udemy_link)

# Save the Udemy links in the "udemy.txt" file
with open("udemy.txt", "w") as file:
    for link in udemy_links:
        file.write(link + "\n")

print("Udemy links saved in 'udemy.txt' file.")
