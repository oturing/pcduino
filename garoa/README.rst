============
Notas
============

---------------------
Sistema pre-instalado
---------------------

PCduino veio com algo parecido com o Lubuntu 12.07. Veja o resultado de 
``lsb_release -a`` ::

	$ lsb_release -a
	No LSB modules are available.
	Distributor ID:	Linaro
	Description:	Linaro 12.07
	Release:	12.07
	Codename:	precise

Este comando e' o mais recomendado para identificar a versao das
distribuicoes GNU/Linux derivadas de Debian, como Ubuntu, Lubuntu etc.

Linaro e' uma organizacao que porta pacotes Linux para CPUs ARM.

--------------------
Python pre-instalado
--------------------

Python 2.7.3 de 32 bits veio instalado. Instalei o pacote ``python-tk`` 
e conferi que o Tkinter funciona rodando o script ``garoa/relogio.py``.

----------------------------------------------
Instalacao de pacotes do GNU/Linux
----------------------------------------------

Para instalar pacotes, use o comando ``sudo apt-get install X`` onde X 
e' o nome do pacote.

Por exemplo, para instalar o tree::

	$ sudo apt-get install tree

No primeiro dia de uso do PCDuino, instalei::

- openssh-client (cliente para conexao ssh)
- scrot (capturador de tela acionado via tecla PrintScreen)
- git (controle de versao de codigo)
- tree (visualizacao de uma arvore de diretorios no console)
- geany (editor para programacao)
- python-tk (biblioteca grafica Tkinter para o Python 2.7.3)
