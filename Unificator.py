import time




print('If you want to see the example of image modifier, press 1, if you want to scrap the website press 2, if you'
      ' want to listen audio press 3, if you want to see data visualisation example press 4, else press q')
input_data = input("Make your choice:")
for elements in input_data:
    if elements == '1':
        import Image_modifaer
    elif elements == '2':
        import Website_scrapper
    elif elements == '3':
        import Audio_player
    elif elements == '4':
        import Data_vizualizer
    elif elements == 'q':
        print('Thank you for using this example programme!')
    else:
        input_data = input("Not right signature, please, enter the possible one:")


time.sleep(2)
input("Нажмите Enter для выхода")