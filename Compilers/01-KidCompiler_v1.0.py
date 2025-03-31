import random
import time
errors = [
    "What is this? 😭",
    "SyntaxError: Kid forgot how to code.",
    "IndentationError: Did you even try?",
    "RuntimeError: Compiler is crying.",
    "Segmentation fault: Too much nonsense detected.",
    "Error 404: Logic not found.",
    "Fatal Error: Kid gave up.",
    "KID-ERR-420: Too much chaos.",
    "FAIL-1337: System disrespects your code.",
    "MemoryError: Brain not found.",
    "Blue Screen of Death incoming... 💀"
]
suggestions = [
    "Try adding more random characters and hope for the best.",
    "Maybe remove that banana you typed in the middle?",
    "Just keep smashing the keyboard, it'll work eventually.",
    "I don't know what you did, but undo it. Now.",
    "Ask ChatGPT, maybe it understands your madness!",
    "Throw your computer out the window.",
    "Just accept that this language will never work.",
    "Buy a new keyboard, maybe it's the problem.",
    "Summon the coding gods to fix this mess.",
    "Close your eyes, press random buttons, and pray.",
    "Have you considered switching careers?",
    "CTRL + ALT + DEL won't save you now."
]
fake_debug_steps = [
    "Analyzing code... (0%)",
    "Finding syntax errors... (23%)",
    "Realizing this code is a mess... (47%)",
    "Crying... (64%)",
    "Regretting life choices... (79%)",
    "Deleting entire project... (95%)",
    "System Overload! Rebooting... (100%)",
    "Debugging failed. Sorry. 🤷‍♂️"
]
def fake_debug():
    print("\n[Debug Mode Activated]")
    for step in fake_debug_steps:
        print(step)
        time.sleep(random.uniform(0.5, 1.5))
    print("\nFix Applied. (Just kidding, nothing changed.)")
def kid_compiler(debug=False):
    print("\n🚀 KidCompiler v1.0 🚀")
    print("Error:", random.choice(errors))
    print("Suggestion:", random.choice(suggestions))
    print("Execution Failed. As expected. 😎")   
    if debug:
        fake_debug()
kid_compiler(debug=True)