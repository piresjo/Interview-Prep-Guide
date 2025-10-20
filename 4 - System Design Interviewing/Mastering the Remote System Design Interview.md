# Mastering the Remote System Design Interview

## What Makes Remote Design Interviews Challenging

- Unfamiliar setting and tooling
  - When you do a remote system design interview, you must utilize a different set of tooling (Bluejeans for VC, Google Draw or an equivalent in place of a whiteboard).
- Communication latency
- Lack of tactile feedback from the interviewer.

## Preparation

### Monitor and Sizing

I recommend that in preparation for remote system interview, you have two monitors set up, one for the Bluejeans/Zoom video itself as well as the Components Setup scratchpad (see below), and one other monitor for the actual Google Draw / Lucidchart where you’ll conduct the system design interview. I also recommend getting a desk lamp and move the interviewer’s video overlay close to your video camera so you make eye contact when looking at them.

## What To Do During The Interview

Keep in mind that the purpose of the interview is for you to help the interviewer collect the signal rather than for you to arrive at the “right answer”. This means that even if you have the perfect answer, but either your interviewer doesn’t grok/buy into it or you fail to communicate in a way they understand, then you’ll fail the interview all the same.

While shadowing interviews, I’ve observed a common failure pattern where a candidate spends most of the interview talking non-stop only to have the interviewer not get a chance to cover a major piece of signal or follow-up to the interview question they wanted to collect signal on.

### Setting Expectations

To ensure that you cover parts of the problem-space that the interviewer cares about, ensure that you level-set during the interview, but do so in a proactive way that gives him/her the impression that you have a broad set of capabilities. Here are some example level-setting statements you can make during the beginning of the interview:

- “This is a very interesting problem that has many different facets. Just off the top of my head, we can talk about API design, doing some computation scale analysis, data modeling for storing the Tweets, I can also talk about how to scale this or how to handle whale users. Is there a specific area you want me to cover first or dive deep into?”
- “Before we start, I’m going to spend 5 minutes quickly doing some back-of-the-envelope calculation to figure out how many PetaBytes of in-memory cache and hard storage we need. Does that sound good to you?”
- “After I talk about the storage layer, I can either talk about how to scale this up for billions of users or I can talk about authentication and security. I think the former is more intellectually interesting, but do you have a preference?”
- “Coming from a startup background, I’m intimately familiar with the AWS stack (redshift, EC2, S3, Cloudflare). Are you okay if I proceed using terminology from that?

### Familiarizing  Self With The Company's Tech Stack

You should do this

### Constant Checking In

To ensure that you’re covering the key points and giving the interviewer sufficient signal, you should constantly check-in with the interviewer to ensure that you’re on the right track. Here are some things you can say:

- “I’ll pause here and see if you have any questions.
- “Would you like me to write out the full API definition, or just go over it a very high-level or just move onto X?”
- “This specific design does have some weaknesses however, it does heavily sacrifice latency/performance for future extensibility and cleaner abstraction. Would you like me to quantify precisely how much or propose an alternative solution that reverses this trade-off?”
- “I front the database call here with a Redis LRU cache, which under the hood is implemented with a LinkedHashMap data structure. Would you like me to explain/explore the specifics of how this works under the hood?”

## Preparation Checklist

- Have two monitors set up, one is your main (interview canvas), and one is your side (put your templated components).
- Do a quick copy-paste test between your “templated components” to your “main interview canvas” to make sure your clipboard is working.
- Practice dialing in and sharing your screen using the given VC software the company’s provided (Bluejeans, Zoom, Webex, etc.).
- Go to the bathroom if needed.
- Set the interview canvas side as appropriate (30 in. by 20 in. for Google Draw).
- Look up your interviewer ahead of time on LinkedIn (usually your recruiter gives you interviewer information).

## Links

[Mastering the Remote System Design Interview](https://tonygwu.medium.com/mastering-the-remote-system-design-interview-de7120b9ea52)