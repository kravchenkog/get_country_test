import requests
import xml.sax.saxutils as sx
from bs4 import BeautifulSoup


baseurl = 'http://www.webservicex.net/country.asmx/'



class TestClass_CountriesAll:




    def test_when_country_code_is_sent_country_response_should_be_correct(self):
        assertation_values = [['qa', 'Qatar']]
        result = self.get_country_by_code(assertation_values[0][0])
        assert result == assertation_values[0][1]

    def test_when_country_name_is_sent_country_curency_response_should_be_correct(self):
        assertation_values = [['Qatar', 'Rial']]
        result = self.get_curreny_by_country_name(assertation_values[0][0])
        assert result == assertation_values[0][1]

    def test_when_currency_code_is_sent_country_name_response_should_be_correct(self):
        name = 'Qatar'
        currency_code = self.get_curreny_code_by_country_name(name)
        assertation_values = [[currency_code, name]]
        result = self.get_country_by_currency_code(assertation_values[0][0])
        assert result == assertation_values[0][1]

    def test_when_currency_name_is_sent_currency_code_response_should_be_correct(self):
        currency_name = 'Rial'

        assertation_values = [[currency_name, 'QQQ']]
        result = self.get_curency_code_by_currency_name(assertation_values[0][0])
        assert result == assertation_values[0][1]


    def get_curency_code_by_currency_name(self, currency_name):
        url = baseurl + 'GetCurrencyCodeByCurrencyName?CurrencyName=' + currency_name
        response = requests.get(url)
        resp_to_xml = sx.unescape(response.text)
        soup = BeautifulSoup(resp_to_xml)
        result = soup.find_all('currencycode')[0].text
        return result

    def get_country_by_code(self, country_code):
        url = baseurl + 'GetCountryByCountryCode?CountryCode='+country_code
        response = requests.get(url)
        resp_to_xml = sx.unescape(response.text)
        soup = BeautifulSoup(resp_to_xml)
        result = soup.find_all('name')[0].text
        return result

    def get_curreny_by_country_name(self, country_name):
        url = baseurl + 'GetCurrencyByCountry?CountryName='+country_name
        response = requests.get(url)
        resp_to_xml = sx.unescape(response.text)
        soup = BeautifulSoup(resp_to_xml)
        result = soup.find_all('currency')[0].text
        return result

    def get_curreny_code_by_country_name(self, country_name):
        url = baseurl + 'GetCurrencyByCountry?CountryName='+country_name
        response = requests.get(url)
        resp_to_xml = sx.unescape(response.text)
        soup = BeautifulSoup(resp_to_xml)
        result = soup.find_all('currencycode')[0].text
        return result

    def get_country_by_currency_code(self, currency_code):
        url = baseurl + 'GetCountryByCurrencyCode?CurrencyCode='+currency_code
        response = requests.get(url)
        resp_to_xml = sx.unescape(response.text)
        soup = BeautifulSoup(resp_to_xml)
        result = soup.find_all('name')[0].text
        return result