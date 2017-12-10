from models_list import models
from functions import distance

models_numbers = len(models)
model_approve = False
second_model_approve = False
model_check = ''
model_choice = ''

input("Kliknij enter aby ropocząć.")
print("""W bazie znajduje się w tej chwili """ + str(models_numbers) +
    """ marek pojazdów elektrycznych.\nKażda z nich ma kilka modeli i ich określone parametry.
Program w przybliżeniu obliczy zasięg oraz pokaże najbliższą stację ładowania.""")
input("Kliknij enter aby kontynuować.")
while model_approve == False:
    model_check = input("Podaj markę pojazdu który chcesz sprawdzić i naciśnij enter. ")
    model_check = model_check.title()
    if model_check in models:
        model_approve = True
        print("W bazie posiadamy następujące modele: ")
        for model in models[model_check]:
            print(model)
        model_choice = input("Wpisz jeden z nich(dokładnie, całą nazwę) a następnie naciśnij "
                             "enter aby przejść do parametrów i obliczeń.")
    else:
        print("Niestety jak na razie w Naszej bazie nie posiadamy takiej marki.")
        repeat_model_check = input("Jeżeli chcesz podać inną wpisz 't'. Jeżeli chcesz zobaczyć"
                                    " listę dostępnych marek wpisz 'm'.")
        if repeat_model_check == "t":
            model_approve = False
        elif repeat_model_check == "m":
            model_approve = True
            print("W bazie posiadamy następujące marki: ")
            for model in models:
                print(model)
            model_check = input("Podaj markę pojazdu który chcesz sprawdzić i naciśnij enter. ")
            model_check = model_check.title()
            if model_check in models:
                print("W bazie posiadamy następujące modele: ")
                for model in models[model_check]:
                    print(model)
                model_choice = input("Wpisz jeden z nich(dokładnie, całą nazwę) a następnie naciśnij "
                                         "enter aby przejść do parametrów i obliczeń.")
                while model_choice not in models[model_check]:
                    model_choice = input("Niestety nazwa jest nie poprawna. Wpisz ponownie(dokładnie, całą nazwę) a następnie naciśnij "
                                         "enter aby przejść do parametrów i obliczeń.")

print("Wybrałeś " + model_choice + ". Jego zasięg to " + str(models[model_check][model_choice][0])
      +" km a średnie zużycie "+ str(models[model_check][model_choice][1]) + " kWh.")

car_distance = input("Podaj dystans jaki chcesz przejechać (w km)")
print("Twoje auto zużyje " + str(distance(car_distance, models[model_check][model_choice][1])) + " kWh energii. ")


