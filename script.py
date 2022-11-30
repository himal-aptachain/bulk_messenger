import pywhatkit
import time
import win32clipboard
msg = "hey I'm NEETXPERT Guru, NEET results are out. I will help you in NEET Councelling  Click on " \
      "https://docs.google.com/forms/d/1n0ZKSeNUgzjIqEs53EUavYeSVPC5lkq5dSeDekZcbUc/edit "
caption = """NEETXPERT GURU 

1) ನೀಟ್ ಲಾಗಿನ್ ಕ್ರಿಯೇಷನ್ 
2) ನೀಟ್ ಡಾಕ್ಯುಮೆಂಟ್ ವೆರಿಫಿಕೇಷನ್ ಸಹಾಯ 
3) ಸ್ಟೂಡೆಂಟ್ ಮತ್ತು ಪೇರೆಂಟ್ಸ್ ಜೊತೆ ಮಾತನಾಡಿ ಮೆಡಿಕಲ್ ಕಾಲೇಜು ಪ್ರಿಯೋರಿಟಿ ಲಿಸ್ಟ್ ರೆಡಿ ಮಾಡುವುದು 
4) ಮೆಡಿಕಲ್ ಕಾಲೇಜು ಆಪ್ಷನ್ ಎಂಟ್ರಿ 
5) ಮೆಡಿಕಲ್ ಕಾಲೇಜು ಅಡ್ಮಿಶನ್ ಸಹಾಯ

ಎಲ್ಲ ಹೆಲ್ಪ್ ಗೆ ವಾಟ್ಸಪ್ಪ್/ಕಾಲ್ ಮಾಡಿ  8904074477 / email - neetxpertguru@gmail.com"""

image = 'image1.jpg'
numbers = "P:/BulkMessenger/numbers.txt"

with open(numbers) as file:
    for number in file:
        number = number.strip()  # preprocess line
        pywhatkit.sendwhatmsg_instantly(number, msg, 25, True, 2)
        pywhatkit.sendwhats_image(number, image, caption, 60
        , True, 2)
        print(number)


# with open('D:/bulk_message/numbers.txt') as number:
#     numbers = f.read().splitlines()

# for number in  numbers:
#     now=time.localtime()
#     print(number)
#     pywhatkit.sendwhatmsg(number, msg, now.tm_hour, now.tm_min)
# syntax: phone number with country code, message, hour and minutes
