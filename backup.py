import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A_4NCSh6xHo2Mzte3eP8YIpE0CE7FIQWJEEh3kfh5__tTgf1dfAiI_-f57cB6V9ajuapVv4GkfsxAy-U2nX9EV3o1Kh6Hev3xMBgFQmGVvAuHUIKbqIoEE_-Zywfw3OVurrsmUY'
    transferData = TransferData(access_token)

    file_from = input("Enter file path to be uploaded ")
    file_to = input("Enter full destination path to be uploaded to ")

    # API v2
    transferData.upload_file(file_from, file_to)
    print("The file has been backed up succesfully")
main()