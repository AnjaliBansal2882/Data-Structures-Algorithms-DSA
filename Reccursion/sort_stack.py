class SortStack:
    def sort_stack(self, stack):
        if not stack:
            return

        top = stack.pop()
        self.sort_stack(stack)
        self.insert_in_sorted_order(stack, top)

    def insert_in_sorted_order(self, stack, element):
        if not stack or stack[-1] <= element:
            stack.append(element)
        else:
            top = stack.pop()
            self.insert_in_sorted_order(stack, element)
            stack.append(top)
