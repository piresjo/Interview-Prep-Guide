enum Suit {
    Club = 0,
    Jack,
    Spade,
    Diamond
}

abstract class Card {
    private availVal: boolean;

    protected val: number;
    protected suitVal: Suit;

    constructor(c : number, s : Suit) {
        this.val = c;
        this.suitVal = s;
    }

    abstract value() : number
    suit() : Suit {
        return this.suitVal;
    }

    isAvailable(): boolean {
        return this.availVal;
    }
}