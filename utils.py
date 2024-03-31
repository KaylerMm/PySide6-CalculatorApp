def valid_input(string: str):
        try:
            float(string)
            return True
        except ValueError:
            return False
        
def is_special_key(key: str):
    if key not in '0123456789.':
          return True
    return False

def is_empty(string: str):
     if len(string) == 0:
          return True
     return False