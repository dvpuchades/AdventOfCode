public class Pair {
    int start;
    int end;

    public Pair(String data) {
        String[] elements = data.split("-");
        this.start = Integer.parseInt(elements[0]);
        this.end = Integer.parseInt(elements[1]);
    }

    public int getStart() {
        return start;
    }

    public int getEnd() {
        return end;
    }

    public boolean fullOverlaps(Pair other) {
        if ((this.start <= other.getStart()) && (this.end >= other.getEnd()))
            return true;
        return false;
    }

    public boolean overlaps(Pair other)
    {
        if ((this.start <= other.getStart()) && (this.end >= other.getEnd()))
            return true;
        if((this.start >= other.getStart()) && (this.start <= other.getEnd()))
            return true;
        if((this.end >= other.getStart()) && (this.end <= other.getEnd()))
            return true;
        return false;
    }
}