from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

# Cole aqui seu código principal
# Paste your main code here



# Fim do código principal
# End of main code here
options = webdriver.ChromeOptions()
options.add_argument("--headless")

browser = webdriver.Chrome(chrome_options=options)
browser.get("https://translate.google.com/")

sleep(5)
browser.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea').send_keys("pronto. tarefa terminada") # Esta linha contém o texto da fala - if you prefer it in English modify this line with something like "Done. Task finished"
sleep(2)
browser.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/div[4]/div[2]/div/div[2]/span/button/div[3]').click()
sleep(20)  # esta linha aguarda 20 segundo para a fala ser completada (caso queira aumentar o texto da fala) - this line waits 20 seconds for the speech to be completed (in case you want to increase the text of the speech)



browser.quit()
