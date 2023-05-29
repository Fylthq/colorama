import colorama
import inspect
help(colorama)
print(type(colorama))
print(dir(colorama))

if inspect.ismodule(colorama):
    print("colorama is module")

if inspect.isclass(colorama):
    print("colorama is class")

if inspect.isfunction(colorama):
    print("colorama is function")

help(colorama.Fore)
help(colorama.Back)
help(colorama.Style)
help(colorama.Cursor)

from colorama import Fore, Back
print(Fore.RED + 'НЕ зеленый текст')
print(Fore.BLUE + 'За допомогою Fore можно змінювати колір тексту, вона найважливіша (для мене)')
print(Back.GREEN + Fore.BLACK + 'Ну, ще також Бек не поганий атрібут')
