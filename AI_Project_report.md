*AI Project Report*

*Project Title:* Hybrid Checkers (Turkish + International )

*Submitted By:* Kundan Kumar (22k-4545), Rohit Kumar(22k-4544)

*Course:* AI

*Instructor:* \[Talha shahid\]

*Submission Date:* \[11-5-2025\]

*1\. Executive Summary*

*Project Overview:*  
This project introduces a hybrid version of Checkers that merges rules from Turkish Draughts and International Draughts, creating a unique two-player strategy game on a 10x10 board. The objective is to capture or immobilize the opponent. To play competitively against humans, we developed an AI agent based on the Minimax algorithm with Alpha-Beta pruning, enabling intelligent move decisions considering all movement and capture rules.

*2\. Introduction*

*Background:*  
Checkers is a classical strategy game, typically played with standard movement and capturing rules depending on the variant. Turkish Draughts emphasizes orthogonal movement, while International Draughts focuses on diagonal movement and larger boards. Our version combines both to increase complexity and strategic depth.

*Objectives of the Project:*

- To design a new hybrid checkers game combining Turkish and International Draughts.
- To implement a rule engine for the combined ruleset.
- To develop an AI opponent using Minimax with Alpha-Beta pruning.
- To test AI performance in gameplay scenarios.

*3\. Game Description*

*Original Game Rules:*  
In Turkish Draughts:

- Players move orthogonally (forward, left, right).
- Kings move straight.
- Capturing is mandatory.

In International Draughts:

- Pieces move diagonally.
- Kings move any distance in diagonal.
- Chain captures are common.

*Innovations and Modifications:*

- Combined movement: Men can move orthogonally and diagonally forward.
- Capturing in all directions (including backward).
- 10x10 board with 20 pieces per player.
- Men promote to Kings with extended movement abilities.

*4\. AI Approach and Methodology*

*AI Techniques Used:*  
We employed the Minimax algorithm with Alpha-Beta Pruning. This technique enables the AI to simulate future moves and counter-moves to choose the most strategic action efficiently.

*Algorithm and Heuristic Design:*

- Heuristic evaluates board states based on:
  - Piece count difference.
  - Number of kings.
  - Mobility (possible moves).
  - Capture opportunities.

*AI Performance Evaluation:*

- Measured using win rate against human testers.
- Average decision time per move.
- Number of optimal captures performed.

*5\. Game Mechanics and Rules*

*Modified Game Rules:*

- Men move in four orthogonal and two diagonal forward directions.
- Kings move any distance in all straight and diagonal directions.
- Captures are mandatory, with the requirement to choose the path with maximum captures.
- Men and Kings can capture in all directions, including backward.

*Turn-based Mechanics:*  
Players alternate turns. On each turn, if a capture is available, it must be taken. Multiple captures in one turn are allowed.

*Winning Conditions:*  
A player wins by capturing all opponent pieces or if the opponent has no legal moves.

*6\. Implementation and Development*

*Development Process:*  
The game was built in Python using the Pygame library for visuals and input handling. The AI logic was implemented in separate modules and integrated with the main game loop.

*Programming Languages and Tools:*

- *Programming Language:* Python
- *Libraries:* Pygame, NumPy
- *Tools:* GitHub (Version control), VS Code

*Challenges Encountered:*

- Balancing the complexity of hybrid rules in the move generator.
- Ensuring the AI chooses chain captures over simple moves.
- Debugging edge cases in promotion and multi-jump logic.

*7\. Team Contributions*

*Team Members and Responsibilities:*

- *Rohit Kumar:* Developed the AI logic using Minimax and Alpha-Beta Pruning.
- *Kundan Kumar:* Designed the hybrid rule set, implemented board mechanics, and built the user interface.

*8\. Results and Discussion*

*AI Performance:*

- Win rate: ~75% against intermediate human players.
- Decision-making time: ~1.5 seconds per move.
- Demonstrated strategic captures and avoided traps by evaluating future consequences.

*9\. References*

- \[1\] Russell, S. & Norvig, P. (2020). Artificial Intelligence: A Modern Approach.
- \[2\] Turkish Draughts Official Rules – World Draughts Federation
- \[3\] International Draughts Rulebook – FMJD
- \[4\] Pygame Documentation – <https://www.pygame.org/docs/>
- \[5\] <https://en.wikipedia.org/wiki/Minimax>
