ano_nacimento = int(input("Ano de nascimento: "))
idade = 2017 - ano_nacimento

if idade < 18:
    print(f"Quem nasceu em {ano_nacimento} tem {idade} anos em 2017.\nAinda faltam {18-idade} anos para o alistamento.\nSeu alistamento sera em {(18-idade)+2017}.")
elif idade > 18:
    print(f"Quem nasceu em {ano_nacimento} tem {idade} anos em 2017.\nVocê já deveria ter se alistado há {idade-18} ano(s)\nSeu alistamento foi em {2017-(idade-18)}.")
else:
    print(f"Quem nasceu em {ano_nacimento} tem {idade} anos em 2017.\nVocê deve se alistar imediatamente")

