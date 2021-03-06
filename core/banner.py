#!/usr/bin/env python
# -*- coding: utf-8 -*-
#autor samir sanchez garnica @sasaga92
from random import choice

from utilities.colors import script_colors

class Banner():
  def __init__(self):

    _colors = ['red','blue','green','yellow','cyan','cafe','black','lpurple','purple']

    _autor = '''
                                                              ANUBIS
                                                        version: 1.0
                                        Autor: Samir Sanchez Garnica
                                                           @sasaga92
    '''

    def banner_welcome_1():
        _banner = '''

                       █████╗ ███╗   ██╗██╗   ██╗██████╗ ██╗███████╗
                      ██╔══██╗████╗  ██║██║   ██║██╔══██╗██║██╔════╝
                      ███████║██╔██╗ ██║██║   ██║██████╔╝██║███████╗
                      ██╔══██║██║╚██╗██║██║   ██║██╔══██╗██║╚════██║
                      ██║  ██║██║ ╚████║╚██████╔╝██████╔╝██║███████║
                      ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═════╝ ╚═╝╚══════╝
                                                                                                                                                                                           
        '''
        print(script_colors(choice(_colors),_banner))
        print(script_colors('lgray',_autor))


    def banner_welcome_2():
      _banner = """
              %dyel                        .,-:;//;:=,
              %dyel                    . :H@@@MM@M#H/.,+%;,
              %dyel                 ,/X+ +M@@M@MM%=,-%HMMM@X/,
              %dyel               -+@MM; $M@@MH+-,;XMMMM@MMMM@+-
              %dyel              ;@M@@M- XM@X;. -+XXXXXHHH@M@M#@/.
              %dyel            ,%MM@@MH ,@%=             .---=-=:=,.
              %dyel            =@#@@@MX.,                -%HX$$%%%:;
              %dyel           =-./@M@M$                   .;@MMMM@MM:
              %dyel           X@/ -$MM/                    . +MM@@@M$
              %dyel          ,@M@H: :@:                    . =X#@@@@-
              %dyel          ,@@@MMX, .                    /H- ;@M@M=
              %dyel          .H@@@@M@+,                    %MM+..%#$.
              %dyel           /MMMM@MMH/.                  XM@MH; =;
              %dyel            /%+%$XHH@$=              , .H@@@@MX,
              %dyel             .=--------.           -%H.,@@@@@MX,
              %dyel             .%MM@@@HHHXX$$$%+- .:$MMX =M@@MM%.
              %dyel               =XMMM@MM@MM#H;,-+HMM@M+ /MMMX=
              %dyel                 =%@M@M#@$-.=$@MM@@@M; %M%=
              %dyel                   ,:+$+-,/H#MMMMMMM@= =,
              %dyel                         =++%%%%+/:-.

      """

      print(script_colors(choice(_colors),_banner))
      print(script_colors('lgray',_autor))



    def banner_welcome_3():
      _banner = """
                                ────────▓▓▓▓▓▓▓────────────▒▒▒▒▒▒
                                ──────▓▓▒▒▒▒▒▒▒▓▓────────▒▒░░░░░░▒▒
                                ────▓▓▒▒▒▒▒▒▒▒▒▒▒▓▓────▒▒░░░░░░░░░▒▒▒
                                ───▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒░░░░░░░░░░░░░░▒
                                ──▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░▒
                                ──▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░▒
                                ─▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░▒
                                ▓▓▒▒▒▒▒▒░░░░░░░░░░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒
                                ▓▓▒▒▒▒▒▒▀▀▀▀▀███▄▄▒▒▒░░░▄▄▄██▀▀▀▀▀░░░░░░▒
                                ▓▓▒▒▒▒▒▒▒▄▀████▀███▄▒░▄████▀████▄░░░░░░░▒
                                ▓▓▒▒▒▒▒▒█──▀█████▀─▌▒░▐──▀█████▀─█░░░░░░▒
                                ▓▓▒▒▒▒▒▒▒▀▄▄▄▄▄▄▄▄▀▒▒░░▀▄▄▄▄▄▄▄▄▀░░░░░░░▒
                                ─▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░▒
                                ──▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░▒
                                ───▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀▀▀░░░░░░░░░░░░░░▒
                                ────▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░▒▒
                                ─────▓▓▒▒▒▒▒▒▒▒▒▒▄▄▄▄▄▄▄▄▄░░░░░░░░▒▒
                                ──────▓▓▒▒▒▒▒▒▒▄▀▀▀▀▀▀▀▀▀▀▀▄░░░░░▒▒
                                ───────▓▓▒▒▒▒▒▀▒▒▒▒▒▒░░░░░░░▀░░░▒▒
                                ────────▓▓▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒
                                ──────────▓▓▒▒▒▒▒▒▒▒▒░░░░░░░░▒▒
                                ───────────▓▓▒▒▒▒▒▒▒▒░░░░░░░▒▒
                                ─────────────▓▓▒▒▒▒▒▒░░░░░▒▒
                                ───────────────▓▓▒▒▒▒░░░░▒▒
                                ────────────────▓▓▒▒▒░░░▒▒
                                ──────────────────▓▓▒░▒▒
                                ───────────────────▓▒░▒
                                ────────────────────▓▒
      """

      print(script_colors(choice(_colors),_banner))
      print(script_colors('lgray',_autor))


    def banner_welcome_4():
      _banner = """
                                      ────────────────────────────────
                                      ───────────────██████████───────
                                      ──────────────████████████──────
                                      ──────────────██────────██──────
                                      ──────────────██▄▄▄▄▄▄▄▄▄█──────
                                      ──────────────██▀███─███▀█──────
                                      █─────────────▀█────────█▀──────
                                      ██──────────────────█───────────
                                      ─█──────────────██──────────────
                                      █▄────────────████─██──████
                                      ─▄███████████████──██──██████ ──
                                      ────█████████████──██──█████████
                                      ─────────────████──██─█████──███
                                      ──────────────███──██─█████──███
                                      ──────────────███─────█████████
                                      ──────────────██─────████████▀
                                      ────────────────██████████
                                      ────────────────██████████
                                      ─────────────────████████
                                      ──────────────────██████████▄▄
                                      ────────────────────█████████▀
                                      ─────────────────────████──███
                                      ────────────────────▄████▄──██
                                      ────────────────────██████───▀
                                      ────────────────────▀▄▄▄▄▀
      """

      print(script_colors(choice(_colors),_banner))
      print(script_colors('lgray',_autor))



    def banner_welcome_5():
      _banner = """
                        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
                        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
                        ▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒
                        ▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒
                        ▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒
                        ▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░▒▒▒▒▒
                        ▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▌░░▒▒▒▒
                        ▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▄▄███▀░░░░▒▒▒
                        ▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░█████░▄█░░░░▒▒
                        ▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▄████████▀░░░░▒▒
                        ▒▒░░░░░░░░░░░░░░░░░░░░░░░░▄█████████░░░░░░░▒
                        ▒░░░░░░░░░░░░░░░░░░░░░░░░░░▄███████▌░░░░░░░▒
                        ▒░░░░░░░░░░░░░░░░░░░░░░░░▄█████████░░░░░░░░▒
                        ▒░░░░░░░░░░░░░░░░░░░░░▄███████████▌░░░░░░░░▒
                        ▒░░░░░░░░░░░░░░░▄▄▄▄██████████████▌░░░░░░░░▒
                        ▒░░░░░░░░░░░▄▄███████████████████▌░░░░░░░░░▒
                        ▒░░░░░░░░░▄██████████████████████▌░░░░░░░░░▒
                        ▒░░░░░░░░████████████████████████░░░░░░░░░░▒
                        ▒█░░░░░▐██████████▌░▀▀███████████░░░░░░░░░░▒
                        ▐██░░░▄██████████▌░░░░░░░░░▀██▐█▌░░░░░░░░░▒▒
                        ▒██████░█████████░░░░░░░░░░░▐█▐█▌░░░░░░░░░▒▒
                        ▒▒▀▀▀▀░░░██████▀░░░░░░░░░░░░▐█▐█▌░░░░░░░░▒▒▒
                        ▒▒▒▒▒░░░░▐█████▌░░░░░░░░░░░░▐█▐█▌░░░░░░░▒▒▒▒
                        ▒▒▒▒▒▒░░░░███▀██░░░░░░░░░░░░░█░█▌░░░░░░▒▒▒▒▒
                        ▒▒▒▒▒▒▒▒░▐██░░░██░░░░░░░░▄▄████████▄▒▒▒▒▒▒▒▒
                        ▒▒▒▒▒▒▒▒▒██▌░░░░█▄░░░░░░▄███████████████████
                        ▒▒▒▒▒▒▒▒▒▐██▒▒░░░██▄▄███████████████████████
                        ▒▒▒▒▒▒▒▒▒▒▐██▒▒▄████████████████████████████
                        ▒▒▒▒▒▒▒▒▒▒▄▄████████████████████████████████
                        ████████████████████████████████████████████

"""

      print(script_colors(choice(_colors),_banner))
      print(script_colors('lgray',_autor))


    def banner_welcome_6():
      _banner = """
                                      ───────█████████████████████
                                      ────████▀─────────────────▀████
                                      ──███▀───────────────────────▀███
                                      ─██▀───────────────────────────▀██
                                      █▀───────────────────────────────▀█
                                      █─────────────────────────────────█
                                      █─────────────────────────────────█
                                      █─────────────────────────────────█
                                      █───█████─────────────────█████───█
                                      █──██▓▓▓███─────────────███▓▓▓██──█
                                      █──██▓▓▓▓▓██───────────██▓▓▓▓▓██──█
                                      █──██▓▓▓▓▓▓██─────────██▓▓▓▓▓▓██──█
                                      █▄──████▓▓▓▓██───────██▓▓▓▓████──▄█
                                      ▀█▄───▀███▓▓▓██─────██▓▓▓███▀───▄█▀
                                      ──█▄────▀█████▀─────▀█████▀────▄█
                                      ─▄██───────────▄█─█▄───────────██▄
                                      ─███───────────██─██───────────███
                                      ─███───────────────────────────███
                                      ──▀██──██▀██──█──█──█──██▀██──██▀
                                      ───▀████▀─██──█──█──█──██─▀████▀
                                      ────▀██▀──██──█──█──█──██──▀██▀
                                      ──────────██──█──█──█──██
                                      ──────────██──█──█──█──██
                                      ──────────██──█──█──█──██
                                      ──────────██──█──█──█──██
                                      ──────────██──█──█──█──██
                                      ──────────██──█──█──█──██
                                      ──────────██──█──█──█──██
                                      ──────────██──█──█──█──██
                                      ──────────██──█──█──█──██
                                      ──────────██──█──█──█──██
                                      ──────────██──█──█──█──██
                                      ──────────██──█──█──█──██
                                      ───────────█▄▄█▄▄█▄▄█▄▄█

"""

      print(script_colors(choice(_colors),_banner))
      print(script_colors('lgray',_autor))

    def banner_welcome_7():
      _banner = """
                            ░░░░░░░░░░░░░░░░░░░░░░█████████
                            ░░███████░░░░░░░░░░███▒▒▒▒▒▒▒▒███
                            ░░█▒▒▒▒▒▒█░░░░░░░███▒▒▒▒▒▒▒▒▒▒▒▒▒███
                            ░░░█▒▒▒▒▒▒█░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
                            ░░░░█▒▒▒▒▒█░░░██▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒███
                            ░░░░░█▒▒▒█░░░█▒▒▒▒▒▒████▒▒▒▒████▒▒▒▒▒▒██
                            ░░░█████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
                            ░░░█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒██
                            ░██▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██
                            ██▒▒▒███████████▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒██
                            █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒████████▒▒▒▒▒▒▒██
                            ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
                            ░█▒▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
                            ░██▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
                            ░░████████████░░░█████████████████
"""

      print(script_colors(choice(_colors),_banner))
      print(script_colors('lgray',_autor))



    choice([banner_welcome_1, banner_welcome_2, banner_welcome_3, banner_welcome_4, banner_welcome_5, banner_welcome_6, banner_welcome_7])()


