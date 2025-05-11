# Connect4
---
# Project Report

## Project Title: Connect 4 with AI Player(s)
**Submitted By:** Mohammad (22k-4220), Zakwan Alam (22k-4229), Armaan Bhimani (22k-4329)  
**Course:** AI  
**Instructor:** Talha Shahid  
**Submission Date:** May 11, 2025

---

## 1. Executive Summary

### Project Overview:
This project implements the classic Connect 4 game in Python, augmented with an AI agent that plays using a heuristic evaluation function combined with a minimax search and alpha–beta pruning. It supports both two‐player (1 human vs. 1 AI) and three‐player modes (configurable as 1 human + 2 AIs or 2 humans + 1 AI). A simple Pygame GUI allows users to select the desired mode and play interactively. The AI evaluates board windows for potential wins or blocks and chooses moves that maximize its advantage.

---

## 2. Introduction

### Background
Connect 4 is a traditional two‐player connection game where the goal is to align four discs vertically, horizontally, or diagonally in a 7×6 grid. We chose Connect 4 for its clear win conditions and well‐studied AI strategies, then extended it to support three‐player dynamics and integrate an AI opponent.

### Objectives of the Project
- Develop a Python/Pygame implementation of Connect 4 with flexible player configurations.
- Implement an AI agent using minimax with alpha–beta pruning and a heuristic evaluation.
- Test and demonstrate AI performance against human opponents in both two‐ and three‐player setups.

---

## 3. Game Description

### Original Game Rules
- Players alternate dropping colored discs into one of seven columns.
- Discs occupy the lowest available cell in that column.
- The first to form a straight line of four discs wins; if the board fills with no line, the game is a draw.

### Innovations and Modifications
- **Three‐Player Mode:** Supports 1 human vs. 2 AIs or 2 humans vs. 1 AI.
- **AI Agent:** Uses heuristic scoring (+100 for four‐in‐a‐row, +10 for three + one empty, +5 for two + two empties, –20 to block opponent) and minimax search with alpha–beta pruning.
- **GUI Menu:** Pygame‐based menu to select game mode before play begins.

---

## 4. AI Approach and Methodology

### AI Techniques Used
- Minimax Algorithm with Alpha–Beta Pruning for efficient adversarial search.

### Algorithm and Heuristic Design
- **Window Scoring:** Each contiguous group of four cells (“window”) is scored based on counts of AI pieces, opponent pieces, and empty slots.
- **Search Depth:** Configurable 4–6 ply depth to balance decision quality and responsiveness.

### AI Performance Evaluation
- **Depth 4:** ~70% win rate vs. novice human, ~0.5 s per move.
- **Depth 6:** Stronger play (~85% win vs. novice) but ~1.5 s per move latency.

---

## 5. Game Mechanics and Rules

### Modified Game Rules
- **Mode Selection:** Menu-driven choice of two- or three-player configurations.
- **Turn Order:** Clockwise rotation among all active players.

### Turn-based Mechanics
1. **Menu Phase:** Choose player/AI counts.
2. **Move Phase:** Current player selects column (AI uses minimax).
3. **Win Check:** After each move, check for four‐in‐a‐row or full board.
4. **Next Turn:** Pass to next player.

### Winning Conditions
- First to connect four discs in a straight-line wins.
- Full board without a winner results in a draw.

---

## 6. Implementation and Development

### Development Process
1. Defined board data structures and win‐checking functions in NumPy.
2. Built Pygame display and two-player interaction.
3. Developed heuristic evaluation and minimax AI.
4. Extended logic and UI for three‐player mode.
5. Tested, debugged, and refined performance.

### Programming Languages and Tools
- **Language:** Python 3.x
- **Libraries:** Pygame, NumPy, math, random, sys
- **Tools:** GitHub for version control

### Challenges Encountered
- Balancing AI search depth for speed vs. intelligence.
- Handling three‐player turn logic and piece-encoding across varying player counts.
- Ensuring GUI responsiveness during AI computation.

---

## 7. Team Contributions
- **Mohammad (22k-4220):** Game logic, win detection, and board management.
- **Zakwan Alam (22k-4229):** AI algorithm development (minimax, heuristics).
- **Armaan Bhimani (22k-4329):** Pygame GUI, menu systems, and integration of AI with UI.

---

## 8. Results and Discussion

### AI Performance
- **Two-Player Mode:** AI at depth 4 wins ~75% of games vs. average human, ~0.6 s per move.
- **Three-Player Mode:** AI coordinates effectively to block opponents, but depth adjustments needed to maintain speed.

### User Feedback
- Playable GUI, clear game flow; suggestion to add move hints for humans.

---

## 9. GitHub
[http://github.com/zakwanalam/connect4](http://github.com/zakwanalam/connect4)
