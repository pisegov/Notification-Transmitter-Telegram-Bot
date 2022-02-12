from dataclasses import dataclass


@dataclass
class Notification:
    def __init__(self, package_name, text):
        self.text = text
        self.package_name = package_name
