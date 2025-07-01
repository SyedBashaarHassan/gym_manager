import datetime

class Member:
    def __init__(self, member_id, name, age, gender, phone, join_date=None, payments=None):
        self.member_id = member_id
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.join_date = join_date or str(datetime.date.today())
        self.payments = payments or []

    def add_payment(self, amount):
        payment = {
            "amount": amount,
            "date": str(datetime.date.today())
        }
        self.payments.append(payment)

    def total_paid(self):
        return sum(p['amount'] for p in self.payments)

    def to_dict(self):
        return {
            "member_id": self.member_id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "phone": self.phone,
            "join_date": self.join_date,
            "payments": self.payments
        }

    @staticmethod
    def from_dict(data):
        return Member(
            data["member_id"],
            data["name"],
            data["age"],
            data["gender"],
            data["phone"],
            data.get("join_date"),
            data.get("payments", [])
        )
