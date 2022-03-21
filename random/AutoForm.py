from selenium import webdriver
import pandas as pd
import time
import json
from datetime import datetime
import pathlib
import glob
import sys
sys.path.append('.')
import faker
import numpy

f = faker.Faker()
colors = ['Blue','Pink','Green','Yellow','Orange','Purple','Black','White','Red']
names = [f.name for i in range(100)]
ages = [np.random.randint(18,65) for i in range(100)]
color_choices = [random.choice(colors) for i in range(100)]

database = pd.DataFrame(dict(names=names, ages=ages, color_choices=color_choices))
database.to_csv('database.csv', index=False)
database.head()

text_question_element_class = 'quantumWizTextinputPaperinputInput'
checkbox_element_class = 'appsMaterialWizToggleRadiogroupOffRadio'
submit_button_class = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[1]/div/content/span'
url = input('Enter the url of the form: ')
