import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token=access_token
    
    def upload_file(self, file_from, file_to):
        dbx=dropbox.Dropbox(self.access_token)
        with open(file_from,"rb")as f:
            dbx.files_upload(f.read(), file_to)
    
def main():
    access_token="sl.BEw6zWtXh0jmIG7d8npmuNFEbA6GBBoZNAkGPY2jgmTzlu37ebDg5Oj7pbdlcP0odli3Bm1TYGX-9aunnR3-x4g6riKRrOaptSrr0a07GpcNl8BW4KUsQmgwLwN1jMRvF6i2I3S6Q2A"
    file_from="test1.txt"
    file_to="/Project for C-102/test.txt"
    transfer_data=TransferData(access_token)
    transfer_data.upload_file(file_from, file_to)

if __name__=="__main__":
    main()