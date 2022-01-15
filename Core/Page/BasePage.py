from abc import ABC, abstractmethod

class BasePage(ABC):
    
    @property
    @classmethod
    @abstractmethod
    def session_state(cls):
        return NotImplementedError
        
    @abstractmethod
    def architecture(self):
        pass
