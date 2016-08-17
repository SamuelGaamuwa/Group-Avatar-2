class PrimeChecker(object):
  
  def __init__(self, number = None):
    if number is None:
      return None
    else:
      self.number = number
 def print_funtions(self):
    print("these things happen")
    
  def is_prime(self):
    try:
        num = int(self.number)
        for i in range(2,num):
          if((num%i) == 0):
            return False
            break
          else:
            if(i == num - 1):
              return True
    except ValueError:
        return False
    
   