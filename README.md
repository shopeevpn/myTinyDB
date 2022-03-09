# TinyDB 🗃️

> ***Simple database using the **tinyDB** module***

## Setup
***Install the tinydb module*** 

```
pip install tinydb
```
create file **db_location** containing the location to create the json file at the root of the *repo*

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
