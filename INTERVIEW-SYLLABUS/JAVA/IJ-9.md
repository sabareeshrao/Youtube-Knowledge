# IJ-9 — Why can nextLine skip input after nextInt?

## Video option — YT-2: Java Full Course for free ☕

**Video:** [Watch this tutorial](https://www.youtube.com/watch?v=xTtL8E4LzTQ)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-2.29 | [38:38](https://www.youtube.com/watch?v=xTtL8E4LzTQ&t=2318s) | 🟢 USEFUL | some reason if you need a Boolean booleans are either true or false here's how we can accept that… |
| YT-2.30 | [39:58](https://www.youtube.com/watch?v=xTtL8E4LzTQ&t=2398s) | 🟢 USEFUL | will be a future lesson we'll cover pretty soon if is student if that's true then we will print let's… |
| YT-2.31 | [41:24](https://www.youtube.com/watch?v=xTtL8E4LzTQ&t=2484s) | 🟢 USEFUL | demonstrate so we have our scanner let's say we ask for a user's age enter your age and I'll make this a… |
| YT-2.32 | [42:51](https://www.youtube.com/watch?v=xTtL8E4LzTQ&t=2571s) | 🟢 USEFUL | enter within the input buffer there's still a new line character because we hit enter so the next line… |
| YT-2.33 | [43:55](https://www.youtube.com/watch?v=xTtL8E4LzTQ&t=2635s) | 🟢 USEFUL | calculate the area of a rectangle what I like to do when creating a project is declare all of my… |
| YT-2.34 | [45:14](https://www.youtube.com/watch?v=xTtL8E4LzTQ&t=2714s) | 🟢 USEFUL | reuse it width equals use our scanner object use the an next Double method because we're accepting a… |

### AI answer — YT-2

| AI answer |
|---|
| nextInt reads the number but leaves the Enter key's newline in the input stream. The next call to nextLine can consume that leftover newline instead of waiting. For example, after reading an age, I can call one extra nextLine before reading a full name. The key is understanding what remains in the input buffer. |

**Source note:** The linked instructor transcript teaches this topic. This clear interview answer is independently written by AI, not spoken by a candidate.
