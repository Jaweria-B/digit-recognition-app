import streamlit as st
import numpy as np
import pygame
import sys
import tensorflow as tf
import time
import subprocess


# -- Recoginition.py file code --
def start_recognition():
    # Load the trained model
    model = tf.keras.models.load_model("model.h5")

    # Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Start pygame
    pygame.init()
    size = width, height = 600, 400
    screen = pygame.display.set_mode(size)

    # Fonts
    OPEN_SANS = "assets/fonts/OpenSans-Regular.ttf"
    smallFont = pygame.font.Font(OPEN_SANS, 20)
    largeFont = pygame.font.Font(OPEN_SANS, 40)

    ROWS, COLS = 28, 28

    OFFSET = 20
    CELL_SIZE = 10

    handwriting = [[0] * COLS for _ in range(ROWS)]
    classification = None

    # Loop until the window is closed
    while True:
        # Check if game quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        # Check for mouse press
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
        else:
            mouse = None

        # Draw each grid cell
        cells = []
        for i in range(ROWS):
            row = []
            for j in range(COLS):
                rect = pygame.Rect(
                    OFFSET + j * CELL_SIZE,
                    OFFSET + i * CELL_SIZE,
                    CELL_SIZE, CELL_SIZE
                )

                # If cell has been written on, darken cell
                if handwriting[i][j]:
                    channel = 255 - (handwriting[i][j] * 255)
                    pygame.draw.rect(screen, (channel, channel, channel), rect)

                # Draw blank cell
                else:
                    pygame.draw.rect(screen, WHITE, rect)
                pygame.draw.rect(screen, BLACK, rect, 1)

                # If writing on this cell, fill in current cell and neighbors
                if mouse and rect.collidepoint(mouse):
                    handwriting[i][j] = 250 / 255
                    if i + 1 < ROWS:
                        handwriting[i + 1][j] = 220 / 255
                    if j + 1 < COLS:
                        handwriting[i][j + 1] = 220 / 255
                    if i + 1 < ROWS and j + 1 < COLS:
                        handwriting[i + 1][j + 1] = 190 / 255

        # Reset button
        resetButton = pygame.Rect(
            30, OFFSET + ROWS * CELL_SIZE + 30,
            100, 30
        )
        resetText = smallFont.render("Reset", True, BLACK)
        resetTextRect = resetText.get_rect()
        resetTextRect.center = resetButton.center
        pygame.draw.rect(screen, WHITE, resetButton)
        screen.blit(resetText, resetTextRect)

        # Classify button
        classifyButton = pygame.Rect(
            150, OFFSET + ROWS * CELL_SIZE + 30,
            100, 30
        )
        classifyText = smallFont.render("Classify", True, BLACK)
        classifyTextRect = classifyText.get_rect()
        classifyTextRect.center = classifyButton.center
        pygame.draw.rect(screen, WHITE, classifyButton)
        screen.blit(classifyText, classifyTextRect)

        # Reset drawing
        if mouse and resetButton.collidepoint(mouse):
            handwriting = [[0] * COLS for _ in range(ROWS)]
            classification = None

        # Generate classification
        if mouse and classifyButton.collidepoint(mouse):
            classification = model.predict(
                [np.array(handwriting).reshape(1, 28, 28, 1)]
            ).argmax()

        # Show classification if one exists
        if classification is not None:
            classificationText = largeFont.render(str(classification), True, WHITE)
            classificationRect = classificationText.get_rect()
            grid_size = OFFSET * 2 + CELL_SIZE * COLS
            classificationRect.center = (
                grid_size + ((width - grid_size) / 2),
                100
            )
            screen.blit(classificationText, classificationRect)

        pygame.display.flip()
        
# Streamlit app UI
st.title("Draw and Guess 🎨✏️")

# Textual statements about the app
st.write("Welcome to Draw and Guess! 🤖💡")
st.write("This app allows you to draw a digit and then predicts what it is. 🎮🕹️")
st.write("Get started by clicking the 'Start Drawing' button below and follow the instructions on the sidebar. 🔢🖼️")

# Instructions for the user
st.sidebar.title("Instructions")
st.sidebar.write("1. Click the 'Start Drawing' button to begin.")
st.sidebar.write("2. A Pygame window will open where you can draw a digit.")
st.sidebar.write("3. Once you've drawn a digit, click the 'Classify' button in the Pygame window to see the prediction.")
st.sidebar.write("4. You can reset the drawing at any time by clicking the 'Reset' button in the Pygame window.")
st.sidebar.write("5. For better performance, it's recommended to use mouse clicks for RESET and CLASSIFY buttons in the Pygame window.")

# Button to start drawing
start_button = st.button("Start Drawing 🖌️")

if start_button:
    # Execute the Pygame script
    start_recognition()
    
    # Footer statements
    st.write("---")
    st.write("Made By **_Jaweria Batool_**")
    st.write("For more information about how the app works, please check out the [GitHub README](https://github.com/Jaweria-B/digit-recognition-app) file.")
