def dev_help(file_location, description):
    print(f"""
***********************************************************************************************************************

 """)

    print(f"{file_location} ------ {description }")


    print(f"""

***********************************************************************************************************************

""")
    while True:
        confirm = input("YES/NO>>>")
        if confirm.lower() == "yes":
            break
        else:
            pass