<a href="#russian">Russian version</a> | <a href="#english">English version</a>

<hr id="russian">

### ИЕРАРХИЯ ЭЛЕМЕНТОВ ПРОГРАММЫ

* COMport  
* окно программы  
	\- расположить области()

	* область новой команды    // наследует от 'область команды'  
		\- сохранить()  
		\* кнопка сохранить  

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
	\* поле ввода команды


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
		\* command name

	* connection parameters frame  
		\- connect()  
		\- disconnect()  
		\- read parameters()  
		\* connect button  
		\* disconnect button  
		\* port number  
		\* baudrate


* command frame  // parent class  
	\- send()  
	\- trim command()  
	\* send button  
	\* command  
	\* command entry

---
