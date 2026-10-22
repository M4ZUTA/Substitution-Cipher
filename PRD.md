# Product Requirements Document (PRD): Frequency Analysis UI

## 1. Project Overview
A web-based user interface for a Python script that performs frequency analysis on substitution ciphers. The app will allow users to input ciphertext, view the letter frequency distribution compared to standard language frequencies, and interactively map/replace cipher letters with plaintext letters to decrypt the message.

## 2. Tech Stack
*   **Language:** Python 3.14.8
*   **Framework:** Streamlit (for UI and state management)
*   **Data Manipulation & Visualization:** Pandas, Plotly/Altair (for interactive frequency charts)

## 3. Core Features
*   **Ciphertext Input:** A large text area for users to paste the encrypted message.
*   **Automated Frequency Calculation:** Instantly calculate and display the frequency of each letter in the inputted ciphertext.
*   **Comparative Visualization:** A bar chart comparing the ciphertext's letter frequencies side-by-side with standard English (or Indonesian) letter frequencies (E, T, A, O, I, N, etc.).
*   **Interactive Substitution Map:** A dynamic table or set of input fields where the user can map a Cipher Letter (e.g., 'X') to a Plaintext Letter (e.g., 'A').
*   **Live Decryption Preview:** A real-time text display showing the partially decrypted text based on the current substitution map. Known/replaced letters should be highlighted or capitalized, while unresolved letters remain distinct.
*   **Reset/Clear Action:** A button to clear all current mappings and start over.

## 4. UI Layout & User Flow
1.  **Header:** Title "Substitution Cipher Frequency Analyzer".
2.  **Section 1: Input:** `st.text_area` for pasting ciphertext.
3.  **Section 2: Analysis & Charts:**
    *   Display total character count.
    *   Render a grouped bar chart (`st.bar_chart` or Plotly) showing standard language frequency vs. ciphertext frequency.
4.  **Section 3: Decryption Workbench:**
    *   **Left Column:** A grid of 26 text inputs (`st.text_input`) for the substitution alphabet mapping.
    *   **Right Column:** A large markdown or text box showing the Live Decryption Preview.

## 5. Technical Constraints & Error Handling
*   **Case Insensitivity:** All ciphertext should be converted to uppercase (or lowercase) for standard analysis. Non-alphabet characters (spaces, punctuation) must be preserved in the final output but ignored in the frequency math.
*   **Session State:** Use Streamlit's `st.session_state` to store the substitution dictionary so that the page doesn't reset the user's progress every time a new letter is mapped.
*   **Input Validation:** The substitution mapping fields should only accept a single alphabetical character.

## 6. Implementation Steps for Agent
1. Scaffold the basic Streamlit app structure and layout columns.
2. Implement the frequency counting logic and link it to the Plotly/Altair chart.
3. Setup `st.session_state` to track user mappings.
4. Build the substitution grid UI.
5. Create the live-update text replacement function that renders the mixed plaintext/ciphertext.