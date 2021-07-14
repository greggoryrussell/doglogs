# Dog Logs

A simple script for tracking one's dog's "business" throughout the day. User chooses if the "business" looks **Normal** or **Concerning** and logs it to a CSV with a date and timestamp. There is also optional comments that will be recorded into the CSV file if specified.

## Menu

To launch the doglogs shell type:

```
./doglogs.py
```

### Menu prompt commands

The following commands work in the prompt:
1. `"q"` = **Quit the Program**
2. `"?"` = **Print Help Menu**
3. `"v"` = **Print Shell Version**
4. `"d"` = **Print Current Date**
5. `"p"` = **Poo Recording Mode**


#### Example Ouput
```
##############################
Dog Logs Shell version: 1.0
Type '?' for the help menu.
Input Command: > p
Input was "p"
Poop Mode Selected
(N)ormal?
(C)oncerning?
Type the First Letter to make your choice: c
You chose: Concerning
Optional Comment? Yikes! Call the vet??
Input Command: > p
Input was "p"
Poop Mode Selected
(N)ormal?
(C)oncerning?
Type the First Letter to make your choice: n
You chose: Normal
Optional Comment? 
Input Command: > q
Input was "q"
Quitting program!
```

The CSV file looks like like:
```
Date,Timestamp,Status,Optional Comment
7/13/2021,09:32:18,Normal,
7/13/2021,11:45:44,Normal,
7/13/2021,14:15:00,Concerning,Is that stuffing from her toy??
7/13/2021,16:08:21,Concerning,Yikes! Call a vet?
7/13/2021,18:35:39,Normal,Vet said this is good and nothing to worry about
7/14/2021,11:10:47,Normal,
7/14/2021,12:30:21,Concerning,Yikes!
7/14/2021,15:45:14,Normal,
```
