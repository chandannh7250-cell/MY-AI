import io
import sys
import re

def generate_code(prompt):
    p = prompt.lower().strip()
    original = prompt.strip()
    
    # --- CALCULATOR FEATURE ---
    # Agar user ne 5+5, 10*2, 100/4 likha
    # Ya add, plus, minus, multiply likha
    if any(x in p for x in ["+", "-", "*", "/", "plus", "add", "minus", "multiply", "divide", "calculator", "calc"]):
        # Sirf number aur + - * / . ko nikal lo
        expr = re.sub(r'[^0-9+\-*/.() ]', '', original)
        if expr.strip():
            return f"print({expr})"
        return "print('Calculator me number likho jaise: 5+5')"

    if "table of" in p:
        try:
            num = int(p.split("table of")[1].strip())
        except:
            num = 5
        code = f"for i in range(1, 11):\n    print(f'{num} x {{i}} = {{{num}*i}}')"
        return code

    elif "hello" in p:
        return "print('Hello! Kya help chahiye?')"
    
    return "print('Mujhe samajh nahi aaya. Calculator try karo: 5+5')"

def run_code(code):
    buf = io.StringIO()
    old = sys.stdout
    sys.stdout = buf
    try:
        exec(code)
    except Exception as e:
        print(f"Error: {e}")
    sys.stdout = old
    return buf.getvalue()
# Yeh tumne jo sikha hai, usi ka final engine file hai

def tuple_all_codes():
    code = """
#1.print tuple
my_tuple=(10,20,40,56,78,90)
print(my_tuple)

# User se lena hai to tuple bana ke lo
my_tuple_input=input("enter no,=")
print(my_tuple_input)

#2.access tuple
names=("Radha","Rani","Sanvi","Sanya")
print(names[0],names[3],names[1])

names_input=input("enter your name-")
# naam ka pehla aur teesra akshar print hoga
print(names_input[0], names_input[2])

#3.lenth of tuple
lenth=(12,34,567,78,567,'key','poor','rich')
print(len(lenth))

lenth_input=input("enter values=")
print(len(lenth_input))

#4.check an element - YEH TUMHARA MAIN CODE HAI
check=("apple","mango","banana",234,567,678,20,30,50)
if 567 in check:
    print("element found")
else:
    print("element not found")

# Sahi check - String ko number me badal ke check karna
user=input("enter your no.=")
try:
    user_no = int(user)
    if user_no in check:
        print("element found")
    else:
        print("element not found")
except:
    # Agar user ne naam likha jaise apple
    if user in check:
        print("element found")
    else:
        print("element not found")
"""
    return code
def password_code():
    code = '''
password=""
while password != "12345":
  password=input("enter your password=")
  if password != "12345":
    print("not login password")
print("login password")
'''
    return code
# Engine isko aise call karega
def search_code(prompt):
    prompt = prompt.lower()
    if "tuple" in prompt or "element" in prompt or "check" in prompt:
        return tuple_all_codes()
    else:
        return "print('Code not found')"
print(tuple_all_codes())
def search_code(prompt):
    prompt = prompt.lower()
    
    if "password" in prompt or "login" in prompt:
        return password_code(prompt)
    
    if "tuple" in prompt or "element" in prompt or "check" in prompt:
        return tuple_all_codes()
        
    return "print('Code not found')"
    
