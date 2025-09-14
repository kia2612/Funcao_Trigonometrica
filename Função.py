import numpy as np
from rich.align import Align
from rich.panel import Panel
from rich.console import Console
import matplotlib.pyplot as plt
from os import system

console = Console()

def trat_error(valorx):
   while True:
      try:
         var = float(input(valorx))
      except ValueError:
         console.print("[bold red]Tipo de dado inválido[/bold red]")
         continue
      break
   return var


def calculo(a,b,c,d,option):
  x = np.linspace(-10, 10, 400)
  
  if option == 'sen':
      y = a * np.sin(b*x + c) + d
      title = (f"{a:.0f}.sen({b:.0f}x + {c:.0f}) + {d:.0f}")
  else:
      y = a * np.cos(b*x + c) + d
      title = (f"{a:.0f}.con({b:.0f}x + {c:.0f}) + {d:.0f}")

  plt.style.use('dark_background')

  fig, ax = plt.subplots(figsize=(7, 5))
  ax.plot(x, y, color="#5b09d6", linewidth=2, label=title.format(a=a,b=b,c=c,d=d))
  plt.title(title)

  ax.axhline(0, color='gray', linewidth=0.7)
  ax.axvline(0, color='gray', linewidth=0.7)

  ax.grid(True, which='both', linestyle='--', color='gray', alpha=0.3)

  ax.set_xlabel("Eixo x", fontsize=7, color='white')
  ax.set_ylabel("Eixo y", fontsize=7, color='white')

  
  ax.tick_params(colors='white', labelsize=7)
  ax.legend(facecolor="#222", edgecolor="none", fontsize=7)

  fig.patch.set_facecolor('#111')
  plt.show()


def menu():
  system('cls')
  titulo = Align.center("[cyan]FUNÇÕES TRIGONOMÉTRICAS[/cyan]")
  painel = Panel((titulo), border_style="magenta", width=50)
  print()
  console.print( Align.center(painel))
  console.print()


def main():
  menu()
  option = ''
  while (option != 'sen') and (option != 'cos'):
    try:
        option = input('Qual o tipo de função trigonométrica será realizada (sen ou cos): ')
        if (option != 'sen') and (option != 'cos'):
            console.print("[bold red]Opção inválida[/bold red]")
    except ValueError:
      console.print("[bold red]Houve um erro acerca do valor digitado!![/bold red]")

  if option == "sen":
      system('cls')
      print()
      func = Align.center('[bold green] f(x) = A.sen(bx + c) + d [/bold green]')
      tt = Align.center(Panel((func), border_style="purple", width= 70))
      console.print(tt)
      try:
        a = trat_error(valorx="Insira o valor de A (Amplitude): ")
        b = trat_error(valorx="Insira o valor de B (Controle da Fequência): ")
        c = trat_error(valorx="Insira o valor de C (Deslocamento horizontal): ")
        d = trat_error(valorx="Insira o valor de D (Deslocamento Vertical): ")
      except TypeError:
         console.print("[bold red]Tipo de dado inválido[/bold red]")
         
  else:
      system('cls')
      print()
      func = Align.center('[bold yellow] f(x) = A.cos(bx + c) + d [/bold yellow]')
      tt = Align.center(Panel((func), border_style="cyan", width= 70))
      console.print(tt)
      try:
        a = trat_error(valorx="Insira o valor de A (Amplitude): ")
        b = trat_error(valorx="Insira o valor de B (Controle da Fequência): ")
        c = trat_error(valorx="Insira o valor de C (Deslocamento horizontal): ")
        d = trat_error(valorx="Insira o valor de D (Deslocamento Vertical): ")
      except ValueError:
         console.print("[bold red]Tipo de dado inválido[/bold red]")        
  calculo(a,b,c,d,option)

main()