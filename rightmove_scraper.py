import requests
import bs4
import csv

counter = 0
price = []
prop_id = []
rental_type = []
final = []
address = []
page = 0
page_index = 0

file_to_output = open('to_save_file.csv','w',newline='')
csv_writer = csv.writer(file_to_output,delimiter=',')

for page in range(1,9):
    base_url = "https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION%5E87515&index={}&propertyTypes=&includeLetAgreed=false&mustHave=&dontShow=&furnishTypes=&keywords="
    
    scrape_url = base_url.format(page_index)
 
    result = requests.get(scrape_url)
    print(scrape_url)
    soup = bs4.BeautifulSoup(result.text,"lxml")
 
    for count in soup.select('.propertyCard-priceValue'):
  
        price_string,unit = soup.select('.propertyCard-priceValue')[counter].getText().replace(",","").replace("£","").split(" ")
        price.append(price_string)

        prop_id_value = soup.select(".propertyCard-anchor")[counter]['id']
        prop_id.append(prop_id_value)
        rental_type_value = soup.select(".propertyCard-title")[counter].getText().strip()
        rental_type.append(rental_type_value)
        address_value = soup.select(".propertyCard-address")[counter].getText().strip()
        address.append(address_value)

        final = [prop_id,price,rental_type, address]

        print(final[0][counter]+ " " + final[1][counter]+ " " + final[2][counter]+" " + final[3][counter])
        csv_writer.writerow([final[0][counter],final[1][counter],final[2][counter],final[3][counter]])

        counter = counter + 1
    
    print("Page number:")
    print(page)        
    
    page_index = page*25
    counter = 0
file_to_output.close()


