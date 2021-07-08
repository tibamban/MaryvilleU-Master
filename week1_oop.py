class Teams:
  def __init__(self, members):
    self.__myTeam = members

  def __len__(self):
    return len(self.__myTeam)
  
  # 3)
  
  def __contains__(self,other_members):
    return (other_members) in (self.__myTeam)
  
  def __iter__(self):
    for element in (self.__myTeam):
      print(element)
  #4)Explain the difference between interfaces and implementation.
      """
        the difference between interfaces and implementation is that the interface is what the user deal with and that can affect him.
         while implementation is everything that is happening behind the scene and that the user doesn't need to know but he is using,
         a good example will be on a car , the steering wheel , the pads and such will be the interface part , but transmission , engine and must of the technicalities are part of the implementation .
      """
        
def main():
  classmates = Teams(['John', 'Steve', 'Tim',"jr"])
  print (len(classmates))
  # 2 -b
  print("jr" in classmates)
  # question 3
  print(hasattr(classmates, '__len__'))
  # 2-a
  print(iter(classmates))
main()
