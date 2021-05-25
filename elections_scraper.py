from bs4 import BeautifulSoup as BS
import requests
import sys
# import os.path as op
my_url = "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103"
my_file_name = "vysledky_prostejov.csv"
import csv
from urllib.parse import urljoin


def main():
    #if not check_args():
        #exit()
    #my_url = sys.argv[1]
    #my_file_name = sys.argv[2]
    print("Downloading data from your url: ", my_url)
    print(f"Saving data in file: {my_file_name}")
    r = requests.get(my_url)
    soup = BS(r.text, "html.parser")
    create_file_header(my_file_name)
    town_codes = get_town_code(soup)
    town_names = get_town_names(soup)
    url_list = get_town_urls(soup)
    while True:
        if url_list:
            new_url = url_list.pop(0)
            new_r = requests.get(new_url)
            new_soup = BS(new_r.text, "html.parser")
            ttl_vts = [[town_codes.pop(0), town_names.pop(0)] + total_votes(new_soup) + get_party_votes(new_soup)]
            write_votes(my_file_name, ttl_vts)
        else:
            print(f"Your file {my_file_name} was created.Enjoy.Exiting program elections_scraper.py.")
            break


def check_args():
    if len(sys.argv) != 3:
        print("My program takes exactly 2 arguments: url,file name")
        return False
    elif "https://volby.cz/pls/ps2017nss/" not in sys.argv[1]:
        print("First argument must be url and second name of your file.Also you can use my program only for volby.cz")
        return False
    elif "https" in sys.argv[2]:
        print("Second argument must be name of your file, not url.")
        return False
    else:
        return True


def write_votes(my_file_name, ttl_vts):

    with open(my_file_name, "a+", newline="") as f:
        write = csv.writer(f)
        write.writerows(ttl_vts)


def get_town_code(soup):

    town_code = soup.find_all("td", attrs={"headers": "t1sa1 t1sb1"})
    town_code2 = soup.find_all("td", attrs={"headers": "t2sa1 t2sb1"})
    town_code3 = soup.find_all("td", attrs={"headers": "t3sa1 t3sb1"})
    town_codes = []
    for code in town_code:
        town_codes.append(code.text)
    for code in town_code2:
        town_codes.append(code.text)
    for code in town_code3:
        town_codes.append(code.text)
    town_codes = town_codes[:-2]
    return town_codes


def get_town_names(soup):

    town = soup.find_all("td", attrs={"headers": "t1sa1 t1sb2"})
    town2 = soup.find_all("td", attrs={"headers": "t2sa1 t2sb2"})
    town3 = soup.find_all("td", attrs={"headers": "t3sa1 t3sb2"})
    towns = []
    for name_of in town:
        towns.append(name_of.text)
    for name_of in town2:
        towns.append(name_of.text)
    for name_of in town3:
        towns.append(name_of.text)
    towns = towns[:-2]
    return towns


def get_town_urls(soup):

    help_url = "https://volby.cz/pls/ps2017nss/"
    get_town_url = soup.find_all("a")
    counter = 0
    town_urls = []
    for elem in get_town_url:
        counter += 1
        if counter % 2 == 0:
            urls = urljoin(help_url, elem["href"])
            if 'http' not in elem['href'] and len(elem['href']) > 40:
                town_urls.append(urls)
    return town_urls


def create_file_header(my_file_name):

    header = ["Town Code", "Town Name", "Registered", "Envelopes", "Valid votes", ]
    header = header + get_parties_names()
    with open(my_file_name, "w", newline="") as f:
        f_writer = csv.writer(f)
        f_writer.writerow(header)


def total_votes(new_soup):

    voters = new_soup.find("td", attrs={"headers": "sa2"}).text
    envelopes = new_soup.find("td", attrs={"headers": "sa3"}).text
    valid_votes = new_soup.find("td", attrs={"headers": "sa6"}).text
    total_vts = [voters, envelopes, valid_votes]
    return total_vts


def get_parties_names():

    parties_url = "https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=12&xobec=589268&xvyber=7103"
    parties_r = requests.get(parties_url)
    parties_soup = BS(parties_r.text, "html.parser")
    get_parties1 = parties_soup.find_all("td", attrs={"headers": "t1sa1 t1sb2"})
    get_parties2 = parties_soup.find_all("td", attrs={"headers": "t2sa1 t2sb2"})
    parties = []
    for party in get_parties1:
        parties.append(party.text)
    for party in get_parties2:
        parties.append(party.text)
    parties = parties[:-1]
    return parties


def get_party_votes(new_soup):

    get_votes1 = new_soup.find_all("td", attrs={"headers": "t1sa2 t1sb3"})
    get_votes2 = new_soup.find_all("td", attrs={"headers": "t2sa2 t2sb3"})
    votes = []
    for vote in get_votes1:
        votes.append(vote.text)
    for vote in get_votes2:
        votes.append(vote.text)
    votes = votes[:-1]
    return votes


if __name__ == "__main__":
    main()
