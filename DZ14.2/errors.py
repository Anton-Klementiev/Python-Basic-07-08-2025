class Error(Exception):
    def __init__(self, message="У групі не може бути більше 10 студентів."):
        Exception.__init__(self,message)