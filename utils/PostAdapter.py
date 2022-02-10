class PostAdapter:

    @staticmethod
    def makePost(notification):
        outputString = f"{notification.package_name}:\n"
        outputString += f"{notification.text}\n"

        return outputString
