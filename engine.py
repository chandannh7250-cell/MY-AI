import re

def search_code(user_input):
    return f"# Code for: {user_input}\nprint('Hello from MY AI')"

def generate_code(user_input):
    """Khud se code banane wala function"""
    prompt = user_input.lower()

    # 1. Agar user ne 'add' bola
    if "add" in prompt or "plus" in prompt or "jod" in prompt:
        # Number nikal lo
        numbers = re.findall(r'\d+', prompt)
        if len(numbers) >= 2:
            a, b = numbers[0], numbers[1]
            return f"print({a} + {b})  # Result: {int(a)+int(b)}"
        else:
            return "a = int(input('Pehla number: '))\nb = int(input('Dusra number: '))\nprint(a + b)"

    # 2. Agar 'hello' bola
    if "hello" in prompt or "print" in prompt:
        return "print('Hello World')"

    # 3. Agar 'loop' bola
    if "loop" in prompt:
        return "for i in range(5):\n    print(i)"

    # 4. Agar 'table' bola
    if "table" in prompt:
        numbers = re.findall(r'\d+', prompt)
        if numbers:
            n = int(numbers[0])
            return f"for i in range(1, 11):\n    print(f\"{n} x {{i}} = {{{n}*i}}\")"
        return "for i in range(1, 11):\n    print(f'5 x {i} = {5*i}')"

    # 5. Agar 'calculator' bola
    if "calculator" in prompt:
        return "a = int(input('Enter first: '))\nb = int(input('Enter second: '))\nprint('Add:', a+b)\nprint('Sub:', a-b)\nprint('Mul:', a*b)"

    # 6. Kuch nahi samjha toh purane collection me dhoondo
    return search_code(user_input)
