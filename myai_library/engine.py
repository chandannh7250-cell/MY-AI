import io
import sys

def generate_code(prompt):
    prompt = prompt.lower().strip()
    
    if "table of" in prompt:
        try:
            num = int(prompt.split("table of")[1].strip())
        except:
            num = 5
        code = f"for i in range(1, 11):\n    print(f'{num} x {{i}} = {{{num}*i}}')"
        return code

    elif "hello" in prompt:
        return "print('Hello! Kya help chahiye?')"
    
    return "print('Mujhe samajh nahi aaya')"

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
