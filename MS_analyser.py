from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import random
import os

#menu
print('-'*50)
print(f'{"SORTEADOR DE NÚMEROS":^50}')
print('-'*50)
print('''O programa irá analisar todos os números sorteados nesse ano, e irá dar 90 jogos: 
> 30 com maiores chances de sair, baseados nos sorteios anteriores.
> 30 jogos aleatórios.
> 30 com as menores chances de sair.
      ''')
sleep(4)
print('Iniciando', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.')
sleep(2)


#web scrapping
browser = webdriver.Chrome()
url = "https://www.lottoland.com/br/megasena/resultados"
#url = 'https://www.lottoland.com/br/megasena/resultados/12-01-2023'
browser.get(url)

temp_list_numbers = list()
numberlist = list()
total_games_count = 0
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

    os.system('cls')
    print(f'Total de jogos analisados: {total_games_count}')
    print(f'{"Carregando..":^30}')
    print('-'*30)
    sleep(1)
    print('█'*10, end='')
    browser.find_element(By.ID, 'dateSelect-selectDrawingsForYear-drawingsForYear').send_keys(Keys.ARROW_DOWN)
    sleep(1)
    print('█'*10, end='')
    browser.find_element(By.ID, 'dateSelect-selectDrawingsForYear-drawingsForYear').send_keys(Keys.RETURN)
    sleep(1)
    print('█'*10, end='')
    print()
    
    if browser.current_url == 'https://www.lottoland.com/br/megasena/resultados/04-01-2023':
        break
    total_games_count += 1
    sleep(0.3)


#analyse
number_weight = list()
number_weight_inverted = list()
number_no_weight = list()
loteria = list()
total_num_drawn = 60

for n in numberlist:
    total_num_drawn += n

for c in range(0, 60):
    number_weight.append(numberlist.count(c + 1) / total_num_drawn)
    number_weight_inverted.append((1 - number_weight[c]))
    number_no_weight.append(1)
    loteria.append(c + 1)

high_prob_numb = list()
normal_prob_numb = list()
low_prob_numb = list()
def numb_draw_to_list(select_weight, select_list):
    temp_number = list()
    index_count = 0
    while True:
        temp_number = sorted(random.choices(loteria, weights = select_weight, k=6))
        for numbers in temp_number:
            if temp_number.count(numbers) == 1:
                index_count += 1
        if index_count == 6:
            select_list.append(temp_number)
            print('print select_list', select_list)
            print('print temp_number', temp_number)
            break
        else:
            temp_number.clear()
            index_count = 0

for c in range(0, 30):
    numb_draw_to_list(number_weight, high_prob_numb)
    numb_draw_to_list(number_no_weight, normal_prob_numb)
    numb_draw_to_list(number_weight_inverted, low_prob_numb)

#results
os.system('cls')
print()
def printlistnum(listnum):
    for game in listnum:
        print(game)

print('Números com alta probabilidade de sair:')
printlistnum(high_prob_numb)
print('Números aleatórios:')
printlistnum(normal_prob_numb)
print('Números com baixa probabilidade de sair:')
printlistnum(low_prob_numb)

with open('goodluck.txt', 'w') as f:
    f.write('Números com alta probabilidade de sair: \n')
    for line in high_prob_numb:
        index_count = 0
        for n in line:
            f.write(str(n))
            if index_count < 5:
                f.write(' - ')
            index_count += 1
        f.write('\n')
    
    f.write('Números aleatórios: \n')
    for line in normal_prob_numb:
        index_count = 0
        for n in line:
            f.write(str(n))
            if index_count < 5:
                f.write(' - ')
            index_count += 1
        f.write('\n')
    
    f.write('Números com baixa probabilidade de sair: \n')
    for line in low_prob_numb:
        index_count = 0
        for n in line:
            f.write(str(n))
            if index_count < 5:
                f.write(' - ')
            index_count += 1
        f.write('\n')
