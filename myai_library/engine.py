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
