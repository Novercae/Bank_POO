class Bank:
    def __init__(self):
        self.branch = [1234, 2222, 4242]  # bank branch number
        self.custumers = []
        self.accounts = []

    def insert_client(self, client):
        self.custumers.append(client)

    def insert_account(self, account):
        self.accounts.append(account)

    def check(self, client):    # check if it exists
        if client not in self.custumers:
            return None

        if client.account not in self.accounts:
            return False

        if client.account.agency not in self.branch:
            return False

        return True
