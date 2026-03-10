import tkinter as tk
import threading
import random
import time

from voice_module import take_command
from action_module import execute_command, talk


def animate_wave():

    canvas.delete("all")

    for i in range(30):

        height = random.randint(20,120)

        canvas.create_line(
            i*20,
            140,
            i*20,
            140-height,
            fill="#00ffff",
            width=3
        )

    window.update()


def jarvis_loop():

    talk("Jarvis system online. Say Hey Jarvis", output_box)

    while True:

        animate_wave()

        command = take_command()

        if command == "":
            continue

        output_box.insert("end","You: "+command+"\n")
        output_box.see("end")

        if "hey jarvis" in command:

            talk("Yes boss", output_box)

            time.sleep(1)

            animate_wave()

            command = take_command()

            if command == "":
                talk("I did not hear the command", output_box)
                continue

            output_box.insert("end","You: "+command+"\n")
            output_box.see("end")

            execute_command(command, output_box)

            time.sleep(2)


window = tk.Tk()

window.title("JARVIS AI")

window.geometry("750x650")

window.configure(bg="#0b0f1a")


title = tk.Label(
    window,
    text="JARVIS AI SYSTEM",
    font=("Orbitron",28),
    fg="#00ffff",
    bg="#0b0f1a"
)

title.pack(pady=20)


canvas = tk.Canvas(
    window,
    width=600,
    height=150,
    bg="#0b0f1a",
    highlightthickness=0
)

canvas.pack(pady=10)


output_box = tk.Text(
    window,
    height=18,
    width=90,
    bg="#05080f",
    fg="#00ffff",
    insertbackground="white",
    font=("Consolas",11)
)

output_box.pack(pady=20)


threading.Thread(target=jarvis_loop, daemon=True).start()

window.mainloop()