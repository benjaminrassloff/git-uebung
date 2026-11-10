def mask_email(email):
    name, domain = email.split("@")
    return name[0] + "***@" + domain