from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import random

#web scrapping

browser = webdriver.Chrome()

#url = "https://www.lottoland.com/br/megasena/resultados"
url = 'https://www.lottoland.com/br/megasena/resultados/12-01-2023'
browser.get(url)

temp_list_numbers = list()
numberlist = list()
while True:
    ms_numeros = browser.find_element(By.TAG_NAME, 'll-lottery-balls').text
    ms_numeros = list(ms_numeros)
    if ms_numeros[2] != '\n':
        ms_numeros.insert(0, '0')
    if ms_numeros[5] != '\n':
        ms_numeros.insert(3, '0')
    if ms_numeros[8] != '\n':
        ms_numeros.insert(6, '0')
    if ms_numeros[11] != '\n':
        ms_numeros.insert(9, '0')
    if ms_numeros[14] != '\n':
        ms_numeros.insert(12, '0')

    for c in range(0, len(ms_numeros), 3):
        temp_list_numbers.append(ms_numeros[c] + ms_numeros[c+1])

    for numbers in temp_list_numbers:
        numberlist.append(int(numbers))

    temp_list_numbers.clear()
    ms_numeros.clear()

    sleep(1)
    browser.find_element(By.ID, 'dateSelect-selectDrawingsForYear-drawingsForYear').send_keys(Keys.ARROW_DOWN)
    sleep(1)
    browser.find_element(By.ID, 'dateSelect-selectDrawingsForYear-drawingsForYear').send_keys(Keys.RETURN)
    sleep(1)
    print(numberlist)
    
    if browser.current_url == 'https://www.lottoland.com/br/megasena/resultados/04-01-2023':
        break


#analyse

number_weight = list()
number_weight_inverted = list()
loteria = list()
total_num_drawn = 60

for n in numberlist:
    total_num_drawn += n

for c in range(0, 60):
    number_weight.append(numberlist.count(c + 1) / total_num_drawn)
    number_weight_inverted.append((1 - number_weight[c]))

#    number_weight.append(numberlist.count(c))
    loteria.append(c +1)

print(loteria)
print(number_weight)
print(number_weight_inverted)
print(total_num_drawn)



#results
print()
print('Números com a maior probabilidade de sair baseado nos jogos anteriores:')
for c in range(0, 10):
    print(sorted(random.choices(loteria, weights = number_weight, k=6)))

print()
print('Números aleatórios:')
for c in range(0, 5):
    print(sorted(random.choices(loteria, k=6)))

print()
print('Números com a menor probabilidade de sair baseado nos jogos anteriores:')
for c in range(0, 5):
    print(sorted(random.choices(loteria, k=6)))