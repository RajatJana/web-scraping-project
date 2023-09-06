from selenium import webdriver
import selenium.webdriver.support.ui
import select
import time
import pandas as pd

data = {'Name':[],'Roll No.':[],'SGPA':[],'SGPA2':[],'YGPA':[],'RESULT':[]}
# Enter roll number start range
i = 12620005001

web = webdriver.Chrome( executable_path="C:\\Users\\RAJAT JANA\\Desktop\\chromedriver-win64\\chromedriver.exe" )

# enter roll number end range
while i <= 12620005065:
    web.get('http://136.232.2.202:8084/stud23e.aspx')

    time.sleep(2)

    RollNo = i
    roll = web.find_element("xpath",'//*[@id="form1"]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/input')
    roll.send_keys(RollNo)

    # copy and paste xpath of semester
    option = web.find_element("xpath",'//*[@id="form1"]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/select/option[7]')

    # option = web.find_element_by_xpath('xpath')
    option.click()

    submit = web.find_element("xpath",'//*[@id="Button1"]')
    submit.click()
    title = web.title

    # crash = web.find_element_by_xpath('//*[@id="form1"]/table/tbody/tr/td/table/tbody/tr[2]/td/span/span[2]/strong').text
    if title == 'HERITAGE INSTITUTE OF TECHNOLOGY':

        name = web.find_element("xpath",'//*[@id="lblname"]')
        print(name.text)
        data["Name"].append(name.text)
    # print('\n')
        rollprint = web.find_element("xpath",'//*[@id="lblroll"]')
        print(rollprint.text)
        data["Roll No."].append(rollprint.text)
    # print('\n')
        sgpa = web.find_element("xpath",'//*[@id="lblbottom1"]')
        print(sgpa.text)
        data["SGPA"].append(sgpa.text)

        sgpa2 = web.find_element("xpath",'//*[@id="lblbottom2"]')
        print(sgpa2.text)
        data["SGPA2"].append(sgpa2.text)
        ygpa = web.find_element("xpath",'//*[@id="lblbottom3"]')
        print(ygpa.text)
        data["YGPA"].append(ygpa.text)
        result = web.find_element("xpath",'//*[@id="lblbottom4"]')
        print(result.text)
        data["RESULT"].append(result.text)
        print('\n')
    # print('\n')

    i = i+1
    df=pd.DataFrame.from_dict(data)
    df.to_csv("data.csv",index=False)