class ReverseStack:
    def reverse_stack(self, stack):
        if not stack:
            return

        top = stack.pop()
        self.reverse_stack(stack)
        self.insert_at_bottom(stack, top)

    def insert_at_bottom(self, stack, element):
        if not stack:
            stack.append(element)
        else:
            top = stack.pop()
            self.insert_at_bottom(stack, element)
            stack.append(top)
