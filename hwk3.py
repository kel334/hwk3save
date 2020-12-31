# Kendra Ludwig (kel334@nau.edu)


# !!WARNING!! !!WARNING!! !!WARNING!! !!WARNING!! !!WARNING!! !!WARNING!!
# You should not use the print() or input() functions anywhere in this file!
# !!WARNING!! !!WARNING!! !!WARNING!! !!WARNING!! !!WARNING!! !!WARNING!!


# Function 1: Same First Digit
def same_first_digit(x, y, z):
    first = str(x)[0]
    second = str(y)[0]
    third = str(z)[0]
    if first == second and second == third:
        return True
    else:
        return False


# Function 2: String Reversal
def reverse(to_reverse):
    return to_reverse[::-1]


# Function 3: Palindrome Detection
def is_palindrome(word):
    word = word.replace(',', '')
    word = word.replace("'", '')
    word = word.replace(" ", '')
    word = word.lower()
    reverse_word = word[::-1]
    if word == reverse_word:
        return True
    else:
        return False


# Function 4: String to ASCII Codes
def str_to_ascii(char):
    x = [ord(i) for i in char]
    return x


# Function 5: Get Piece Value
def get_piece_value(chess_piece):
    chess_piece = chess_piece.lower()
    piece_value_dict = {"pawn": 1,
                        "bishop": 3,
                        "knight": 3,
                        "rook": 5,
                        "queen": 9
                        }
    return piece_value_dict.get(chess_piece)


# Function 6: Formatting Dates
def format_date(yyyymmdd):
    stringVer = str(yyyymmdd)
    year = stringVer[0:4]
    mon = stringVer[4:6]
    d = stringVer[6:9]
    day = str(int(d))
    month_dict = {'01': 'January',
                  '02': 'February',
                  '03': 'March',
                  '04': 'April',
                  '05': 'May',
                  '06': 'June',
                  '07': 'July',
                  '08': 'August',
                  '09': 'September',
                  '10': 'October',
                  '11': 'November',
                  '12': 'December'
                  }

    month = month_dict.get(mon, 'None')
    full_date_dict = {'1': '1st',
                      '2': '2nd',
                      '3': '3rd',
                      '4': '4th',
                      '5': '5th',
                      '6': '6th',
                      '7': '7th',
                      '8': '8th',
                      '9': '9th',
                      '10': '10th',
                      '11': '11th',
                      '12': '12th',
                      '13': '13th',
                      '14': '14th',
                      '15': '15th',
                      '16': '16th',
                      '17': '17th',
                      '18': '18th',
                      '19': '19th',
                      '20': '20th',
                      '21': '21st',
                      '22': '22nd',
                      '23': '23rd',
                      '24': '24th',
                      '25': '25th',
                      '26': '26th',
                      '27': '27th',
                      '28': '28th',
                      '29': '29th',
                      '30': '30th',
                      '31': '31st'
                      }

    short_date_dict = {'1': '1st',
                       '2': '2nd',
                       '3': '3rd',
                       '4': '4th',
                       '5': '5th',
                       '6': '6th',
                       '7': '7th',
                       '8': '8th',
                       '9': '9th',
                       '10': '10th',
                       '11': '11th',
                       '12': '12th',
                       '13': '13th',
                       '14': '14th',
                       '15': '15th',
                       '16': '16th',
                       '17': '17th',
                       '18': '18th',
                       '19': '19th',
                       '20': '20th',
                       '21': '21st',
                       '22': '22nd',
                       '23': '23rd',
                       '24': '24th',
                       '25': '25th',
                       '26': '26th',
                       '27': '27th',
                       '28': '28th',
                       '29': '29th',
                       '30': '30th'
                       }

    leap_date_dict = {'1': '1st',
                      '2': '2nd',
                      '3': '3rd',
                      '4': '4th',
                      '5': '5th',
                      '6': '6th',
                      '7': '7th',
                      '8': '8th',
                      '9': '9th',
                      '10': '10th',
                      '11': '11th',
                      '12': '12th',
                      '13': '13th',
                      '14': '14th',
                      '15': '15th',
                      '16': '16th',
                      '17': '17th',
                      '18': '18th',
                      '19': '19th',
                      '20': '20th',
                      '21': '21st',
                      '22': '22nd',
                      '23': '23rd',
                      '24': '24th',
                      '25': '25th',
                      '26': '26th',
                      '27': '27th',
                      '28': '28th',
                      '29': '29th'
                      }

    feb_date_dict = {'1': '1st',
                     '2': '2nd',
                     '3': '3rd',
                     '4': '4th',
                     '5': '5th',
                     '6': '6th',
                     '7': '7th',
                     '8': '8th',
                     '9': '9th',
                     '10': '10th',
                     '11': '11th',
                     '12': '12th',
                     '13': '13th',
                     '14': '14th',
                     '15': '15th',
                     '16': '16th',
                     '17': '17th',
                     '18': '18th',
                     '19': '19th',
                     '20': '20th',
                     '21': '21st',
                     '22': '22nd',
                     '23': '23rd',
                     '24': '24th',
                     '25': '25th',
                     '26': '26th',
                     '27': '27th',
                     '28': '28th'
                     }

    if month == "February":
        if int(year) % 4 == 0:
            date = leap_date_dict.get(day, 'None')
        else:
            date = feb_date_dict.get(day, 'None')
    elif month == 'April' or 'June' or 'September' or 'November':
        date = short_date_dict.get(day, 'None')
    else:
        date = full_date_dict.get(day, 'None')

    if date == 'None':
        return None

    formatted = str(month + " " + date + "," + " " + year)
    return formatted
