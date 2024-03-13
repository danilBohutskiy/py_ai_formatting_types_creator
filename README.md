# AI Character Creator

## Description

This project is a simple graphical application designed to facilitate the creation of character descriptions. It provides users with the ability to format descriptions in various styles, including:

- W++ Format
- Boostyle
- Bracketed List

After installing the required dependencies, users can run the application by executing the `main.py` file. This will launch the graphical interface, allowing users to input character details and format them according to their chosen style.

## Installation

To install the required dependencies, please run:

```bash
pip install -r requirements.txt
```

## Usage

After installing the required dependencies, you can run the application by executing the `main.py` file. 

```bash
python3 main.py
```
or
```bash
python main.py
```

## Usage example

To use the application, follow these steps:

1. Run the program by executing the `main.py` file.
2. Enter the character's name.
3. Optionally, choose a template (this will automatically populate fields).
4. Fill in the fields. Fields should be in the format "field: value1, value2, value3..." (separated by commas).
5. Select the desired formatting style from the dropdown list.
6. Click the "Generate" button.
7. Use the generated text to create your character.

## Example
Input:
```
Nickname: Merlin Wizard
Age:  25
Features: famous wizard, skilled + powerful, 
```
Output:
```
[
{
Name("Wizard Merlin")
Nickname("Merlin Wizard")
Age("25")
Features("famous wizard"+"skilled + powerful")
}]
```

## More details
1. [W++ For Dummies By Kuma](https://rentry.co/WPP_For_Dummies)
2. [Advanced Character Creator Guide](https://yodayo.notion.site/Advanced-Character-Creator-Guide-ff2f71e2576544d68bd295195a84d8e4)
