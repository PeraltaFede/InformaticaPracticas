from dataclasses import dataclass
from IPython.display import HTML
import random
from IPython.display import clear_output
from hashlib import sha1


@dataclass
class Problem:
  name: str
  pups = [
            "2m78jPG",
            "pn1e9TO",
            "MQCIwzT",
            "udLK6FS",
            "ZNem5o3",
            "DS2IZ6K",
            "aydRUz8",
            "MVUdQYK",
            "kLvno0p",
            "wScLiVz",
            "Z0TII8i",
            "F1SChho",
            "9hRi2jN",
            "lvzRF3W",
            "fqHxOGI",
            "1xeUYme",
            "6tVqKyM",
            "CCxZ6Wr",
            "lMW0OPQ",
            "wHVpHVG",
            "Wj2PGRl",
            "HlaTE8H",
            "k5jALH0",
            "3V37Hqr",
            "Eq2uMTA",
            "Vy9JShx",
            "g9I2ZmK",
            "Nu4RH7f",
            "sWp0Dqd",
            "bRKfspn",
            "qawCMl5",
            "2F6j2B4",
            "fiJxCVA",
            "pCAIlxD",
            "zJx2skh",
            "2Gdl1u7",
            "aJJAY4c",
            "ros6RLC",
            "DKLBJh7",
            "eyxH0Wc",
            "rJEkEw4"]
  results = [
      "1b6453892473a467d07372d45eb05abc2031647a",
      "356a192b7913b04c54574d18c28d46e6395428ab",
      "da4b9237bacccdf19c0760cab7aec4a8359010b0",
      "b6589fc6ab0dc82cf12099d1c2d40ab994e8410c",
      "356a192b7913b04c54574d18c28d46e6395428ab",
      "356a192b7913b04c54574d18c28d46e6395428ab",
      "da4b9237bacccdf19c0760cab7aec4a8359010b0",
      "fe16aeba67707eb00791df7e1e416aaf590a4891",
  ]
  frset = frozenset(['A', 'B', 'C', 'D', '*', '!', ' ', '+'])
  errset = frozenset(['A', 'B', 'C', 'D'])
  
  def validate(self, no_problem, *args, **kwargs):
    if no_problem == 1:
      try:
        ent1 = int(args[0])
        ent2 = int(args[1])
      except Exception:
        clear_output()
        print("CUIDADO: Las entradas y salidas deben ser enteros naturales")
        return False
      return True
    elif no_problem == 2:
      try:
        ent1 = int(args[0])
        ent2 = int(args[1])
        ent1 = int(args[2])
        ent2 = int(args[3])
        ent2 = int(args[4])
      except Exception:
        clear_output()
        print("CUIDADO: Las entradas y salidas deben ser enteros naturales")
        return False
      return True
    elif no_problem == 3:
      return True
    elif no_problem == 4:
      try:
        full_str = args[0]
        if not set(full_str) <= self.frset:
          raise ValueError("check string")
        pre_cha = full_str[0]
        for cha in full_str[1:]:
          if set(pre_cha) <= self.errset and (set(cha) <= self.errset or cha== '!'):
            raise ValueError("check string")
          else:
            pre_cha = cha

      except Exception:
        clear_output()
        print("CUIDADO: La función puede tener solo A, B, C, D, *, !, + \n"
              "Debe asegurarse que al usar AND utilice el asterisco *\n"
              "Ej.: \U0000274C AB"
              "     \U00002705 A*B")
        return False
      return True
    else:
      return False
  
  def check(self, no_problem, *args, **kwargs):
    if not self.validate(no_problem, *args, **kwargs):
      return
    if no_problem == 1:
      h0 = sha1(str(args[0]).encode("utf-8")).hexdigest()
      h1 = sha1(str(args[1]).encode("utf-8")).hexdigest()
      if h1 == self.results[1] and h0 == self.results[0]:
        print("\U0001f973 \U0001f973 Enhorabuena ! \U0001f973 \U0001f973 \n")
        return HTML("""
        <video alt="test" controls autoplay=1>
        <source src="https://openpuppies.com/mp4/%s.mp4"  type="video/mp4">
        </video>
        """%(random.sample(self.pups, 1)[0]))
      else:
        clear_output()
        print("Fijese de nuevo en la imagen. La entrada y salidas son otras.")
    elif no_problem == 2:
      h0 = sha1(str(args[0]).encode("utf-8")).hexdigest()
      h1 = sha1(str(args[1]).encode("utf-8")).hexdigest()
      h2 = sha1(str(args[2]).encode("utf-8")).hexdigest()
      h3 = sha1(str(args[3]).encode("utf-8")).hexdigest()
      h4 = sha1(str(args[4]).encode("utf-8")).hexdigest()
      if h0 == self.results[2] and h1 == self.results[3] and h2 == self.results[4] and h3 == self.results[5]and h4 == self.results[6]:
        print(f"\U0001f973 \U0001f973 Enhorabuena {name}! \U0001f973 \U0001f973 \n")
        return HTML("""
        <video alt="test" controls autoplay=1>
        <source src="https://openpuppies.com/mp4/%s.mp4"  type="video/mp4">
        </video>
        """%(random.sample(self.pups, 1)[0]))
      else:
        clear_output()
        print("Fijese de nuevo en la imagen. Las cantidades de compuertas son otras.")
    elif no_problem == 3:
      res_str = ''.join(str(e) for e in args[0])
      h0 = sha1(res_str.encode("utf-8")).hexdigest()
      if h0 == self.results[7]:
        print(f"\U0001f973 \U0001f973 Enhorabuena {name}! \U0001f973 \U0001f973 \n")
        return HTML("""
        <video alt="test" controls autoplay=1>
        <source src="https://openpuppies.com/mp4/%s.mp4"  type="video/mp4">
        </video>
        """%(random.sample(self.pups, 1)[0]))
      else:
        # clear_output()
        print("La tabla de verdad no es la correcta.")
    elif no_problem == 4:
      numbers = []
      results = []
      for i in range(16):
        DCBA = format(i, '#06b')[2:]
        res = eval(args[0].upper().replace('*', ' and ').replace('+', ' or ')
        .replace('!', 'not ').replace('A', DCBA[3])
        .replace('B', DCBA[2]).replace('C', DCBA[1])
        .replace('D', DCBA[0]))
        if res == 1:
          results.append(1)
        else:
          results.append(0)
      
      res_str = ''.join(str(e) for e in results)
      h0 = sha1(res_str.encode("utf-8")).hexdigest()
      if h0 == self.results[7]:
        print(f"\U0001f973 \U0001f973 Enhorabuena {name}! \U0001f973 \U0001f973 \n")
        return HTML("""
        <video alt="test" controls autoplay=1>
        <source src="https://openpuppies.com/mp4/%s.mp4"  type="video/mp4">
        </video>
        """%(random.sample(self.pups, 1)[0]))
      else:
        # clear_output()
        print("La funcion no es la correcta.")
        
