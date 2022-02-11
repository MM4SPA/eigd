
# Example Annotations

## Download
You may need to download the resource files (image, video) first:

```sh
wget https://data.uni-hannover.de/dataset/8ccb364e-145f-4b28-8ff4-954b86e9b30d/resource/f249b451-d277-4f6f-9a3f-83cae423c3b6/download/screenshots_and_clips.zip
unzip screenshots_and_clips.zip -d screenshots_and_clips
```


## Examples
<hr>

### **Dribbling** with Contact from Opponenct
No need to tag since **unsuccessful interference** is not part of the base taxonomy.
Individual ball possession has not changed between **Ball Reception** and **Ball Release**.
<figure class="video_container">
  <video controls="true" allowfullscreen="true" poster="" style="width: 100%;">
    <source src="screenshots_and_clips/Argentina-vs-Belgium-Fifa-World-Cup-2014-Quater-final-full-match-YouTube_25fps_20198_20299_25.0_dribbling_contact_opponent.mp4" type="video/mp4">
  </video>
</figure>

<hr>

### **Successful Pass** with Contact from Opponent
Player has intention to pass to one teammate and (other) teammate recieves it &rarr; **Pass Successful Deflected**.  

**Do not annotate**: Successfull pass + unintended ball release from opponent

<figure class="video_container">
  <video controls="true" allowfullscreen="true" poster="" style="width: 100%;">
    <source src="screenshots_and_clips/Argentina-vs-Belgium-Fifa-World-Cup-2014-Quater-final-full-match-YouTube_25fps_27264_27300_25.0_successful_pass_w_contact_opponent.mp4" type="video/mp4">
  </video>
</figure>

<hr>

### **Successful Interference** without Contact from Opponent &rarr; **Ball Out of Bounds**  
Direct reason for the ball release is the interference. Timestamp: When the ball leaves the player.
Hint: No foul.

<figure class="video_container">
  <video controls="true" allowfullscreen="true" poster="" style="width: 100%;">
    <source src="screenshots_and_clips/Argentina-vs-Belgium-Fifa-World-Cup-2014-Quater-final-full-match-YouTube_25fps_22890_22945_25.0_interference_wo_contact_opponent.mp4" type="video/mp4">
  </video>
</figure>

<hr>

###  **Successful Interference** with Contact from Opponent
- Not an **Unsuccessful Pass** (Red jersey, number 6, Witsel), since there is no primary(!) intention for a pass
- Not an **Unintended Ball Release &rarr; Other** since it is the direct outcome of a tackle, i.e. successful interference. 
Remember that **Individual Ball Event**s are mutually exclusive and hence this direct contact should be annotated as **Successful Interference**.
In this case **Successful Interference** replaces **Ball Release**. However, in another case **Successful Interference** could replace **Ball Reception**.

<figure class="video_container">
  <video controls="true" allowfullscreen="true" poster="" style="width: 100%;">
    <source src="screenshots_and_clips/Argentina-vs-Belgium-Fifa-World-Cup-2014-Quater-final-full-match-YouTube_25fps_20609_20793_25.0_interference_contact_opponent.mp4" type="video/mp4">
  </video>
</figure>

<hr>

### **Goalkick+Unsuccessfull Pass** &rarr; **Unsuccessfull Pass**

(1) Goalkeeper performs an unsuccessfull pass, because an opponent touches the ball first. Since the ball was touched in the end of the sequence and the direction was right, the sub-event **Off Target** should be annotated.
(2) **Unsuccessfull Pass** (off target) since there is a primary intention, but the direction and movement of the teamate is not correct. 
However, it can be argued that the main intention is to win the tackling with the cost of an throw-in, i.e. a **successful interference** or there is no clear intention, then **Unintentional Ball Release Other**


<figure class="video_container">
  <video controls="true" allowfullscreen="true" poster="" style="width: 100%;">
    <source src="screenshots_and_clips/Argentina-vs-Belgium-Fifa-World-Cup-2014-Quater-final-full-match-YouTube_25fps_22538_22674_25.0_pass_unsuccessful_or_unintentional_ball_release_other.mp4" type="video/mp4">
  </video>
</figure>

<hr>

### **Intercepted Shot** &rarr; **Unsuccessfull Pass** &rarr; **Ball Out of Field**

<figure class="video_container">
  <video controls="true" allowfullscreen="true" poster="" style="width: 100%;">
    <source src="screenshots_and_clips/Argentina-vs-Belgium-Fifa-World-Cup-2014-Quater-final-full-match-YouTube_25fps_21491_21616_25.0_pass_successful_or_unintentional_ball_release_other.mp4" type="video/mp4">
  </video>
</figure>


<table>
  <tr>
        <td>**Blocked Shot**</td>
        <td>**Unsuccessfull Pass**</td>
        <td>**Ball Out of Field**</td>
  </tr>
  <tr>
        <td>Blocked/intercepted shot, i.e. one event and thus one timestamp: on ball release of the shooting player</td>
        <td>**Unsuccessfull Pass** since it is the primary intention to pass to a teammate instead of **unintentional ball release**. In particular, no "successfull interference" since there is no opponent in range. </td>
        <td> No visible/audible decision from referee, thus when the ball leaves the field.</td>
  </tr>
  <tr>
        <td><img src="screenshots_and_clips/Argentina-vs-Belgium-Fifa-World-Cup-2014-Quater-final-full-match-YouTube_25fps_21491.jpg" width="100%"></td>
        <td><img src="screenshots_and_clips/Argentina-vs-Belgium-Fifa-World-Cup-2014-Quater-final-full-match-YouTube_25fps_21522.jpg" width="100%"></td>
        <td><img src="screenshots_and_clips/Argentina-vs-Belgium-Fifa-World-Cup-2014-Quater-final-full-match-YouTube_25fps_21603.jpg" width="100%"></td>
  </tr>
 </table>

<hr>

### Complex Situation

<figure class="video_container">
  <video controls="true" allowfullscreen="true" poster="" style="width: 100%">
    <source src="screenshots_and_clips/Argentina-vs-Belgium-Fifa-World-Cup-2014-Quater-final-full-match-YouTube_25fps_24084_24340_25.0_unkown.mp4" type="video/mp4">
  </video>
</figure>

<table>
  <tr>
        <td>**Throw-in+unsuccessfull pass** (unsuccessfull if teammate does not touch the ball, successful otherwise)</td>
        <td>**Successful Pass**</td>
        <td>**Ball Reception**</td>
        <td>**Successful Interference** (no extra pass, i.e. interference timestamp would be equal to pass timestamp). In this case interference represents ball release (ball reception otherwise: remember mutually exclusive on-ball-event events)</td>
  </tr>
  <tr>
            <td><img src="screenshots_and_clips/Argentina-vs-Belgium-Fifa-World-Cup-2014-Quater-final-full-match-YouTube_25fps_24084_throw-in.jpg" width="100%"></td>
            <td><img src="screenshots_and_clips/Argentina-vs-Belgium-Fifa-World-Cup-2014-Quater-final-full-match-YouTube_25fps_24132_pass_successful.jpg" width="100%"></td>
            <td><img src="screenshots_and_clips/Argentina-vs-Belgium-Fifa-World-Cup-2014-Quater-final-full-match-YouTube_25fps_24169_ball_reception.jpg" width="100%"></td>
            <td><img src="screenshots_and_clips/Argentina-vs-Belgium-Fifa-World-Cup-2014-Quater-final-full-match-YouTube_25fps_24192_successful_interference.jpg" width="100%"></td>
  </tr>
    <tr>
        <td>**Ball Reception**</td>
        <td>**Unsuccessful Pass (off target)** since teammate is not touching the ball after ball release. Unfortunately, off target despite correct direction and pass strength</td>
        <td>**Ball Reception**</td>
        <td>**Foul** tagged at whistle</td>
  </tr>
  <tr>
            <td><img src="screenshots_and_clips/Argentina-vs-Belgium-Fifa-World-Cup-2014-Quater-final-full-match-YouTube_25fps_24222_reception.jpg" width="100%"></td>
            <td><img src="screenshots_and_clips/Argentina-vs-Belgium-Fifa-World-Cup-2014-Quater-final-full-match-YouTube_25fps_24238_unsucessful_pass.jpg" width="100%"></td>
            <td><img src="screenshots_and_clips/Argentina-vs-Belgium-Fifa-World-Cup-2014-Quater-final-full-match-YouTube_25fps_24302_reception.jpg" width="100%"></td>
            <td><img src="screenshots_and_clips/Argentina-vs-Belgium-Fifa-World-Cup-2014-Quater-final-full-match-YouTube_25fps_24331_foul_whistle.jpg" width="100%"></td>
  </tr>
 </table>
<hr>

