from dataclasses import dataclass


@dataclass
class Direction:
    def __init__(self, package_name, text):
        self.text = text
        self.packageName = package_name
