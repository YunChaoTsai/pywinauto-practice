import pywinauto
import win32api
from time import sleep


def main():
    pywinauto.keyboard.send_keys('{LWIN down}{I down}{LWIN up}{I up}')
    sleep(1)
    pywinauto.keyboard.send_keys('{TAB}{RIGHT}{RIGHT}{RIGHT}{RIGHT}{RIGHT}{RIGHT}{RIGHT}')
    sleep(1)
    pywinauto.keyboard.send_keys('{ENTER}')
    sleep(1)
    pywinauto.keyboard.send_keys('{TAB}')
    sleep(1)
    pywinauto.keyboard.send_keys('{DOWN}')
    sleep(1)
    pywinauto.keyboard.send_keys('{ENTER}')
    sleep(1)
    pywinauto.keyboard.send_keys('{VK_MENU down}{F4 down}{VK_MENU up}{F4 up}')

    print('hooray')


if __name__ == '__main__':
   main()