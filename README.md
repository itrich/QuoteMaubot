# QuoteMaubot
Maubot plugin to answer with a random quote from a configurable list

## Setup

Add your quotes to the `basic-configuration.yaml` under the corresponding keys. You can also change the base-config.yaml from within the Maubot Manager after you created the instance.

```
quotes:
    oscarwilde:
        - "Be yourself; everyone else is already taken."
        - "To live is the rarest thing in the world. Most people exist, that is all."
    einstein:
        - "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe."
        - "I am enough of an artist to draw freely upon my imagination. Imagination is more important than knowledge. Knowledge is limited. Imagination encircles the world."
```

To request a random quote, simply use `!quote <key>`, e.g. `!quote einstein`.