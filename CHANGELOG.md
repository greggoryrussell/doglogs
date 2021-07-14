# Changelog for Version: '1.0'
## 7/14/2021
- Added error handling for wrong status choice


# Changelog for Version: 'rat-cakes'
## 12/28/2020
- Added CSV Writer. 
- Added menu option '`d`' for date and time.
    - They print the `return_current_time` and `return_date_string` functions which return strings.
- Added a version printing command and function to the menu '`v`'
- Version is now `self.version`, a class variable.
- Added 30 `#` character shell border when the program first launches. 

# Changelog for Version: 'raw-burger'
## 12/28/2020
- Gone is the naked while loop sitting outside of main.
- The menu itself is now a Class called `PromptMenu`
- The boolean `self.keep_prompting` is set to **True** when the program is started.
    - As long as the boolean is true the menu will keep prompting the user for inputs
    - This makes quitting the program easier from a programming standpoint as the `check_input` function simply changes `self.keep_prompting` to **False** when *'q'* is detected as the input.
- `help_menu()` simply iterates through the class variable's `menu_items` rather than a separate class variable. This is a much simpler way of how I used to write these things in the past.