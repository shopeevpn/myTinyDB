# TinyDB 🗃️

> ***Simple password generator and database that uses the **tinyDB** module***

## Setup

***Clone the repo***
```sh
git clone https://github.com/musaubrian/tinydb
```

***Install the tinydb module*** 

```sh
windows
pip install -r requirements.txt

linux
pip3 install -r requirements.txt
```
Add location of the database in the **db_location** file

### Commands
1. Add >> **a**
2. Search >> **s**
3. Delete >> **d**
4. Show_all >> **sh**

## 1. Adding user and related content
Sites are added without the extension
**example:**
- github.com ❌
- github or Github ✔
    
Enter **a** to the prompt
``` 
***********************************************

                  TinyDB🗃️
➕ Add / 🔍 Search / ❌ Delete / 👀 Show-all
              (𝗮 / 𝘀 / 𝗱 / 𝘀𝗵)

***********************************************

~$ a
```


It will prompt you to select whether you want to insert **mutliple inputs`m`** or just a single **input `s`**
``` 
***********************************************

                  TinyDB🗃️
➕ Add / 🔍 Search / ❌ Delete / 👀 Show-all
              (𝗮 / 𝘀 / 𝗱 / 𝘀𝗵)

***********************************************

~$ a
Multpile or Single input(m/s)
~$
```

It exits automatically

## 2. Searching for user and related information
> Currently ony searches by *site name*

Input `s` into the prompt to enter search mode.


Enter **sitename**
``` 
***********************************************

                  TinyDB🗃️
➕ Add / 🔍 Search / ❌ Delete / 👀 Show-all
              (𝗮 / 𝘀 / 𝗱 / 𝘀𝗵)

***********************************************

~$ s
**************************************
🔍Searches for Sites and related info
**************************************
Enter sitename: example

```

## 3. Delete user and related content

Enter **d** to enter delete mode

Enter user to delete 

``` 
***********************************************

                  TinyDB🗃️
➕ Add / 🔍 Search / ❌ Delete / 👀 Show-all
              (𝗮 / 𝘀 / 𝗱 / 𝘀𝗵)

***********************************************

~$ d
*********************************
Deletes user and related info 💀
*********************************
Enter username: testUser
```

## 4.Show-all users and related information
Shows all the user
Input `sh`
``` 
***********************************************

                  TinyDB🗃️
➕ Add / 🔍 Search / ❌ Delete / 👀 Show-all
              (𝗮 / 𝘀 / 𝗱 / 𝘀𝗵)

***********************************************

~$ sh

```
