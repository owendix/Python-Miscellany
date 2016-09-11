# Python-Miscellany
Miscellaneous Python programs using various modules such as SciPy, NumPy, and PyPlot

carJumpPredictDx: estimates the distance traveled by a Hot Wheel car jumping off a ramp from a table. The car starts from different
initial heights. This uses NumPy's vectorized calculations.

countNumAsWords: write numbers as words, count the letters, convert this to words, and repeat toward stability.

skiFootTorque: Estimates the effect of a shorter but wider (equal area) ski on the torque needed to turn it at a certain angular 
velocity. Incorporates both the smaller moment arm by friction with the snow and the smaller rotational inertia, 
which turns out to be neglible for reasonable values (~0.5-10%). 
Result: a skiboard/snowblade requires roughly 60% of the torque to maneuver, though medical and other literature still indicates 
nonreleasable bindings result in a serious risk of injury to the ACL.

slideEstSnowBowl: I lost control at Arizona Snowbowl and slid down the mountain. This is how far (from GPS data) an oblate spheroid 
model and superimposed variations in altitude.

unJumbler: simple tools I wrote for fun for unjumbling a word in Python:
  unJumble: unjumbles a word with a brute force method (slow for long words)
  visuallyUnJumble: write all permutations of possible first and last letters so you can possibly see the solution(s) more easily. 
  This seems mildly helpful.
  myWord: initialize visuallyUnJumble with a word and see if you can solve it by comparing to the result from unJumble
