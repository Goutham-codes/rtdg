# Usage

## Running CLI

```sh
python source/cli.py
```

![](https://github.com/Goutham-codes/rtdg/blob/master/docs/img/cli.PNG)

---

### Args

* positional args
  * fields - total no of fields
  * total - total no of records to be generated
  * filename - file path of the csv file
* optional arguments
  * help
  * verbose

## Running GUI
```sh
python source/gui.py
```

![](https://github.com/Goutham-codes/rtdg/blob/master/docs/img/interface.PNG)

---

### Widgets in interface

The Add Field button is to add the required field.   
Add Field requires three inputs  
* field name
* domain type
* subdomain type

Delete button intends to delete a field completely.  
Delete field requires the id of the field to remove it.  

Choose File button is to choose the required file to which the data should be saved.  
A dialog box appears and user choose the file to be saved.  

Save to file button saves the datas successfully.
