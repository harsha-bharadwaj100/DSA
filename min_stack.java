import java.util.Stack;

class MinStack {
    private Stack<Integer> stack, min_stack;

    public MinStack() {
        stack = new Stack<>();
        min_stack = new Stack<>();
    }

    public void push(int val) {
        stack.push(val);
        if (min_stack.isEmpty() || val <= min_stack.peek()) {
            min_stack.push(val);
            return;
        }
        min_stack.push(min_stack.peek());
    }

    public void pop() {
        if (!stack.isEmpty()) {
            stack.pop();
            min_stack.pop();
        }
    }

    public int top() {
        return stack.peek();
    }

    public int getMin() {
        return min_stack.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */