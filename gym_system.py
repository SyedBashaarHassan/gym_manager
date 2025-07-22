import json
from member import Member

class GymSystem:
    def __init__(self, data_file="data.json"):
        self.members = {}
        self.data_file = data_file
        self.load_data()

    def load_data(self):
        try:
            with open(self.data_file, 'r') as file:
                data = json.load(file)
                for m in data.values():
                    member = Member.from_dict(m)
                    self.members[member.member_id] = member
        except:
            self.members = {}

    def save_data(self):
        with open(self.data_file, 'w') as file:
            data = {m.member_id: m.to_dict() for m in self.members.values()}
            json.dump(data, file, indent=4)

    def add_member(self, member_id, name, age, gender, phone):
        if member_id in self.members:
            return False
        member = Member(member_id, name, int(age), gender, phone)
        self.members[member_id] = member
        self.save_data()
        return True

    def get_all_members(self):
        members_list = list(self.members.values())
        print(members_list)  # 
        return members_list


        
    def add_payment(self, member_id, amount):
        member = self.members.get(member_id)
        if member:
            member.add_payment(amount)

    def delete_member(self, member_id):
    if member_id in self.members:
        del self.members[member_id]
        self.save_data()
        return True
    return False

            self.save_data()
            return True
        return False


