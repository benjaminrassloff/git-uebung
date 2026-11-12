def mask_email(email):
    name, domain = email.split("@")
    return name[0] + "***@" + domain

def mask_iban(iban):
    masked = iban[:4] + "*" * (len(iban) - 6) + iban[-2:]
    return masked

def mask_phone(phone):
    masked = phone[:3] + "*" * (len(phone) - 3) + phone[-3:]
    return masked