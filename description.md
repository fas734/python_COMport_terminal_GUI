<a href="#russian">Russian version</a> | <a href="#english">English version</a>

<hr id="russian">

### ИЕРАРХИЯ ЭЛЕМЕНТОВ ПРОГРАММЫ

* COMport  
* окно программы  
	\- расположить области()

	* область новой команды    // наследует от 'область команды'  
		\- сохранить()  
		\* кнопка сохранить  
		\* поле ввода команды

	* область сохранённых команд    // наследует от 'область команды'  
		\- поменять имя()  
		\- удалить()  
		\* кнопка удалить  
		\* название команды

	* область параметров подключения  
		\- подключиться()  
		\- отключиться()  
		\- считать параметры()  
		\* кнопка подключиться  
		\* кнопка отключиться  
		\* номер порта  
		\* скорость соединения


* область команды  // родительский класс  
	\- отправить()  
	\- очистить команду от мусора()  
	\* кнопка отправить  
	\* поле команды


<hr id="english">


### HIERARCHY OF PROGRAM ELEMENTS

* COMport  
* program window  
	\- place regions in window()

	* new command frame    // inherits by 'command frame'  
		\- save()  
		\* save button

	* saved command frame    // inherits by 'command frame'  
		\- change label()  
		\- delete()  
		\* delete button

	* connection parameters frame  
		\- connect()  
		\- disconnect()  
		\- read parameters()  
		\* port number  
		\* baudrate


* command frame  // parent class  
	\- send()  
	\- trim command()  
	\* send button  
	\* command

---
