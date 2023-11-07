

class Actual_Customer():
    def __init__(self):
        self.LoginOrNot = False
        self.Email = ""
        self.Password = ""
        self.FirstName = ""
        self.LastName = ""
        self.UserName = ""
        self.Phone = 0
        self.AdminOrNot = False

    def Complete_Accept(self):
        if (self.Email != "") & (self.Password != "") & (self.FirstName != "") & (self.LastName != "") & (self.UserName != "") & (self.Phone != 0):
            return True
        else:
            return False
    
    def Copy_To_Actual_Customer(self, result):
        self.LogOrNot = True
        self.Email = result[0]['Email']
        self.Password = result[0]['Password']
        self.FirstName = result[0]['FirstName']
        self.LastName = result[0]['LastName']
        self.UserName = result[0]['UserName']
        self.Phone = result[0]['Phone']
        self.AdminOrNot = result[0]['AdminOrNot']