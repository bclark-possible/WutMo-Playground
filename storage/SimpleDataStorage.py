from abc import ABC, abstractmethod

class SimpleDataStorage(ABC):
    def set(self, key, value):
        pass
    
    def get(self, key):
        pass