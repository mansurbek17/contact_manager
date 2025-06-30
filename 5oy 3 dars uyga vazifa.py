import time


def log_dec(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"ketgan vaqti: {end - start} ")

    return wrapper


class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def get_info(self):
        return f" Ism: {self.name}   Telefon raqami: {self.phone}"


class ContactManager:
    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.contacts = []

    def get_owner_info(self):
        return f"Kontakt menejeri: {self.owner_name}"

    def show_all_contacts(self):
        if not self.contacts:
            print(" Kontaktlar yo‘q")
        else:
            print("                    |Kontaktlar ro‘yxati|")
            for i, c in enumerate(self.contacts, 1):
                print(f"{i}. {c.get_info()}")

    @log_dec
    def add_contact(self, name, phone):
        contact = Contact(name, phone)
        self.contacts.append(contact)
        print(f"Kontakt qo‘shildi: {name}")

    def add_ready_contact(self, contact_obj):
        self.contacts.append(contact_obj)

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"{name} o‘chirildi")
                return
        print(f" {name} topilmadi")


manager = ContactManager("Mansurbekning  kontaktlari")

a1 = Contact("ali ", '942873399')
a2 = Contact("avaz akam ", '939561703')
a3 = Contact("rixsitilla ", '500059343')
a4 = Contact("anvar akam  ", '943040615')
a5 = Contact("mansurbek ", '940463606')
a6 = Contact("mansurbek2 ", '770008824')
a7 = Contact("javohir", '931973325')
a8 = Contact("Malika", "+998933335555")
a9 = Contact("Jasur", "+998991112233")
a10 = Contact("Sevara", "+998909988877")

manager.add_ready_contact(a1)
manager.add_ready_contact(a2)
manager.add_ready_contact(a3)
manager.add_ready_contact(a4)
manager.add_ready_contact(a5)
manager.add_ready_contact(a6)
manager.add_ready_contact(a7)
manager.add_ready_contact(a8)
manager.add_ready_contact(a9)
manager.add_ready_contact(a10)

while True:
    print("                                                   | Kontakt Menejeri |")
    a = input('1-Barcha kontaktlar | 2-Kontakt qo‘shish | 3-Kontakt o‘chirish | 4-Menejer haqida | 0-Chiqish: ')

    if a == '1':
        manager.show_all_contacts()
    elif a == '2':
        ism = input("Ism: ")
        tel = input("Telefon: ")
        manager.add_contact(ism, tel)
    elif a == '3':
        ism = input("O‘chiriladigan kontakt ismi: ")
        manager.delete_contact(ism)
    elif a == '4':
        print(manager.get_owner_info())
    elif a == '0':
        print(" Chiqildi.")
        break
    else:
        print("Siz adashdingiz, qaytadan urinib koring")
