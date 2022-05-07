from services.first.first import first_calls_print_sister #call using relative path should be called by python -m script.third.third at main directory(app/)
from script.second.second import print_second_script #call using relative path should be called by python -m script.third.third at main directory(app/)

print("third called")
print_second_script()