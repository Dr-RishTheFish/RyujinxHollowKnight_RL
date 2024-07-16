import pyautogui

def execute_action(action):
    if action == 'MOVE_LEFT':
        pyautogui.keyDown('left')
        pyautogui.keyUp('left')
    elif action == 'MOVE_RIGHT':
        pyautogui.keyDown('right')
        pyautogui.keyUp('right')
    elif action == 'JUMP':
        pyautogui.keyDown('up')
        pyautogui.keyUp('up')
    # ... implement other actions