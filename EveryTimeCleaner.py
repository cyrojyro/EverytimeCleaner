#에브리타임 클리너 V0.1

import time
from selenium import webdriver
from selenium.common.exceptions import *

chromedriver_dir = r'C:\chromedriver.exe'
loginBtnName = 'button.login'
idTextBoxName = 'userid'
pwTextBoxName = 'password'
submitBtnName = 'submit'
myArticleURL = 'myarticle'
myCommentURL = "mycommentarticle"
articleName = 'article'
deleteBtnText = '삭제'

print('에브리타임 클리너를 사용하기 위해서는 \'크롬 인터넷 브라우저\'와, C 드라이브에 \'chromeDriver.exe 파일\'이 필요합니다.')
print('크롬 드라이버는 https://chromedriver.chromium.org/downloads에서 다운로드 받으실 수 있습니다.')

try:
    driver = webdriver.Chrome(chromedriver_dir)
    time.sleep(1)
    print("학교 코드는 https://xxx.everytime.kr/ 에서 xxx값입니다.")
    school = input("학교 코드를 입력해주세요: ")
    driver.get('https://' + school + '.everytime.kr/login')

    #로그인
    while True:
        id = driver.find_element_by_name(idTextBoxName)
        id.clear()
        usr_id = input("아이디를 입력해주세요: ")
        id.send_keys(usr_id)
        pw = driver.find_element_by_name(pwTextBoxName)
        usr_pw = input("비밀번호를 입력해주세요: ")
        pw.send_keys(usr_pw)
        submit = driver.find_element_by_class_name(submitBtnName)
        submit.click()
        try:
            alert = driver.switch_to.alert
            print('로그인에 실패했습니다.')
            alert.accept()
        except:
            print('로그인에 성공했습니다.')
            break

    #작업
    while True:
        process = input("게시글을 전부 삭제하시려면 1, 댓글을 전부 삭제하시려면 2를 입력하세요: ")
        
        #게시글 삭제 작업
        if process == "1":
            n = 0
            print("삭제 딜레이를 설정합니다. 컴퓨터 성능이 낮거나, 인터넷 속도가 느릴 수록 높게 설정하세요.")
            delay = input("삭제 딜레이를 입력해주세요(0.5 이상 권장, 초 단위):")
            delay = float(delay)
            while True:
                driver.get('https://' + school + '.everytime.kr/' + myArticleURL)
                time.sleep(delay)
                article = driver.find_element_by_class_name(articleName)
                article.click()
                time.sleep(delay)
                article = driver.find_element_by_class_name(articleName)
                status = article.find_element_by_tag_name('ul')
                li_list = status.find_elements_by_tag_name('li')
                for li in li_list:
                    if li.text == deleteBtnText:
                        li.click()
                        break
                try:
                    alert = driver.switch_to.alert
                    alert.accept()
                    n += 1
                    print('삭제 (%d)' % n)
                except:
                    print("삭제 완료.")
                    break

        #댓글 삭제 작업
        elif process == "2":
            n = 0
            print("삭제 딜레이를 설정합니다. 컴퓨터 성능이 낮거나, 인터넷 속도가 느릴 수록 높게 설정하세요.")
            delay = input("삭제 딜레이를 입력해주세요(0.5 이상 권장, 초 단위):")
            delay = float(delay)
            while True:
                driver.get('https://' + school + '.everytime.kr/' + myCommentURL)
                time.sleep(delay)
                article = driver.find_element_by_class_name(articleName)
                article.click()
                time.sleep(delay)
                comments = driver.find_elements_by_class_name(articleName)
                flag = False

                #삭제 가능한 댓글 탐색
                for comment in comments:
                    if flag:
                        break
                    li_list = comment.find_elements_by_tag_name('li')
                    for li in li_list:
                        if li.text == deleteBtnText:
                            li.click()
                            flag = True
                            break
                try:
                    alert = driver.switch_to.alert
                    alert.accept()
                    n += 1
                    print('삭제 (%d)' % n)
                except:
                    print("삭제 완료.")
                    break
        else:
            print("잘못된 입력입니다.")

except WebDriverException as e:
    print(e)

