#!/usr/bin/env python3

import os
import sys
import shutil
import random
import time
import subprocess
import signal
import math


# MATRIX TERMINAL LAUNCHER

def launch_matrix_terminal():

    script = os.path.abspath(__file__)

    subprocess.Popen([
        "xfce4-terminal",
        "--hide-menubar",
        "--fullscreen",
        "--command",
        f"python3 {script} --render"
    ])


# RENDER MODE

if "--render" not in sys.argv:

    launch_matrix_terminal()

    sys.exit(0)


# ACTUAL MATRIX ENGINE STARTS HERE

# YAHAN SE TERA CURRENT ADVANCED MATRIX CODE
# START HOGA
# ADVANCED TERMINAL CYBER RAIN
# SYMBOL POOL
# No emoji characters.
SYMBOLS = (
    "01"
    "@#$%&*+=~^"
    "<>/\\|"
    "{}[]()"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "abcdefghijklmnopqrstuvwxyz"
    "▲▼◀▶"
    "△▽◁▷"
    "◆◇◈"
    "●○◎◉"
    "■□▪▫"
    "★☆✦✧"
    "✚✖"
    "⊕⊗⊙⊛"
    "∎∙·"
    "※§¶"
    "∞≠≈≤≥"
    "±÷×"
    "∑√∆"
    "µπΩ"
    "⌁⌂⌘"
    "⌜⌝⌞⌟"
    "⟐⟡⟢⟣"
    "◐◑◒◓"
    "◩◪◫◧"
    "⬢⬡"
    "⬟⬣"
    "⇐⇒⇑⇓"
    "↖↗↘↙"
    "↔↕"
)

BINARY = "01"
HEX = "0123456789ABCDEF"
CYBER = "01@#$%&*+=<>[]{}"

# 256-COLOR PALETTE
COLORS = list(range(16, 256))

# SETTINGS
FPS = 50

MIN_SPEED = 0.35
MAX_SPEED = 2.4

MIN_TRAIL = 5
MAX_TRAIL = 22

PATTERN_CHANGE_MIN = 0.08
PATTERN_CHANGE_MAX = 0.9

GLITCH_CHANCE = 0.035
BRIGHT_HEAD_CHANCE = 0.90
BIG_PATTERN_CHANCE = 0.012

WAVE_AMOUNT = 0.45
COLOR_SHIFT_SPEED = 12

# CREATE RANDOM PATTERN
def make_pattern():

    mode = random.randint(0, 14)

    # Single character
    if mode <= 2:
        return random.choice(SYMBOLS)

    # Binary
    if mode == 3:
        return "".join(
            random.choice(BINARY)
            for _ in range(random.randint(3, 10))
        )

    # Hexadecimal
    if mode == 4:
        return "".join(
            random.choice(HEX)
            for _ in range(random.randint(3, 8))
        )

    # Cyber symbols
    if mode == 5:
        return "".join(
            random.choice(CYBER)
            for _ in range(random.randint(3, 9))
        )

    # Random symbols
    if mode <= 8:
        return "".join(
            random.choice(SYMBOLS)
            for _ in range(random.randint(2, 7))
        )

    # Symmetric
    if mode == 9:
        a = random.choice(SYMBOLS)
        b = random.choice(SYMBOLS)
        c = random.choice(SYMBOLS)

        return f"{a}{b}{c}{b}{a}"

    # Box
    if mode == 10:
        a = random.choice(SYMBOLS)
        b = random.choice(SYMBOLS)

        return f"[{a}{b}]"

    # Diamond
    if mode == 11:
        a = random.choice(SYMBOLS)

        return f"<{a}>"

    # Binary + symbols
    if mode == 12:
        return (
            random.choice(SYMBOLS)
            + random.choice(BINARY)
            + random.choice(SYMBOLS)
            + random.choice(BINARY)
        )

    # Mathematical
    if mode == 13:
        return (
            random.choice("∆∑√∞±÷×")
            + random.choice(SYMBOLS)
        )

    # Completely random
    return "".join(
        random.choice(SYMBOLS)
        for _ in range(random.randint(1, 10))
    )

# CREATE DROP
def create_drop(height, start_random=True):

    if start_random:
        y = random.uniform(-height, 0)
    else:
        y = random.uniform(-height * 0.25, 0)

    return {
        "y": y,

        "speed": random.uniform(
            MIN_SPEED,
            MAX_SPEED
        ),

        "trail": random.randint(
            MIN_TRAIL,
            MAX_TRAIL
        ),

        "color": random.choice(
            COLORS
        ),

        "pattern": make_pattern(),

        "phase": random.uniform(
            0,
            math.tau
        ),

        "pattern_timer": random.uniform(
            PATTERN_CHANGE_MIN,
            PATTERN_CHANGE_MAX
        ),

        "density": random.uniform(
            0.55,
            1.0
        ),

        "drift": random.uniform(
            -WAVE_AMOUNT,
            WAVE_AMOUNT
        ),

        "color_phase": random.uniform(
            0,
            256
        ),

        "glitch": False,
    }

# TERMINAL SIZE
def get_size():

    size = shutil.get_terminal_size(
        fallback=(120, 40)
    )

    return size.columns, size.lines

# FULLSCREEN
def fullscreen():

    try:

        subprocess.run(
            [
                "wmctrl",
                "-r",
                ":ACTIVE:",
                "-b",
                "add,fullscreen"
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

    except Exception:
        pass


def restore_window():

    try:

        subprocess.run(
            [
                "wmctrl",
                "-r",
                ":ACTIVE:",
                "-b",
                "remove,fullscreen"
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

    except Exception:
        pass

# TERMINAL SETUP
def setup_terminal():

    # Alternate screen
    sys.stdout.write("\033[?1049h")

    # Hide cursor
    sys.stdout.write("\033[?25l")

    # Clear screen
    sys.stdout.write("\033[2J\033[H")

    # Disable line wrapping
    sys.stdout.write("\033[?7l")

    sys.stdout.flush()

# RESTORE TERMINAL
def restore_terminal():

    sys.stdout.write("\033[0m")
    sys.stdout.write("\033[?7h")
    sys.stdout.write("\033[?25h")
    sys.stdout.write("\033[?1049l")

    sys.stdout.flush()

# SIGNAL HANDLING
running = True


def stop(signum, frame):

    global running

    running = False


signal.signal(
    signal.SIGINT,
    stop
)

signal.signal(
    signal.SIGTERM,
    stop
)

# COLOR CALCULATION
def dynamic_color(base, phase):

    # Keep within ANSI 256 palette
    shifted = int(
        base
        + math.sin(phase)
        * COLOR_SHIFT_SPEED
    )

    return max(
        16,
        min(255, shifted)
    )

# DRAW CHARACTER
def draw_char(
    x,
    y,
    char,
    color,
    level
):

    if (
        x < 0
        or y < 0
    ):
        return

    # Bright white head
    if level == 0:

        style = (
            "\033[1;38;5;255m"
        )

    # Very bright
    elif level == 1:

        style = (
            f"\033[1;38;5;{color}m"
        )

    # Normal
    elif level == 2:

        style = (
            f"\033[38;5;{color}m"
        )

    # Dim
    elif level == 3:

        style = (
            f"\033[2;38;5;{color}m"
        )

    # Very dim
    else:

        style = (
            f"\033[2;38;5;{color}m"
        )

    sys.stdout.write(
        f"\033[{y + 1};{x + 1}H"
        f"{style}{char}\033[0m"
    )

# MAIN ENGINE
def main():

    setup_terminal()

    # Give the terminal a moment before fullscreen
    time.sleep(0.05)

    fullscreen()

    width, height = get_size()

    drops = [
        create_drop(height)
        for _ in range(width)
    ]

    last_time = time.monotonic()

    try:

        while running:

            # RESIZE

            new_width, new_height = get_size()

            if (
                new_width != width
                or new_height != height
            ):

                width = new_width
                height = new_height

                drops = [
                    create_drop(height)
                    for _ in range(width)
                ]

                sys.stdout.write(
                    "\033[2J\033[H"
                )


            # DELTA TIME

            now = time.monotonic()

            dt = now - last_time

            last_time = now

            dt = min(
                dt,
                0.1
            )


            # UPDATE EVERY STREAM

            for x, drop in enumerate(drops):

                # Vertical movement
                drop["y"] += (
                    drop["speed"]
                    * dt
                    * 35
                )

                # Phase
                drop["phase"] += (
                    dt
                    * drop["speed"]
                )

                # Pattern timer
                drop["pattern_timer"] -= dt

                if (
                    drop["pattern_timer"]
                    <= 0
                ):

                    drop["pattern"] = (
                        make_pattern()
                    )

                    drop["pattern_timer"] = (
                        random.uniform(
                            PATTERN_CHANGE_MIN,
                            PATTERN_CHANGE_MAX
                        )
                    )


                    # RESET STREAM
    
                if (
                    int(drop["y"])
                    - drop["trail"]
                    > height
                ):

                    drops[x] = create_drop(
                        height,
                        start_random=False
                    )

                    continue


                head = int(drop["y"])


                    # DRAW TRAIL
    
                for i in range(
                    drop["trail"]
                ):

                    y = head - i

                    if (
                        y < 0
                        or y >= height
                    ):
                        continue


                    # Density
                    if (
                        i > 2
                        and random.random()
                        > drop["density"]
                    ):
                        continue


                    pattern = drop["pattern"]


                    # Pattern character
                    if pattern:

                        char = pattern[
                            (
                                i
                                + int(
                                    drop["phase"]
                                    * 4
                                )
                            )
                            % len(pattern)
                        ]

                    else:

                        char = random.choice(
                            SYMBOLS
                        )


                            # GLITCH
        
                    if (
                        random.random()
                        < GLITCH_CHANCE
                    ):

                        char = random.choice(
                            SYMBOLS
                        )


                            # HEAD SPECIAL
        
                    if (
                        i == 0
                        and random.random()
                        < BRIGHT_HEAD_CHANCE
                    ):

                        char = random.choice(
                            SYMBOLS
                        )


                            # OCCASIONAL SPECIAL SHAPE
        
                    if (
                        i == 0
                        and random.random()
                        < BIG_PATTERN_CHANCE
                    ):

                        char = random.choice(
                            "◆◇◈◎◉★☆▲▼"
                        )


                            # BRIGHTNESS
        
                    if i == 0:

                        level = 0

                    elif i <= 2:

                        level = 1

                    elif i <= 6:

                        level = 2

                    elif i <= 11:

                        level = 3

                    else:

                        level = 4


                            # DYNAMIC COLOR
        
                    color = dynamic_color(
                        drop["color"],
                        drop["color_phase"]
                        + i * 0.35
                    )


                            # DRAW
        
                    draw_char(
                        x,
                        y,
                        char,
                        color,
                        level
                    )


                # Color evolution
                drop["color_phase"] += (
                    dt * drop["speed"]
                )


            # FLUSH

            sys.stdout.flush()

            time.sleep(
                1 / FPS
            )


    finally:

        restore_window()

        restore_terminal()

# START
if __name__ == "__main__":

    main()
