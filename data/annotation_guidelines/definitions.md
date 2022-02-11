
# Event Definitions
<hr>

## Ball Possession
Changes if and only if one team gain and control the ball at least for $t$ seconds. 
Ball ping pong is consequently "n.d.". Team A corresponds to the left team according to the scoreboard.
If no scoreboard is visible (independent of the half), A is the team which attacks from left to right.

We set $t=3s$ for soccer and $t=1s$ for handball which is somewhat arbitrary but a good compromise between precise annotations and annotation effort.
Examples soccer:  
-  A ($>=t$) &rarr; B($<t$) &rarr;A($>t$): from A to A, i.e. no ball possession change (should not be tagged)  
-  A($>=t$) &rarr; B($<t$) &rarr; A($<t$): Change from A to "n.d."

Ball possession only changes, when the **game status** is active, e.g., in parallel when a **throw-in** occurs.

## Individual Ball Event

-  **Ball Reception**: Motoric skill: Player receives the ball (from opponent or team mate) and controls it \cite{link2017individual}, e.g. starts dribbling; timestamp: first contact.
-  **Ball Release**: Timestamp: on release
-  **Ball Release** &rarr; **Intentional**: Motoric skill: player releases ball in a controlled manner
-  **Ball Release** &rarr; **Unintentional**: Player releases ball in an uncontrolled manner
-  **Unintentional Ball Release** &rarr; **Successful Interference**: Player releases ball involuntary due to opponents impact; individual ball possession changed, i.e. player looses ball. Replaces **Ball Reception** and **Ball Release**. If the player starts dribbling, and then releases the ball, a new event should be annotated.
-  **Unintentional Ball Release** &rarr; **Other**: Player releases ball without directly involved opponent, e.g. slips/stumble, no reaction time for controlled ball release. For instance, after intercepted/blocked pass/shot event.
-  **Intentional Ball Release** &rarr; **Pass**: Player kicks the ball (head, foot, etc.) with the intention that a teammate receives it. **Successful** if and only if any one teammate touches the ball (opponent can touch the ball during the pass, i.e. sub-event **Deflected**). Fair play passes should not be tagged as pass.
For a case where a player only takes one touch only consider the **Ball Release** as relevant and do not annotate a **Ball reception**.
-  **Pass** &rarr; **Unsuccessful** &rarr; **Off target**: Pass without any subsequent ball reception from a teammate
-  **Pass** &rarr; **Unsuccessful** &rarr; **Intercepted**: Opponent steals the ball after the pass was played.
-  **Intentional Ball Release** &rarr; **Shot**: Intention (drawn) towards target; timestamp: on Ball Release
-   **Shot** &rarr; **Successful**: Potential scoring point, e.g. ball crosses/hits target
-  **Shot**  &rarr; **Unsuccessful** &rarr; **Goal Frame**: Ball touches Goal Frame, but is unsuccessful in terms of potential scoring point 
-  **Shot** &rarr; **Unsuccessful** &rarr; **Blocked**: Blocked or intercepted ball (own team, opponent, field player (,goal keeper)) 
-  **Shot** &rarr; **Unsuccessful** &rarr; **Off Target**: Ball does not hit target (goal, frame)

## Game Status Changing Events

-  **Game Status Changing Event**: Game state ("paused", "running") is changed only by **Static Ball Events** and **Referee's Decisions**, respectively. **Static Ball Event**, **Referee's Decision** &rarr; **Other** indices not covered base events, e.g. referee ball or fair play
-  **Static Ball Event**: Game status "paused" followed by game status "running", e.g. "ball leaves player event" after game status "paused"; timestamp: ball leaves player
-  **Static Ball Event** &rarr; **After Foul**: Player releases ball that changes the game state to "running" after a **foul** occurs; timestamp: Ball Release
-  **Static Ball Event** &rarr; **Ball in Field**: Player releases ball that changes the game state to "running" after a **ball out of field** occurs; timestamp: Ball Release
-  **Static Ball Event** &rarr; **Game Start**: Player releases ball that changes the game state to "running", i.e. the first kick-off
-  **Static Ball Event** &rarr; **Kick-off**: Player releases ball that changes the game state to "running" after a **Goal** occurs; timestamp: Ball Release
-  **Referee Decision**: Decision from referee; timestamp: at the moment of the decision, e.g., whistle or hand sign; If no decision is shown, but game state obviously changed to "paused", choose best candidate, e.g. ball leaves field.
-  **Referee's Decision** &rarr; **Foul**: Referee's decision that an illegal action occurred
-  **Referee's Decision** &rarr; **Ball Out of Field**: Ball is out of field. Timestamp: decision, if not possible, then when the ball leaves the field
-  **Referee's Decision** &rarr; **Game End**: Game end event. If the game is divided into several half times, each half time end should be annotated.

## Annotation Notes
-  No **individual ball events** needs to be annotated for the duration between **game status** "paused" and "running".
-  Due to the nature of TV broadcasts, different shots and camera angles are shown: Events and timestamps should be annotated for all visible events. However, when an event directly can be derived from the context, i.e. the event and approx. timestamp is clear, but is not concretely shown (e.g. transition), the respective event can be annotated. For instance, if the frame where the ball releases a player is hidden (cut, transition, etc.), the approximated timestamp should be annotated since the context is clear.
-  **Moving Ball Event**s are mutually exclusive, i.e. one **Moving Ball Event** event for one timestamp.
-  **Static-ball Event**: Always do a **double-annotation** as a **Static Ball Event** **followed by** a **Individual Ball Event** (e.g. penalty + shot).
-  **Substitution**, i.e. a **Non-on-Ball Event**: One player leaves the pitch and another player enters the pitch; timestamp: when the new player enters the pitch
-  Implication: **Dribbling**: **Ball Reception** followed by one ball-leaves-player event (e.g. Ball Release, tackling, foul); implicitly encoded, thus no annotation required, timestamp same as **Reception**.
