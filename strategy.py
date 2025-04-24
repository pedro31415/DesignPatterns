
from abc import ABC, abstractmethod

class PasswordStrategy(ABC):
    @abstractmethod
    def generate(self):
        pass

class AlphaPasswordStrategy(PasswordStrategy):
    def generate(self):
        return "apapspwdowod"
    
class NumericPasswordStrategy(PasswordStrategy):
    def generate(self):
        return "122434"

class DefaultPasswordStrategy(PasswordStrategy):
    def generate(self):
        return "password"
    
class PasswordGenerator():

    def generate_password(self, password_gen: PasswordStrategy):
        return password_gen.generate()

if __name__ == "__main__":
    pg = PasswordGenerator()
    password = pg.generate_password(NumericPasswordStrategy())
    print(password)