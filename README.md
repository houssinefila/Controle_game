# Hand Gesture Game Controller 🎮✋

Control your games using hand gestures detected through your webcam! This project uses MediaPipe and OpenCV to track hand movements and translate them into keyboard inputs.

## Features

- **Real-time hand tracking** using MediaPipe
- **4 directional controls**: Jump, Down, Left, Right
- **Deliberate control system**: Requires neutral position between actions to prevent accidental inputs
- **Visual feedback**: On-screen display of current gesture and controller status
- **Low latency**: Optimized for responsive gaming experience

## Requirements

- Python 3.7+
- Webcam

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/hand-gesture-controller.git
cd hand-gesture-controller
```

2. Install required packages:
```bash
pip install opencv-python mediapipe numpy pyautogui
```

## Usage

1. Run the program:
```bash
python hand_controller.py
```

2. Position your hand in front of the webcam

3. Perform gestures to control:
   - **Thumb LEFT + Index UP** = Jump (↑)
   - **Thumb LEFT + Index DOWN** = Right (→)
   - **Thumb RIGHT + Index UP** = Left (←)
   - **Thumb RIGHT + Index DOWN** = Down (↓)

4. **Important**: Return to a neutral position (no clear gesture) between each action

5. Press **'q'** to quit

## Gesture Guide

### Jump
- Point your thumb to the left
- Point your index finger up
- Returns to neutral, then executes UP arrow key

### Right
- Point your thumb to the left
- Point your index finger down
- Returns to neutral, then executes RIGHT arrow key

### Left
- Point your thumb to the right
- Point your index finger up
- Returns to neutral, then executes LEFT arrow key

### Down
- Point your thumb to the right
- Point your index finger down
- Returns to neutral, then executes DOWN arrow key

### Neutral Position
- Relax your hand or make a fist
- Required between each action to prevent accidental repeats

## Visual Feedback

The program displays:
- **Current Gesture**: Shows detected gesture in real-time
  - Green text = Neutral position (ready for next action)
  - Yellow text = Active gesture detected
- **Status Indicator**: 
  - "READY" (green) = Can perform new action
  - "RETURN TO NEUTRAL" (orange) = Must reset to neutral first

## Configuration

You can adjust these settings in the code:
```python
# Camera selection (try 0 or 1)
cap = cv2.VideoCapture(1)

# Detection sensitivity
min_detection_confidence=0.7
min_tracking_confidence=0.7

# Response delay (in seconds)
debounce_delay = 0.15

# Key mappings
if current_gesture == "Jump":
    pyautogui.press('up')  # Change 'up' to your preferred key
```

## Troubleshooting

### Camera not detected
- Change `cv2.VideoCapture(1)` to `cv2.VideoCapture(0)`
- Check if another application is using the camera

### Gestures not detected
- Ensure good lighting
- Keep hand at medium distance from camera (30-50cm)
- Adjust `min_detection_confidence` (lower = more sensitive)

### Actions too sensitive or not sensitive enough
- Increase `debounce_delay` for less sensitivity
- Decrease `debounce_delay` for faster response
- Adjust detection confidence values

### Wrong keys being pressed
- Modify the key mappings in the action execution section
- Common game keys: 'space', 'w', 'a', 's', 'd', 'up', 'down', 'left', 'right'

## Compatible Games

This controller works with any game that uses keyboard input. Tested with:
- Chrome Dinosaur Game
- 2D platformers
- Retro arcade games
- Browser-based games

## How It Works

1. **Hand Detection**: MediaPipe detects 21 hand landmarks in real-time
2. **Gesture Recognition**: Analyzes thumb and index finger positions
3. **Action Mapping**: Converts gestures to keyboard inputs via PyAutoGUI
4. **Debouncing**: Requires neutral position between actions for precision

## Landmark Reference

The program uses these MediaPipe hand landmarks:
- Landmark 0: Wrist
- Landmark 2: Thumb middle joint
- Landmark 4: Thumb tip
- Landmark 6: Index finger middle joint
- Landmark 8: Index finger tip

## Performance Tips

- Close unnecessary applications to free up CPU
- Use a solid-colored background for better detection
- Keep your hand within the camera frame
- Avoid rapid movements for more stable detection

## Future Improvements

- [ ] Add more gesture options (peace sign, fist, etc.)
- [ ] Configurable key bindings via config file
- [ ] Support for two-hand controls
- [ ] Recording and replay of gesture sequences
- [ ] GUI for easier configuration

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [MediaPipe](https://mediapipe.dev/) for hand tracking
- [OpenCV](https://opencv.org/) for computer vision
- [PyAutoGUI](https://pyautogui.readthedocs.io/) for keyboard control

## Author

Your Name - [Your GitHub Profile](https://github.com/yourusername)

## Support

If you encounter any issues or have questions, please open an issue on GitHub.

---

**Enjoy gaming with your hands! 🎮✋**
