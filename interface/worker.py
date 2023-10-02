from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Any

@dataclass
class IWorker(ABC):
    options: Any

    @abstractmethod
    def run(self):
        """Actual worker code"""
        pass
